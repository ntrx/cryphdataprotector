# -*- coding: utf-8 -*-

from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
from future_builtins import *

from PyQt4 import QtCore, QtGui
import sys
import rsa
import elgamal
import rabin
import functions as func
import random


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
# global


class Ui_MainWindow(QtGui.QWidget):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.setWindowTitle('Encryption')
        self.setupUi(self)
        self.events(self)
        # RSA AUTO SETTINGS
        d = -1
        while d<0:
            p = func.random_n(10,100)
            q = func.random_n(10,100)

            while len(str(p)) != len(str(q)):
                q = func.random_n(10,100)
            
            while p == q:
                q = func.random_n(10,100)
            
            self.lineEdit.setText(unicode(p))
            
            self.lineEdit_2.setText(unicode(q))
            
            n = p*q
            key = (p-1)*(q-1)
            e = func.random_n(0,10)
            self.lineEdit_3.setText(unicode(e))
            while func.gcd(key,e) != 1:
                e = func.random_n(0,10)		
            tmp = func.egcd(e,key)
            d = int(tmp[1])
            
        # EL-GAMAL AUTOSETTINGS
        p = func.random_n(30,100)   # value 1
        g = random.randint(1,1000)  # value 2
        x = random.randint(1,1000)  # value 3
        
        while g > p-1:
            g = random.randint(1,1000)
        while x > p:
            x = random.randint(1,1000)

        k = random.randint(1,1000)  # value 4
        while func.gcd(k, p-1) != 1:
            k = random.randint(1,1000)
            
        self.lineEdit_4.setText(unicode(p))
        self.lineEdit_5.setText(unicode(g))
        self.lineEdit_6.setText(unicode(x))
        self.lineEdit_7.setText(unicode(k))
        
        # Rabin AUTO SETTINGS
        p, q = func.rand34() # value 1,2
        self.lineEdit_8.setText(unicode(p))
        self.lineEdit_9.setText(unicode(q))
        
    def events(self, MainWindow):
        self.pushButton.clicked.connect(self.buttonClicked) # RSA
        self.pushButton_2.clicked.connect(self.buttonClicked_2) # El-Gamal
        self.pushButton_3.clicked.connect(self.buttonClicked_3) # Rabin
        
    def buttonClicked(self):
        q = unicode(self.lineEdit_2.text())
        p = unicode(self.lineEdit.text())
        self.textBrowser.append("q = {0}".format(q))
        self.textBrowser.append("p = {0}".format(p))
        
        e = unicode(self.lineEdit_3.text())
        self.textBrowser.append("e = {0}".format(e))
        
        key = (int(p)-1)*(int(q)-1)
        tmp = func.egcd(int(e),key)
        d = int(tmp[1])
        self.textBrowser.append("key = {0}, d = {1}".format(unicode(key),unicode(d)))
        
        input = self.plainTextEdit.toPlainText()
        self.textBrowser.append("Text lenght: {0}".format(len(input)))
        
        if self.radioButton.isChecked() is True:
            [time, output] = rsa.rsa(unicode(input),1,int(p),int(q),int(e))

            self.textBrowser.append("Encoded text: {0}".format(str(unicode(output))))
        
            self.textBrowser.append("Time elapsed: {0} s<br>".format(time))
        elif self.radioButton_2.isChecked() is True:
            [time, output] = rsa.rsa(input,0,int(p),int(q),int(e))
            self.textBrowser.append("Decoded text: {0}".format(unicode(output)))
            self.textBrowser.append("Time elapsed: {0} s<br>".format(time))
        
    def buttonClicked_2(self):
        p = int(unicode(self.lineEdit_4.text()))
        g = int(unicode(self.lineEdit_5.text()))
        x = int(unicode(self.lineEdit_6.text()))
        k = int(unicode(self.lineEdit_7.text()))
        
        y = g ** x % p
        a = g ** k % p
        
        self.textBrowser_2.append("p = {0}, g = {1}, x = {2}".format(p,g,x))
        self.textBrowser_2.append("k = {0}".format(k))
        self.textBrowser_2.append("y = {0}, a = {1}".format(y,a))
        
        input = self.plainTextEdit_2.toPlainText()
        self.textBrowser_2.append("Text length: {0}".format(len(input)))
        if self.radioButton_3.isChecked() is True:
            [time, output] = elgamal.elgamal(unicode(input),1,p,g,k,x)
            self.textBrowser_2.append("Encoded text: {0}".format(str(unicode(output))))
            self.textBrowser_2.append("Time elapsed: {0} s<br>".format(str(unicode(time))))
        if self.radioButton_4.isChecked() is True:
            [time, output] = elgamal.elgamal(unicode(input),0,p,g,k,x)
            self.textBrowser_2.append("Decoded text: {0}".format(str(unicode(output))))
            self.textBrowser_2.append("Time elapsed: {0} s<br>".format(time))
    
    def buttonClicked_3(self):
        p = int(unicode(self.lineEdit_8.text()))
        q = int(unicode(self.lineEdit_9.text()))
        
        n = p*q
        
        self.textBrowser_3.append("p = {0}, q = {1}, n = {2}".format(p,q,n))
        input = self.plainTextEdit_3.toPlainText()
        self.textBrowser_3.append("Text lenght: {0}".format(len(input)))
        if self.radioButton_5.isChecked() is True:
            [time, output] = rabin.rabin(unicode(input),1,p,q)
            self.textBrowser_3.append("Encoded text: {0}".format(str(unicode(output))))
            self.textBrowser_3.append("Time elapsed: {0} s<br>".format(str(unicode(time))))
        if self.radioButton_6.isChecked() is True:
            [time, a,b,c,d] = rabin.rabin(unicode(input),0,p,q)
            self.textBrowser_3.append("Decoded text:")
            self.textBrowser_3.append("{0}".format(str(unicode(a))))
            self.textBrowser_3.append("{0}".format(str(unicode(b))))
            self.textBrowser_3.append("{0}".format(str(unicode(c))))
            self.textBrowser_3.append("{0}".format(str(unicode(d))))
            self.textBrowser_3.append("Time elapsed: {0} s<br>".format(time))
            
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(711, 451)
        MainWindow.setFixedSize(711,451)
        self.gridlayout = QtGui.QGridLayout(MainWindow)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(6)
        self.gridlayout.setObjectName(_fromUtf8("gridlayout"))
        self.tabWidget = QtGui.QTabWidget(MainWindow)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setGeometry(QtCore.QRect(250, 0, 431, 77))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.groupBox_2)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.pushButton = QtGui.QPushButton(self.groupBox_2)
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QtCore.QRect(380, 20, 41, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setGeometry(QtCore.QRect(0, 0, 251, 77))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.radioButton = QtGui.QRadioButton(self.groupBox)
        self.radioButton.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName(_fromUtf8("radioButton"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(120, 10, 16, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.groupBox)
        self.lineEdit.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label_2 = QtGui.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(120, 30, 16, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lineEdit_2 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(120, 50, 16, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lineEdit_3 = QtGui.QLineEdit(self.groupBox)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 50, 113, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setGeometry(QtCore.QRect(0, 80, 681, 321))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.textBrowser = QtGui.QTextBrowser(self.groupBox_3)
        self.textBrowser.setGeometry(QtCore.QRect(10, 20, 661, 291))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setLineWrapMode(QtGui.QTextEdit.NoWrap)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setGeometry(QtCore.QRect(250, 0, 431, 77))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.plainTextEdit_2 = QtGui.QPlainTextEdit(self.groupBox_4)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.plainTextEdit_2.setObjectName(_fromUtf8("plainTextEdit_2"))
        self.pushButton_2 = QtGui.QPushButton(self.groupBox_4)
        self.pushButton_2.setGeometry(QtCore.QRect(380, 20, 41, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.groupBox_5 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_5.setGeometry(QtCore.QRect(0, 0, 251, 77))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.radioButton_3 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_3.setChecked(True)
        self.radioButton_3.setObjectName(_fromUtf8("radioButton_3"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_4.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.label_4 = QtGui.QLabel(self.groupBox_5)
        self.label_4.setGeometry(QtCore.QRect(120, 10, 16, 16))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.lineEdit_4 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_4.setGeometry(QtCore.QRect(130, 10, 113, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setGeometry(QtCore.QRect(120, 30, 16, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lineEdit_5 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 30, 113, 20))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setGeometry(QtCore.QRect(120, 50, 16, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_6 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_6.setGeometry(QtCore.QRect(130, 50, 41, 20))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(self.groupBox_5)
        self.lineEdit_7.setGeometry(QtCore.QRect(200, 50, 41, 20))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setGeometry(QtCore.QRect(190, 50, 16, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.groupBox_6 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_6.setGeometry(QtCore.QRect(0, 80, 681, 321))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.textBrowser_2 = QtGui.QTextBrowser(self.groupBox_6)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 20, 661, 291))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.groupBox_7 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_7.setGeometry(QtCore.QRect(250, 0, 431, 77))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.plainTextEdit_3 = QtGui.QPlainTextEdit(self.groupBox_7)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(10, 20, 361, 51))
        self.plainTextEdit_3.setObjectName(_fromUtf8("plainTextEdit_3"))
        self.pushButton_3 = QtGui.QPushButton(self.groupBox_7)
        self.pushButton_3.setGeometry(QtCore.QRect(380, 20, 41, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.groupBox_8 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_8.setGeometry(QtCore.QRect(0, 0, 251, 77))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.radioButton_5 = QtGui.QRadioButton(self.groupBox_8)
        self.radioButton_5.setGeometry(QtCore.QRect(10, 20, 82, 17))
        self.radioButton_5.setChecked(True)
        self.radioButton_5.setObjectName(_fromUtf8("radioButton_5"))
        self.radioButton_6 = QtGui.QRadioButton(self.groupBox_8)
        self.radioButton_6.setGeometry(QtCore.QRect(10, 40, 82, 17))
        self.radioButton_6.setObjectName(_fromUtf8("radioButton_6"))
        self.label_8 = QtGui.QLabel(self.groupBox_8)
        self.label_8.setGeometry(QtCore.QRect(120, 20, 16, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lineEdit_8 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_8.setGeometry(QtCore.QRect(130, 20, 113, 20))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.label_9 = QtGui.QLabel(self.groupBox_8)
        self.label_9.setGeometry(QtCore.QRect(120, 40, 16, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lineEdit_9 = QtGui.QLineEdit(self.groupBox_8)
        self.lineEdit_9.setGeometry(QtCore.QRect(130, 40, 113, 20))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.groupBox_9 = QtGui.QGroupBox(self.tab_3)
        self.groupBox_9.setGeometry(QtCore.QRect(0, 80, 681, 321))
        self.groupBox_9.setObjectName(_fromUtf8("groupBox_9"))
        self.textBrowser_3 = QtGui.QTextBrowser(self.groupBox_9)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 20, 661, 291))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.gridlayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Encryption System", None))
        self.groupBox_2.setTitle(_translate("MainWindow", "Input Text", None))
        self.pushButton.setText(_translate("MainWindow", "OK", None))
        self.groupBox.setTitle(_translate("MainWindow", "Settings", None))
        self.radioButton.setText(_translate("MainWindow", "Encrypt", None))
        self.radioButton_2.setText(_translate("MainWindow", "Decrypt", None))
        self.label.setText(_translate("MainWindow", "p", None))
        self.label_2.setText(_translate("MainWindow", "q", None))
        self.label_3.setText(_translate("MainWindow", "e", None))
        self.groupBox_3.setTitle(_translate("MainWindow", "Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "RSA", None))
        self.groupBox_4.setTitle(_translate("MainWindow", "Input Text", None))
        self.pushButton_2.setText(_translate("MainWindow", "OK", None))
        self.groupBox_5.setTitle(_translate("MainWindow", "Settings", None))
        self.radioButton_3.setText(_translate("MainWindow", "Encrypt", None))
        self.radioButton_4.setText(_translate("MainWindow", "Decrypt", None))
        self.label_4.setText(_translate("MainWindow", "p", None))
        self.label_5.setText(_translate("MainWindow", "g", None))
        self.label_6.setText(_translate("MainWindow", "x", None))
        self.label_7.setText(_translate("MainWindow", "k", None))
        self.groupBox_6.setTitle(_translate("MainWindow", "Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "ElGamal", None))
        self.groupBox_7.setTitle(_translate("MainWindow", "Input Text", None))
        self.pushButton_3.setText(_translate("MainWindow", "OK", None))
        self.groupBox_8.setTitle(_translate("MainWindow", "Settings", None))
        self.radioButton_5.setText(_translate("MainWindow", "Encrypt", None))
        self.radioButton_6.setText(_translate("MainWindow", "Decrypt", None))
        self.label_8.setText(_translate("MainWindow", "p", None))
        self.label_9.setText(_translate("MainWindow", "q", None))
        self.groupBox_9.setTitle(_translate("MainWindow", "Output", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Rabin", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Williams", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "Diffie-Hellman", None))
        
    def updateUi(self):
        pass

