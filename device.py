#!/usr/bin/env python2
# # -*- coding: utf-8 -*-
import sys
import traceback
import argparse
import time
import datetime
import codecs
from builtins import input
sys.path.append("zk")
from zk import ZK, const
from zk.user import User
from zk.finger import Finger
from zk.attendance import Attendance
from zk.exception import ZKErrorResponse, ZKNetworkError
import threading as thread
import requests
import mysql.connector
from db import db

class Device:
    conn = None
    
    def __init__(self):
        self.live = False
        
        self.status = False
        parser = argparse.ArgumentParser(description='ZK Basic Reading Tests')
        parser.add_argument('-a', '--address', 
                            help='ZK device Address [192.168.1.201]', default='192.168.1.201')
        parser.add_argument('-p', '--port', type=int,
                            help='ZK device port [4370]', default=4370)
        parser.add_argument('-T', '--timeout', type=int,
                            help='Default [10] seconds (0: disable timeout)', default=10)
        parser.add_argument('-P', '--password', type=int,
                            help='Device code/password', default=0)
        parser.add_argument('-b', '--basic', action="store_true",
                            help='get Basic Information only. (no bulk read, ie: users)')
        parser.add_argument('-f', '--force-udp', action="store_true",
                            help='Force UDP communication')
        parser.add_argument('-v', '--verbose', action="store_true",
                            help='Print debug information')
        parser.add_argument('-t', '--templates', action="store_true",
                            help='Get templates / fingers (compare bulk and single read)')
        parser.add_argument('-tr', '--templates-raw', action="store_true",
                            help='Get raw templates (dump templates)')
        parser.add_argument('-ti', '--templates-index', type=int,
                            help='Get specific template', default=0)
        parser.add_argument('-r', '--records', action="store_true",
                            help='Get attendance records')
        parser.add_argument('-u', '--updatetime', action="store_true",
                            help='Update Date/Time')
        parser.add_argument('-l', '--live-capture', action="store_true",
                            help='Live Event Capture')
        parser.add_argument('-o', '--open-door', action="store_true",
                            help='Open door')
        parser.add_argument('-D', '--deleteuser', type=int,
                            help='Delete a User (uid)', default=0)
        parser.add_argument('-A', '--adduser', type=int,
                            help='Add a User (uid) (and enroll)', default=0)
        parser.add_argument('-E', '--enrolluser', type=int,
                            help='Enroll a User (uid)', default=0)
        parser.add_argument('-F', '--finger', type=int,
                            help='Finger for enroll (fid=0)', default=0)

        args = parser.parse_args()

        zk = ZK(args.address, port=args.port, timeout=args.timeout, password=args.password, force_udp=args.force_udp, verbose=args.verbose)
        print('Connecting to device ...')
        try:
            Device.conn = zk.connect()
            print('SDK build=1      : %s' % Device.conn.set_sdk_build_1()) # why?
            print ('Disabling device ...')
            self.status = True
            Device.conn.disable_device()
            fmt = Device.conn.get_extend_fmt()
            print ('ExtendFmt        : {}'.format(fmt))
            fmt = Device.conn.get_user_extend_fmt()
            print ('UsrExtFmt        : {}'.format(fmt))
            print ('Face FunOn       : {}'.format(Device.conn.get_face_fun_on()))
            print ('Face Version     : {}'.format(Device.conn.get_face_version()))
            print ('Finger Version   : {}'.format(Device.conn.get_fp_version()))
            print ('Old Firm compat  : {}'.format(Device.conn.get_compat_old_firmware()))
            net = Device.conn.get_network_params()
            print ('IP:{} mask:{} gateway:{}'.format(net['ip'],net['mask'], net['gateway']))
            now = datetime.datetime.today().replace(microsecond=0)
            thread.start_new_thread(self.liveCapture())
        except Exception as ex:
            pass
    #end liveCapture
    def endliveCapture(self):
        Device.conn.end_live_capture = True
    #start live capture
    def liveCapture(self):
        print ('')
        print ('--- Live Capture! (press ctrl+C to break) ---')
        print('--- Place Finger To Authenticate ---')
        counter = 0
        mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")
        mycursor = mydb.cursor()
        
        mycursor.execute("CREATE TABLE IF NOT EXISTS  logs (id INT AUTO_INCREMENT PRIMARY KEY, uid VARCHAR(255), user_id  VARCHAR(255),timestamp VARCHAR(255), status VARCHAR(255), punch VARCHAR(255))")
        # payload = {"ATT":att.name, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
        sql = "INSERT INTO logs (uid, user_id,status,timestamp,punch) VALUES (%s, %s,%s, %s,%s)"
                
        for att in Device.conn.live_capture():# using a generator!
            if att is None:
                pass
            else:
                try:
                    val = (att.uid, att.user_id,att.status,att.timestamp,att.punch)
                    v = mycursor.execute(sql, val)
                    mydb.commit()
                    mydb.close()
                except Exception as identifier:
                    pass
                
            if counter >= 10:
                Device.conn.end_live_capture = True
        print('')
        print('--- capture End!---')
        print ('')
    #ennroll user
    def enrollUser(self,uid,finger):
        
        uid = uid
        print ('--- Enrolling User #{} ---'.format(uid))
        Device.conn.delete_user_template(uid, finger)
        Device.conn.reg_event(0xFFFF) #
        if Device.conn.enroll_user(uid,finger):
            Device.conn.test_voice(18) # register ok
            tem = Device.conn.get_user_template(uid,finger)
            print (tem)
        else:
            Device.conn.test_voice(18) # not registered
        Device.conn.refresh_data()
    #addUser
    def addUser(self,uid=0,name='nn',admin='y',password='123',user_id='1',card_number=12345):
        if self.live:
            self.live = False
            self.end_live_capture()
        name = name
        admin = admin
        privilege = 14 if admin == 'y' else 0
        password = password
        user_id = user_id
        card = card_number
        card = int(card) if card else 0
        #if prev:
        #    conn.delete_user(uid) #borrado previo
        try:
            Device.conn.set_user(uid=uid, name=name, privilege=privilege, password=password, group_id='', user_id=user_id, card=0)
            
        except ZKErrorResponse as e:
            print ("error: %s" % e)
            #try new format
            zk_user = User(uid, name, privilege, password, '', user_id, card)
            Device.conn.save_user_template(zk_user)# forced creation
            
        Device.conn.refresh_data()

    def getUsers(self):
            userrs = []
            users = Device.conn.get_users()
            for user in users:
                privilege = 'User'
                if user.privilege == const.USER_ADMIN:
                    privilege = 'Admin'
                user = Users(user.uid,user.name,privilege,user.password,user.group_id,user.user_id)
                userrs.append(user)
            return userrs

    def restart(self):
        Device.conn.restart()

    #deleteUser
    def deleteUser(self,user_id):
        try:
            Device.conn.delete_user(user_id)
        except Exception as exception:
            print(exception)

class Users:
    def __init__(self,uid,name,privilege,password,group_id,user_id):
        self.UID = uid
        self.NAME = name
        self.PRIVILEGE = privilege
        self.PASSWORD = password
        self.GROUP_ID = group_id
        self.USER_ID = user_id

if __name__ == "__main__":
    device = Device()
    try:
        
        device.liveCapture()
    except Exception as identifier:
        pass
    
    