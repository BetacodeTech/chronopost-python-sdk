import datetime


class Delivery:
    def __init__(self, OrigemMoradaNome: str, OrigemMoradaLinha1: str, OrigemMoradaCodigoPostal: str, OrigemMoradaLocalidade: str,
                 OrigemEmail: str, DestinoMoradaNome: str, DestinoMoradaLinha1: str,
                 NumeroVolumes: int, DataExpedicao: datetime,
                 Conta: str = "02496101", OrigemMoradaPais: str = "PT", TipoDestino: int = 1,
                 EnviarEtiquetasEmail: int = 2,
                 DestinoMoradaCodigoPostal: str = None, DestinoMoradaLocalidade: str = None, DestinoMoradaPais: str="PT",
                 OrigemMoradaLinha2=None, OrigemTelefone=None, OrigemTelemovel=None,
                 OrigemFax=None, OrigemContactoNome=None, OrigemContactoTelefone=None,
                 OrigemContactoTelemovel=None, OrigemContactoEmail=None, DestinoLojaId=None,
                 DestinoMoradaLinha2=None, DestinoContactoTelefone=None, DestinoContactoTelemovel=None,
                 DestinoContactoNome=None,
                 DestinoContactoEmail=None, DestinoLojaAlternativaId=None, DestinoLojaAlternativaNomeReceptor=None,
                 DestinoLojaAlternativaEmailReceptor=None, DestinoLojaAlternativaTelemovelReceptor=None, ObservacoesLinha1=None,
                 ObservacoesLinha2=None, Peso=None, Referencia=None, ValorCOD=None):
        self.Conta = Conta
        self.OrigemMoradaNome = OrigemMoradaNome
        self.OrigemMoradaLinha1 = OrigemMoradaLinha1
        self.OrigemMoradaCodigoPostal = OrigemMoradaCodigoPostal
        self.OrigemMoradaLocalidade = OrigemMoradaLocalidade
        self.OrigemMoradaPais = OrigemMoradaPais
        self.OrigemEmail = OrigemEmail
        self.TipoDestino = TipoDestino
        self.DestinoMoradaNome = DestinoMoradaNome
        self.DestinoMoradaLinha1 = DestinoMoradaLinha1
        self.NumeroVolumes = NumeroVolumes
        #self.tipoResposta = tipoResposta
        self.DataExpedicao = DataExpedicao
        self.EnviarEtiquetasEmail = EnviarEtiquetasEmail
        #self.tipoEtiqueta = tipoEtiqueta
        self.DestinoMoradaCodigoPostal = DestinoMoradaCodigoPostal
        self.DestinoMoradaLocalidade = DestinoMoradaLocalidade
        self.DestinoMoradaPais = DestinoMoradaPais
        self.OrigemMoradaLinha2 = OrigemMoradaLinha2
        self.OrigemTelefone = OrigemTelefone
        self.OrigemTelemovel = OrigemTelemovel
        self.OrigemFax = OrigemFax
        self.OrigemContactoNome = OrigemContactoNome
        self.OrigemContactoTelefone = OrigemContactoTelefone
        self.OrigemContactoTelemovel = OrigemContactoTelemovel
        self.OrigemContactoEmail = OrigemContactoEmail
        self.DestinoLojaId = DestinoLojaId
        self.DestinoMoradaLinha2 = DestinoMoradaLinha2
        self.DestinoContactoTelefone = DestinoContactoTelefone
        self.DestinoContactoTelemovel = DestinoContactoTelemovel
        #self.DestinoMoradaFax = DestinoMoradaFax
        #self.DestinoMoradaEmail = DestinoMoradaEmail
        self.DestinoContactoNome = DestinoContactoNome
        #self.DestinoMoradaTelefone = DestinoMoradaTelefone
        #self.DestinoMoradaTelemovel = DestinoMoradaTelemovel
        self.DestinoContactoEmail = DestinoContactoEmail
        self.DestinoLojaAlternativaId = DestinoLojaAlternativaId
        self.DestinoLojaAlternativaNomeReceptor = DestinoLojaAlternativaNomeReceptor
        self.DestinoLojaAlternativaEmailReceptor = DestinoLojaAlternativaEmailReceptor
        self.DestinoLojaAlternativaTelemovelReceptor = DestinoLojaAlternativaTelemovelReceptor
        self.ObservacoesLinha1 = ObservacoesLinha1
        self.ObservacoesLinha2 = ObservacoesLinha2
        self.Peso = Peso
        self.Referencia = Referencia
        self.ValorCOD = ValorCOD