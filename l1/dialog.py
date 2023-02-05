from PyQt5 import QtWidgets, uic
import json

class Runner(QtWidgets.QDialog):
    window = None

    def __init__(self):
        super().__init__()
        with open('dialog.ui', encoding="utf-8") as f:
            uic.loadUi(f, self)
        self.pushButtonLoad.clicked.connect(self.onLoadClick)

    def onLoadClick(self):
        KRAJE = []
        if self.checkBoxJc.isChecked():
            KRAJE.append('jc')
        if self.checkBoxJm.isChecked():
            KRAJE.append('jm')
        if self.checkBoxKa.isChecked():
            KRAJE.append('ka')
        if self.checkBoxKh.isChecked():
            KRAJE.append('kh')
        if self.checkBoxLb.isChecked():
            KRAJE.append('lb')
        if self.checkBoxMs.isChecked():
            KRAJE.append('ms')
        if self.checkBoxOl.isChecked():
            KRAJE.append('ol')
        if self.checkBoxPa.isChecked():
            KRAJE.append('pa')
        if self.checkBoxPl.isChecked():
            KRAJE.append('pl')
        if self.checkBoxSt.isChecked():
            KRAJE.append('st')
        if self.checkBoxUs.isChecked():
            KRAJE.append('us')
        if self.checkBoxVy.isChecked():
            KRAJE.append('vy')
        if self.checkBoxZl.isChecked():
            KRAJE.append('zl')

        self.plainTextEditInfo.appendPlainText("Právě jsi vybral kraje: " + json.dumps(KRAJE))
        self.plainTextEditInfo.appendPlainText("\nTvým úkolem je vypsat informace o vybraných krajích ze souboru kraje.geojson. Zajímá nás název a region soudržnosti.")

def main():
    app = QtWidgets.QApplication([])
    window = Runner()
    window.show()
    return app.exec()

main()
