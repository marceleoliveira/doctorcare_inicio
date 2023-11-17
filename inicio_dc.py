from PyQt5 import uic, QtWidgets

class TelaInicio(QtWidgets.QMainWindow):
    def __init__(self):
        super(TelaInicio, self).__init__()
        uic.loadUi("inicio_dc.ui", self)
