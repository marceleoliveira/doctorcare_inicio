from PyQt5 import uic, QtWidgets
import pyodbc

dados_conexao = (
    "Driver={SQL Server};"
    "Server=DESKTOP-3S3ERL1\\SQLEXPRESS;"
    "Database=Doctor_Care;"
)

conexao = pyodbc.connect(dados_conexao)

def validar_codigo(codigo):
    cursor = conexao.cursor()
    comando = "SELECT COUNT(*) FROM Ativacao_dc WHERE codigo = ?"
    dados = (codigo,)
    cursor.execute(comando, dados)
    resultado = cursor.fetchone()
    return resultado[0] > 0

class TelaErroInicio(QtWidgets.QMainWindow):
    def __init__(self, ativacao_dc_instance):
        super(TelaErroInicio, self).__init__()
        uic.loadUi("erro_inicio_dc.ui", self)
        self.ativacao_dc = ativacao_dc_instance
        self.pushButton_2.clicked.connect(self.tentar_novamente)

    def tentar_novamente(self):
        self.hide()
        self.ativacao_dc.limpar_campos()
        self.ativacao_dc.show()

class TelaInicio(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaInicio, self).__init__()
        uic.loadUi("inicio_dc.ui", self)

class AtivacaoDC(QtWidgets.QMainWindow):
    def __init__(self, tela_inicio, tela_erro_inicio):
        super(AtivacaoDC, self).__init__()
        uic.loadUi("ativacao_dc.ui", self)
        self.tela_inicio = tela_inicio
        self.tela_erro_inicio = tela_erro_inicio

        self.pushButton.clicked.connect(self.funcao_principal)

    def funcao_principal(self):
        chave = self.lineEdit_2.text()

        print("Chave do produto:", chave)

        if validar_codigo(chave):
            print("Código válido. Direcionando para Tela Início.")
            self.tela_erro_inicio.hide()
            self.tela_inicio.show()
            self.limpar_campos()
            self.hide()
        else:
            print("Código não é válido. Direcionando para Tela Erro Início.")
            self.tela_inicio.hide()
            self.tela_erro_inicio.ativacao_dc = self
            self.tela_erro_inicio.show()
            self.hide()

    def limpar_campos(self):
        self.lineEdit_2.clear()

app = QtWidgets.QApplication([])

tela_inicio = TelaInicio()
tela_erro_inicio = TelaErroInicio(ativacao_dc_instance=None)
ativacao_dc = AtivacaoDC(tela_inicio, tela_erro_inicio)

tela_erro_inicio.ativacao_dc = ativacao_dc

ativacao_dc.show()
app.exec()
