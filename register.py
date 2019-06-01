# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'register.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
from db import db
from datetime import date
# Create a database in RAM
class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(439, 252)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(30, 50, 101, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 80, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 151, 21))
        self.label_3.setObjectName("label_3")
        self.txt_username = QtWidgets.QTextEdit(Dialog)
        self.txt_username.setGeometry(QtCore.QRect(180, 50, 191, 31))
        self.txt_username.setObjectName("txt_username")
        self.txt_password = QtWidgets.QTextEdit(Dialog)
        self.txt_password.setGeometry(QtCore.QRect(180, 90, 191, 31))
        self.txt_password.setObjectName("txt_password")
        self.txt_confirm_password = QtWidgets.QTextEdit(Dialog)
        self.txt_confirm_password.setGeometry(QtCore.QRect(180, 130, 191, 31))
        self.txt_confirm_password.setObjectName("txt_confirm_password")
        self.btn_save = QtWidgets.QPushButton(Dialog)
        self.btn_save.setGeometry(QtCore.QRect(180, 180, 191, 30))
        self.btn_save.setObjectName("btn_save")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "HR SYSTEM"))
        self.label.setText(_translate("Dialog", "Username"))
        self.label_2.setText(_translate("Dialog", "Password"))
        self.label_3.setText(_translate("Dialog", "Confirm Password"))
        self.btn_save.setText(_translate("Dialog", "SAVE"))
        self.btn_save.clicked.connect(self.registerUser)

    def registerUser(self):

        val_name = self.txt_username.toPlainText()
        val_password = self.txt_password.toPlainText()
        val_confirm_password = self.txt_confirm_password.toPlainText()
        
        cursor = db.cursor()
        today = date.today()
        # Insert user 1
        val_date = str(today.strftime("%d/%m/%Y"))
        cursor.execute('''INSERT INTO users(name, password,date)
                        VALUES(?,?,?)''', (val_name,val_password,val_date))
        self.txt_username.setText("")
        self.txt_password.setText("")
        db.commit()
        self.txt_confirm_password.setText("")


