from TS_DCM_Sudoku_ok import SudokuOk
from TS_DCM_Sudoku_nok import SudokuNOk
class TestesSudoku: #Verifica se o Sudoku está correto
    def test_sudokuOk_deve_retornar_true(self):
        esperado = True

        resultado = SudokuOk("TS_DCM_solucao_sim.txt").valido( )

        assert resultado == esperado


    def  test_sudokuOk_deve_retornar_false(self): #Verifica se o Sudoku está correto
        esperado = False

        resultado = SudokuNOk("TS_DCM_solucao_nao.txt").valido( )

        assert resultado == esperado