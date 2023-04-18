# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(628, 507)
        MainWindow.setStyleSheet(u"background-color: qconicalgradient(cx:1, cy:0, angle:82.1, stop:0 rgba(166, 140, 41, 255), stop:0.261364 rgba(204, 181, 74, 255), stop:0.267045 rgba(245, 236, 112, 255), stop:0.295455 rgba(235, 219, 102, 255), stop:0.528409 rgba(208, 231, 78, 255), stop:0.556818 rgba(168, 142, 42, 255), stop:0.57 rgba(187, 156, 51, 255), stop:0.58183 rgba(218, 202, 86, 255), stop:0.837526 rgba(208, 187, 73, 255), stop:0.88 rgba(187, 156, 51, 255), stop:0.935 rgba(137, 108, 26, 255));\n"
"font-family: Forte")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.balance_fr = QFrame(self.centralwidget)
        self.balance_fr.setObjectName(u"balance_fr")
        self.balance_fr.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.balance_fr)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(13, 13, 12, 13)
        self.label_current_balance = QLabel(self.balance_fr)
        self.label_current_balance.setObjectName(u"label_current_balance")
        self.label_current_balance.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_current_balance)

        self.label_balance = QLabel(self.balance_fr)
        self.label_balance.setObjectName(u"label_balance")
        self.label_balance.setStyleSheet(u"\n"
"font-size: 25pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_balance)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_icon_up_arrow = QLabel(self.balance_fr)
        self.label_icon_up_arrow.setObjectName(u"label_icon_up_arrow")
        self.label_icon_up_arrow.setMaximumSize(QSize(24, 16777215))
        self.label_icon_up_arrow.setStyleSheet(u"\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_icon_up_arrow.setPixmap(QPixmap(u":/icon/icon/north_west_black_24dp.svg"))

        self.horizontalLayout.addWidget(self.label_icon_up_arrow)

        self.label_income = QLabel(self.balance_fr)
        self.label_income.setObjectName(u"label_income")
        self.label_income.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout.addWidget(self.label_income)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_income_balance = QLabel(self.balance_fr)
        self.label_income_balance.setObjectName(u"label_income_balance")
        self.label_income_balance.setStyleSheet(u"\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_income_balance)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_down_arrow_icon = QLabel(self.balance_fr)
        self.label_down_arrow_icon.setObjectName(u"label_down_arrow_icon")
        self.label_down_arrow_icon.setMaximumSize(QSize(24, 16777215))
        self.label_down_arrow_icon.setStyleSheet(u"\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")
        self.label_down_arrow_icon.setPixmap(QPixmap(u":/icon/icon/call_received_black_24dp.svg"))

        self.horizontalLayout_2.addWidget(self.label_down_arrow_icon)

        self.label_outcome_balance = QLabel(self.balance_fr)
        self.label_outcome_balance.setObjectName(u"label_outcome_balance")
        self.label_outcome_balance.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;\n"
"padding-top: 10px;")

        self.horizontalLayout_2.addWidget(self.label_outcome_balance)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.label_outcome_balance_2 = QLabel(self.balance_fr)
        self.label_outcome_balance_2.setObjectName(u"label_outcome_balance_2")
        self.label_outcome_balance_2.setStyleSheet(u"\n"
"font-size: 18pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout.addWidget(self.label_outcome_balance_2)


        self.horizontalLayout_7.addWidget(self.balance_fr)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.btn_edit_transaction = QPushButton(self.centralwidget)
        self.btn_edit_transaction.setObjectName(u"btn_edit_transaction")
        self.btn_edit_transaction.setStyleSheet(u"QPushButton {\n"
"color: Black;\n"
"background-color: rgba(255 , 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border radius: 3px;\n"
"width: 20px;\n"
"height: 50px;\n"
"font-size: 8pt;\n"
"\n"
"}\n"
"QPushButton: hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton: pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icon/icon/edit_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_transaction.setIcon(icon)
        self.btn_edit_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_edit_transaction)

        self.btn_new_transaction = QPushButton(self.centralwidget)
        self.btn_new_transaction.setObjectName(u"btn_new_transaction")
        self.btn_new_transaction.setStyleSheet(u"QPushButton {\n"
"color: Black;\n"
"background-color: rgba(255 , 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border radius: 3px;\n"
"width: 20px;\n"
"height: 50px;\n"
"font-size: 8pt;\n"
"}\n"
"QPushButton: hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton: pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icon/icon/add_circle_outline_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_new_transaction.setIcon(icon1)
        self.btn_new_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_new_transaction)

        self.btn_delet_transaction = QPushButton(self.centralwidget)
        self.btn_delet_transaction.setObjectName(u"btn_delet_transaction")
        self.btn_delet_transaction.setStyleSheet(u"QPushButton {\n"
"color: Black;\n"
"background-color: rgba(255 , 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border radius: 3px;\n"
"width: 20px;\n"
"height: 50px;\n"
"font-size: 8pt;\n"
"}\n"
"QPushButton: hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton: pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icon/icon/delete_black_24dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_delet_transaction.setIcon(icon2)
        self.btn_delet_transaction.setIconSize(QSize(24, 24))

        self.verticalLayout_3.addWidget(self.btn_delet_transaction)


        self.horizontalLayout_7.addLayout(self.verticalLayout_3)

        self.cater_fr = QFrame(self.centralwidget)
        self.cater_fr.setObjectName(u"cater_fr")
        self.cater_fr.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.cater_fr)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.label_expense_categories = QLabel(self.cater_fr)
        self.label_expense_categories.setObjectName(u"label_expense_categories")
        self.label_expense_categories.setStyleSheet(u"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: none;\n"
"border: none;")

        self.verticalLayout_2.addWidget(self.label_expense_categories)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_icon_smartphone = QLabel(self.cater_fr)
        self.label_icon_smartphone.setObjectName(u"label_icon_smartphone")
        self.label_icon_smartphone.setMaximumSize(QSize(24, 16777215))
        self.label_icon_smartphone.setStyleSheet(u"background-color: none;\n"
"border: nonel;")
        self.label_icon_smartphone.setPixmap(QPixmap(u":/icon/icon/smartphone_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_6.addWidget(self.label_icon_smartphone)

        self.label_smartphone = QLabel(self.cater_fr)
        self.label_smartphone.setObjectName(u"label_smartphone")
        self.label_smartphone.setStyleSheet(u"\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_smartphone)

        self.label_smartphone_balance = QLabel(self.cater_fr)
        self.label_smartphone_balance.setObjectName(u"label_smartphone_balance")
        self.label_smartphone_balance.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_6.addWidget(self.label_smartphone_balance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_icon_televisions = QLabel(self.cater_fr)
        self.label_icon_televisions.setObjectName(u"label_icon_televisions")
        self.label_icon_televisions.setMaximumSize(QSize(24, 16777215))
        self.label_icon_televisions.setStyleSheet(u"background-color: none;\n"
"border: nonel;")
        self.label_icon_televisions.setPixmap(QPixmap(u":/icon/icon/tv_gen_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_5.addWidget(self.label_icon_televisions)

        self.label_televisions = QLabel(self.cater_fr)
        self.label_televisions.setObjectName(u"label_televisions")
        self.label_televisions.setStyleSheet(u"\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_5.addWidget(self.label_televisions)

        self.label_televisions_balance = QLabel(self.cater_fr)
        self.label_televisions_balance.setObjectName(u"label_televisions_balance")
        self.label_televisions_balance.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_5.addWidget(self.label_televisions_balance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_icon_laptope = QLabel(self.cater_fr)
        self.label_icon_laptope.setObjectName(u"label_icon_laptope")
        self.label_icon_laptope.setMaximumSize(QSize(24, 16777215))
        self.label_icon_laptope.setStyleSheet(u"background-color: none;\n"
"border: nonel;")
        self.label_icon_laptope.setPixmap(QPixmap(u":/icon/icon/laptop_chromebook_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_4.addWidget(self.label_icon_laptope)

        self.label_laptope = QLabel(self.cater_fr)
        self.label_laptope.setObjectName(u"label_laptope")
        self.label_laptope.setStyleSheet(u"\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_4.addWidget(self.label_laptope)

        self.label_laptope_balance = QLabel(self.cater_fr)
        self.label_laptope_balance.setObjectName(u"label_laptope_balance")
        self.label_laptope_balance.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_4.addWidget(self.label_laptope_balance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_icon_other = QLabel(self.cater_fr)
        self.label_icon_other.setObjectName(u"label_icon_other")
        self.label_icon_other.setMaximumSize(QSize(24, 16777215))
        self.label_icon_other.setStyleSheet(u"background-color: none;\n"
"border: nonel;")
        self.label_icon_other.setPixmap(QPixmap(u":/icon/icon/list_FILL0_wght400_GRAD0_opsz24.svg"))

        self.horizontalLayout_3.addWidget(self.label_icon_other)

        self.label_other = QLabel(self.cater_fr)
        self.label_other.setObjectName(u"label_other")
        self.label_other.setStyleSheet(u"\n"
"font-size: 15pt;\n"
"background-color: none;\n"
"border: none;\n"
"")

        self.horizontalLayout_3.addWidget(self.label_other)

        self.label_other_balance = QLabel(self.cater_fr)
        self.label_other_balance.setObjectName(u"label_other_balance")
        self.label_other_balance.setStyleSheet(u"\n"
"font-size: 16pt;\n"
"background-color: none;\n"
"border: none;")

        self.horizontalLayout_3.addWidget(self.label_other_balance)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout_7.addWidget(self.cater_fr)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"color: Black;\n"
"border: 1px solid rgba(255, 255, 255, 60);\n"
"border-bottom-right-radius: 7 px;\n"
"border-bottom-left-radius: 7 px;\n"
"}\n"
"\n"
"QTableView: section{\n"
"background-color: rgba(63, 63, 63);\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;\n"
"}\n"
"\n"
"QTableView: item {\n"
"border-style: none;\n"
"border_bottom: rgba(255, 255, 255, 90);\n"
"}\n"
"\n"
"QTableView: item: selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255 , 255, 90);\n"
"}\n"
"\n"
"")
        self.tableView.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.tableView.setShowGrid(False)
        self.tableView.horizontalHeader().setDefaultSectionSize(135)

        self.verticalLayout_4.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0421ost accounting", None))
        self.label_current_balance.setText(QCoreApplication.translate("MainWindow", u"Current Balance", None))
        self.label_balance.setText(QCoreApplication.translate("MainWindow", u"$1230", None))
        self.label_icon_up_arrow.setText("")
        self.label_income.setText(QCoreApplication.translate("MainWindow", u"Income", None))
        self.label_income_balance.setText(QCoreApplication.translate("MainWindow", u"$1230", None))
        self.label_down_arrow_icon.setText("")
        self.label_outcome_balance.setText(QCoreApplication.translate("MainWindow", u"Outcome", None))
        self.label_outcome_balance_2.setText(QCoreApplication.translate("MainWindow", u"$1230", None))
        self.btn_edit_transaction.setText(QCoreApplication.translate("MainWindow", u"Edit transaction", None))
        self.btn_new_transaction.setText(QCoreApplication.translate("MainWindow", u"New transaction", None))
        self.btn_delet_transaction.setText(QCoreApplication.translate("MainWindow", u"Delet transaction", None))
        self.label_expense_categories.setText(QCoreApplication.translate("MainWindow", u"Expense categories", None))
        self.label_icon_smartphone.setText("")
        self.label_smartphone.setText(QCoreApplication.translate("MainWindow", u"Smartphone", None))
        self.label_smartphone_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.label_icon_televisions.setText("")
        self.label_televisions.setText(QCoreApplication.translate("MainWindow", u"Televisions", None))
        self.label_televisions_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.label_icon_laptope.setText("")
        self.label_laptope.setText(QCoreApplication.translate("MainWindow", u"Laptops", None))
        self.label_laptope_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
        self.label_icon_other.setText("")
        self.label_other.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        self.label_other_balance.setText(QCoreApplication.translate("MainWindow", u"$1000", None))
    # retranslateUi

