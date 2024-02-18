
import sys
import crypto

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_MainWindow(object):
    """ Main window of the gui-program 
    Methods:
        setupUi(MainWindow): creating widget objects
        retranslateUi(MainWindow): sets the text and headers of the widgets
        __warning_icon(text, info): pop-up message when an exception occurs
        __success_icon(text, info): pop-up message when the process is success
        caesar_cipher(): Caesar's Cipher
        load_file(): downloading text from a file
        save_file(): saving text to a file from a text field
    """
    def setupUi(self, MainWindow: QtWidgets.QMainWindow) -> None:
        """Creating widget objects in the appropriate containers
        Args:
            MainWindow: base window of the gui-program        
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(820, 687) 
        self.path = None
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(50, 80, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(50, 310, 113, 22))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(50, 280, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(50, 350, 181, 61))
        self.pushButton.setStyleSheet("background-color: rgb(255, 170, 127)")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.caesar_cipher)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(50, 430, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(50, 150, 651, 131))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(50, 500, 651, 131))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(50, 110, 111, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.load_file)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(50, 460, 151, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.save_file)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(390, 300, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(550, 300, 151, 31))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
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
        self.label.setText(_translate("MainWindow", "Шифр Цезаря"))
        self.label_2.setText(_translate("MainWindow", "Введите текст для шифрования или загрузите файл"))
        self.label_3.setText(_translate("MainWindow", "Ключ"))
        self.pushButton.setText(_translate("MainWindow", "Зашифровать"))
        self.label_4.setText(_translate("MainWindow", "Зашифрованный текст"))
        self.pushButton_2.setText(_translate("MainWindow", "Загрузить файл"))
        self.pushButton_3.setText(_translate("MainWindow", "Сохранить результат"))
        self.label_5.setText(_translate("MainWindow", "Выберите алфавит:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Русский"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Английский"))

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

    def caesar_cipher(self) -> None:
        """Caesar's Cipher"""
        text = self.plainTextEdit.toPlainText()
        key = self.lineEdit_2.text()
        alphabet = self.comboBox.currentText()
        if (key.isdigit() and int(key) > 0):
            encrypted_text = crypto.caesar_cipher(text, int(key), alphabet == "Английский")
            self.plainTextEdit_2.setPlainText(encrypted_text)
        else:
            self.__warning_icon("Предупреждение", "Введите корректное значение ключа key")

    def load_file(self) -> None:
        '''Downloading text from a file'''
        self.path = QtWidgets.QFileDialog.getOpenFileName()[0]
        if self.path != '':
            try:
                with open(self.path, "r", encoding="utf-8") as file:
                    self.plainTextEdit.setPlainText(file.read())
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
                    file.write(self.plainTextEdit_2.toPlainText())
                    self.__success_icon("Сообщение", "Текст записан в файл")
            except Exception as e:
                self.__warning_icon("Ошибка", f"Детали ошибки: {e}")
        else:
            self.__warning_icon("Предупреждение", "Вы не выбрали файл")


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    print(type(MainWindow))
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())