from classe.produto import Produto
from rich import print
from rich.traceback import install
from rich.table import Table
from rich.panel import Panel
from os import system
from time import sleep
install()

def titulo(texto):
    system('cls')
    print('-' * len(texto))
    print(f'[red]{texto}[/]')
    print('-' * len(texto))
titulo('Cadastro produto')