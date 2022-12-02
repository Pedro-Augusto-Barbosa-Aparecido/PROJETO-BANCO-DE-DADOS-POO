from generic import BaseModel


class Localidade(BaseModel):
    def __init__(self, table, database):
        super(Localidade, self).__init__(table, database)

    def create(self, rua, bairro, cidade, numero):
        query = f'INSERT INTO {self.table} (rua, bairro, cidade, numero) VALUES ("{rua}", "{bairro}", "{cidade}", "{numero}")'
        self.exec_insert_and_update(query)

    def get(self, id_localidade):
        query = f'SELECT * FROM {self.table} WHERE id={id_localidade}'
        return self.exec_get_data(query)


class Veterinario(BaseModel):
    def __init__(self, table, database):
        super(Veterinario, self).__init__(table, database)

    def create(self, nome, endereco, telefone, email):
        query = f'INSERT INTO {self.table} (nome, endereco, telefone, email) VALUES ("{nome}", "{endereco}", "{telefone}", "{email}")'
        self.exec_insert_and_update(query)


class Clinica(BaseModel):
    def __init__(self, table, database):
        super(Clinica, self).__init__(table, database)

    def create(self, nome, endereco):
        query = f'INSERT INTO {self.table} (nome, endereco) VALUES ("{nome}", "{endereco}")'
        self.exec_insert_and_update(query)

    def get(self, id_clinica):
        query = f'SELECT * FROM {self.table} WHERE id={id_clinica}'
        return self.exec_get_data(query)


class Agendamento(BaseModel):
    def __init__(self, table, database):
        super(Agendamento, self).__init__(table, database)

    @staticmethod
    def _get_update_keys(data_as_dict):
        values = []
        for key in data_as_dict.keys():
            if not data_as_dict[key] is None:
                values.append(f"{key}=\"{data_as_dict[key]}\"")

        return ",".join(values)

    def create(self, data, clinica, animal):
        query = f'INSERT INTO {self.table} (data, clinica, animal) VALUES ("{data}", "{clinica}", "{animal}")'
        self.exec_insert_and_update(query)

    def get(self, id):
        query = f'SELECT s.data, a.nome, s.animal, s.id FROM {self.table} as s, Clinica as a WHERE s.id={id} and a.id = s.clinica'
        return self.exec_get_data(query)

    def list(self):
        query = f"SELECT s.data, a.nome, s.animal, s.id FROM {self.table} as s, Clinica as a where a.id = s.clinica"
        return self.exec_get_data(query)

    def update(self, id_agendamento, data=None, clinica=None, animal=None):
        query = f'UPDATE {self.table} SET {self._get_update_keys({"data": data, "clinica": clinica, "animal": animal})} WHERE id={id_agendamento}'
        self.exec_insert_and_update(query)

    def delete(self, id_agendamento):
        query = f'DELETE FROM {self.table} WHERE id={id_agendamento}'
        self.exec_insert_and_update(query)
