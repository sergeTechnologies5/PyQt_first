# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.12
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
from login import Ui_MainWindow as Login
from dashboard import Ui_MainWindow as Dashboard
from setting import Ui_Dialog as Settings
from register import Ui_Dialog as Register
from db import db
from device import Device
import threading
import time

class Ui_Form(object):
# @staticmethod
    def __init(self):
        pass

    def settings(self):
        self.window = QtWidgets.QDialog()
        self.ui = Settings()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.btn_back.clicked.connect(self.openwindow)
    def openlogin(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Dashboard()
        self.ui.setupUi(self.window)
        
        self.window.hide()
        ui.setupUi(Form)
        Form.show()

    def openwindow(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Dashboard()
        self.ui.setupUi(self.window)
        Form.hide()
        self.window.show()
        self.ui.btn_logout.clicked.connect(self.logout)
        self.ui.btn_add.clicked.connect(self.ui.registerUser)
        self.ui.btn_settings.clicked.connect(self.settings)

    def logout(self):
        Ui_Form.openlogin(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(734, 428)
        self.label_username = QtWidgets.QLabel(Form)
        self.label_username.setGeometry(QtCore.QRect(160, 130, 121, 31))
        self.label_username.setObjectName("label_username")
        self.label_password = QtWidgets.QLabel(Form)
        self.label_password.setGeometry(QtCore.QRect(160, 190, 111, 21))
        self.label_password.setObjectName("label_password")
        self.txt_input_username = QtWidgets.QLineEdit(Form)
        self.txt_input_username.setGeometry(QtCore.QRect(380, 140, 201, 21))
        self.txt_input_username.setObjectName("txt_input_username")
        self.txt_input_password = QtWidgets.QLineEdit(Form)
        self.txt_input_password.setGeometry(QtCore.QRect(380, 190, 201, 21))
        self.txt_input_password.setObjectName("txt_input_password")
        self.btn_submit = QtWidgets.QPushButton(Form)
        self.btn_submit.setGeometry(QtCore.QRect(380, 240, 100, 32))
        self.btn_submit.setObjectName("btn_submit")
        self.btn_register = QtWidgets.QPushButton(Form)
        self.btn_register.setGeometry(QtCore.QRect(500, 240, 100, 32))
        self.btn_register.setObjectName("btn_submit")
        self.text_title = QtWidgets.QLabel(Form)
        self.text_title.setGeometry(QtCore.QRect(60, 10, 629, 51))
        self.text_title.setObjectName("text_title")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(390, 290, 191, 20))
        self.radioButton.setObjectName("radioButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Login Page"))
        self.label_username.setText(_translate("Form", "Enter User Name"))
        self.label_password.setText(_translate("Form", "Enter Password"))
        self.btn_submit.setText(_translate("Form", "Submit"))
        self.btn_register.setText(_translate("Form", "Register"))


        self.text_title.setText(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                   "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                   "p, li { white-space: pre-wrap; }\n"
                                                   "</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
                                                   "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">sergetech<span style=\" font-size:24pt; color:#cf0f39;\"></span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "Keep me Logged In"))

        self.btn_submit.clicked.connect(self.btn_submit_handler)
        self.btn_register.clicked.connect(self.btn_register_handler)

    def btn_register_handler(self):
        self.window = QtWidgets.QDialog()
        self.ui = Register()
        self.ui.setupUi(self.window)
      
        self.window.show()
        
    def thread_function(self):
        device = Device()
        device.liveCapture()
    
    def btn_submit_handler(self):
        val_pass = self.txt_input_password.text()
        val_username = self.txt_input_username.text()

        result = db.execute("SELECT name, password FROM users WHERE name = ? AND password = ?", (val_username, val_pass))
        if(len(result.fetchall())>0):
            print("User found")
            self.openwindow()
        else:
            print("User not Found")

if __name__ == "__main__":
    import sys
    
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    x = threading.Thread(target=ui.thread_function)
    x.start()
    ui.setupUi(Form)
    Form.show()

    sys.exit(app.exec_())