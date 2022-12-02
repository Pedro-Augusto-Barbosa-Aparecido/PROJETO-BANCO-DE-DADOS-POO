from connection import Connection


class BaseModel:
    def __init__(self, table: str, database: str):
        self.con = Connection(database)
        self.table = table

    def exec_get_data(self, query: str):
        result = None
        with self.con.cursor as cursor:
            cursor.execute(operation=query)
            result = cursor.fetchall()

        return result

    def exec_insert_and_update(self, query: str):
        with self.con.cursor as cursor:
            cursor.execute(query)
            self.con.con.commit()
