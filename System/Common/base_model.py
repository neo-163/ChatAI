
# baseModel.py

import pyodbc
from Config.connection import get_database_config

class BaseModel:
    def __init__(self):
        config_class = get_database_config()
        self.conn_str = config_class.connection_string()

    def _connect(self):
        return pyodbc.connect(self.conn_str)

    def _select_query(self, query, *params):
        with self._connect() as conn:
            cursor = conn.cursor()
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            columns = [column[0] for column in cursor.description]
            results = []
            for row in cursor.fetchall():
                results.append(dict(zip(columns, row)))
            cursor.close()
            return results

    def _execute_query(self, query, *params):
        with self._connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, *params)
            conn.commit()
            cursor.close()
