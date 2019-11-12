from PyQt5 import QtCore, QtGui, QtWidgets
from moviepy.editor import VideoFileClip
import os
import mutagen

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1038, 864)
        MainWindow.setStyleSheet("background-color: rgb(246, 247, 247);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.browse = QtWidgets.QPushButton(self.centralwidget)
        self.browse.setGeometry(QtCore.QRect(760, 50, 111, 61))
        self.browse.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.browse.setObjectName("browse")
        self.go = QtWidgets.QPushButton(self.centralwidget)
        self.go.setGeometry(QtCore.QRect(890, 50, 93, 61))
        self.go.setStyleSheet("font: 18pt \"Times New Roman\";")
        self.go.setObjectName("go")
        self.path = QtWidgets.QLineEdit(self.centralwidget)
        self.path.setGeometry(QtCore.QRect(40, 50, 701, 61))
        self.path.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"font: 12pt \"MS Shell Dlg 2\";")
        self.path.setObjectName("path")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setGeometry(QtCore.QRect(40, 140, 951, 681))
        self.main_frame.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gen_info = QtWidgets.QListWidget(self.main_frame)
        self.gen_info.setGeometry(QtCore.QRect(0, 70, 481, 601))
        self.gen_info.setStyleSheet("background-color: rgb(246, 247,255);\n"
"font: 75 14pt \"MS Sans Serif\";")
        self.gen_info.setObjectName("gen_info")
        self.extension_listwidget = QtWidgets.QListWidget(self.main_frame)
        self.extension_listwidget.setGeometry(QtCore.QRect(500, 70, 451, 601))
        self.extension_listwidget.setStyleSheet("background-color: rgb(246, 247,255);\n"
"font: 75 14pt \"MS Sans Serif\";")
        self.extension_listwidget.setObjectName("extension_listwidget")
        self.label = QtWidgets.QLabel(self.main_frame)
        self.label.setGeometry(QtCore.QRect(500, 10, 321, 51))
        self.label.setStyleSheet("background-color: rgb(227, 227, 255);\n"
"font: 75 16pt \"Adobe Caslon Pro Bold\";\n"
"")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.main_frame)
        self.label_2.setGeometry(QtCore.QRect(820, 10, 131, 51))
        self.label_2.setStyleSheet("background-color: rgb(227, 227, 255);\n"
"font: 75 16pt \"Adobe Caslon Pro Bold\";\n"
"")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.main_frame)
        self.label_3.setGeometry(QtCore.QRect(0, 10, 481, 51))
        self.label_3.setStyleSheet("background-color: rgb(227, 227, 255);\n"
"font: 75 16pt \"Adobe Caslon Pro Bold\";\n"
"\n"
"")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.main_frame)
        self.label_4.setGeometry(QtCore.QRect(330, 10, 91, 51))
        self.label_4.setStyleSheet("background-color: rgb(227, 227, 255);\n"
"font: 75 16pt \"Adobe Caslon Pro Bold\";\n"
"")
        self.label_4.setObjectName("label_4")
        self.gen_info.raise_()
        self.extension_listwidget.raise_()
        self.label.raise_()
        self.label.raise_()
        self.label_2.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.main_frame.raise_()
        self.browse.raise_()
        self.go.raise_()
        self.path.raise_()
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
        self.go.setText(_translate("MainWindow", "Go"))
        self.label.setText(_translate("MainWindow", "Extensions"))
        self.label_2.setText(_translate("MainWindow", "File Count"))
        self.label_3.setText(_translate("MainWindow", "General Information"))
        self.label_4.setText(_translate("MainWindow", "Total"))

        self.go.clicked.connect(self.write_path)
        self.browse.clicked.connect(self.browse_path)

    def write_path(self):

        path = str(self.path.text())
        if path == "":
            a = os.walk("blank_folder")
        else:
            a = os.walk(path)
        self.work(a)

    def browse_path(self):
        try:
            result = QtWidgets.QFileDialog.getOpenFileName()
            a = os.walk(result[0])
            self.path.setText(result[0])
            self.work(a)



        except BaseException as err:
            item = QtWidgets.QListWidgetItem()
            self.gen_info.addItem(item)
            item.setText(err)

    def work(self, a):
        try:
            self.gen_info.clear()
            self.extension_listwidget.clear()

            extension = []
            file_list = []
            file_count = 0
            folder_count = 0
            count_mp4 = 0
            count_mp3 = 0
            length_mp4 = 0
            length_mp3 = 0

            # Finding extension dynamically
            for root, folder, files in a:
                folder_count += len(folder)
                file_count += len(files)
                for file in files:
                    for i in range(len(file) - 1, 0, -1):
                        if file[i] == ".":
                            file_list.append(file[i + 1:])
                            if file[i + 1:] not in extension:
                                extension.append(file[i + 1:])
                                break
                            else:
                                break

                    if file.endswith(("mp4", "avi", "flv", "wmv", "mov", "mkv")):
                        video = VideoFileClip(root + "/" + file)
                        # print(file, end=" ")
                        # print("{:.2f}".format(video.duration / 60))
                        count_mp4 += 1
                        length_mp4 += video.duration
                        video.reader.close()
                        video.audio.reader.close_proc()
                        # del video.reader
                    elif file.endswith("mp3"):
                        song = mutagen.File(root + "/" + file)
                        # print(file, end=" ")
                        # print("{:.2f}".format(song.info.length / 60))
                        count_mp3 += 1
                        length_mp3 += song.info.length
            gen_data = "Folders\t\t\t {}\nFiles\t\t\t\t {}\nAudio Files\t\t\t {}\n" \
                       "Video Files\t\t\t {}\nAudio Length\t\t\t {}:{}:{}\n" \
                       "Video Length\t\t\t {}:{}:{}\n".format(folder_count, file_count,
                        count_mp3, count_mp4, int(length_mp3 // 3600), int((length_mp3 % 3600)//60), int((length_mp3 % 3600)
                        % 60), int(length_mp4 // 3600), int((length_mp4 % 3600)//60), int((length_mp4 % 3600) % 60))

            item = QtWidgets.QListWidgetItem()
            self.gen_info.addItem(item)
            item.setText(gen_data)

            for i in range(len(extension)):
                item = QtWidgets.QListWidgetItem()
                self.extension_listwidget.addItem(item)
                item.setText("{}\t\t\t\t{}".format(extension[i], file_list.count(extension[i])))


        except BaseException as err:
            item = QtWidgets.QListWidgetItem()
            self.gen_info.addItem(item)
            item.setText(err)
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
