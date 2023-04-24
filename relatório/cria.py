class Relatório:
    def __init__(self) -> None:
        self.cabeçalho=None

    def inicialize(self):
        with open('../dados/cabeçalho.tex') as f:
            self.cabeçalho = f.head
