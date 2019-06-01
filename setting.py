# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

import sqlite3
from db import db
from datetime import date
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(777, 386)
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.btn_back = QtWidgets.QPushButton(Dialog)
        self.btn_back.setGeometry(QtCore.QRect(20, 20, 60, 21))
        self.btn_back.setObjectName("btn_back")
        self.label_2.setGeometry(QtCore.QRect(80, 60, 231, 21))
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setGeometry(QtCore.QRect(450, 50, 80, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setGeometry(QtCore.QRect(440, 160, 80, 21))
        self.label_8.setObjectName("label_8")
        self.btn_saveIp = QtWidgets.QPushButton(Dialog)
        self.btn_saveIp.setGeometry(QtCore.QRect(640, 100, 101, 41))
        self.btn_saveIp.setObjectName("btn_saveIp")
        self.btn_saveUrl = QtWidgets.QPushButton(Dialog)
        self.btn_saveUrl.setGeometry(QtCore.QRect(390, 270, 106, 30))
        self.btn_saveUrl.setObjectName("btn_saveUrl")
        self.txt_url = QtWidgets.QTextEdit(Dialog)
        self.txt_url.setGeometry(QtCore.QRect(390, 200, 351, 41))
        self.txt_url.setObjectName("txt_url")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(120, 10, 121, 31))
        self.label.setObjectName("label")
        self.txt_ip = QtWidgets.QTextEdit(Dialog)
        self.txt_ip.setGeometry(QtCore.QRect(390, 100, 241, 41))
        self.txt_ip.setObjectName("txt_ip")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setGeometry(QtCore.QRect(50, 210, 121, 21))
        self.label_9.setObjectName("label_9")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setGeometry(QtCore.QRect(50, 100, 121, 21))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setGeometry(QtCore.QRect(50, 150, 121, 21))
        self.label_12.setObjectName("label_12")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(180, 270, 181, 30))
        self.btn_save.setObjectName("btn_save")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(-149, -60, 181, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(-60, -120, 121, 31))
        self.label_4.setObjectName("label_4")
        self.txt_oldPassword = QtWidgets.QTextEdit(Dialog)
        self.txt_oldPassword.setGeometry(QtCore.QRect(180, 210, 181, 31))
        self.txt_oldPassword.setObjectName("txt_oldPassword_2")
        self.txt_username = QtWidgets.QTextEdit(Dialog)
        self.txt_username.setGeometry(QtCore.QRect(180, 100, 181, 31))
        self.txt_username.setObjectName("txt_username")
        self.txt_newPassword = QtWidgets.QTextEdit(Dialog)
        self.txt_newPassword.setGeometry(QtCore.QRect(180, 150, 181, 31))
        self.txt_newPassword.setObjectName("txt_newPassword")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Settings"))
        self.label_2.setText(_translate("Dialog", "Change       Password"))
        self.label_7.setText(_translate("Dialog", "Set IP"))
        self.label_8.setText(_translate("Dialog", "Set URL"))
        self.btn_saveIp.setText(_translate("Dialog", "Save"))
        self.btn_saveUrl.setText(_translate("Dialog", "Save"))
        self.label.setText(_translate("Dialog", "Settings"))
        self.label_9.setText(_translate("Dialog", "Old Password"))
        self.label_11.setText(_translate("Dialog", "Username"))
        self.label_12.setText(_translate("Dialog", "New Password"))
        self.btn_save.setText(_translate("Dialog", "Save"))
        self.btn_back.setText(_translate("Dialog", "Back"))
        self.label_3.setText(_translate("Dialog", "Change       Password"))
        self.label_4.setText(_translate("Dialog", "Settings"))

        self.btn_saveUrl.clicked.connect(self.saveUrl)
        self.btn_saveIp.clicked.connect(self.saveIP)
        self.btn_save.clicked.connect(self.saveUserDetails)
        cursor = db.cursor()
        cursor.execute('SELECT url FROM url')
        self.txt_url.setText(cursor.fetchone()[-1])
        cursor.execute('SELECT ip FROM ip')
        self.txt_ip.setText(cursor.fetchone()[-1])
        cursor.close()
    def saveUrl(self):
        url = self.txt_url.toPlainText()
        cursor = db.cursor()
        cursor.execute('DELETE FROM url')
        cursor.execute('INSERT INTO url VALUES(?)', (url,))
        db.commit()
        
        cursor.execute('SELECT url FROM url')
        self.txt_url.setText(cursor.fetchone()[-1])


    def saveIP(self):
        ip = self.txt_ip.toPlainText()
        cursor = db.cursor()
        cursor.execute('DELETE FROM ip')
        cursor.execute('INSERT INTO ip VALUES(?)', (ip,))
        db.commit()
        cursor.execute('SELECT ip FROM ip')
        self.txt_ip.setText(cursor.fetchone()[-1])
        

    def saveUserDetails(self):
        username = self.txt_username.toPlainText()
        new_password = self.txt_newPassword.toPlainText()
        old_password = self.txt_oldPassword.toPlainText()
        url = self.txt_url.toPlainText()
        cursor = db.cursor()
        cursor.execute('''INSERT INTO databasecredentials(url, usernname,password)
                        VALUES(?,?,?)''', (url,username,new_password))
        db.commit()
        self.txt_url.setText("")
        self.txt_username.setText("")
        self.txt_newPassword.setText("")
        self.txt_oldPassword.setText("")