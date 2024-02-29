import select
import socket
import sys

import PyQt5.QtCore
import PyQt5.QtWidgets
import PyQt5.uic

client_socket = socket.socket()
client_socket.connect(("localhost", 8080))


class SocketReaderThread(PyQt5.QtCore.QThread):
    data_received = PyQt5.QtCore.pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            if client_socket in select.select([client_socket], [], [], 0)[0]:
                received_data = client_socket.recv(1024).decode()
                self.data_received.emit(received_data)


class MainWindow(PyQt5.QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        PyQt5.uic.loadUi("form.ui", self)
        self.ui_components()
        self.btn_functions()
        self.show()
        self.socket_thread = SocketReaderThread()
        self.socket_thread.data_received.connect(self.handle_received_data)
        self.socket_thread.start()

    def handle_received_data(self, received_data):
        self.chatPlain.appendPlainText(received_data)

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
        text = self.messagePlain.toPlainText()
        if text != "":
            client_socket.send(bytes(text, "utf-8"))
            self.messagePlain.clear()


app = PyQt5.QtWidgets.QApplication(sys.argv)
window = MainWindow()
sys.exit(app.exec())
