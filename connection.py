from PySide6 import QtWidgets, QtSql
# QtWidgets диалоговое окно которое будет появлятся в том случае когда приложение не сможет открыть базу данных и будет информировать нас об этом.
# QtSql это модул библиотеки qt которая повляет рабтать с базами данных в qt приложениях он предоставляет классы и функции для подключения к базе данных
# выполняя запросы и получая результат

class Data:
    def __init__(self):
        super(Data, self).__init__()
        self.create_connection()

# "create_connection" он предназначен для создания подключения к базе данных sqli3 и создание таблицы если она не существует.
# объект "db" класса qsql database с испоьлзованием статического метода database который принимает строковый аргумент указывающий на используемый драйвер базы
# данных в данном случае используется драйвер qtsqlite.
# expense_db.db - имя базы данных.
    def create_connection(self):
        db = QtSql.QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('expense_db.db')
# условие "if" проверяет удалось ли открыть базу данных испльзуя метод "Ореn" объект "db" если не удалось выведим сообщение об ошибке в диалоговое окно
# "messagebox" окно а метод #"create_connection" возращает значение "false"
        if not db.open():
            QtWidgets.QMessageBox.critical(None, "Cannot open database",
                                           "Click Cancel to exit.", QtWidgets.QMessageBox.Cancel)
# Далее создаём объект query класса qsquery который используется для выполнения запросов к базе данных в данном случае выполняется запрос на создание таблицы
# "eхpence" содержащий несколько полей. Поле "ID" определим как первичный ключ автоинструментом автоинструмент будет добавлять плюс один в созданной записи
# в таблице тем самым мы реализуем нумерацию по порядку в таблице основного окна если выполнение запроса прошел успешно метод "create_connection" вернет нам "тру"

            return False

        query = QtSql.QSqlQuery()
        query.exec("CREATE TABLE IF NOT EXISTS expenses (ID integer primary key AUTOINCREMENT, Date VARCHAR(20), "
                   "Category VARCHAR(20), Description VARCHAR(20), Balance REAL, Status VARCHAR(20))")

# execute_query представляет собой объект для взаимодействия с базой данных с помощью его выполняются запросы о добавления, удаление, редактирование записи
# записи в таблице базы данных запрос на подсчет сумм по категория расходов и доходов. Общий метод реализован для того что бы не писать повторяющийся код для
# запросов.
        return True

    def execute_query(self, sql_query, values=None):
        query = QtSql.QSqlQuery()
        query.prepare(sql_query)

        if values is not None:
            for value in values:
                query.addBindValue(value)

        query.exec()

# Общий метод создает sql запрос который будет выполнен с помощью метода execute_query ещё используется для добавления новой транзакции в таблицу расходов
# он создает sql запрос для вставки данных в таблицу и передаёт ее в качестве аргумента метода exec
# INSERT выполняет вставку новой записи VALUES передаёт запись
    def add_new_transaction_query(self, date, category, description, balance, status):
        sql_query = "INSERT INTO expenses (Date, Category, Description, Balance, Status) VALUES (?, ?, ?, ?, ?)"
        self.execute_query(sql_query, [date, category, description, balance, status])

# UPDATE Выполняет действие обновление записи и ключивое слово тут будет Set указывает наименование полей подлежащие к изменению.
# WHERE будет принимать ID записи которую необходимо изменить то есть надо указать где изменить?
    def update_transaction_query(self, date, category, description, balance, status, id):
        sql_query = "UPDATE expenses SET Date=?, Category=?, Description=?, Balance=?, Status=? WHERE ID=?"
        self.execute_query(sql_query, [date, category, description, balance, status, id])

    def delet_transaction_query(self, id):
        sql_query = "DELETE FROM expenses WHERE ID=?"
        self.execute_query(sql_query, [id])

# модет гет тотал вычисляет сумму значений в заданном в столбце таблицы базы данных он также может фильтровать результаты запроса если были переданы соответствующие
# параметры, если параметры фильтрации не переданы метод вернет сумму всех значений в заданном столбце если параметры фильтрации переданы метод вернёт сумму значений
# только тех строк где значение в заданном столбце соответствует заданному значению.
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

# получение результат запроса. Если метод "next" исрользуется для получения следующей строки результата. "value" используется для получения значение суммы в
# столбце указанном sql запросе, полученные значения конвертируется в строку, и возращается методом добавляет знак доллара к сумме, если запрос небыл выполнен
# успешно или результат не был получен метод возращвет строку 0

        if query.next():
            return str(query.value(0)) + '$'

        return '0'
#реализуем методы которые будут их подсчитывать для каждой категории. создадим отдельный метод который будет выполнять следующие действия вызывать общий
#метод тотал и передовать ему параметры фильтрации и получать результат.

#  total_balance суммируем полностью всю таблицу по балансу то есть мы получаем общую баланс на нашем счету
    def total_balance(self):
        return self.get_total(column="1")

#  total_income то есть всего доходов. Мы фильтруем так же по балансу только здесь уже в столбце статус мы указываем что фильтруем по значению Income
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