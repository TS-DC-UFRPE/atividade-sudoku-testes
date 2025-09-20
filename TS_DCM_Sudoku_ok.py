class SudokuOk:
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
