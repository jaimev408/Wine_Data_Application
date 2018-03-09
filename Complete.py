# To Run This app, please install PyQt5
# You can install it through the command prompt with the command "conda install pyqt" or "conda update pyqt"

import sqlite3
import seaborn
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import pandas as pd
import scipy.stats
from pylab import savefig

import sys
from PyQt5 import QtCore, QtGui, QtWidgets

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Lalo\Anaconda3\Library\bin\UI\contactUs.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class faq(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 50, 771, 61))
        font = QtGui.QFont()
        font.setFamily("Papyrus")
        font.setPointSize(14)
        font.setItalic(True)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 160, 221, 61))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 671, 101))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 290, 321, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 511, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 380, 451, 61))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 420, 631, 81))
        self.label_7.setScaledContents(True)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "FREQUENTLY ASKED QUESTIONS"))
        self.label_2.setText(_translate("MainWindow", "Question: What is residual sugar?\n"
""))
        self.label_3.setText(_translate("MainWindow", "Residual Sugar, or RS is any sugar that is leftover from the fermentation process.\n"
""))
        self.label_4.setText(_translate("MainWindow", "What are fixed acids in wine?\n"
""))
        self.label_5.setText(_translate("MainWindow", " The predominant fixed acids found in wines are tartaric, malic, citric, and succinic."))
        self.label_6.setText(_translate("MainWindow", "What is volatile acidity? \n"
""))
        self.label_7.setText(_translate("MainWindow", "Volatile acidity (VA) is a measure of the wine’s volatile (or gaseous) acids. The primary volatile acid in wine is acetic acid, which is also the primary acid associated with the smell and taste of vinegar."))


class faqControl(QtWidgets.QMainWindow, faq):
    def __init__(self):
        super(faqControl, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)

class contact(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(537, 698)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.contactUsImage = QtWidgets.QLabel(self.centralwidget)
        self.contactUsImage.setGeometry(QtCore.QRect(110, 20, 301, 101))
        self.contactUsImage.setText("")
        self.contactUsImage.setObjectName("contactUsImage")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 160, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 230, 461, 131))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 420, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 480, 481, 121))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setWordWrap(True)
        self.label_4.setObjectName("label_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 537, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Contact Us"))
        self.label_2.setText(_translate("MainWindow", "John Merlot\n"
"J.Merlot@wine.com\n"
"555 Chardonnay Way\n"
"San Jose,  95123\n"
""))
        self.label_3.setText(_translate("MainWindow", "Questions? Comments? Concerns?"))
        self.label_4.setText(_translate("MainWindow", "Share your thoughts about WineTracker5000® visit, or any questions you might have. We\'d love to hear what you have to say! Or, to speak with Guest Relations by phone, please call 1-866-444-5144"))

class contactControl(QtWidgets.QMainWindow, contact):
    def __init__(self):
        super(contactControl, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(753, 500)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Storage/Desktop/110a/110a/168570.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(5, 60, 741, 40))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.loginGroupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.loginGroupBox.setGeometry(QtCore.QRect(225, 200, 301, 161))
        self.loginGroupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.loginGroupBox.setMouseTracking(True)
        self.loginGroupBox.setTitle("")
        self.loginGroupBox.setObjectName("loginGroupBox")
        self.label_3 = QtWidgets.QLabel(self.loginGroupBox)
        self.label_3.setGeometry(QtCore.QRect(10, 40, 121, 61))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.loginGroupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 0, 111, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.label_2.setPalette(palette)
        self.label_2.setObjectName("label_2")
        self.loginButton = QtWidgets.QPushButton(self.loginGroupBox)
        self.loginButton.setGeometry(QtCore.QRect(170, 100, 111, 51))
        self.loginButton.setDefault(True)
        self.loginButton.setObjectName("loginButton")
        self.clearButton = QtWidgets.QPushButton(self.loginGroupBox)
        self.clearButton.setGeometry(QtCore.QRect(20, 100, 111, 51))
        self.clearButton.setObjectName("clearButton")
        self.passwordInput = QtWidgets.QLineEdit(self.loginGroupBox)
        self.passwordInput.setGeometry(QtCore.QRect(130, 60, 150, 20))
        self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordInput.setObjectName("passwordInput")
        self.emailInput = QtWidgets.QLineEdit(self.loginGroupBox)
        self.emailInput.setGeometry(QtCore.QRect(130, 10, 150, 20))
        self.emailInput.setClearButtonEnabled(False)
        self.emailInput.setObjectName("emailInput")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 753, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setToolTipDuration(-1)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionContact_Us = QtWidgets.QAction(MainWindow)
        self.actionContact_Us.setObjectName("actionContact_Us")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionContact_Us)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wine Tracker  5000"))
        self.label.setText(_translate("MainWindow", "WELCOME TO THE WINE SHOP"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email</span></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.clearButton.setText(_translate("MainWindow", "Show Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the app"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionContact_Us.setText(_translate("MainWindow", "Contact Us"))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Wine Tracker  5000"))
        self.label.setText(_translate("MainWindow", "WELCOME TO THE WINE SHOP"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Email</span></p></body></html>"))
        self.loginButton.setText(_translate("MainWindow", "Log In"))
        self.clearButton.setText(_translate("MainWindow", "Show Password"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setStatusTip(_translate("MainWindow", "Exit the app"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionContact_Us.setText(_translate("MainWindow", "Contact Us"))




class mainWindowShow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(mainWindowShow, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)
        self.show()

        self.loginButton.clicked.connect(self.loginButtonHandler)
        self.clearButton.clicked.connect(self.showPassword)
        self.actionExit.triggered.connect(self.closeApplication)

    def closeApplication(self):
        choice = QtWidgets.QMessageBox.question(self, 'Goodbye!', "Are you sure you want to Exit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass

    def showPassword(self):
        if self.passwordInput.echoMode() == 2:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Normal)
            self.clearButton.setText("Hide Password")
        else:
            self.passwordInput.setEchoMode(QtWidgets.QLineEdit.Password)
            self.clearButton.setText("Show Password")


    def loginButtonHandler(self):
        conn = sqlite3.connect('LevinEmployee.db')

        email = self.emailInput.text()
        password = self.passwordInput.text()

        with conn:

            try:
                cur = conn.cursor()
                cur.execute("SELECT COUNT(EmployeeID) FROM Employee WHERE Email = '" + email + "' AND Password = '" + password + "';")
                count = cur.fetchone()

                if email == "" and password == "":
                    QtWidgets.QMessageBox.warning(self, 'Could not Log In', "Usermame and Password Missing")

                elif email == "":
                    QtWidgets.QMessageBox.warning(self, 'Could not Log In', "Usermame Missing", QtWidgets.QMessageBox.Retry)
                elif password == "":
                    QtWidgets.QMessageBox.warning(self, 'Could not Log In', "Password Missing", QtWidgets.QMessageBox.Retry)
                elif count[0] == 0:
                    QtWidgets.QMessageBox.warning(self, 'Could not Log In', "Invalid Account", QtWidgets.QMessageBox.Retry)
                else:

                    self.ui = mainMenuControl()
                    self.ui.show()
                    self.hide()

            except:
                QtWidgets.QMessageBox.critical(self, 'CONNECTION ERROR!', "No database connection", QtWidgets.QMessageBox.Ok)

class mainMenu(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(791, 577)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("D:/Storage/Desktop/110a/110a/168570.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(9, 9, 781, 541))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.groupBox = QtWidgets.QGroupBox(self.page)
        self.groupBox.setGeometry(QtCore.QRect(50, 170, 320, 350))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(10, 10, 301, 41))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setScaledContents(True)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.registerButton = QtWidgets.QPushButton(self.groupBox)
        self.registerButton.setGeometry(QtCore.QRect(90, 80, 129, 81))
        self.registerButton.setObjectName("registerButton")
        self.pushButton_3 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 200, 131, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.page)
        self.groupBox_2.setGeometry(QtCore.QRect(410, 170, 320, 350))
        self.groupBox_2.setTitle("")
        self.groupBox_2.setObjectName("groupBox_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 301, 51))
        font = QtGui.QFont()
        font.setFamily("MV Boli")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setScaledContents(True)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label_3")
        self.wineStatsButton = QtWidgets.QPushButton(self.groupBox_2)
        self.wineStatsButton.setGeometry(QtCore.QRect(90, 80, 141, 81))
        self.wineStatsButton.setObjectName("wineStatsButton")
        self.inputWineStats = QtWidgets.QPushButton(self.groupBox_2)
        self.inputWineStats.setGeometry(QtCore.QRect(90, 200, 141, 81))
        self.inputWineStats.setObjectName("inputWineStats")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.page_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(150, 110, 491, 251))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setHorizontalSpacing(100)
        self.formLayout.setVerticalSpacing(5)
        self.formLayout.setObjectName("formLayout")
        self.regIDLabel = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.regIDLabel.setFont(font)
        self.regIDLabel.setObjectName("regIDLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.regIDLabel)
        self.lineEdit = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.lineEdit_9)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.lineEdit_10)
        self.label_12 = QtWidgets.QLabel(self.page_2)
        self.label_12.setGeometry(QtCore.QRect(0, 30, 771, 51))
        font = QtGui.QFont()
        font.setFamily("Lucida Calligraphy")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setScaledContents(True)
        self.label_12.setAlignment(QtCore.Qt.AlignCenter)
        self.label_12.setWordWrap(True)
        self.label_12.setObjectName("label_12")
        self.regConfirmButton = QtWidgets.QPushButton(self.page_2)
        self.regConfirmButton.setGeometry(QtCore.QRect(330, 390, 121, 71))
        self.regConfirmButton.setObjectName("regConfirmButton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_13 = QtWidgets.QLabel(self.page_3)
        self.label_13.setGeometry(QtCore.QRect(10, 30, 761, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setScaledContents(True)
        self.label_13.setAlignment(QtCore.Qt.AlignCenter)
        self.label_13.setWordWrap(True)
        self.label_13.setObjectName("label_13")
        self.groupBox_3 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_3.setGeometry(QtCore.QRect(50, 90, 261, 101))
        self.groupBox_3.setObjectName("groupBox_3")
        self.redWineChoice1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.redWineChoice1.setGeometry(QtCore.QRect(20, 20, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.redWineChoice1.setFont(font)
        self.redWineChoice1.setObjectName("redWineChoice1")
        self.whiteWineChoice1 = QtWidgets.QRadioButton(self.groupBox_3)
        self.whiteWineChoice1.setGeometry(QtCore.QRect(20, 60, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.whiteWineChoice1.setFont(font)
        self.whiteWineChoice1.setObjectName("whiteWineChoice1")
        self.groupBox_4 = QtWidgets.QGroupBox(self.page_3)
        self.groupBox_4.setGeometry(QtCore.QRect(50, 200, 261, 201))
        self.groupBox_4.setObjectName("groupBox_4")
        self.radioButton = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton.setGeometry(QtCore.QRect(20, 0, 231, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton.setFont(font)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_2.setGeometry(QtCore.QRect(20, 60, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_2.setFont(font)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_3.setGeometry(QtCore.QRect(20, 90, 231, 61))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_3.setFont(font)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.groupBox_4)
        self.radioButton_4.setGeometry(QtCore.QRect(20, 120, 221, 81))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_4.setFont(font)
        self.radioButton_4.setObjectName("radioButton_4")
        self.statsButton = QtWidgets.QPushButton(self.page_3)
        self.statsButton.setGeometry(QtCore.QRect(110, 410, 131, 51))
        self.statsButton.setObjectName("statsButton")
        self.DataLabel = QtWidgets.QLabel(self.page_3)
        self.DataLabel.setGeometry(QtCore.QRect(360, 100, 381, 401))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.DataLabel.setFont(font)
        self.DataLabel.setText("")
        self.DataLabel.setWordWrap(True)
        self.DataLabel.setObjectName("DataLabel")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_15 = QtWidgets.QLabel(self.page_4)
        self.label_15.setGeometry(QtCore.QRect(0, 30, 761, 61))
        font = QtGui.QFont()
        font.setFamily("Snap ITC")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setScaledContents(True)
        self.label_15.setAlignment(QtCore.Qt.AlignCenter)
        self.label_15.setWordWrap(True)
        self.label_15.setObjectName("label_15")
        self.groupBox_5 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_5.setGeometry(QtCore.QRect(50, 140, 261, 101))
        self.groupBox_5.setObjectName("groupBox_5")
        self.redWineChoice1_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.redWineChoice1_2.setGeometry(QtCore.QRect(20, 10, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.redWineChoice1_2.setFont(font)
        self.redWineChoice1_2.setObjectName("redWineChoice1_2")
        self.whiteWineChoice1_2 = QtWidgets.QRadioButton(self.groupBox_5)
        self.whiteWineChoice1_2.setGeometry(QtCore.QRect(20, 46, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.whiteWineChoice1_2.setFont(font)
        self.whiteWineChoice1_2.setObjectName("whiteWineChoice1_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.page_4)
        self.groupBox_6.setGeometry(QtCore.QRect(50, 260, 261, 201))
        self.groupBox_6.setObjectName("groupBox_6")
        self.radioButton_5 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_5.setGeometry(QtCore.QRect(20, 20, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_5.setFont(font)
        self.radioButton_5.setObjectName("radioButton_5")
        self.radioButton_6 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_6.setGeometry(QtCore.QRect(20, 60, 251, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_6.setFont(font)
        self.radioButton_6.setObjectName("radioButton_6")
        self.radioButton_7 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_7.setGeometry(QtCore.QRect(20, 100, 271, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_7.setFont(font)
        self.radioButton_7.setObjectName("radioButton_7")
        self.radioButton_8 = QtWidgets.QRadioButton(self.groupBox_6)
        self.radioButton_8.setGeometry(QtCore.QRect(20, 140, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        self.radioButton_8.setFont(font)
        self.radioButton_8.setObjectName("radioButton_8")
        self.label = QtWidgets.QLabel(self.page_4)
        self.label.setGeometry(QtCore.QRect(320, 140, 281, 61))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setScaledContents(True)
        self.label.setWordWrap(True)
        self.label.setObjectName("label")
        self.lineEdit_11 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_11.setGeometry(QtCore.QRect(610, 150, 111, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_16 = QtWidgets.QLabel(self.page_4)
        self.label_16.setGeometry(QtCore.QRect(320, 200, 281, 51))
        font = QtGui.QFont()
        font.setFamily("MS Reference Sans Serif")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_16.setFont(font)
        self.label_16.setScaledContents(True)
        self.label_16.setWordWrap(True)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.page_4)
        self.label_17.setGeometry(QtCore.QRect(330, 300, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setText("")
        self.label_17.setWordWrap(True)
        self.label_17.setObjectName("label_17")
        self.lineEdit_12 = QtWidgets.QLineEdit(self.page_4)
        self.lineEdit_12.setGeometry(QtCore.QRect(610, 220, 113, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.pushButton = QtWidgets.QPushButton(self.page_4)
        self.pushButton.setGeometry(QtCore.QRect(360, 400, 121, 61))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.page_4)
        self.pushButton_2.setGeometry(QtCore.QRect(560, 400, 111, 61))
        self.pushButton_2.setObjectName("pushButton_2")
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 791, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionFAQ = QtWidgets.QAction(MainWindow)
        self.actionFAQ.setObjectName("actionFAQ")
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionFAQ)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "User Options"))
        self.registerButton.setText(_translate("MainWindow", "Register New User"))
        self.pushButton_3.setText(_translate("MainWindow", "Contact Us"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Wine Data</span></p></body></html>"))
        self.wineStatsButton.setText(_translate("MainWindow", "View Wine Statistics"))
        self.inputWineStats.setText(_translate("MainWindow", "View Stats by Input"))
        self.regIDLabel.setText(_translate("MainWindow", "ID"))
        self.label_4.setText(_translate("MainWindow", "First Name"))
        self.label_5.setText(_translate("MainWindow", "Last Name"))
        self.label_6.setText(_translate("MainWindow", "Address"))
        self.label_7.setText(_translate("MainWindow", "City"))
        self.label_8.setText(_translate("MainWindow", "State"))
        self.label_9.setText(_translate("MainWindow", "Zip Code"))
        self.label_10.setText(_translate("MainWindow", "Email"))
        self.label_11.setText(_translate("MainWindow", "Password"))
        self.label_14.setText(_translate("MainWindow", "Retype Password"))
        self.label_12.setText(_translate("MainWindow", "Registration Page"))
        self.regConfirmButton.setText(_translate("MainWindow", "Register New User"))
        self.label_13.setText(_translate("MainWindow", "Summary of Statistics"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Choose One"))
        self.redWineChoice1.setText(_translate("MainWindow", "Red Wine"))
        self.whiteWineChoice1.setText(_translate("MainWindow", "White Wine"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Choose One"))
        self.radioButton.setText(_translate("MainWindow", "Volatie Acidity"))
        self.radioButton_2.setText(_translate("MainWindow", "Fixed Acidity"))
        self.radioButton_3.setText(_translate("MainWindow", "Alocohol Percentage"))
        self.radioButton_4.setText(_translate("MainWindow", "Residual Sugar"))
        self.statsButton.setText(_translate("MainWindow", "Calculate"))
        self.label_15.setText(_translate("MainWindow", "User Input Values"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Choose One"))
        self.redWineChoice1_2.setText(_translate("MainWindow", "Red Wine"))
        self.whiteWineChoice1_2.setText(_translate("MainWindow", "White Wine"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Choose One"))
        self.radioButton_5.setText(_translate("MainWindow", "Volatie Acidity"))
        self.radioButton_6.setText(_translate("MainWindow", "Fixed Acidity"))
        self.radioButton_7.setText(_translate("MainWindow", "Alocohol Percentage"))
        self.radioButton_8.setText(_translate("MainWindow", "Residual Sugar"))
        self.label.setText(_translate("MainWindow", "MAX Value Searching For:"))
        self.label_16.setText(_translate("MainWindow", "MIN Value Searching For:"))
        self.pushButton.setText(_translate("MainWindow", "View Ranges"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate Graph"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+Q"))
        self.actionFAQ.setText(_translate("MainWindow", "FAQ"))



class mainMenuControl(QtWidgets.QMainWindow, mainMenu):
    def __init__(self):
        super(mainMenuControl, self).__init__()

        self.setupUi(self)
        self.retranslateUi(self)

        label = QtWidgets.QLabel(self.page)
        pixmap = QtGui.QPixmap("welcome")

        label.setPixmap(pixmap)
        label.move(225, 0)

        extractAction = QtWidgets.QAction(QtGui.QIcon('200.png'), 'Home', self)
        extractAction2 = QtWidgets.QAction(QtGui.QIcon('reg'), 'Register Page', self)
        extractAction3 = QtWidgets.QAction(QtGui.QIcon('stat'), 'Stats Page', self)
        extractAction4 = QtWidgets.QAction(QtGui.QIcon('input'), 'Input Stats Page', self)
        extractAction.setStatusTip('Go Home')
        extractAction2.setStatusTip('Go To Register Page')
        extractAction3.setStatusTip('Go To Stats Page')
        extractAction4.setStatusTip('Go To Input Stats Page')
        extractAction.triggered.connect(self.goHome)
        extractAction2.triggered.connect(self.register)
        extractAction3.triggered.connect(self.wineStats)
        extractAction4.triggered.connect(self.goInput)


        toolBar = self.addToolBar("Extraction")
        toolBar.addAction(extractAction)
        toolBar.addAction(extractAction2)
        toolBar.addAction(extractAction3)
        toolBar.addAction(extractAction4)

        self.actionExit.triggered.connect(self.close_application)

        self.registerButton.clicked.connect(self.register)
        self.wineStatsButton.clicked.connect(self.wineStats)

        # User Registration Button
        self.regConfirmButton.clicked.connect(self.regConfirm)

        # Wine Data Button
        self.statsButton.clicked.connect(self.wineStatsShow)

        # wine stats button
        self.inputWineStats.clicked.connect(self.goInput)

        self.pushButton.clicked.connect(self.statsRange)

        self.pushButton_2.clicked.connect(self.inputStats)

        self.pushButton_3.clicked.connect(self.contact)

        self.actionFAQ.triggered.connect(self.faq)


        self.show()

    def faq(self):
        self.ui = faqControl()
        self.ui.show()

    def contact(self):
        self.ui = contactControl()
        self.ui.show()

    def goHome(self):
        self.stackedWidget.setCurrentIndex(0)

    def register(self):
        self.stackedWidget.setCurrentIndex(1)

    def goInput(self):
        self.stackedWidget.setCurrentIndex(3)

    def statsRange(self):
        wineColor = ""
        WineChar = ""

        if self.redWineChoice1_2.isChecked():
            wineColor ="red"

        if self.whiteWineChoice1_2.isChecked():
            wineColor = "white"

        if self.radioButton_5.isChecked():
            WineChar = "volatile acidity"

        if self.radioButton_6.isChecked():
            WineChar = "fixed acidity"

        if self.radioButton_7.isChecked():
            WineChar = "alcohol"

        if self.radioButton_8.isChecked():
            WineChar = "residual sugar"

        if wineColor == "" or WineChar == "":
                QtWidgets.QMessageBox.warning(self, 'Wrong Data', "Both Left Hand values must be filled", QtWidgets.QMessageBox.Retry)
                return
        else:
            allWines = pd.read_csv('winequality-both.csv')

            wine = allWines.loc[allWines['type'] == wineColor, :]

            message = "The ranges for are:\nMin: " + str(wine[WineChar].min()) + "\tMax: " + str(wine[WineChar].max())

            self.label_17.setText(message)

    def inputStats(self):
        wineColor = ""
        WineChar = ""
        WineChar2 = 'quality'

        if self.lineEdit_11.text() == "" or self.lineEdit_12 == "":
            QtWidgets.QMessageBox.warning(self, 'Wrong Data', "Both Input Values must be Entered", QtWidgets.QMessageBox.Retry)
            return

        if self.redWineChoice1_2.isChecked():
            wineColor ="red"

        if self.whiteWineChoice1_2.isChecked():
            wineColor = "white"

        if self.radioButton_5.isChecked():
            WineChar = "volatile acidity"

        if self.radioButton_6.isChecked():
            WineChar = "fixed acidity"

        if self.radioButton_7.isChecked():
            WineChar = "alcohol"

        if self.radioButton_8.isChecked():
            WineChar = "residual sugar"

        if wineColor == "" or WineChar == "":
                QtWidgets.QMessageBox.warning(self, 'Wrong Data', "Both Left Hand values must be filled", QtWidgets.QMessageBox.Retry)
                return

        try:
            maxValue = float(self.lineEdit_11.text())
            minValue = float(self.lineEdit_12.text())
        except:
            QtWidgets.QMessageBox.warning(self, 'Wrong Data', "Input Values Must be Numeric", QtWidgets.QMessageBox.Retry)
            return

        allWines = pd.read_csv('winequality-both.csv')

        wine = allWines.loc[allWines['type'] == wineColor, :]

        RedResidualSugar = wine.loc[(wine[WineChar] >= minValue) & (wine[WineChar] <= maxValue), :]

        if RedResidualSugar.empty:
            QtWidgets.QMessageBox.information(self, 'Sorry...', "No Results Found", QtWidgets.QMessageBox.Retry)
            return

        WineCharValueDataset = RedResidualSugar.loc[:, WineChar2]

        if (WineCharValueDataset.size) == 1:
            plt.hist(WineCharValueDataset, bins=10)
            plt.title(WineChar + " value frequencies by " + WineChar2)

            plt.xlabel(WineChar2)
            plt.ylabel('Number of wines')
            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()

        else:
            seaborn.distplot(WineCharValueDataset, bins=10, kde=False)

            plt.title(WineChar + " value frequencies by " + WineChar2)
            plt.ylabel('Number of wines')

            plt.xticks([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
            plt.show()




    def regConfirm(self):
        # User input validation

        REGISTER_CRITERIA = ['ID', 'First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Email', 'Password']
        count = 0
        count2 = 0

        ID = self.lineEdit.text()
        firstName = self.lineEdit_2.text()
        lastName = self.lineEdit_3.text()
        address = self.lineEdit_4.text()
        city = self.lineEdit_5.text()
        state = self.lineEdit_6.text()
        zipCode = self.lineEdit_7.text()
        email = self.lineEdit_8.text()
        password = self.lineEdit_9.text()
        password2 = self.lineEdit_10.text()

        list = [ID, firstName, lastName, address, city, state, zipCode, email, password]

        for strings in list:
            if strings == "":
                QtWidgets.QMessageBox.warning(self, 'Registration Error', REGISTER_CRITERIA[count] + " cannot be left blank", QtWidgets.QMessageBox.Retry)
                return
            count = count + 1

        if password != password2:
            QtWidgets.QMessageBox.warning(self, 'Registration Error', "Passwords must match.", QtWidgets.QMessageBox.Retry)
            return

        conn = sqlite3.connect('LevinEmployee.db')

        with conn:
            cur = conn.cursor()
            try:
                cur.execute("SELECT * FROM Employee")
                results = cur.fetchall()

                if list[0] in [x[0] for x in results]:
                    QtWidgets.QMessageBox.warning(self, 'Registration Error', "User ID already exists", QtWidgets.QMessageBox.Retry)
                    return

                if list[7] in [x[7] for x in results]:
                    QtWidgets.QMessageBox.warning(self, 'Registration Error', "Email already in use", QtWidgets.QMessageBox.Retry)
                    return

                string = "INSERT INTO Employee VALUES ('"
                for regis in list:
                    string += regis + "', '"

                string = string[:-3] + ")"

                cur.execute(string)
                conn.commit()

                cur.execute("SELECT * FROM Employee WHERE EmployeeID = '" + list[0] + "'")

                results = cur.fetchone()
                print(results[0])
                message2 = "User " + results[0] + " added to system!"
                print(message2)

                QtWidgets.QMessageBox.information(self, 'Registration Complete', message2, QtWidgets.QMessageBox.Ok)

            except sqlite3.Error as e:
                print(e)


    def wineStats(self):
        self.stackedWidget.setCurrentIndex(2)

    def wineStatsShow(self):
        wineColor = ""
        WineCharY = ""
        WineCharX = "quality"

        if self.redWineChoice1.isChecked():
            wineColor ="red"

        if self.whiteWineChoice1.isChecked():
            wineColor = "white"

        if self.radioButton.isChecked():
            WineCharY = "volatile acidity"

        if self.radioButton_2.isChecked():
            WineCharY = "fixed acidity"

        if self.radioButton_3.isChecked():
            WineCharY = "alcohol"

        if self.radioButton_4.isChecked():
            WineCharY = "residual sugar"

        if wineColor == "" or WineCharY == "":
            QtWidgets.QMessageBox.warning(self, 'Wrong Data', "Both values must be filled", QtWidgets.QMessageBox.Retry)
            return

        print(wineColor + "   " + WineCharY)

        allWines = pd.read_csv('winequality-both.csv')

        try:
            wine = allWines.loc[allWines['type'] == wineColor, :]
            getCorr = scipy.stats.spearmanr(wine[WineCharX], wine[WineCharY])
            correlation = str(getCorr[0])
            pValue = str(getCorr[1])
            seaborn.lmplot(x=WineCharX, y=WineCharY, data=wine)
            if WineCharY == "alcohol":
                WineCharY += " percentage"

            message = ("For " + wineColor + " wine, the correlation between " + WineCharX + " and " + WineCharY + " is: " + correlation)
            message += ("\n\nwith p value of: " + pValue)

            plt.xlabel(WineCharX)
            plt.ylabel(WineCharY)
            plt.title(wineColor + " Wine: " + WineCharX + " X " + WineCharY)
            plt.show()

            self.DataLabel.setWordWrap(True)
            self.DataLabel.setText(message)

        except (KeyError) as e:
            print('Please check the spelling of the wine characteristics you want to test')



    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Goodbye!', "Are you sure you want to Exit?", QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            sys.exit()
        else:
            pass



def run():

    app = QtWidgets.QApplication(sys.argv)
    GUI = mainWindowShow()
    # = QtWidgets.QMainWindow()
   # GUI.setupUi(mainWindow)



    app.exec_()

if __name__ == "__main__":
    run()