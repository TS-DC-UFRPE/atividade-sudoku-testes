from TS_DCM_Sudoku_ok import SudokuOk
class TestesSudoku:
    def test_sudokuOk_deve_retornar_true(self):
        esperado = True

        resultado = SudokuOk("TS_DCM_solucao_sim.txt").valido( )

        assert resultado == esperado


    def  test_sudokuOk_deve_retornar_false(self):
        esperado = False

        resultado = SudokuOk("TS_DCM_solucao_nao.txt").valido( )

        assert resultado == esperado