from PyQt5 import uic, QtWidgets

class TelaErroInicio(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaErroInicio, self).__init__()
        uic.loadUi("erro_inicio_dc.ui", self)
