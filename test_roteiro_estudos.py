import unittest
import datetime
from unittest.mock import patch
from roteiro_estudos import (
    adicionar_entrada,
)


class TestRoteiroEstudos(unittest.TestCase):

    @patch(
        "roteiro_estudos.input",
        side_effect=["", "", "", ""],
    )
    @patch(
        "roteiro_estudos.capturar_horario_atual",
        side_effect=[
            datetime.datetime(2022, 1, 1, 12, 0, 0),
            datetime.datetime(2022, 1, 1, 14, 0, 0),
        ],
    )
    def test_adicionar_entrada(self, mock_input, mock_capturar_horario_atual):
        roteiro = []
        adicionar_entrada(roteiro)
        entrada = roteiro[0]
        self.assertEqual(len(roteiro), 1)
        self.assertEqual(entrada["Matéria/Assunto"], "")
        self.assertEqual(entrada["Anotações"], "")
        self.assertEqual(
            entrada["Data Início"], datetime.datetime(2022, 1, 1, 12, 0, 0)
        )
        self.assertEqual(entrada["Data Fim"], datetime.datetime(2022, 1, 1, 14, 0, 0))
        self.assertEqual(entrada["Tempo Estudado"], datetime.timedelta(hours=2))


if __name__ == "__main__":
    unittest.main()
