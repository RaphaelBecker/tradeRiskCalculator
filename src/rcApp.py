#!/usr/bin/env python
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtWidgets
from src import calculator as cal

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QGroupBox, QCheckBox
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QDialogButtonBox
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QVBoxLayout


class Dialog(QDialog):
    long_short = True  # True == long, False == short

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        self.savedText = {}

        button_box = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        button_box.accepted.connect(self.calculate_trade)
        button_box.rejected.connect(self.reject)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.form_group_box_insert)
        main_layout.addWidget(button_box)
        self.setLayout(main_layout)
        self.setWindowTitle("Trade Risk Caluclator: Long")
        self.setGeometry(300, 300, 350, 250)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('Trade Risk Caluclator: Short')
            self.long_short = False
        else:
            self.setWindowTitle('Trade Risk Caluclator: Long')
            self.long_short = True

    def createFormGroupBox(self):
        self.form_group_box_insert = QGroupBox(" ")
        self.layout_insert = QFormLayout()
        self.available_balance = QLineEdit()
        self.available_balance.textEdited.connect(self.make_saveTextEdit(1))
        self.trade = QLineEdit()
        self.trade.textEdited.connect(self.make_saveTextEdit(2))
        self.current_price = QLineEdit()
        self.current_price.textEdited.connect(self.make_saveTextEdit(3))
        self.leverage = QLineEdit()
        self.leverage.textEdited.connect(self.make_saveTextEdit(4))
        self.cb = QCheckBox('short', self)
        self.cb.stateChanged.connect(self.changeTitle)
        self.layout_insert.addRow(self.cb)
        self.layout_insert.addRow(QLabel("Available balance [crypt]:"), self.available_balance)
        self.layout_insert.addRow(QLabel("Initial bet [crypt]:"), self.trade)
        self.layout_insert.addRow(QLabel("Current price [fiat]:"), self.current_price)
        self.layout_insert.addRow(QLabel("Leverage:"), self.leverage)

        self.output_rd = QtWidgets.QTextBrowser(self.form_group_box_insert)
        self.output_rd.setGeometry(QtCore.QRect(10, 90, 331, 111))
        self.output_rd.setObjectName("output_rd")
        self.layout_insert.addRow(self.output_rd)

        self.form_group_box_insert.setLayout(self.layout_insert)

    def make_saveTextEdit(self, x):
        def saveTextEdit(text):
            self.savedText[x] = text

        return saveTextEdit

    def calculate_trade(self):
        try:
            bal = float(dialog.available_balance.text())
            ft = float(dialog.trade.text())
            cp = float(dialog.current_price.text())
            lev = int(dialog.leverage.text())
            if self.long_short:
                long_return_string = cal.calc_long_trade(bal, ft, cp, lev)
                self.output_rd.append(long_return_string)
            else:
                short_return_string = cal.calc_short_trade(bal, ft, cp, lev)
                self.output_rd.append(short_return_string)
        except ValueError:
            print('Only float values allowed!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
    dialog.exec_()
    app.exit()
