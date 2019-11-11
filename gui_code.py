from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 860)
        MainWindow.setStyleSheet("background-color: rgb(246, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(760, 50, 111, 61))
        self.browse.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.browse.setObjectName("browse")
        self.path = QtWidgets.QTextEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(50, 50, 691, 61))
        self.path.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 255, 255);")
        self.path.setObjectName("path")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(890, 50, 93, 61))
        self.pushButton.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.pushButton.setObjectName("pushButton")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(50, 150, 931, 671))
        self.tableView.setObjectName("tableView")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(60, 320, 591, 491))
        self.listView.setStyleSheet("background-color: rgb(246, 247,255);")
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(670, 320, 301, 491))
        self.listView_2.setStyleSheet("background-color: rgb(246, 247,255);")
        self.listView_2.setObjectName("listView_2")
        self.gen_info = QtWidgets.QListView(self.centralwidget)
        self.gen_info.setGeometry(QtCore.QRect(60, 160, 911, 151))
        self.gen_info.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(246, 247,255);")
        self.gen_info.setObjectName("gen_info")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 330, 571, 51))
        self.label.setStyleSheet("background-color: rgb(227,227,255);\n"
"font: 75 16pt \"Adobe Caslon Pro\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(680, 330, 281, 41))
        self.label_2.setStyleSheet("background-color: rgb(227, 227, 255);\n"
"font: 75 16pt \"Adobe Caslon Pro\";")
        self.label_2.setObjectName("label_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.browse.setText(_translate("MainWindow", "Browse"))
        self.pushButton.setText(_translate("MainWindow", "GO"))
        self.label.setText(_translate("MainWindow", "Extensions"))
        self.label_2.setText(_translate("MainWindow", "File Count"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

