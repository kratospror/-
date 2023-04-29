import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from ui_main import Ui_MainWindow
from new_transaction import Ui_Dialog
from connection import Data


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()

        self.ui.btn_new_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_edit_transaction.clicked.connect(self.open_new_transaction_window)
        self.ui.btn_delet_transaction.clicked.connect(self.delete_current_transaction)

        self.ui.label_balance.setText(self.conn.total_balance())
        self.ui.label_income_balance.setText(self.conn.total_income())
        self.ui.label_outcome_balance_2.setText(self.conn.total_outcome())
        self.ui.label_smartphone_balance.setText(self.conn.label_smartphone_balance())
        self.ui.label_laptope_balance.setText(self.conn.label_laptope_balance())
        self.ui.label_televisions_balance.setText(self.conn.label_televisions_balance())
        self.ui.label_other_balance.setText(self.conn.label_other_balance())

    def view_data(self):
        self.model = QSqlTableModel(self)
        self.model.setTable('expenses')
        self.model.select()
        self.ui.tableView.setModel(self.model)

    def open_new_transaction_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "New transaction":
            self.ui_window.pb_save_new_transaction.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.pb_save_new_transaction.clicked.connect(self.edit_current_transaction)

    def add_new_transaction(self):
        date = self.ui_window.data.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_window.le_discription.text()
        balance = self.ui_window.le2_balance.text()
        status = self.ui_window.cb2_jncome.currentText()

        self.conn.add_new_transaction_query(date, category, description, balance, status)
        self.view_data()
        self.new_window.close()

    def edit_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        date = self.ui_window.data.text()
        category = self.ui_window.cb_choose_category.currentText()
        description = self.ui_window.le_discription.text()
        balance = self.ui_window.le2_balance.text()
        status = self.ui_window.cb2_jncome.currentText()

        self.conn.update_transaction_query(date, category, description, balance, status, id)
        self.view_data()
        self.new_window.close()

    def delete_current_transaction(self):
        index = self.ui.tableView.selectedIndexes()[0]
        id = str(self.ui.tableView.model().data(index))

        self.conn.delet_transaction_query(id)
        self.view_data()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())
