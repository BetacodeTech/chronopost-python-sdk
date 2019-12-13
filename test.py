import unittest
import datetime
import requests

from chronopost_python_sdk import Delivery
from chronopost_python_sdk.ChronopostService import ChronopostService


class ChronopostTest(unittest.TestCase):
    def setUp(self):
        self.chronopost_service = ChronopostService(username="024961", password="X024961X")

    def tearDown(self):
        pass

    def testGetResult(self):
        today = datetime.datetime(2029, 12, 4)

        delivery = Delivery(OrigemMoradaNome='rafik', OrigemMorada='Lorem ipsum dolor sit amet, consectetuer adipiscin', OrigemMoradaCodigoPostal='1234-123',
                            OrigemMoradaLocalidade='Lisboa', OrigemEmail='sloth577@gmail.com',
                            DestinoMoradaNome='andre', DestinoMoradaCodigoPostal='7080-038', DestinoMoradaLocalidade='Vendas Novas',
                            DestinoMorada='Lorem ipsum dolor sit amet, consectetuer adipiscin', NumeroVolumes=1, DataExpedicao=today)

        self.assertIsNotNone(delivery)
        self.assertEqual(delivery.Conta, '02496101')
        self.assertEqual(delivery.OrigemMoradaNome, 'rafik')
        self.assertEqual(delivery.OrigemMoradaLinha1, 'Rua xyz')
        self.assertEqual(delivery.OrigemMoradaLinha2, 'Rua xyz')
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

        response_json = self.chronopost_service.dispatch(delivery)

        self.assertIn('Codigo', response_json)
        self.assertIn('Descricao', response_json)
        self.assertIn('NrGuia', response_json)
        self.assertIn('CorpoResposta', response_json)

    def testDispatch(self):
        tomorrow = datetime.datetime.today() + datetime.timedelta(days=1)

        delivery = Delivery(OrigemMoradaNome='rafik', OrigemMorada='Lorem ipsum dolor sit amet, consectetuer adipiscin',
                            OrigemMoradaCodigoPostal='1234-123',
                            OrigemMoradaLocalidade='Lisboa', OrigemEmail='sloth577@gmail.com',
                            DestinoMoradaNome='andre', DestinoMoradaCodigoPostal='7080-038',
                            DestinoMoradaLocalidade='Vendas Novas',
                            DestinoMorada='Lorem ipsum dolor sit amet, consectetuer adipiscin', NumeroVolumes=1,
                            DataExpedicao=tomorrow)

        result = self.chronopost_service.dispatch(delivery)

        self.assertIsNotNone(result)


    def testRequest(self):
        url = 'http://cliente.chronopost.pt:10002/Services/Services.asmx'
        header = {'Content-type': 'text/xml'}

        today = datetime.datetime(2019, 12, 4)

        delivery = Delivery(OrigemMoradaNome='rafik', OrigemMoradaLinha1='Rua xyz', OrigemMoradaCodigoPostal='1234-123',
                            OrigemMoradaLocalidade='Lisboa', OrigemEmail='sloth577@gmail.com',
                            DestinoMoradaNome='andre', DestinoMoradaCodigoPostal='7080-038',
                            DestinoMoradaLocalidade='Vendas Novas',
                            DestinoMoradaLinha1='Rua JFF', NumeroVolumes=1, DataExpedicao=today)

        text = '''
<soap-env:Envelope
    xmlns:soap-env="http://www.w3.org/2003/05/soap-envelope">
    <soap-env:Body>
        <ns0:RegistarExpedicao3
            xmlns:ns0="http://tempuri.org/">
            <ns0:username>024961</ns0:username>
            <ns0:password>X024961X</ns0:password>
            <ns0:expedicao>
                <ns0:Conta>02496101</ns0:Conta>
                <ns0:OrigemMoradaNome>rafik</ns0:OrigemMoradaNome>
                <ns0:OrigemMoradaLinha1>Rua xyz</ns0:OrigemMoradaLinha1>
                <ns0:OrigemMoradaCodigoPostal>1234-123</ns0:OrigemMoradaCodigoPostal>
                <ns0:OrigemMoradaLocalidade>Lisboa</ns0:OrigemMoradaLocalidade>
                <ns0:OrigemMoradaPais>PT</ns0:OrigemMoradaPais>
                <ns0:OrigemEmail>sloth577@gmail.com</ns0:OrigemEmail>
                <ns0:TipoDestino>{destino}</ns0:TipoDestino>
                <ns0:DestinoMoradaNome>andre</ns0:DestinoMoradaNome>
                <ns0:DestinoMoradaLinha1>Rua JFF</ns0:DestinoMoradaLinha1>
                <ns0:DestinoMoradaCodigoPostal>7080-038</ns0:DestinoMoradaCodigoPostal>
                <ns0:DestinoMoradaLocalidade>Vendas Novas</ns0:DestinoMoradaLocalidade>
                <ns0:DestinoMoradaPais>PT</ns0:DestinoMoradaPais>
                <ns0:DataExpedicao>2020-12-04 00:00:00</ns0:DataExpedicao>
                <ns0:EnviarEtiquetasEmail>2</ns0:EnviarEtiquetasEmail>
                <ns0:NumeroVolumes>1</ns0:NumeroVolumes>
            </ns0:expedicao>
            <ns0:tipoResposta>1</ns0:tipoResposta>
            <ns0:enviarEmail>1</ns0:enviarEmail>
            <ns0:email>rosado_andre@live.com.pt</ns0:email>
            <ns0:tipoEtiqueta>0</ns0:tipoEtiqueta>
        </ns0:RegistarExpedicao3>
    </soap-env:Body>
</soap-env:Envelope>      
        '''

        r = requests.post(url, data=text, headers=header)
