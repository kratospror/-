from PySide6 import QtWidgets, QtSql

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')

        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")
        return True

    def execute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()

    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query(sql_query, [date, category, description, balance, status])

    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query(sql_query, [date, category, description, balance, status, id])

    def delet_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query(sql_query, [id])

    def get_total(self, column, filter=None, value=None):
        sql_query = f"SELECT SUM(Balance) FROM expenses WHERE {column} = ?"

        if filter is not None and value is not None:
            sql_query += f" AND {filter} = ?"

        query_values = [value]

        if filter is not None and value is not None:
            query_values.append(value)

        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        for query_value in query_values:
            query.addBindValue(query_value)

        query.exec()

        if query.next():
            return str(query.value(0)) + '$'

        return '0'

    def total_balance(self):
        return self.get_total(column="1")

    def total_income(self):
        return self.get_total(column="Status", filter="Status", value="Income")

    def total_outcome(self):
        return self.get_total(column="Status", filter="Status", value="Outcome")

    def label_smartphone_balance(self):
        return self.get_total(column="Category", filter="Category", value="Smartphone")

    def label_laptope_balance(self):
        return self.get_total(column="Category", filter="Category", value="Laptops")

    def label_televisions_balance(self):
        return self.get_total(column="Category", filter="Category", value="Televisions")

    def label_other_balance(self):
        return self.get_total(column="Category", filter="Category", value="Other")