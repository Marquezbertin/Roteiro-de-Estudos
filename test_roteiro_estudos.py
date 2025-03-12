import unittest
import datetime
from unittest.mock import patch
from roteiro_estudos import (
    adicionar_entrada,
    calcular_tempo_estudado,
    salvar_roteiro_txt,
    capturar_horario_atual
)

class TestRoteiroEstudos(unittest.TestCase):

    def test_calcular_tempo_estudado(self):
        inicio = datetime.datetime(2022, 1, 1, 12, 0, 0)
        fim = datetime.datetime(2022, 1, 1, 14, 0, 0)
        esperado = datetime.timedelta(hours=2)
        resultado = calcular_tempo_estudado(inicio, fim)
        self.assertEqual(resultado, esperado)

    @patch("roteiro_estudos.capturar_horario_atual", side_effect=[
        datetime.datetime(2022, 1, 1, 12, 0, 0),
        datetime.datetime(2022, 1, 1, 14, 0, 0)
    ])
    def test_adicionar_entrada(self, mock_capturar_horario_atual):
        roteiro = []
        materia = "Matemática"
        anotacoes = "Estudando álgebra"
        data_inicio = capturar_horario_atual()
        data_fim = capturar_horario_atual()
        adicionar_entrada(roteiro, materia, anotacoes, data_inicio, data_fim)
        entrada = roteiro[0]
        self.assertEqual(len(roteiro), 1)
        self.assertEqual(entrada["Matéria/Assunto"], materia)
        self.assertEqual(entrada["Anotações"], anotacoes)
        self.assertEqual(entrada["Data Início"], data_inicio)
        self.assertEqual(entrada["Data Fim"], data_fim)
        self.assertEqual(entrada["Tempo Estudado"], datetime.timedelta(hours=2))

    @patch("builtins.open", unittest.mock.mock_open())
    def test_salvar_roteiro_txt(self, mock_open):
        roteiro = [
            {
                'Data Início': datetime.datetime(2022, 1, 1, 12, 0, 0),
                'Data Fim': datetime.datetime(2022, 1, 1, 14, 0, 0),
                'Tempo Estudado': datetime.timedelta(hours=2),
                'Matéria/Assunto': 'Matemática',
                'Anotações': 'Estudando álgebra'
            }
        ]
        salvar_roteiro_txt(roteiro)
        mock_open.assert_called_with('Matemática.txt', 'w', encoding='utf-8')
        handle = mock_open()
        handle.write.assert_any_call('--- Entrada 1 ---\n')
        handle.write.assert_any_call('Data Início: 2022-01-01 12:00:00\n')
        handle.write.assert_any_call('Data Fim: 2022-01-01 14:00:00\n')
        handle.write.assert_any_call('Tempo Estudado: 2:00:00\n')
        handle.write.assert_any_call('Matéria/Assunto: Matemática\n')
        handle.write.assert_any_call('Anotações: Estudando álgebra\n')
        handle.write.assert_any_call('-------------------\n\n')

if __name__ == "__main__":
    unittest.main()
