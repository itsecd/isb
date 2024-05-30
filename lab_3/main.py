import json
import sys
sys.path.append('crypto')

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget, QComboBox, QPushButton, QMessageBox, QFileDialog
from crypto.file import generate_keys, encrypt_file, decrypt_file

class EncryptionApp(QMainWindow):
    def __init__(self):
        super().__init__()

        with open('settings.json', 'r') as f:
            self.settings = json.load(f)

        self.initUI()

    def initUI(self):
        self.setWindowTitle('Encryption App')
        self.setGeometry(100, 100, 400, 300)

        # Создание виджетов выбора действия
        self.mode_label = QLabel('Choose action:')
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Key Generation', 'Encryption', 'Decryption'])

        self.start_button = QPushButton('Start Action')

        # Создание макета для выбора действия
        layout = QVBoxLayout()
        layout.addWidget(self.mode_label)
        layout.addWidget(self.mode_combo)
        layout.addWidget(self.start_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Подключение сигналов к слотам
        self.start_button.clicked.connect(self.start_selected_action)

    def start_selected_action(self):
        selected_action = self.mode_combo.currentText().lower()

        match selected_action:
            case 'key generation':
                self.generate_keys()
            case 'encryption':
                self.encrypt_data()
            case 'decryption':
                self.decrypt_data()
                pass

    def generate_keys(self):
        # Получение путей к ключам из диалога с пользователем
        asym_private_key_path = self.get_file_path("Выберите путь для приватного ключа", "Файлы ключей (*.pem)")
        asym_public_key_path = self.get_file_path("Выберите путь для публичного ключа", "Файлы ключей (*.pem)")
        symmetric_key_path = self.get_file_path("Выберите путь для симметричного ключа", "Файлы ключей (*.txt)")

        # Генерация ключей
        generate_keys(asym_private_key_path, asym_public_key_path, symmetric_key_path)
        QMessageBox.information(self, 'Key Generation', 'Keys were generated successfully!')

    def encrypt_data(self):
        # Получение путей к файлам и ключам от пользователя
        initial_file_path = self.get_file_path("Выберите исходный файл", "Текстовые файлы (*.txt)")
        encrypted_file_path = self.get_file_path("Выберите путь для зашифрованного файла", "Текстовые файлы (*.txt)")
        asym_private_key_path = self.get_file_path("Выберите путь для приватного ключа", "Файлы ключей (*.pem)")
        symmetric_key_path = self.get_file_path("Выберите путь для симметричного ключа", "Файлы ключей (*.txt)")

        # Шифрование данных
        encrypt_file(initial_file_path, asym_private_key_path, symmetric_key_path, encrypted_file_path)
        QMessageBox.information(self, 'Encryption', 'Data was encrypted successfully!')

    def decrypt_data(self):
        # Получение путей к файлам и ключам от пользователя
        encrypted_file_path = self.get_file_path("Выберите зашифрованный файл", "Текстовые файлы (*.txt)")
        decrypted_file_path = self.get_file_path("Выберите путь для расшифрованного файла", "Текстовые файлы (*.txt)")
        asym_private_key_path = self.get_file_path("Выберите путь для приватного ключа", "Файлы ключей (*.pem)")
        symmetric_key_path = self.get_file_path("Выберите путь для симметричного ключа", "Файлы ключей (*.txt)")

        # Расшифровка данных
        decrypt_file(encrypted_file_path, asym_private_key_path, symmetric_key_path, decrypted_file_path)
        QMessageBox.information(self, 'Decryption', 'Decrypted text was saved to file.')

    def get_file_path(self, title, file_filter):
        # Диалог выбора файла
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle(title)
        file_dialog.setNameFilter(file_filter)
        if file_dialog.exec_():
            return file_dialog.selectedFiles()[0]
        return None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    enc_app = EncryptionApp()
    enc_app.show()
    sys.exit(app.exec_())
