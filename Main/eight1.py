
import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def openform1(self):
        from four2 import Ui_Formsss
        self.Form = QtWidgets.QWidget()
        self.ui = Ui_Formsss()
        self.ui.setupUi(self.Form)
        self.Form.show()
    def meetfunction(self):
        name = self.lineEdit.text()
        time = self.comboBox.currentText()
        date = self.comboBox_2.currentText()
        month = self.comboBox_4.currentText()
        year = self.comboBox_3.currentText()
        bank = self.comboBox_5.currentText()

        if len(name) == 0:
            self.label_5.setText("please fill all the required field ")


        else:
            conn = sqlite3.connect('meeting.db')
            cur = conn.cursor()
            user_info = [name, time, date, month, year, bank]
            cur.execute('INSERT INTO met(name,time,date,month,year,bank) VALUES (?,?,?,?,?,?)',user_info)

            conn.commit()
            conn.close()
            self.label_5.setText("your meeting will fixed")
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(521, 501)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(-1, -1, 541, 501))
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(-20, 0, 571, 501))
        self.label.setStyleSheet("border-image: url(C:/Users/F I ENTERPRISES/Documents/ise project/ise project 2k22/login.jpeg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(90, 10, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(79, 90, 102);")
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(self.widget)
        self.comboBox.setGeometry(QtCore.QRect(170, 100, 141, 22))
        self.comboBox.setStyleSheet("color:rgb(0, 0, 0);\n"
"background-color: rgb(162, 162, 162);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.widget)
        self.pushButton_3.setGeometry(QtCore.QRect(150, 340, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.meetfunction)

        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(50, 50, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(79, 90, 102);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(50, 390, 421, 81))
        font = QtGui.QFont()
        font.setPointSize(17)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgb(0, 0, 0)")
        self.label_4.setObjectName("label_4")
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setGeometry(QtCore.QRect(10, 10, 61, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(100, 190, 301, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(79, 90, 102);")
        self.label_6.setObjectName("label_6")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget)
        self.comboBox_3.setGeometry(QtCore.QRect(310, 150, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_3.setFont(font)
        self.comboBox_3.setStyleSheet("QLineEdit {\n"
" border: 2.5px solid gray;\n"
" border-radius: 7px;\n"
" background-color: rgb(214, 214, 214);\n"
"    \n"
"    \n"
"    color: rgb(113, 113, 113)\n"
"}")
        self.comboBox_3.setEditable(False)
        self.comboBox_3.setMaxVisibleItems(10)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(5, "")
        self.comboBox_3.addItem("")
        self.comboBox_3.setItemText(6, "")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setGeometry(QtCore.QRect(190, 150, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_4.setFont(font)
        self.comboBox_4.setStyleSheet("QLineEdit {\n"
" border: 2.5px solid gray;\n"
" border-radius: 7px;\n"
" background-color: rgb(214, 214, 214);\n"
"    \n"
"    \n"
"    color: rgb(113, 113, 113)\n"
"}")
        self.comboBox_4.setEditable(False)
        self.comboBox_4.setMaxVisibleItems(10)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(11, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(12, "")
        self.comboBox_4.addItem("")
        self.comboBox_4.setItemText(13, "")
        self.comboBox_2 = QtWidgets.QComboBox(self.widget)
        self.comboBox_2.setGeometry(QtCore.QRect(60, 150, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QLineEdit {\n"
" border: 2.5px solid gray;\n"
" border-radius: 7px;\n"
" background-color: rgb(214, 214, 214);\n"
"    \n"
"    \n"
"    color: rgb(113, 113, 113)\n"
"}")
        self.comboBox_2.setEditable(False)
        self.comboBox_2.setMaxVisibleItems(10)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(31, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(32, "")
        self.comboBox_2.addItem("")
        self.comboBox_2.setItemText(33, "")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget)
        self.comboBox_5.setGeometry(QtCore.QRect(190, 270, 101, 25))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.comboBox_5.setFont(font)
        self.comboBox_5.setStyleSheet("QLineEdit {\n"
" border: 2.5px solid gray;\n"
" border-radius: 7px;\n"
" background-color: rgb(214, 214, 214);\n"
"    \n"
"    \n"
"    color: rgb(113, 113, 113)\n"
"}")
        self.comboBox_5.setEditable(False)
        self.comboBox_5.setMaxVisibleItems(10)
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(170, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color: rgb(214, 214, 214);")
        self.lineEdit.setInputMask("")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.widget)
        self.label_5.setGeometry(QtCore.QRect(100, 299, 351, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(255, 0, 0);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        self.pushButton_4.clicked.connect(self.openform1)
        self.pushButton_4.clicked.connect(Form.close)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; color:#ffffff;\">Meeting </span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Form", "10am-11am"))
        self.comboBox.setItemText(1, _translate("Form", "12am-1pm"))
        self.comboBox.setItemText(2, _translate("Form", "3pm-4pm"))
        self.pushButton_3.setText(_translate("Form", "Submit"))
        self.label_3.setText(_translate("Form", "<html><head/><body><p align=\"center\">Select the given Meeting Time and Date</p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p align=\"center\"><span style=\" font-size:12pt;\">Note:In this meeting we will discussed</span></p><p align=\"center\"><span style=\" font-size:12pt;\">about estimate and the completion of the project!!</span></p></body></html>"))
        self.pushButton_4.setText(_translate("Form", "BACK"))
        self.label_6.setText(_translate("Form", "<html><head/><body><p align=\"center\">payment detail</p><p align=\"center\"><br/></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Form", "2023"))
        self.comboBox_3.setItemText(1, _translate("Form", "2024"))
        self.comboBox_3.setItemText(2, _translate("Form", "2025"))
        self.comboBox_3.setItemText(3, _translate("Form", "2026"))
        self.comboBox_3.setItemText(4, _translate("Form", "2027"))
        self.comboBox_4.setItemText(0, _translate("Form", "jan"))
        self.comboBox_4.setItemText(1, _translate("Form", "feb"))
        self.comboBox_4.setItemText(2, _translate("Form", "mar"))
        self.comboBox_4.setItemText(3, _translate("Form", "may"))
        self.comboBox_4.setItemText(4, _translate("Form", "jun"))
        self.comboBox_4.setItemText(5, _translate("Form", "jul"))
        self.comboBox_4.setItemText(6, _translate("Form", "aug"))
        self.comboBox_4.setItemText(7, _translate("Form", "sep"))
        self.comboBox_4.setItemText(8, _translate("Form", "oct"))
        self.comboBox_4.setItemText(9, _translate("Form", "nov"))
        self.comboBox_4.setItemText(10, _translate("Form", "dec"))
        self.comboBox_2.setItemText(0, _translate("Form", "1"))
        self.comboBox_2.setItemText(1, _translate("Form", "2"))
        self.comboBox_2.setItemText(2, _translate("Form", "3"))
        self.comboBox_2.setItemText(3, _translate("Form", "4"))
        self.comboBox_2.setItemText(4, _translate("Form", "5"))
        self.comboBox_2.setItemText(5, _translate("Form", "6"))
        self.comboBox_2.setItemText(6, _translate("Form", "7"))
        self.comboBox_2.setItemText(7, _translate("Form", "8"))
        self.comboBox_2.setItemText(8, _translate("Form", "9"))
        self.comboBox_2.setItemText(9, _translate("Form", "10"))
        self.comboBox_2.setItemText(10, _translate("Form", "11"))
        self.comboBox_2.setItemText(11, _translate("Form", "12"))
        self.comboBox_2.setItemText(12, _translate("Form", "13"))
        self.comboBox_2.setItemText(13, _translate("Form", "14"))
        self.comboBox_2.setItemText(14, _translate("Form", "15"))
        self.comboBox_2.setItemText(15, _translate("Form", "16"))
        self.comboBox_2.setItemText(16, _translate("Form", "17"))
        self.comboBox_2.setItemText(17, _translate("Form", "18"))
        self.comboBox_2.setItemText(18, _translate("Form", "19"))
        self.comboBox_2.setItemText(19, _translate("Form", "20"))
        self.comboBox_2.setItemText(20, _translate("Form", "21"))
        self.comboBox_2.setItemText(21, _translate("Form", "22"))
        self.comboBox_2.setItemText(22, _translate("Form", "23"))
        self.comboBox_2.setItemText(23, _translate("Form", "24"))
        self.comboBox_2.setItemText(24, _translate("Form", "25"))
        self.comboBox_2.setItemText(25, _translate("Form", "26"))
        self.comboBox_2.setItemText(26, _translate("Form", "27"))
        self.comboBox_2.setItemText(27, _translate("Form", "28"))
        self.comboBox_2.setItemText(28, _translate("Form", "29"))
        self.comboBox_2.setItemText(29, _translate("Form", "30"))
        self.comboBox_2.setItemText(30, _translate("Form", "31"))
        self.comboBox_5.setItemText(0, _translate("Form", "HBL"))
        self.comboBox_5.setItemText(1, _translate("Form", "MCB"))
        self.comboBox_5.setItemText(2, _translate("Form", "UBL"))
        self.comboBox_5.setItemText(3, _translate("Form", "MEZAN"))
        self.lineEdit.setToolTip(_translate("Form", "<html><head/><body><p align=\"center\"><br/></p></body></html>"))
        self.lineEdit.setPlaceholderText(_translate("Form", " Name"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
