import zeep
from chronopost_python_sdk import Delivery

class ChronopostService:

    def __init__(self, username, password, tipoEtiqueta=0,
                 tipoResposta=1, enviarEmail=1,
                 wsdl='https://cliente.chronopost.pt:10003/Services/Services.asmx?wsdl'):
        self.client = zeep.Client(wsdl=wsdl)
        self.username = username
        self.password = password
        #self.email = 'laboratorio@youpii.pt'
        self.email = 'rosado_andre@live.com.pt'
        self.tipoEtiqueta = tipoEtiqueta
        self.tipoResposta = tipoResposta
        self.enviarEmail = enviarEmail

    def dispatch(self, delivery: Delivery):
        input = {
            "username": self.username,
            "password": self.password,
            "expedicao": delivery.__dict__,
            "tipoEtiqueta": self.tipoEtiqueta,
            "tipoResposta": self.tipoResposta,
            "enviarEmail": self.enviarEmail
        }

        result = self.client.service.RegistarExpedicao3(**input)

        return result
