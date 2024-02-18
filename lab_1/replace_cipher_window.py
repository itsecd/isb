import sys
import crypto
import file_handler

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    """ Main window of the gui-program
    Methods:
        setupUi(MainWindow): creating widget objects
        retranslateUi(MainWindow): sets the text and headers of the widgets
        __warning_icon(text, info): pop-up message when an exception occurs
        __success_icon(text, info): pop-up message when the process is success
        get_key(self): reading the decoding key from the json file
        load_file(): downloading text from a file
        save_file(): saving text to a file from a text field
        decode(self): decryption of the text by the key"
    """
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """ Creating widget objects in the appropriate containers
        Args:
            MainWindow: base window of the gui-program        
        """
        self.path = None
        self.key = None
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 781, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 561, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 350, 181, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.decode)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 430, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.encryptedplainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.encryptedplainTextEdit.setGeometry(QtCore.QRect(50, 150, 651, 131))
        self.encryptedplainTextEdit.setObjectName("encryptedplainTextEdit")
        self.decryptedTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.decryptedTextEdit.setGeometry(QtCore.QRect(50, 500, 651, 131))
        self.decryptedTextEdit.setObjectName("decryptedTextEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load_file)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 460, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.save_file)
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(50, 310, 111, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.get_key)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 820, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Sets the text and headers of the widgets
        Args:
            MainWindow: base window of the gui-program  
        """
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Расшифровка текста, закодированного шифром простой подстановки, по ключу"))
        self.label_2.setText(_translate("MainWindow", "Введите текст для расшифровки или загрузите из файла"))
        self.label_3.setText(_translate("MainWindow", "Загрузите ключ"))
        self.pushButton.setText(_translate("MainWindow", "Расшифровать"))
        self.label_4.setText(_translate("MainWindow", "Расшифрованный текст"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить результат"))
        self.pushButton_4.setText(_translate("MainWindow", "Загрузить файл"))
        
    def get_key(self) -> None:
        """Reading the decoding key from the json file"""
        path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if path != "":
            try:
                self.key = file_handler.read_json(path)
            except Exception as e:
                self.__warning_icon("Ошибка", f"Детали ошибки: {e}")
        else:
            self.__warning_icon("Предупреждение", "Вы не выбрали файл")
        
        
    def decode(self) -> None:
        """Decryption of the text encoded with a simple substitution cipher by the key"""
        code = self.encryptedplainTextEdit.toPlainText()
        if self.key is None:
            self.__warning_icon("Предупреждение", "Выберите ключ декодирования")
            return
        try:
            decrypted_text = crypto.decryption_by_key(code, self.key)
            self.decryptedTextEdit.setPlainText(decrypted_text)
        except Exception as e:
            self.__warning_icon("Ошибка", f"Детали ошибки: {e}")
        
    def __warning_icon(self, text: str, info: str) -> None:
        """A pop-up message when an exception occurs
        Args:
            text: the MessageBox header
            info: text of MessageBox
        """
        error = QtWidgets.QMessageBox()
        error.setIcon(QMessageBox.Warning)
        error.setWindowTitle(text)
        error.setText(info)
        error.exec_()

    def __success_icon(self, text: str, info: str) -> None:
        """A pop-up message when the process is completed successfully
        Args:
            text: the MessageBox header
            info: text of MessageBox
        """
        success = QtWidgets.QMessageBox()
        success.setWindowTitle(text)
        success.setText(info)
        success.exec_()

    def load_file(self) -> None:
        '''Downloading text from a file'''
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if self.path != '':
            try:
                with open(self.path, "r", encoding="utf-8") as file:
                    self.encryptedplainTextEdit.setPlainText(file.read())
            except Exception as e:
                self.__warning_icon("Ошибка", f"Детали ошибки: {e}")
        else:
            self.__warning_icon("Предупреждение", "Вы не выбрали файл")

    def save_file(self) -> None:
        '''Saving text to a file from a text field'''
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if self.path != '':
            try:
                with open(self.path, "w", encoding="utf-8") as file:
                    file.write(self.decryptedTextEdit.toPlainText())
                    self.__success_icon("Сообщение", "Текст записан в файл")
            except Exception as e:
                self.__warning_icon("Ошибка", f"Детали ошибки: {e}")
        else:
            self.__warning_icon("Предупреждение", "Вы не выбрали файл")

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
