class SudokuOk:
    """
Classe feita pelo Chat GPT, com os seguintes inputs:
(Input das regras 2 e 3 da atividade)

Certo, vamos por partes, o que eu preciso fazer, por onde começar? e eu vou usar o python em vez do Java, usando o pytest, coverage etc. 
Eu devo fazer essa atividade no meu vscode ou no minizinc? Esse sudoku o minizinc vai gerar? e eu tenho que resolver com testes no python? 
ou eu tenho que gerar outro sudoku? Me lembro do professor usando alguma parte no propio site do minizinc e em que o out do sudoku ficava com algumas partes em vermelho caso falhasse algo.

Certo. Agora proximo passo eu preciso criar uma classe?
"""
    def __init__(self, pathTxt):
        self.tabuleiro = []
        with open(pathTxt, "r") as arquivoTxt:
            for linha in arquivoTxt:
                # divide os numeros por vírgula, tira os espaços e converte pra int
                numeros = [int(x.strip()) for x in linha.split(",")]
                self.tabuleiro.append(numeros)


    #Verifica se existem numeros faltando ou repetidos
    def valido(self):
        for linha in self.tabuleiro:
            if sorted(linha) != list(range(1, 10)):
                return False

        for colunaIndex in range(9):
            coluna = [self.tabuleiro[linhaIndex][colunaIndex] for linhaIndex in range(9)]
            if sorted(coluna) != list(range(1, 10)):
                return False

        # Verifica blocos 3x3
        for indexLinhaBloco in range(0, 9, 3):
            for indexColunaBloco in range(0, 9, 3):
                bloco = []
                for i in range(3):
                    for j in range(3):
                        bloco.append(self.tabuleiro[indexLinhaBloco+i][indexColunaBloco+j])
                if sorted(bloco) != list(range(1, 10)):
                    return False

        return True

sudokuCerto = SudokuOk("TS_DCM_solucao_sim.txt")
sudokuErrado = SudokuOk("TS_DCM_solucao_nao.txt")
print(sudokuCerto.valido())
print(sudokuErrado.valido())
