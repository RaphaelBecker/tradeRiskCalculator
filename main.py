# #!/usr/bin/env python

import calculator as cal

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QGroupBox, QWidget, QTextBrowser
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout

class Dialog(QDialog):
    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        self.savedText = {}

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonBox.accepted.connect(self.calculate)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("Trade Risk Caluclator")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Insert values:")
        self.layout = QFormLayout()
        self.available_balance = QLineEdit()
        self.available_balance.textEdited.connect(self.make_saveTextEdit(1))
        self.trade = QLineEdit()
        self.trade.textEdited.connect(self.make_saveTextEdit(2))
        self.current_price = QLineEdit()
        self.current_price.textEdited.connect(self.make_saveTextEdit(3))
        self.leverage = QLineEdit()
        self.leverage.textEdited.connect(self.make_saveTextEdit(4))
        self.layout.addRow(QLabel("Available Balance:"), self.available_balance)
        self.layout.addRow(QLabel("First trade:"), self.trade)
        self.layout.addRow(QLabel("Current price:"), self.current_price)
        self.layout.addRow(QLabel("Leverage:"), self.leverage)
        self.formGroupBox.setLayout(self.layout)

    def make_saveTextEdit(self, x):
        def saveTextEdit(text):
            self.savedText[x] = text
        return saveTextEdit

    def calculate(self):
        try:
            bal = float(dialog.available_balance.text())
            ft = float(dialog.trade.text())
            cp = float(dialog.current_price.text())
            lev = int(dialog.leverage.text())
            return_string = cal.calc_trade(bal, ft, cp, lev)
        except ValueError:
            print('Only float values allowed!')
        # self.statusBar().showMessage('Calculated!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec_()
    app.exit()