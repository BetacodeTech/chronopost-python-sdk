import unittest
import datetime

from chronopost_python_sdk import Delivery
from chronopost_python_sdk.ChronopostService import ChronopostService


class ChronopostTest(unittest.TestCase):
    def setUp(self):
        self.chronopost_service = ChronopostService(username="024961", password="X024961X")

    def tearDown(self):
        pass

    def testGetResult(self):
        today = datetime.datetime(2019, 12, 4)

        delivery = Delivery(OrigemMoradaNome='rafik', OrigemMoradaLinha1='Rua xyz', OrigemMoradaCodigoPostal='1234-123',
                            OrigemMoradaLocalidade='Lisboa', OrigemEmail='sloth577@gmail.com',
                            DestinoMoradaNome='andre', DestinoMoradaCodigoPostal='7080-038', DestinoMoradaLocalidade='Vendas Novas',
                            DestinoMoradaLinha1='Rua JFF', NumeroVolumes=1, DataExpedicao=today)

        result = self.chronopost_service.dispatch(delivery)

        self.assertIsNotNone(delivery)
        self.assertEqual(delivery.Conta, '02496101')
        self.assertEqual(delivery.OrigemMoradaNome, 'rafik')
        self.assertEqual(delivery.OrigemMoradaLinha1, 'Rua xyz')
        self.assertEqual(delivery.OrigemMoradaCodigoPostal, '1234-123')
        self.assertEqual(delivery.OrigemMoradaLocalidade, 'Lisboa')
        self.assertEqual(delivery.OrigemMoradaPais, 'PT')
        self.assertEqual(delivery.OrigemEmail, 'sloth577@gmail.com')
        self.assertEqual(delivery.TipoDestino, 1)
        self.assertEqual(delivery.DestinoMoradaNome, 'andre')
        self.assertEqual(delivery.DestinoMoradaLinha1, 'Rua JFF')
        self.assertEqual(delivery.DestinoMoradaCodigoPostal, '7080-038')
        self.assertEqual(delivery.DestinoMoradaLocalidade, 'Vendas Novas')
        self.assertEqual(delivery.DestinoMoradaPais, 'PT')
        self.assertEqual(delivery.DataExpedicao, today)
        self.assertEqual(delivery.EnviarEtiquetasEmail, 2)
        self.assertEqual(delivery.NumeroVolumes, 1)
        self.assertEqual(delivery.DataExpedicao, today)
