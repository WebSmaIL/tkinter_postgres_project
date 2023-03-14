import psycopg2
from psycopg2 import Error

def create_connection ():
    try:
        # Подключение к существующей базе данных
        connection = psycopg2.connect(user="postgres",
                                    # пароль, который указали при установке PostgreSQL
                                    password="root",
                                    host="127.0.0.1",
                                    port="5432",
                                    database="shop_db")

        # Курсор для выполнения операций с базой данных
        cursor = connection.cursor()
        # Распечатать сведения о PostgreSQL
        print("Информация о сервере PostgreSQL")
        print(connection.get_dsn_parameters(), "\n")
        # Выполнение SQL-запроса
        cursor.execute("SELECT version();")
        # Получить результат
        record = cursor.fetchone()
        print("Вы подключены к - ", record, "\n")

        return [connection, cursor]
    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)
        return error