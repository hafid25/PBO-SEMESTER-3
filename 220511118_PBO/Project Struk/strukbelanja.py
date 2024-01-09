from PyQt5.QtWidgets import * 
from PyQt5 import uic

class MyGUI(QMainWindow):

    def __init__(self):
        super(MyGUI, self).__init__()
        uic.loadUi("struk_fixed.ui", self)
        self.show()

        self.pushButton.clicked.connect(self.tambah_barang)

    def tambah_barang(self):
        # Get input values from the QLineEdit widgets
        nama_barang = self.lineEdit.text()
        harga = float(self.lineEdit_2.text())
        jumlah = int(self.lineEdit_3.text())

        # Calculate total cost
        total_biaya = harga * jumlah

        # Display the result in the QLineEdit widget
        current_text = self.lineEdit_4.toPlainText()
        new_text = f"{current_text}{'='*20}\n==STRUK TAGIHAN BELANJA==\n{'='*20}\nNama Barang: {nama_barang}\nHarga: Rp. {harga}\nJumlah: {jumlah}\nTotal Harga: Rp. {total_biaya}\n{'='*20}\nTERIMA KASIH KUNJUNGANNYA\n{'='*20}\n"

        self.lineEdit_4.setText(new_text)

        # Clear input fields for the next entry
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()

def main():
    app = QApplication([])
    window = MyGUI()
    app.exec_()

if __name__ == '__main__':
    main()