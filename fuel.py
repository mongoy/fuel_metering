# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fuel.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.btn_report_M = QtWidgets.QPushButton(self.centralwidget)
        self.btn_report_M.setGeometry(QtCore.QRect(680, 290, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_report_M.setFont(font)
        self.btn_report_M.setObjectName("btn_report_M")
        self.lbl_1 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_1.setGeometry(QtCore.QRect(10, 6, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_1.setFont(font)
        self.lbl_1.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_1.setObjectName("lbl_1")
        self.lbl_6 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_6.setGeometry(QtCore.QRect(10, 180, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_6.setFont(font)
        self.lbl_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_6.setObjectName("lbl_6")
        self.lbl_2 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_2.setGeometry(QtCore.QRect(20, 40, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_2.setFont(font)
        self.lbl_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_2.setObjectName("lbl_2")
        self.lbl_3 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_3.setGeometry(QtCore.QRect(20, 76, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_3.setFont(font)
        self.lbl_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_3.setObjectName("lbl_3")
        self.lbl_4 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_4.setGeometry(QtCore.QRect(20, 110, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_4.setFont(font)
        self.lbl_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_4.setObjectName("lbl_4")
        self.lbl_5 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_5.setGeometry(QtCore.QRect(20, 141, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_5.setFont(font)
        self.lbl_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_5.setObjectName("lbl_5")
        self.calendar = QtWidgets.QCalendarWidget(self.centralwidget)
        self.calendar.setGeometry(QtCore.QRect(680, 0, 312, 183))
        self.calendar.setObjectName("calendar")
        self.cBox_drive = QtWidgets.QComboBox(self.centralwidget)
        self.cBox_drive.setGeometry(QtCore.QRect(680, 230, 301, 22))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.cBox_drive.setFont(font)
        self.cBox_drive.setEditable(True)
        self.cBox_drive.setObjectName("cBox_drive")
        self.lbl_8 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_8.setEnabled(True)
        self.lbl_8.setGeometry(QtCore.QRect(20, 250, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_8.setFont(font)
        self.lbl_8.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_8.setObjectName("lbl_8")
        self.lbl_13 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_13.setGeometry(QtCore.QRect(680, 200, 221, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_13.setFont(font)
        self.lbl_13.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_13.setObjectName("lbl_13")
        self.lbl_9 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_9.setEnabled(True)
        self.lbl_9.setGeometry(QtCore.QRect(30, 290, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_9.setFont(font)
        self.lbl_9.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_9.setObjectName("lbl_9")
        self.lbl_10 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_10.setEnabled(True)
        self.lbl_10.setGeometry(QtCore.QRect(20, 330, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_10.setFont(font)
        self.lbl_10.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_10.setObjectName("lbl_10")
        self.lbl_11 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_11.setEnabled(True)
        self.lbl_11.setGeometry(QtCore.QRect(30, 370, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_11.setFont(font)
        self.lbl_11.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_11.setObjectName("lbl_11")
        self.lbl_12 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_12.setEnabled(True)
        self.lbl_12.setGeometry(QtCore.QRect(20, 410, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_12.setFont(font)
        self.lbl_12.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_12.setObjectName("lbl_12")
        self.lbl_7 = QtWidgets.QLabel(self.centralwidget)
        self.lbl_7.setEnabled(True)
        self.lbl_7.setGeometry(QtCore.QRect(20, 213, 500, 30))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.lbl_7.setFont(font)
        self.lbl_7.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(0, 0, 255);")
        self.lbl_7.setObjectName("lbl_7")
        self.btn_report_D = QtWidgets.QPushButton(self.centralwidget)
        self.btn_report_D.setGeometry(QtCore.QRect(680, 340, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btn_report_D.setFont(font)
        self.btn_report_D.setObjectName("btn_report_D")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1000, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "???????? ??????"))
        self.btn_report_M.setText(_translate("MainWindow", "?????????? ???? ??????????"))
        self.lbl_1.setText(_translate("MainWindow", "???????? ????????????:"))
        self.lbl_6.setText(_translate("MainWindow", "???????????? (????):"))
        self.lbl_2.setText(_translate("MainWindow", "?????????????? ???? ???????????? ???????????? (??):"))
        self.lbl_3.setText(_translate("MainWindow", "???????????????? (??):"))
        self.lbl_4.setText(_translate("MainWindow", "???????????? (??):"))
        self.lbl_5.setText(_translate("MainWindow", "?????????????? ???? ?????????? ???????????? ???????????? (??):"))
        self.cBox_drive.setCurrentText(_translate("MainWindow", "???????????????? ..."))
        self.lbl_8.setText(_translate("MainWindow", "???? ???????????? (????):"))
        self.lbl_13.setText(_translate("MainWindow", "????????????????????:"))
        self.lbl_9.setText(_translate("MainWindow", " -  ?? ?????????????????????????? (????):"))
        self.lbl_10.setText(_translate("MainWindow", "???? ???????????? (????):"))
        self.lbl_11.setText(_translate("MainWindow", " -  ?? ?????????????????????????? (????):"))
        self.lbl_12.setText(_translate("MainWindow", "????????????????:"))
        self.lbl_7.setText(_translate("MainWindow", "??????????????????:"))
        self.btn_report_D.setText(_translate("MainWindow", "?????????? ???? ????????"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
