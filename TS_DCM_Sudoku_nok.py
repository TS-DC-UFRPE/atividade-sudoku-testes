class SudokuNOk:
    def __init__(self, pathTxt):
        self.tabuleiro = []
        with open(pathTxt, "r") as arquivoTxt:
            for linha in arquivoTxt:
                # divide por vírgula, tira espaços e converte para int
                numeros = [int(x.strip()) for x in linha.split(",")]
                self.tabuleiro.append(numeros)



    # Verifica linhas e colunas, porém INCORRETAS retornam True
    def valido(self):

        for linha in self.tabuleiro:
            if sorted(linha) != list(range(1, 10)):
                return True

        for colunaIndex in range(9):
            coluna = [self.tabuleiro[linhaIndex][colunaIndex] for linhaIndex in range(9)]
            if sorted(coluna) != list(range(1, 10)):
                return True

        return False


sudokuSim = SudokuNOk("TS_DCM_solucao_sim.txt")
sudokuNao = SudokuNOk("TS_DCM_solucao_nao.txt")
print(sudokuSim.valido())
print(sudokuNao.valido())
