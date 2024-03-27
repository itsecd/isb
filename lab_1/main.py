import sys

from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QApplication,
    QPushButton,
    QToolTip,
    QVBoxLayout,
    QGridLayout,
    QScrollArea,
    QDialog,
    QLineEdit,
    QFileDialog,
    QMessageBox,
)
from PyQt5.QtGui import QFont, QIcon

import lib


class MessageBox:
    def __init__(self, parent: QWidget, text: str) -> None:
        """constructor of MessageBox
        Args:
            parent (_type_): QWidget
            text (str): text to show
        """
        message_box = QMessageBox(parent)
        message_box.setText(text)
        ok_button = message_box.addButton(QMessageBox.Ok)
        ok_button.setStyleSheet(
            "background:#0e172c; border-radius: 5px; min-width: 100px;"
        )
        message_box.setStyleSheet("color: white")
        message_box.exec_()


class ScrollLabel(QScrollArea):
    def __init__(self, *args, **kwargs) -> None:
        """
        Constructor of ScrollLabel
        """
        QScrollArea.__init__(self, *args, **kwargs)
        self.setWidgetResizable(True)
        text = QWidget(self)
        self.setWidget(text)
        lay = QVBoxLayout(text)
        self.label = QLabel(text)
        self.label.setWordWrap(True)
        lay.addWidget(self.label)
        self.label.setFont(QFont("SansSerif", 15))

    def setText(self, text: str) -> None:
        """The function set text to ScrollLabel object

        Args:
            text (str): text to set
        """
        self.label.setText(text)


class Window(QWidget):
    def __init__(self) -> None:
        """
        Constructor of main Window
        """
        super().__init__()
        self.initUI()
        self.setStyleSheet(
            "background:#061E33; color: #C3D0DB; font-weight:bold; border-radius: 5px;"
        )

    def initUI(self) -> None:
        """
        The function create an UI object of main Window
        """
        self.showFullScreen()

        self.setWindowTitle("Encoder")
        QToolTip.setFont(QFont("SansSerif", 10))
        self.setWindowIcon(QIcon("home.png"))

        self.button_load_key_from_file = QPushButton("Load key", self)
        self.button_load_key_from_file.adjustSize()
        self.button_load_key_from_file.setFont(QFont("Arial", 15))
        self.button_load_key_from_file.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;"
        )
        self.button_load_key_from_file.clicked.connect(self.key_window)

        self.button_load_text_from_file = QPushButton("Load text", self)
        self.button_load_text_from_file.adjustSize()
        self.button_load_text_from_file.setFont(QFont("Arial", 15))
        self.button_load_text_from_file.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;"
        )
        self.button_load_text_from_file.clicked.connect(self.text_window)

        self.crypt = QPushButton("Decrypt/Crypt", self)
        self.crypt.adjustSize()
        self.crypt.setFont(QFont("Arial", 15))
        self.crypt.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;"
        )
        self.crypt.clicked.connect(self.double_choice)

        self.exit = QPushButton("Exit", self)
        self.exit.adjustSize()
        self.exit.setFont(QFont("Arial", 15))
        self.exit.setStyleSheet(
            "background:#8C5A75; border-radius: 5px; min-width: 300px; min-height: 200px;"
        )
        self.exit.clicked.connect(self.choice_exit)

        self.text_main_label = ScrollLabel(self)
        self.text_main_label.setStyleSheet("background:#d9d4e7; color: #3C5A75; ")

        self.key_main_label = ScrollLabel(self)
        self.key_main_label.setStyleSheet("background:#f9d4e7; color: #3C5A75; ")

        self.freq_main_label = ScrollLabel(self)
        self.freq_main_label.setStyleSheet("background:#a9d4e7; color: #3C5A75; ")

        layout = QGridLayout()
        self.setLayout(layout)

        layout.addWidget(self.button_load_key_from_file, 0, 0)
        layout.addWidget(self.button_load_text_from_file, 1, 0)
        layout.addWidget(self.crypt, 2, 0)
        layout.addWidget(self.exit, 3, 0)
        layout.addWidget(self.text_main_label, 0, 2, 4, 1)
        layout.addWidget(self.key_main_label, 0, 3, 2, 1)
        layout.addWidget(self.freq_main_label, 2, 3, 2, 1)
        self.show()

    def dialogue_window(self) -> None:
        """
        The function show dialog window to load text or key files
        """
        dialog = QDialog(self)
        dialog.setWindowTitle("Load")
        dialog.setFixedSize(500, 200)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet("color: #C3D0DB; min-height:30%")
        self.file_path = ""
        self.path_line_edit = QLineEdit(dialog)
        self.path_line_edit.setEnabled(False)
        self.path_line_edit.setTextMargins(10, 10, 10, 10)
        self.path_line_edit.setStyleSheet(
            "background:#d9d4e7; border-radius: 5px; color: #0e172c; min-height:30%"
        )

        browse_button = QPushButton("Select path", dialog)
        browse_button.setFont(QFont("Sanserif", 10))
        if self.mode == "key":
            browse_button.clicked.connect(self.select_key_path)
        elif self.mode == "text":
            browse_button.clicked.connect(self.select_text_path)
        browse_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%"
        )
        browse_button.adjustSize()

        load_button = QPushButton("Load file", dialog)
        load_button.setFont(QFont("Sanserif", 10))
        load_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px;min-height:30%"
        )
        if self.mode == "key":
            load_button.clicked.connect(self.load_key_from_file)
        elif self.mode == "text":
            load_button.clicked.connect(self.load_text_from_file)
        load_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.path_line_edit)
        layout.addWidget(browse_button)
        layout.addWidget(load_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def double_choice(self) -> None:
        """
        The function show window to save a result of crypting/decrypting
        """
        dialog = QDialog(self)
        dialog.setWindowTitle("Decrypt/Encrypt")
        dialog.setFixedSize(500, 250)
        path_label = QLabel("Choose path:", dialog)
        path_label.setStyleSheet("color: #C3D0DB; min-height:30%")
        self.new_folderpath = ""

        self.new_path_line_edit = QLineEdit(dialog)
        self.new_path_line_edit.setEnabled(False)
        self.new_path_line_edit.setTextMargins(10, 10, 10, 10)
        self.new_path_line_edit.setStyleSheet(
            "background:#d9d4e7; border-radius: 5px; color: #0e172c;"
        )

        path_to_save_button = QPushButton("Browse destination directory", dialog)
        path_to_save_button.setFont(QFont("Sanserif", 10))
        path_to_save_button.clicked.connect(self.path_to_save)
        path_to_save_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%"
        )
        path_to_save_button.adjustSize()

        decyp_button = QPushButton("Decrypt ", dialog)
        decyp_button.setFont(QFont("Sanserif", 10))
        decyp_button.clicked.connect(self.decrypt_by_key)
        decyp_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%"
        )
        decyp_button.adjustSize()

        cyp_button = QPushButton("Encrypt", dialog)
        cyp_button.setFont(QFont("Sanserif", 10))
        cyp_button.setStyleSheet(
            "background:#3C5A75; border-radius: 5px; min-height:30%"
        )
        cyp_button.clicked.connect(self.encrypt_by_key)
        cyp_button.adjustSize()

        layout = QVBoxLayout()
        layout.addWidget(path_label)
        layout.addWidget(self.new_path_line_edit)
        layout.addWidget(path_to_save_button)
        layout.addWidget(decyp_button)
        layout.addWidget(cyp_button)
        dialog.setLayout(layout)

        dialog.exec_()

    def key_window(self) -> None:
        """
        Function switch mode to 'key' and run dialogue_window with this mode
        """
        self.mode = "key"
        self.dialogue_window()

    def text_window(self) -> None:
        """
        Function switch mode to 'text' and run dialogue_window with this mode
        """
        self.mode = "text"
        self.dialogue_window()

    def select_key_path(self) -> None:
        """
        The function gets the path to the cryption-key (.json) file
        """
        self.key_path = QFileDialog.getOpenFileNames(
            self, "Load key", "", "Json files(*.json)"
        )
        if len(self.key_path[0]) > 0:
            self.key_path = self.key_path[0][0].replace("/", "\\")
            self.path_line_edit.setText(self.key_path)
        else:
            MessageBox(self, "Incorrect path")
            self.key_path = ""

    def select_text_path(self) -> None:
        """
        The function gets the path to the text (.txt) file
        """
        self.text_path = QFileDialog.getOpenFileNames(
            self, "Load text", "", "Text files (*.txt)"
        )
        if len(self.text_path[0]) > 0:
            self.text_path = self.text_path[0][0].replace("/", "\\")
            self.path_line_edit.setText(self.text_path)
        else:
            MessageBox(self, "Incorrect path")
            self.text_path = ""

    def load_key_from_file(self) -> None:
        """
        The function runs a library function to read the key from a file and display it in window
        """
        try:
            self.key = lib.get_key(self.key_path)
            self.key_main_label.setText(lib.print_dict(self.key))
        except AttributeError:
            MessageBox(self, "Incorrect path")

    def load_text_from_file(self) -> None:
        """
        The function runs a library function to read the text and analysis its symbol frequency from a file and display it in window
        """
        try:
            self.text = lib.get_text(self.text_path)
            self.text_main_label.setText(self.text)
            self.freq_main_label.setText(lib.print_dict(lib.get_freq(self.text)))
        except AttributeError:
            MessageBox(self, "Incorrect path")

    def path_to_save(self) -> None:
        """
        The function gets the path to the save file
        """
        self.result_text_path = (QFileDialog.getSaveFileName(self, "Select File"))[
            0
        ].replace("/", "\\")
        self.new_path_line_edit.setText(self.result_text_path)

    def decrypt_by_key(self) -> None:
        """
        The function decrypts the text and writes it to a file
        """
        try:
            res_text = lib.decrypt_by_key(self.text, self.key)
            lib.write_to_file(res_text, self.result_text_path)
        except AttributeError:
            MessageBox(self, "Load text and key")

    def encrypt_by_key(self) -> None:
        """
        The function crypts the text and writes it to a file
        """
        try:
            res_text = lib.encrypt_by_key(self.text, self.key)
            lib.write_to_file(res_text, self.result_text_path)
        except AttributeError:
            MessageBox(self, "Load text and key")

    def choice_exit(self) -> None:
        """
        The function closes the program
        """
        sys.exit()


def run() -> None:
    """
    The function makes a main Window and show it
    """
    app = QApplication(sys.argv)
    ex = Window()
    ex.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    run()
