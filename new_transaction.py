# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_transaction.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QDateEdit,
    QDialog, QFrame, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import res_nw_window

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(302, 322)
        Dialog.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:0, angle:82.1, stop:0 rgba(166, 140, 41, 255), stop:0.261364 rgba(204, 181, 74, 255), stop:0.267045 rgba(245, 236, 112, 255), stop:0.295455 rgba(235, 219, 102, 255), stop:0.528409 rgba(208, 231, 78, 255), stop:0.556818 rgba(168, 142, 42, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.58183 rgba(218, 202, 86, 255), stop:0.837526 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255));\n"
"font-family: Forte")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_new_transaction = QLabel(self.frame)
        self.lbl_new_transaction.setObjectName(u"lbl_new_transaction")
        self.lbl_new_transaction.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_new_transaction)

        self.cb_choose_category = QComboBox(self.frame)
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.addItem("")
        self.cb_choose_category.setObjectName(u"cb_choose_category")
        self.cb_choose_category.setStyleSheet(u"QComboBox {\n"
"font-size: 16pt;\n"
"color: black;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"\n"
"}")

        self.verticalLayout.addWidget(self.cb_choose_category)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"font-size: 16px;\n"
"color: black;\n"
"padding-lift: 10px;\n"
"height: 30px;\n"
"")
        self.data.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.data.setDateTime(QDateTime(QDate(2023, 3, 31), QTime(8, 0, 0)))

        self.verticalLayout.addWidget(self.data)

        self.le_discription = QLineEdit(self.frame)
        self.le_discription.setObjectName(u"le_discription")
        self.le_discription.setStyleSheet(u"font-size: 16px;\n"
"color: black;\n"
"padding-lift: 10px;\n"
"height: 30px;\n"
"")

        self.verticalLayout.addWidget(self.le_discription)

        self.le2_balance = QLineEdit(self.frame)
        self.le2_balance.setObjectName(u"le2_balance")
        self.le2_balance.setStyleSheet(u"font-size: 16px;\n"
"color: black;\n"
"padding-lift: 10px;\n"
"height: 30px;\n"
"")

        self.verticalLayout.addWidget(self.le2_balance)

        self.cb2_jncome = QComboBox(self.frame)
        self.cb2_jncome.addItem("")
        self.cb2_jncome.addItem("")
        self.cb2_jncome.setObjectName(u"cb2_jncome")
        self.cb2_jncome.setStyleSheet(u"font-size: 16px;\n"
"color: black;\n"
"padding-lift: 10px;\n"
"height: 30px;\n"
"")

        self.verticalLayout.addWidget(self.cb2_jncome)

        self.pb_save_new_transaction = QPushButton(self.frame)
        self.pb_save_new_transaction.setObjectName(u"pb_save_new_transaction")
        self.pb_save_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: Black;\n"
"background-color: rgba(255 , 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border radius: 3px;\n"
"width: 20px;\n"
"height: 50px;\n"
"font-size: 15pt;\n"
"\n"
"}\n"
"QPushButton: hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton: pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/add_circle_outline_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_save_new_transaction.setIcon(icon)
        self.pb_save_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout.addWidget(self.pb_save_new_transaction)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.cb_choose_category.setCurrentIndex(-1)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.lbl_new_transaction.setText(QCoreApplication.translate("Dialog", u"New transaction", None))
        self.cb_choose_category.setItemText(0, QCoreApplication.translate("Dialog", u"Smartphone", None))
        self.cb_choose_category.setItemText(1, QCoreApplication.translate("Dialog", u"Televisions", None))
        self.cb_choose_category.setItemText(2, QCoreApplication.translate("Dialog", u"Laptops", None))
        self.cb_choose_category.setItemText(3, QCoreApplication.translate("Dialog", u"Other", None))

        self.cb_choose_category.setPlaceholderText(QCoreApplication.translate("Dialog", u"Choose category", None))
        self.le_discription.setPlaceholderText(QCoreApplication.translate("Dialog", u"Discription", None))
        self.le2_balance.setPlaceholderText(QCoreApplication.translate("Dialog", u"Balance", None))
        self.cb2_jncome.setItemText(0, QCoreApplication.translate("Dialog", u"Income", None))
        self.cb2_jncome.setItemText(1, QCoreApplication.translate("Dialog", u"Outcome", None))

        self.pb_save_new_transaction.setText(QCoreApplication.translate("Dialog", u"Save new transaction", None))
    # retranslateUi

