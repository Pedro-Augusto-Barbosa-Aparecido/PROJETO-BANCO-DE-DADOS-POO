import time

from rich.console import Console
from rich.panel import Text
from rich.prompt import Prompt, Confirm
from rich.table import Table
from rich import box, print

from models import Agendamento, Localidade, Clinica, Veterinario


class ManagerClinicVeterinary:
    def __init__(self, database):
        self._localidade_controller = Localidade("Localidade", database)
        self._clinica_controller = Clinica("Clinica", database)
        self._agendamento_controller = Agendamento("Agendamento", database)
        self._veterinario_controller = Veterinario("Veterinario", database)

        self._console = Console()

        self._console.print(Text("Manager Clinic Veterinary", justify="center"), justify="center",
                            style="red on black bold")
        self._prompt = Prompt()
        self._table = Table(title="Listagem dos dados", title_style="bold red", box=box.HEAVY)

        self._show_options()

    def _show_options(self):
        stop = False
        while not stop:
            try:
                choices = ["[1] - Criar Localidade", "[2] - Criar Agendamento", "[3] - Criar Veterinario",
                           "[4] - Criar Clinica", "[5] - Listar Agendamentos", "[6] - Detalhar Agendamento",
                           "[7] - Deletar Agendamento", "[8] - Atualizar Agendamento", "[9] - Sair do sistema"]
                for choice in choices:
                    self._console.print(choice, style="white bold", justify="left")
                choices_values = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
                self._console.style = "white bold"
                choice = self._prompt.ask("\nO que você deseja fazer?", choices=choices_values, console=self._console,
                                          show_choices=False)

                match int(choice):
                    case 1:
                        self._console.print("Para inserir uma localidade, precisamos de algumas informações: ")
                        rua = self._prompt.ask("Rua")
                        bairro = self._prompt.ask("Bairro")
                        cidade = self._prompt.ask("Cidade")
                        numero = self._prompt.ask("Numero")

                        self._console.print("Criando localidade!!", style="bold dark_blue blink")
                        self._localidade_controller.create(rua, bairro, cidade, numero)
                        time.sleep(2)
                        self._console.clear()
                    case 2:
                        self._console.print("Para inserir um agendamento, precisamos de algumas informações: ")
                        data = self._prompt.ask("Data")
                        clinica = self._prompt.ask("Clinica")
                        animal = self._prompt.ask("Nome do pet")

                        self._console.print("Criando Agendamento!!", style="bold dark_blue blink")

                        if len(self._clinica_controller.get(clinica)) == 0:
                            self._console.print("Clinica invalida", style="bold red")
                            res = self._prompt.ask("Deseja tentar outra (S/N)?", choices=["S", "s", "N", "n"],
                                                   show_choices=False, default="n", show_default=False)
                            while res.lower() == "s":
                                clinica = self._prompt.ask("clinica")
                                if len(self._clinica_controller.get(clinica)) == 0:
                                    res = self._prompt.ask("Deseja inserir outra (S/N)?", choices=["S", "s", "N", "n"],
                                                           show_choices=False, default="n", show_default=False)

                        self._agendamento_controller.create(data, clinica, animal)
                        time.sleep(2)
                        self._console.clear()
                    case 3:
                        self._console.print("Para inserir um veterinario, precisamos de algumas informações: ")
                        nome = self._prompt.ask("Nome")
                        endereco = self._prompt.ask("Endereço")
                        telefone = self._prompt.ask("telefone")
                        email = self._prompt.ask("email")

                        self._console.print("Criando Veterinario!!", style="bold dark_blue blink")
                        self._veterinario_controller.create(nome, endereco, telefone, email)
                        time.sleep(2)
                        self._console.clear()
                    case 4:
                        self._console.print("Para inserir uma clinica, precisamos de algumas informações: ")
                        nome = self._prompt.ask("Nome")
                        endereco = self._prompt.ask("Endereco")

                        self._console.print("Criando Clinica!!", style="bold dark_blue blink")

                        if len(self._localidade_controller.get(endereco)) == 0:
                            self._console.print("Localidade invalida", style="bold red")
                            res = self._prompt.ask("Deseja inserir outra (S/N)?", choices=["S", "s", "N", "n"],
                                                   show_choices=False, default="n", show_default=False)
                            while res.lower() == "s":
                                endereco = self._prompt.ask("Endereco")
                                if len(self._localidade_controller.get(endereco)) == 0:
                                    res = self._prompt.ask("Deseja inserir outra (S/N)?", choices=["S", "s", "N", "n"],
                                                           show_choices=False, default="n", show_default=False)

                        self._clinica_controller.create(nome, endereco)
                        time.sleep(2)
                        self._console.clear()
                    case 5:
                        self._table = Table(title="Listagem dos dados", title_style="bold red", box=box.HEAVY)

                        if len(self._table.columns) == 0:
                            self._table.add_column("Data")
                            self._table.add_column("Clinica")
                            self._table.add_column("Animal")
                            self._table.add_column("ID")

                        for row in self._agendamento_controller.list():
                            self._table.add_row(str(row[0]).split(" ")[0], str(row[1]), str(row[2]), str(row[3]))

                        print(self._table)
                    case 6:
                        id_agendamento = self._prompt.ask("Id do agendamento")
                        self._table = Table(title="Detalhe do Agendamento", title_style="bold red", box=box.HEAVY)
                        if len(self._table.columns) == 0:
                            self._table.add_column("Data")
                            self._table.add_column("Clinica")
                            self._table.add_column("Animal")
                            self._table.add_column("ID")

                        for row in self._agendamento_controller.get(id_agendamento):
                            self._table.add_row(str(row[0]).split(" ")[0], str(row[1]), str(row[2]), str(row[3]))

                        print(self._table)

                    case 7:
                        id_agendamento = self._prompt.ask("Id do agendamento")
                        if Confirm.ask("Deseja apagar mesmo?"):
                            self._agendamento_controller.delete(id_agendamento)
                            self._console.print("Agendamento deletado", style="bold yellow")
                            time.sleep(2)
                        self._console.clear()
                    case 8:
                        id_agendamento = self._prompt.ask("Id do agendamento")

                        data = None
                        clinica = None
                        animal = None

                        if Confirm.ask("Atualizar a data?"):
                            data = self._prompt.ask("Data")
                        if Confirm.ask("Atualizar Clinica?"):
                            clinica = self._prompt.ask("Clinica")
                        if Confirm.ask("Atualizar Animal?"):
                            animal = self._prompt.ask("Animal")

                        if Confirm.ask(f"Deseja mesmo atualizar agendamento {id_agendamento}"):
                            self._agendamento_controller.update(id_agendamento, data, clinica, animal)
                            self._console.print("Agendamento atualizado!!", style="bold red")
                            time.sleep(2)
                        self._console.clear()
                    case 9:
                        stop = True
                        break
            except:
                self._console.print("Ocorreu um erro na operação do banco de dados!!", "justify bold red")

            choice = self._prompt.ask("Deseja continuar? [S/n]", choices=["S", "s", "N", "n"],
                                      show_choices=False, default="n", show_default=False)

            if choice in ["n", "N"]:
                break

        return choice


if __name__ == "__main__":
    mcv = ManagerClinicVeterinary("proj_lab")
