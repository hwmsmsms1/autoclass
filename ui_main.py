# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainrkojgM.ui'
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
    QPushButton, QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(581, 595)
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(-8, -10, 351, 611))
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 120, 291, 441))
        self.label.setStyleSheet(u"background-color:white;\n"
"border-radius: 12px;\n"
"border-width: 3px;\n"
"border-color:rgb(77,77,255);\n"
"border-style:outset;")
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 10, 141, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"background-color:white;\n"
"border-radius:5px;\n"
"")
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(50, 280, 50, 16))
        font1 = QFont()
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.class_data = QLineEdit(Dialog)
        self.class_data.setObjectName(u"class_data")
        self.class_data.setGeometry(QRect(50, 300, 211, 21))
        font2 = QFont()
        font2.setPointSize(7)
        self.class_data.setFont(font2)
        self.class_data.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.classroom_num = QLineEdit(Dialog)
        self.classroom_num.setObjectName(u"classroom_num")
        self.classroom_num.setGeometry(QRect(50, 370, 211, 21))
        self.classroom_num.setFont(font2)
        self.classroom_num.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.start_btn = QPushButton(Dialog)
        self.start_btn.setObjectName(u"start_btn")
        self.start_btn.setGeometry(QRect(120, 520, 81, 21))
        font3 = QFont()
        font3.setPointSize(8)
        font3.setBold(True)
        self.start_btn.setFont(font3)
        self.start_btn.setStyleSheet(u"QPushButton {\n"
"background-color:rgba(77,77,255,0.8);\n"
"border-radius:5px;\n"
"color:white;\n"
"}\n"
"QPushButton:hover {\n"
"background-color:rgba(77,77,255,1);\n"
"}")
        self.url2 = QPushButton(Dialog)
        self.url2.setObjectName(u"url2")
        self.url2.setGeometry(QRect(90, 490, 141, 31))
        font4 = QFont()
        font4.setPointSize(8)
        self.url2.setFont(font4)
        self.url2.setStyleSheet(u"QPushButton {\n"
"border:none;\n"
"background-color:white;\n"
"color:#007bff;\n"
"}\n"
"QPushButton:hover {\n"
"color:#000088;\n"
"}")
        self.class_data2 = QLineEdit(Dialog)
        self.class_data2.setObjectName(u"class_data2")
        self.class_data2.setGeometry(QRect(50, 440, 211, 21))
        self.class_data2.setFont(font2)
        self.class_data2.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 350, 50, 16))
        self.label_5.setFont(font1)
        self.label_6 = QLabel(Dialog)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(50, 420, 71, 16))
        self.label_6.setFont(font1)
        self.label_7 = QLabel(Dialog)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(120, 40, 111, 41))
        font5 = QFont()
        font5.setPointSize(15)
        font5.setBold(True)
        self.label_7.setFont(font5)
        self.label_8 = QLabel(Dialog)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(50, 140, 50, 16))
        self.label_8.setFont(font1)
        self.label_9 = QLabel(Dialog)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 210, 50, 16))
        self.label_9.setFont(font1)
        self.eclass_id = QLineEdit(Dialog)
        self.eclass_id.setObjectName(u"eclass_id")
        self.eclass_id.setGeometry(QRect(50, 160, 211, 21))
        self.eclass_id.setFont(font2)
        self.eclass_id.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.eclass_pw = QLineEdit(Dialog)
        self.eclass_pw.setObjectName(u"eclass_pw")
        self.eclass_pw.setGeometry(QRect(50, 230, 211, 21))
        self.eclass_pw.setFont(font2)
        self.eclass_pw.setStyleSheet(u"border-radius:5px;\n"
"border: solid 1px #f3f3f3;\n"
"background-color:#f3f3f3")
        self.eclass_pw.setEchoMode(QLineEdit.Password)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\ud559\ubc88(\uc778\uc99d\ud0a4)", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\uac15\uc758\uba85", None))
        self.class_data.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uac15\uc758\uba85\uc744 \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.classroom_num.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uc22b\uc790\ub9cc \uc801\uc5b4\uc8fc\uc138\uc694.", None))
        self.start_btn.setText(QCoreApplication.translate("Dialog", u"\uc2dc\uc791", None))
        self.url2.setText(QCoreApplication.translate("Dialog", u"\uac00\uc774\ub4dc\ub77c\uc778 \ud398\uc774\uc9c0", None))
        self.class_data2.setText("")
        self.class_data2.setPlaceholderText(QCoreApplication.translate("Dialog", u"\uc2f8\uac15\uc774 \uba87 \ubc88\uc9f8 \uc21c\ubc88\uc5d0 \uc788\ub294 \uc9c0 \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\uac15\uc758 \ubc88\ud638", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\uac15\uc758\uc2e4 \ubc88\ud638", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\uba54\uc778 \ud398\uc774\uc9c0", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\ud559\ubc88", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\ube44\ubc00\ubc88\ud638", None))
        self.eclass_id.setPlaceholderText(QCoreApplication.translate("Dialog", u"E-class \uc544\uc774\ub514\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
        self.eclass_pw.setPlaceholderText(QCoreApplication.translate("Dialog", u"E-class \ube44\ubc00\ubc88\ud638\ub97c \uc785\ub825\ud574\uc8fc\uc138\uc694", None))
    # retranslateUi

