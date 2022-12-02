from mysql import connector


class Connection:
    def __init__(self, database: str):
        self.con = connector.connect(
            database=database,
            host="localhost",
            user="root",
            password="root"
        )

    def _get_cursor(self):
        return self.con.cursor()

    @property
    def cursor(self):
        return self._get_cursor()
