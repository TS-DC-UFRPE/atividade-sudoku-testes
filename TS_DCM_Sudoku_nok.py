class SudokuNOk:
    def __init__(self, pathTxt):
        self.tabuleiro = []
        self.verificacao_valores_em_branco = True
        with open(pathTxt, "r") as arquivoTxt:
            for linha in arquivoTxt:
                try:
                    # Tenta converter os números
                    numeros = [int(x.strip()) for x in linha.split(",")]
                    self.tabuleiro.append(numeros)
                except ValueError:
                    # Se der erro (ex: um campo vazio ''), a leitura é inválida
                    self.verificacao_valores_em_branco = False


    #Verifica se existem numeros faltando ou repetidos
    def valido(self):
        # Verifica se há números fora do intervalo 1-9
        for linha in self.tabuleiro:
            for numero in linha:
                if numero > 9 or numero < 1:
                    return False
                
        if not self.verificacao_valores_em_branco:
            return False
        for linha in self.tabuleiro:
            if sorted(linha) != list(range(1, 10)):
                return True

        for colunaIndex in range(9):
            coluna = [self.tabuleiro[linhaIndex][colunaIndex] for linhaIndex in range(9)]
            if sorted(coluna) != list(range(1, 10)):
                return True

        # Verifica blocos 3x3
        for indexLinhaBloco in range(0, 9, 3):
            for indexColunaBloco in range(0, 9, 3):
                bloco = []
                for i in range(3):
                    for j in range(3):
                        bloco.append(self.tabuleiro[indexLinhaBloco+i][indexColunaBloco+j])
                if sorted(bloco) != list(range(1, 10)):
                    return True

        return True


sudokuSim = SudokuNOk("TS_DCM_solucao_sim.txt")
sudokuNao = SudokuNOk("TS_DCM_solucao_nao.txt")
print("Resultados do SudokuNOk:")
print("Arquivo solucao_sim:", sudokuSim.valido())
print("Arquivo solucao_nao",sudokuNao.valido())
