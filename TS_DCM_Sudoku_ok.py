class SudokuOk:
    """

Prompt 1:

Classe feita pelo Chat GPT, com os seguintes inputs:
(Input das regras 2 e 3 da atividade)

Certo, vamos por partes, o que eu preciso fazer, por onde começar? e eu vou usar o python em vez do Java, usando o pytest, coverage etc. 
Eu devo fazer essa atividade no meu vscode ou no minizinc? Esse sudoku o minizinc vai gerar? e eu tenho que resolver com testes no python? 
ou eu tenho que gerar outro sudoku? Me lembro do professor usando alguma parte no propio site do minizinc e em que o out do sudoku ficava com algumas partes em vermelho caso falhasse algo.

Certo. Agora proximo passo eu preciso criar uma classe?

Prompt 2:
Preciso que você adicione uma nova verificação, caso aja um valor em branco na lista de números do sudoku,
deverá retornar False, faça isso modificando o mínimo possível do código atual.

Prompt 3:
Agora, similar a isso quero que faça uma verificação que confira se a números de 2 algarismos estão repetidos na mesma linha ou coluna, por exemplo, 33, 41, 14, 28, etc. (Novamente, modifique o mínimo possível do código atual)

A validação pode ser feita com o valor numérico de cada número do sudoku, caso seja > 9 ou < 1, retorne False.
"""
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
print("Resultados do SudokuOk:")
print("Arquivo solucao_sim:", sudokuCerto.valido())
print("Arquivo solucao_nao:",sudokuErrado.valido())
print("\n")