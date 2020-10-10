# This Python file uses the following encoding: utf-8
import sys
import os
import handlers


from PySide2.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox
from PySide2.QtCore import QFile
from PySide2.QtUiTools import QUiLoader

def clicked2():
    print("clicked")
    msgBox = QMessageBox();
    msgBox.setText("The document has been modified.");
    msgBox.exec();


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.load_ui()

    def load_ui(self):
        loader = QUiLoader()
        path = os.path.join(os.path.dirname(__file__), "form.ui")
        ui_file = QFile(path)
        ui_file.open(QFile.ReadOnly)
        window = loader.load(ui_file, self)
        ui_file.close()


        #self.btnPusher = QPushButton('Push')
        #self.btnPusher.clicked.connect(self.Pushed)
        #BtnWdth = 175; BtnHght = 123
        #self.btnPusher.setFixedSize(BtnWdth, BtnHght)
        #self.setFixedSize(100,100)
        #self.addWidget(self.btnPusher)

        #btn = self.window.findChild(QPushButton, 'pushButton')
        btn1 = self.findChild(QPushButton, 'btn1')
        btn1.clicked.connect(clicked2)

if __name__ == "__main__":
    app = QApplication([])
    widget = MainWindow()

    #widget.btn1.setFixedSize(100,100)

    #widget.addWidget(self.btnPusher)

    #widget.btn1.clicked.connect(clicked)
    #btn1.clicked.connect(clicked)

    widget.show()
    sys.exit(app.exec_())
