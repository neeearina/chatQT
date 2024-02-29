import socket
import sys

import PyQt5.QtWidgets
import PyQt5.uic

client_socket = socket.socket()
client_socket.connect(("localhost", 8080))


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        PyQt5.uic.loadUi("form.ui", self)
        self.ui_components()
        self.btn_functions()
        self.show()

    def ui_components(self):
        self.setWindowTitle("Chat")
        self.chatPlain.setReadOnly(True)
        btn_settings = (
            "QPushButton { background-color: #4B0082 }"
            "QPushButton:pressed { background-color: #6A5ACD }"
        )
        self.clearButton.setStyleSheet(btn_settings)
        self.sendButton.setStyleSheet(btn_settings)

    def btn_functions(self):
        self.clearButton.clicked.connect(self.clear_message)
        self.sendButton.clicked.connect(self.send_message)

    def clear_message(self):
        self.messagePlain.clear()

    def send_message(self):
        client_socket.send(bytes(
            self.messagePlain.toPlainText() + "\n", "utf-8"))
        self.chatPlain.appendPlainText(
            "\n you: " + self.messagePlain.toPlainText())
        self.messagePlain.clear()


app = PyQt5.QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
