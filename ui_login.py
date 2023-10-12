# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'logincYbYgf.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(271, 465)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-20, -30, 291, 501))
        self.label.setStyleSheet(u"background-color:white;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 90, 271, 41))
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(50, 160, 41, 16))
        font1 = QFont()
        font1.setFamilies([u"\ub9d1\uc740 \uace0\ub515"])
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 220, 50, 16))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.label_4.setFont(font2)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 280, 50, 16))
        self.label_5.setFont(font2)
        self.account_id = QLineEdit(Dialog)
        self.account_id.setObjectName(u"account_id")
        self.account_id.setGeometry(QRect(50, 180, 171, 21))
        font3 = QFont()
        font3.setPointSize(7)
        self.account_id.setFont(font3)
        self.account_id.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.account_key = QLineEdit(Dialog)
        self.account_key.setObjectName(u"account_key")
        self.account_key.setGeometry(QRect(50, 300, 171, 21))
        self.account_key.setFont(font3)
        self.account_key.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.account_key.setEchoMode(QLineEdit.Normal)
        self.account_pw = QLineEdit(Dialog)
        self.account_pw.setObjectName(u"account_pw")
        self.account_pw.setGeometry(QRect(50, 240, 171, 21))
        self.account_pw.setFont(font3)
        self.account_pw.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.account_pw.setEchoMode(QLineEdit.Password)
        self.login_btn = QPushButton(Dialog)
        self.login_btn.setObjectName(u"login_btn")
        self.login_btn.setGeometry(QRect(50, 370, 81, 21))
        font4 = QFont()
        font4.setPointSize(8)
        font4.setBold(True)
        self.login_btn.setFont(font4)
        self.login_btn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(77,77,255,0.8);\n"
"border-radius:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(77,77,255,1);\n"
"}")
        self.key_btn = QPushButton(Dialog)
        self.key_btn.setObjectName(u"key_btn")
        self.key_btn.setGeometry(QRect(140, 370, 81, 21))
        self.key_btn.setFont(font4)
        self.key_btn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(77,77,255,0.8);\n"
"border-radius:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(77,77,255,1);\n"
"}")
        self.radioButton = QRadioButton(Dialog)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(50, 330, 101, 16))
        font5 = QFont()
        font5.setPointSize(8)
        font5.setBold(False)
        self.radioButton.setFont(font5)
        self.url1 = QPushButton(Dialog)
        self.url1.setObjectName(u"url1")
        self.url1.setGeometry(QRect(70, 420, 141, 31))
        font6 = QFont()
        font6.setPointSize(8)
        self.url1.setFont(font6)
        self.url1.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color:white;\n"
"color:#007bff;\n"
"}\n"
"QPushButton:hover {\n"
"color:#000088;\n"
"}")
        self.main_logo = QLabel(Dialog)
        self.main_logo.setObjectName(u"main_logo")
        self.main_logo.setGeometry(QRect(100, 20, 71, 51))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\uc0ac\uc774\ubc84 \uac15\uc758 \uc790\ub3d9\ud654 BOT", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\uc544\uc774\ub514", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\ube44\ubc00\ubc88\ud638", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\uc778\uc99d\ud0a4", None))
        self.account_id.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.account_key.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uc778\uc99d\ud0a4\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.account_pw.setPlaceholderText(QCoreApplication.translate("Dialog", u"\ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.login_btn.setText(QCoreApplication.translate("Dialog", u"\ub85c\uadf8\uc778", None))
        self.key_btn.setText(QCoreApplication.translate("Dialog", u"\uc778\uc99d\ud0a4 \ucc3e\uae30", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"\uacc4\uc815 \uae30\uc5b5\ud558\uae30", None))
        self.url1.setText(QCoreApplication.translate("Dialog", u"E-Class \ud648\ud398\uc774\uc9c0 \uc774\ub3d9\ud558\uae30", None))
        self.main_logo.setText("")
    # retranslateUi

