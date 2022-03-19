# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'calc1.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets
import sys
from stylesheet import *


class DraggableWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.mainWindow = QtWidgets.QMainWindow(self)
        self.center()
        self.oldPos = self.pos()

    def center(self):
        frame = self.frameGeometry()
        point = QtWidgets.QDesktopWidget().geometry().center()
        frame.moveCenter(point)
        self.move(frame.topLeft())

    def mousePressEvent(self, event):
        self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
            if int(event.pos().x() in range(0, 400) and int(event.pos().y() in range(0, 80))):
                delta = QtCore.QPoint(event.globalPos() - self.oldPos)
                self.move(self.x() + delta.x(), self.y() + delta.y())
                self.oldPos = event.globalPos()
            else:
                event.ignore()

class Ui_Calculator(object):
    def setupUi(self, Calculator):
        self.calculation_string = "0"
        Calculator.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Calculator.setObjectName("Calculator")
        Calculator.resize(400, 700)
        Calculator.setMinimumSize(QtCore.QSize(400, 700))
        Calculator.setMaximumSize(QtCore.QSize(400, 700))
        Calculator.setStyleSheet(css_calculator)
        self.more_less_button = QtWidgets.QPushButton(Calculator)
        self.more_less_button.setGeometry(QtCore.QRect(50, 610, 60, 60))
        self.more_less_button.setStyleSheet(css_operational_button)
        self.more_less_button.setObjectName("more_less_button")
        self.more_less_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero_button = QtWidgets.QPushButton(Calculator)
        self.zero_button.setGeometry(QtCore.QRect(130, 610, 60, 60))
        self.zero_button.setStyleSheet(css_numbers_button)
        self.zero_button.setObjectName("zero_button")
        self.zero_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.zero_button.clicked.connect(self.zero_button_clicked)
        self.dot_button = QtWidgets.QPushButton(Calculator)
        self.dot_button.setGeometry(QtCore.QRect(210, 610, 60, 60))
        self.dot_button.setStyleSheet(css_operational_button)
        self.dot_button.setObjectName("dot_button")
        self.dot_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.equals_button = QtWidgets.QPushButton(Calculator)
        self.equals_button.setGeometry(QtCore.QRect(290, 610, 60, 60))
        self.equals_button.setStyleSheet(css_operational_button)
        self.equals_button.setObjectName("equals_button")
        self.equals_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_button = QtWidgets.QPushButton(Calculator)
        self.plus_button.setGeometry(QtCore.QRect(290, 530, 60, 60))
        self.plus_button.setStyleSheet(css_operational_button)
        self.plus_button.setObjectName("plus_button")
        self.plus_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.plus_button.clicked.connect(self.plus_button_clicked)
        self.subtract_button = QtWidgets.QPushButton(Calculator)
        self.subtract_button.setGeometry(QtCore.QRect(290, 450, 60, 60))
        self.subtract_button.setStyleSheet(css_operational_button)
        self.subtract_button.setObjectName("subtract_button")
        self.subtract_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.subtract_button.clicked.connect(self.subtract_button_clicked)
        self.multiply_button = QtWidgets.QPushButton(Calculator)
        self.multiply_button.setGeometry(QtCore.QRect(290, 370, 60, 60))
        self.multiply_button.setStyleSheet(css_operational_button)
        self.multiply_button.setObjectName("multiply_button")
        self.multiply_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.multiply_button.clicked.connect(self.multiply_button_clicked)
        self.division_button = QtWidgets.QPushButton(Calculator)
        self.division_button.setGeometry(QtCore.QRect(290, 290, 60, 60))
        self.division_button.setStyleSheet(css_operational_button)
        self.division_button.setObjectName("division_button")
        self.division_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.division_button.clicked.connect(self.division_button_clicked)
        self.backspace_button = QtWidgets.QPushButton(Calculator)
        self.backspace_button.setGeometry(QtCore.QRect(290, 210, 60, 60))
        self.backspace_button.setStyleSheet(css_operational_button)
        self.backspace_button.setObjectName("backspace_button")
        self.backspace_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.c_button = QtWidgets.QPushButton(Calculator)
        self.c_button.setGeometry(QtCore.QRect(210, 210, 60, 60))
        self.c_button.setStyleSheet(css_operational_button)
        self.c_button.setObjectName("c_button")
        self.c_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.ce_button = QtWidgets.QPushButton(Calculator)
        self.ce_button.setGeometry(QtCore.QRect(130, 210, 60, 60))
        self.ce_button.setStyleSheet(css_operational_button)
        self.ce_button.setObjectName("ce_button")
        self.ce_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.percentage_button = QtWidgets.QPushButton(Calculator)
        self.percentage_button.setGeometry(QtCore.QRect(50, 210, 60, 60))
        self.percentage_button.setStyleSheet(css_operational_button)
        self.percentage_button.setObjectName("percentage_button")
        self.percentage_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.divide_by_x_button = QtWidgets.QPushButton(Calculator)
        self.divide_by_x_button.setGeometry(QtCore.QRect(50, 290, 60, 60))
        self.divide_by_x_button.setStyleSheet(css_operational_button)
        self.divide_by_x_button.setObjectName("divide_by_x_button")
        self.divide_by_x_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square_multiply_button = QtWidgets.QPushButton(Calculator)
        self.square_multiply_button.setGeometry(QtCore.QRect(130, 290, 60, 60))
        self.square_multiply_button.setStyleSheet(css_operational_button)
        self.square_multiply_button.setObjectName("square_multiply_button")
        self.square_multiply_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.square_root_button = QtWidgets.QPushButton(Calculator)
        self.square_root_button.setGeometry(QtCore.QRect(210, 290, 60, 60))
        self.square_root_button.setStyleSheet(css_operational_button)
        self.square_root_button.setObjectName("square_root_button")
        self.square_root_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.one_button = QtWidgets.QPushButton(Calculator)
        self.one_button.setGeometry(QtCore.QRect(50, 530, 60, 60))
        self.one_button.setStyleSheet(css_numbers_button)
        self.one_button.setObjectName("one_button")
        self.one_button.clicked.connect(self.one_button_clicked)
        self.one_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two_button = QtWidgets.QPushButton(Calculator)
        self.two_button.setGeometry(QtCore.QRect(130, 530, 60, 60))
        self.two_button.setStyleSheet(css_numbers_button)
        self.two_button.setObjectName("two_button")
        self.two_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.two_button.clicked.connect(self.two_button_clicked)
        self.three_button = QtWidgets.QPushButton(Calculator)
        self.three_button.setGeometry(QtCore.QRect(210, 530, 60, 60))
        self.three_button.setStyleSheet(css_numbers_button)
        self.three_button.setObjectName("three_button")
        self.three_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.three_button.clicked.connect(self.three_button_clicked)
        self.four_button = QtWidgets.QPushButton(Calculator)
        self.four_button.setGeometry(QtCore.QRect(50, 450, 60, 60))
        self.four_button.setStyleSheet(css_numbers_button)
        self.four_button.setObjectName("four_button")
        self.four_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.four_button.clicked.connect(self.four_button_clicked)
        self.five_button = QtWidgets.QPushButton(Calculator)
        self.five_button.setGeometry(QtCore.QRect(130, 450, 60, 60))
        self.five_button.setStyleSheet(css_numbers_button)
        self.five_button.setObjectName("five_button")
        self.five_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.five_button.clicked.connect(self.five_button_clicked)
        self.six_button = QtWidgets.QPushButton(Calculator)
        self.six_button.setGeometry(QtCore.QRect(210, 450, 60, 60))
        self.six_button.setStyleSheet(css_numbers_button)
        self.six_button.setObjectName("six_button")
        self.six_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.six_button.clicked.connect(self.six_button_clicked)
        self.seven_button = QtWidgets.QPushButton(Calculator)
        self.seven_button.setGeometry(QtCore.QRect(50, 370, 60, 60))
        self.seven_button.setStyleSheet(css_numbers_button)
        self.seven_button.setObjectName("seven_button")
        self.seven_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.seven_button.clicked.connect(self.seven_button_clicked)
        self.eight_button = QtWidgets.QPushButton(Calculator)
        self.eight_button.setGeometry(QtCore.QRect(130, 370, 60, 60))
        self.eight_button.setStyleSheet(css_numbers_button)
        self.eight_button.setObjectName("eight_button")
        self.eight_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.eight_button.clicked.connect(self.eight_button_clicked)
        self.nine_button = QtWidgets.QPushButton(Calculator)
        self.nine_button.setGeometry(QtCore.QRect(210, 370, 60, 60))
        self.nine_button.setStyleSheet(css_numbers_button)
        self.nine_button.setObjectName("nine_button")
        self.nine_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nine_button.clicked.connect(self.nine_button_clicked)
        self.equals_button.clicked.connect(self.equal_sign_clicked)
        self.ce_button.clicked.connect(self.ce_button_clicked)
        self.calculation_board = QtWidgets.QLabel(Calculator)
        self.calculation_board.setGeometry(QtCore.QRect(50, 50, 300, 130))
        self.calculation_board.setMinimumSize(QtCore.QSize(300, 130))
        self.calculation_board.setMaximumSize(QtCore.QSize(300, 130))
        self.calculation_board.setStyleSheet(css_calculation_board)
        self.calculation_board.setText(self.calculation_string)
        self.calculation_board.setObjectName("calculation_board")
        self.minimize_button = QtWidgets.QPushButton(Calculator)
        self.minimize_button.setGeometry(QtCore.QRect(320, 0, 40, 5))
        self.minimize_button.setMinimumSize(QtCore.QSize(40, 5))
        self.minimize_button.setMaximumSize(QtCore.QSize(40, 5))
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.minimize_button.setFont(font)
        self.minimize_button.setStyleSheet(css_minimize_button)
        self.minimize_button.setText("")
        self.minimize_button.setObjectName("minimize_button")
        self.close_button = QtWidgets.QPushButton(Calculator)
        self.close_button.setGeometry(QtCore.QRect(360, 0, 40, 5))
        self.close_button.setMinimumSize(QtCore.QSize(40, 5))
        self.close_button.setMaximumSize(QtCore.QSize(40, 5))
        self.close_button.clicked.connect(self.close_app)
        self.minimize_button.clicked.connect(self.minimize_app)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.close_button.setFont(font)
        self.close_button.setStyleSheet(css_close_button)
        self.close_button.setText("")
        self.close_button.setObjectName("close_button")

        self.retranslateUi(Calculator)
        QtCore.QMetaObject.connectSlotsByName(Calculator)

    def retranslateUi(self, Calculator):
        _translate = QtCore.QCoreApplication.translate
        Calculator.setWindowTitle(_translate("Calculator", "Form"))
        self.more_less_button.setText(_translate("Calculator", "+/-"))
        self.zero_button.setText(_translate("Calculator", "0"))
        self.dot_button.setText(_translate("Calculator", "."))
        self.equals_button.setText(_translate("Calculator", "="))
        self.plus_button.setText(_translate("Calculator", "+"))
        self.subtract_button.setText(_translate("Calculator", "-"))
        self.multiply_button.setText(_translate("Calculator", "x"))
        self.division_button.setText(_translate("Calculator", "/"))
        self.backspace_button.setText(_translate("Calculator", "<"))
        self.c_button.setText(_translate("Calculator", "C"))
        self.ce_button.setText(_translate("Calculator", "CE"))
        self.percentage_button.setText(_translate("Calculator", "%"))
        self.divide_by_x_button.setText(_translate("Calculator", "¹/x"))
        self.square_multiply_button.setText(_translate("Calculator", "x²"))
        self.square_root_button.setText(_translate("Calculator", "²x"))
        self.one_button.setText(_translate("Calculator", "1"))
        self.two_button.setText(_translate("Calculator", "2"))
        self.three_button.setText(_translate("Calculator", "3"))
        self.four_button.setText(_translate("Calculator", "4"))
        self.five_button.setText(_translate("Calculator", "5"))
        self.six_button.setText(_translate("Calculator", "6"))
        self.seven_button.setText(_translate("Calculator", "7"))
        self.eight_button.setText(_translate("Calculator", "8"))
        self.nine_button.setText(_translate("Calculator", "9"))

    def zero_button_clicked(self):
        self.calculation_string += "0"
        self.calculation_board.setText(self.calculation_string)

    def one_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "1"
        self.calculation_board.setText(self.calculation_string)
    
    def two_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "2"
        self.calculation_board.setText(self.calculation_string)
    
    def three_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "3"
        self.calculation_board.setText(self.calculation_string)
    
    def four_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "4"
        self.calculation_board.setText(self.calculation_string)
    
    def five_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "5"
        self.calculation_board.setText(self.calculation_string)
    
    def six_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "6"
        self.calculation_board.setText(self.calculation_string)

    def seven_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "7"
        self.calculation_board.setText(self.calculation_string)
    
    def eight_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "8"
        self.calculation_board.setText(self.calculation_string)
    
    def nine_button_clicked(self):
        if self.calculation_string[0] == "0":
            self.calculation_string = ""
        self.calculation_string += "9"
        self.calculation_board.setText(self.calculation_string)
    
    def plus_button_clicked(self):
        if len(self.calculation_string) > 1 and int(self.calculation_string[-1]):
            self.calculation_string += "+"
            self.calculation_board.setText(self.calculation_string)

    def subtract_button_clicked(self):
        if len(self.calculation_string) > 1 and int(self.calculation_string[-1]):
            self.calculation_string += "-"
            self.calculation_board.setText(self.calculation_string)

    def multiply_button_clicked(self):
        if len(self.calculation_string) > 1 and int(self.calculation_string[-1]):
            self.calculation_string += "*"
            self.calculation_board.setText(self.calculation_string)
    
    def division_button_clicked(self):
        if len(self.calculation_string) > 1 and int(self.calculation_string[-1]):
            self.calculation_string += "/"
            self.calculation_board.setText(self.calculation_string)
    
    def equal_sign_clicked(self):
        calc = str(eval(self.calculation_string))
        self.calculation_string = calc
        self.calculation_board.setText(self.calculation_string)

    def ce_button_clicked(self):
        self.calculation_string = "0"
        self.calculation_board.setText("0")
    
    def close_app(self):
        sys.exit()
    
    def minimize_app(self):
        MainWindow.showMinimized()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyle('Fusion')
    MainWindow = DraggableWindow()
    ui = Ui_Calculator()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
