import sys
import logging

from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QMessageBox,
    QComboBox,
    QFileDialog,
    QVBoxLayout,
    QWidget,
    QGridLayout,
)

import cryptography_part as cp

logging.basicConfig(level=logging.INFO)


class MainWindow(QMainWindow):
    def __init__(self) -> None:
        """Initialize the main window with buttons and layouts"""
        super().__init__()

        self.setGeometry(400, 100, 500, 500)
        self.setWindowTitle("Tooltips")
        main_widget = QWidget()
        button_layout = QVBoxLayout()
        layout = QGridLayout()

        self.setWindowTitle("Шифрование с помощью TripleDes")

        self.dialog = QFileDialog()
        self.dialog.setFileMode(QFileDialog.FileMode.Directory)
        self.symmetric_key_path = self.dialog.getSaveFileName(
            None, "Выберите файл (symmetric)", "", "Text File(*.txt)"
        )[0]
        self.public_key_path = self.dialog.getSaveFileName(
            None, "Выберите файл (public)", "", "Text File(*.pem)"
        )[0]
        self.private_key_path = self.dialog.getSaveFileName(
            None, "Выберите файл (private)", "", "Text File(*.pem)"
        )[0]
        self.key_size = 8

        self.comboBox = QComboBox()
        self.comboBox.addItem("Размер ключа")
        self.comboBox.addItems(["8", "16", "24"])
        self.comboBox.currentIndexChanged.connect(self.set_key_size)

        # кнопки
        self.btn_generation_key = self.add_button("Сгенерировать ключи", 250, 40)
        self.btn_encryption = self.add_button("Зашифровать текст", 250, 40)
        self.btn_decryption = self.add_button("Расшифровать текст", 250, 40)
        self.go_to_exit = self.add_button("Выйти из программы", 150, 40)

        # делаем виджеты адаптивными под размер окна
        button_layout.addWidget(self.comboBox)
        button_layout.addWidget(self.btn_generation_key)
        button_layout.addWidget(self.btn_encryption)
        button_layout.addWidget(self.btn_decryption)
        button_layout.addWidget(self.go_to_exit)
        layout.addLayout(button_layout, 0, 1)
        main_widget.setLayout(layout)
        self.setCentralWidget(main_widget)

        self.cryptography = cp.Cryptograthy(
            self.symmetric_key_path,
            self.public_key_path,
            self.private_key_path,
            self.key_size,
        )

        self.btn_generation_key.clicked.connect(self.generation)
        self.btn_encryption.clicked.connect(self.encryption_text)
        self.btn_decryption.clicked.connect(self.decryption_text)
        self.go_to_exit.clicked.connect(self.close)

        self.show()

    def add_button(self, name: str, size_x: int, size_y: int) -> QPushButton:
        """The function creates buttons with the specified names and sizes
        parametrs:
            name: the name of the button;
            size_x: size by x;
            size_y: size by y
        return QPushButton"""
        button = QPushButton(name, self)
        button.resize(button.sizeHint())
        button.setFixedSize(QSize(size_x, size_y))
        return button

    def set_key_size(self) -> None:
        """The functions that sets the key size from ComboBox in self.key_size"""
        self.key_size = int(self.comboBox.currentText())

    def generation(self) -> None:
        """The function calls metod key_generation from cryptography_part module.
        If one of the parameters MainWindow is empty - return to the MainWindow"""
        try:
            if (
                (self.symmetric_key_path == "")
                or (self.public_key_path == "")
                or (self.private_key_path == "")
            ):
                QMessageBox.information(
                    None, "Не указан путь", "Не был выбран файл для одного из ключей"
                )
                return
            self.cryptography.key_generation()
            QMessageBox.information(None, "Успешно", "Ключи сгенерированы успешно!")
        except Exception as ex:
            logging.error(f"Couldn't generation keys: {ex.message}\n{ex.args}\n")

    def encryption_text(self) -> None:
        """The function calls metod encryption from cryptography_part module.
        If one of the parameters MainWindow or cp.encryption is empty - return to the MainWindow
        """
        base_text = QFileDialog.getOpenFileName(
            self,
            "Выберите путь к файлу с исходным текстом:",
            "",
            "Text File(*.txt)",
        )[0]
        new_file = QFileDialog.getSaveFileName(
            self,
            "Выберите путь сохранения зашифрованного текста:",
            "",
            "Text File(*.txt)",
        )[0]
        try:
            if (not base_text) or (not new_file):
                QMessageBox.information(None, "Не указан путь", "Не был выбран путь")
                return
            self.cryptography.encryption(base_text, new_file)
            QMessageBox.information(None, "Успешно", "Текст зашифрован!")
        except Exception as ex:
            logging.error(f"Couldn't encryption text: {ex.message}\n{ex.args}\n")

    def decryption_text(self):
        """The function calls metod decryption from cryptography_part module.
        If one of the parameters MainWindow or cp.decryption is empty - return to the MainWindow
        """
        encryption_text = QFileDialog.getOpenFileName(
            self,
            "Выберите путь к файлу с зашифрованным текстом:",
            "",
            "Text File(*.txt)",
        )[0]
        new_file = QFileDialog.getSaveFileName(
            self,
            "Выберите путь сохранения дешифрованного текста:",
            "",
            "Text File(*.txt)",
        )[0]
        try:
            if (not encryption_text) or (not new_file):
                QMessageBox.information(None, "Не указан путь", "Не был выбран путь")
                return
            self.cryptography.decryption(encryption_text, new_file)
            QMessageBox.information(None, "Успешно", "Текст расшифрован!")
        except Exception as ex:
            logging.error(f"Couldn't encryption text:{ex.message}\n{ex.args}\n")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()
