import logging


class Delivery:
    def __init__(self, OrigemMoradaNome: str, OrigemMorada: str, OrigemMoradaCodigoPostal: str, OrigemMoradaLocalidade: str,
                 OrigemEmail: str, DestinoMoradaNome: str, DestinoMorada: str,
                 NumeroVolumes: int, DataExpedicao: str,
                 Conta: str = "02496101", OrigemMoradaPais: str = "PT", TipoDestino: int = 1,
                 EnviarEtiquetasEmail: int = 2,
                 DestinoMoradaCodigoPostal: str = "", DestinoMoradaLocalidade: str = "", DestinoMoradaPais: str="PT",
                 OrigemMoradaLinha2="", OrigemTelefone="", OrigemTelemovel="",
                 OrigemFax="", OrigemContactoNome="", OrigemContactoTelefone="",
                 OrigemContactoTelemovel="", OrigemContactoEmail="", DestinoLojaId="", DestinoContactoTelefone="", DestinoContactoTelemovel="",
                 DestinoContactoNome="",
                 DestinoContactoEmail="", DestinoLojaAlternativaId="", DestinoLojaAlternativaNomeReceptor="",
                 DestinoLojaAlternativaEmailReceptor="", DestinoLojaAlternativaTelemovelReceptor="", ObservacoesLinha1="",
                 ObservacoesLinha2="", Peso="", Referencia="", ValorCOD=""):

        self.DestinoMoradaLinha1 = DestinoMorada[0:31]
        self.DestinoMoradaLinha2 = DestinoMorada[31:64]
        self.Conta = Conta
        self.OrigemMoradaNome = OrigemMoradaNome

        self.OrigemMoradaLinha1 = OrigemMorada[0:31]
        self.OrigemMoradaLinha2 = OrigemMorada[31:63]

        self.OrigemMoradaCodigoPostal = OrigemMoradaCodigoPostal
        self.OrigemMoradaLocalidade = OrigemMoradaLocalidade
        self.OrigemMoradaPais = OrigemMoradaPais
        self.OrigemEmail = OrigemEmail
        self.TipoDestino = TipoDestino
        self.DestinoMoradaNome = DestinoMoradaNome
        self.NumeroVolumes = NumeroVolumes
        #self.tipoResposta = tipoResposta
        self.DataExpedicao = DataExpedicao
        self.EnviarEtiquetasEmail = EnviarEtiquetasEmail
        #self.tipoEtiqueta = tipoEtiqueta
        self.DestinoMoradaCodigoPostal = DestinoMoradaCodigoPostal
        self.DestinoMoradaLocalidade = DestinoMoradaLocalidade
        self.DestinoMoradaPais = DestinoMoradaPais
        # self.OrigemMoradaLinha2 = OrigemMoradaLinha2
        # self.OrigemTelefone = OrigemTelefone
        # self.OrigemTelemovel = OrigemTelemovel
        # self.OrigemFax = OrigemFax
        # self.OrigemContactoNome = OrigemContactoNome
        # self.OrigemContactoTelefone = OrigemContactoTelefone
        # self.OrigemContactoTelemovel = OrigemContactoTelemovel
        # self.OrigemContactoEmail = OrigemContactoEmail
        # self.DestinoLojaId = DestinoLojaId
        # self.DestinoMoradaLinha2 = DestinoMoradaLinha2
        # self.DestinoContactoTelefone = DestinoContactoTelefone
        # self.DestinoContactoTelemovel = DestinoContactoTelemovel
        #self.DestinoMoradaFax = DestinoMoradaFax
        #self.DestinoMoradaEmail = DestinoMoradaEmail
        #self.DestinoContactoNome = DestinoContactoNome
        #self.DestinoMoradaTelefone = DestinoMoradaTelefone
        #self.DestinoMoradaTelemovel = DestinoMoradaTelemovel
        #self.Peso = Peso
        #self.Referencia = Referencia
        #self.ValorCOD = ValorCOD

        if self.OrigemMoradaLinha1 + self.OrigemMoradaLinha2 != OrigemMorada:
            logging.warning("Origem Morada has more than max 64 characters allowed please consider limiting this field")

        if self.DestinoMoradaLinha1 + self.DestinoMoradaLinha2 != DestinoMorada:
            logging.warning("Destino Morada has more than max 64 characters allowed please consider limiting this field")
