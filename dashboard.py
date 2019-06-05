# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget
from PyQt5 import QtCore, QtGui, QtWidgets
from device import Device
from PyQt5.QtCore import pyqtSlot
import threading as thread
import mysql.connector
import datetime
class Ui_MainWindow(object):

    def reload(self):
        self.data = []
        self.device = Device()
        users = self.device.getUsers()
        id = 1
        for user in users:
            self.data.append((user.NAME,user.PRIVILEGE,user.PASSWORD,user.GROUP_ID,user.USER_ID))
            id = id + 1

        return self.data
    def __init__(self):
        self.data = self.reload()
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(850, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(310, 20, 261, 21))
        self.label.setObjectName("label")
        self.txt_name = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_name.setGeometry(QtCore.QRect(120, 70, 251, 31))
        self.txt_name.setObjectName("txt_name")
        self.txt_password = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_password.setGeometry(QtCore.QRect(120, 120, 251, 31))
        self.txt_password.setObjectName("txt_password")
        self.txt_cardid = QtWidgets.QTextEdit(self.centralwidget)
        self.txt_cardid.setGeometry(QtCore.QRect(120, 170, 251, 31))
        self.txt_cardid.setObjectName("txt_cardid")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 80, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 130, 80, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 180, 80, 21))
        self.label_4.setObjectName("label_4")
        self.btn_add = QtWidgets.QPushButton(self.centralwidget)
        self.btn_add.setGeometry(QtCore.QRect(190, 220, 106, 30))
        self.btn_add.setObjectName("btn_add")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(390, 70, 451, 341))
        self.connection = QtWidgets.QLabel(self.centralwidget)
        self.connection.setGeometry(QtCore.QRect(60, 240, 500, 50))
        self.connection.setObjectName("label_4")
        self.tableView.setObjectName("tableView")
        self.btn_enrol = QtWidgets.QPushButton(self.centralwidget)
        self.btn_enrol.setGeometry(QtCore.QRect(390, 430, 106, 30))
        self.btn_enrol.setObjectName("btn_enrol")
        self.btn_update = QtWidgets.QPushButton(self.centralwidget)
        self.btn_update.setGeometry(QtCore.QRect(550, 430, 106, 30))
        self.btn_update.setObjectName("btn_update")
        self.btn_delete = QtWidgets.QPushButton(self.centralwidget)
        self.btn_delete.setGeometry(QtCore.QRect(680, 430, 106, 30))
        self.btn_delete.setObjectName("btn_delete")
        self.btn_settings = QtWidgets.QPushButton(self.centralwidget)
        self.btn_settings.setGeometry(QtCore.QRect(640, 20, 151, 30))
        self.btn_settings.setObjectName("btn_settings")
        self.btn_logout = QtWidgets.QPushButton(self.centralwidget)
        self.btn_logout.setGeometry(QtCore.QRect(0, 0, 106, 30))
        self.btn_logout.setObjectName("btn_logout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dashboard"))
        self.label.setText(_translate("MainWindow", "Welcome to hr system"))
        self.connection.setText(_translate("MainWindow", ""))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Password"))
        self.label_4.setText(_translate("MainWindow", "Card ID"))
        self.btn_add.setText(_translate("MainWindow", "ADD"))
        self.btn_enrol.setText(_translate("MainWindow", "ENROL"))
        self.btn_update.setText(_translate("MainWindow", "UPDATE"))
        self.btn_delete.setText(_translate("MainWindow", "DELETE"))
        self.btn_settings.setText(_translate("MainWindow", "SETTINGS"))
        self.btn_logout.setText(_translate("MainWindow", "Logout"))
        self.tableReload()
   
    def tableReload(self):
        self.tableView.setRowCount(len(self.data))
        self.tableView.setColumnCount(5)
        self.tableView.setHorizontalHeaderLabels(['NAME','PRIVILEGE','PASSWORD','GROUP','USER ID'])
        self.tableView.clicked.connect(self.tableClick)
        row=0
 
        for tup in self.data:
 
            col=0
    
            for item in tup:
 
                cellinfo=QTableWidgetItem(item)
 
                self.tableView.setItem(row, col, cellinfo)
 
                col+=1
 
            row += 1
    def tableClick(self):
        print("\n")
        for currentQTableWidgetItem in self.tableView.selectedItems():
            try:
                id = int(currentQTableWidgetItem.text())
                if id == 1 :
                    id = 1
                else:
                    id = int(currentQTableWidgetItem.text())
                self.device.deleteUser(id)
                self.reload()
                self.tableReload()
            except Exception as identifier:
                pass
            
            

    def registerUser(self):
        self.connection.setText("")
        users = self.device.getUsers()
        val_name = ''
        val_password = ''
        val_cardid = ''
        try:
            val_name = self.txt_name.toPlainText()
            val_password = self.txt_password.toPlainText()
            val_cardid = self.txt_cardid.toPlainText()
        except Exception as identifier:
            val_cardid = '12345'
        
        if self.device.status: 
            try:
                if not users:
                    userid = 0
                for user in users:
                    userid = user.UID
                uid = userid + 1
               
                self.device.addUser(uid=uid,name=val_name,admin='n',password=val_password,user_id= str(uid),card_number=val_cardid)
                mydb = mysql.connector.connect(host="167.99.208.98",user="root",passwd="1conl1v1ng",database="hr")

                mycursor = mydb.cursor()
                mycursor.execute("CREATE TABLE IF NOT EXISTS  users_bio (id INT AUTO_INCREMENT PRIMARY KEY, user_id  VARCHAR(255),timestamp VARCHAR(255), empo_no VARCHAR(255))")
                # payload = {"ATT":counter, "uid":att.uid, "user_id":att.user_id, "timestamp":str( att.timestamp), "status": att.status, "punch":att.punch}
                sql = "INSERT INTO users_bio (user_id,employee_no,timestamp) VALUES (%s, %s,%s)"
                val = (uid, val_name,str(datetime.datetime.now()))
                v = mycursor.execute(sql, val)
                mydb.commit()
                
            #access 
                self.device.enrollUser(uid=uid,finger=0)
                self.reload()
                self.tableReload()
            except Exception as identifier:
                print(identifier)
            self.txt_name.setText("")
            self.txt_password.setText("")
            self.txt_cardid.setText("")
        else :

            self.connection.setText("Device connection bad")
            
