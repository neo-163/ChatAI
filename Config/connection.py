# Config/connection.py

db_type = 'mysql'


class BaseConfig:
    @staticmethod
    def connection_string():
        raise NotImplementedError("Subclasses should implement this method!")


class MSSQLConfig(BaseConfig):
    DRIVER = '{ODBC Driver 17 for SQL Server}'
    SERVER = '127.0.0.1'
    DATABASE = 'chat_ai'
    USERNAME = 'root'
    PASSWORD = '123456'

    @staticmethod
    def connection_string():
        return f'DRIVER={MSSQLConfig.DRIVER};SERVER={MSSQLConfig.SERVER};DATABASE={MSSQLConfig.DATABASE};UID={MSSQLConfig.USERNAME};PWD={MSSQLConfig.PASSWORD}'


class MySQLConfig(BaseConfig):
    HOST = '127.0.0.1'
    DATABASE = 'chat_ai'
    USERNAME = 'root'
    PASSWORD = '123456'
    PORT = 3306

    @staticmethod
    def connection_string():
        return f"mysql+mysqlconnector://{MySQLConfig.USERNAME}:{MySQLConfig.PASSWORD}@{MySQLConfig.HOST}:{MySQLConfig.PORT}/{MySQLConfig.DATABASE}"

# Factory function to get the right config object


def get_database_config():
    if db_type == 'mssql':
        return MSSQLConfig
    elif db_type == 'mysql':
        return MySQLConfig
    else:
        raise ValueError("Unsupported database type")
