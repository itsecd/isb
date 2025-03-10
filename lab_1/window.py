import sys
from PyQt5.QtWidgets import (
    QApplication, 
    QWidget, 
    QVBoxLayout, 
    QPushButton,
    QLabel, 
    QTextEdit, 
    QFileDialog
)

from function import *


class EncryptionApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Encryption Tool')

        layout = QVBoxLayout()

        self.label = QLabel('Load text and key to encrypt:')
        layout.addWidget(self.label)

        self.text_edit = QTextEdit()
        self.text_edit.setReadOnly(True)
        layout.addWidget(self.text_edit)

        self.load_text_button = QPushButton('Load Text')
        self.load_text_button.clicked.connect(self.load_text)
        layout.addWidget(self.load_text_button)

        self.load_key_button = QPushButton('Load Key')
        self.load_key_button.clicked.connect(self.load_key)
        layout.addWidget(self.load_key_button)

        self.encrypt_button = QPushButton('Encrypt')
        self.encrypt_button.clicked.connect(self.encrypt_text)
        layout.addWidget(self.encrypt_button)

        self.save_encrypted_button = QPushButton('Save Encrypted Text')
        self.save_encrypted_button.clicked.connect(self.save_encrypted_text)
        layout.addWidget(self.save_encrypted_button)

        self.save_frequency_button = QPushButton('Save Frequency Analysis')
        self.save_frequency_button.clicked.connect(self.save_frequency_analysis)
        layout.addWidget(self.save_frequency_button)

        self.setLayout(layout)


    def load_text(self):
        text_path, _ = QFileDialog.getOpenFileName(self, 'Open Text File', '', 'Text Files (*.txt)')
        if text_path:
            self.text = read_txt_file(text_path)
            self.text_edit.setPlainText(self.text)
            print("Text loaded successfully.")


    def load_key(self):
        key_path, _ = QFileDialog.getOpenFileName(self, 'Open Key File', '', 'JSON Files (*.json)')
        if key_path:
            self.key = read_key(key_path)
            print("Key loaded successfully.")


    def encrypt_text(self):
        if hasattr(self, 'text') and hasattr(self, 'key'):
            encrypted_text = encryption(self.text, self.key)
            self.text_edit.setPlainText(encrypted_text)
            print("Text encrypted successfully.")
        else:
            print("Please load text and key first.")


    def save_encrypted_text(self):
        encrypted_text = self.text_edit.toPlainText()
        if encrypted_text:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Encrypted Text File', '', 'Text Files (*.txt)')
            if save_path:
                write_txt_file(encrypted_text, save_path)
                print("Encrypted text saved successfully.")


    def save_frequency_analysis(self):
        encrypted_text = self.text_edit.toPlainText()
        if encrypted_text:
            save_path, _ = QFileDialog.getSaveFileName(self, 'Save Frequency Analysis File', '', 'JSON Files (*.json)')
            if save_path:
                save_frequency(save_path, encrypted_text)
                print("Frequency analysis saved successfully.")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = EncryptionApp()
    ex.resize(400, 300)
    ex.show()
    sys.exit(app.exec_())
