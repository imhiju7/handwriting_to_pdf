# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1550, 800)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 700, 749))
        self.frame.setStyleSheet("background-color: rgb(238, 238, 238);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.frame_3 = QtWidgets.QFrame(parent=self.frame)
        self.frame_3.setGeometry(QtCore.QRect(0, 0, 700, 60))
        self.frame_3.setStyleSheet("border-bottom: 1px solid rgb(255, 255, 255);\n"
"background-color: rgb(205, 255, 255);\n"
"border-right: 2px solid rgb(255, 255, 255);\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.addImage = QtWidgets.QPushButton(parent=self.frame_3)
        self.addImage.setGeometry(QtCore.QRect(0, 0, 70, 60))
        self.addImage.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./img/photo.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.addImage.setIcon(icon)
        self.addImage.setIconSize(QtCore.QSize(40, 40))
        self.addImage.setObjectName("addImage")
        self.pasteImage = QtWidgets.QPushButton(parent=self.frame_3)
        self.pasteImage.setGeometry(QtCore.QRect(70, 0, 70, 60))
        self.pasteImage.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("./img/paste.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.pasteImage.setIcon(icon1)
        self.pasteImage.setIconSize(QtCore.QSize(40, 40))
        self.pasteImage.setObjectName("pasteImage")
        self.fitImage = QtWidgets.QPushButton(parent=self.frame_3)
        self.fitImage.setGeometry(QtCore.QRect(160, 0, 70, 60))
        self.fitImage.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("./img/resize.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.fitImage.setIcon(icon2)
        self.fitImage.setIconSize(QtCore.QSize(40, 40))
        self.fitImage.setObjectName("fitImage")
        self.actualSize = QtWidgets.QPushButton(parent=self.frame_3)
        self.actualSize.setGeometry(QtCore.QRect(230, 0, 70, 60))
        self.actualSize.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("./img/reduce.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.actualSize.setIcon(icon3)
        self.actualSize.setIconSize(QtCore.QSize(40, 40))
        self.actualSize.setObjectName("actualSize")
        self.zoomOut = QtWidgets.QPushButton(parent=self.frame_3)
        self.zoomOut.setGeometry(QtCore.QRect(390, 0, 70, 60))
        self.zoomOut.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("./img/zoom-out.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.zoomOut.setIcon(icon4)
        self.zoomOut.setIconSize(QtCore.QSize(40, 40))
        self.zoomOut.setObjectName("zoomOut")
        self.zoomIn = QtWidgets.QPushButton(parent=self.frame_3)
        self.zoomIn.setGeometry(QtCore.QRect(320, 0, 70, 60))
        self.zoomIn.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("./img/zoom-in.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.zoomIn.setIcon(icon5)
        self.zoomIn.setIconSize(QtCore.QSize(40, 40))
        self.zoomIn.setObjectName("zoomIn")
        self.turnLeft = QtWidgets.QPushButton(parent=self.frame_3)
        self.turnLeft.setGeometry(QtCore.QRect(480, 0, 70, 60))
        self.turnLeft.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("./img/turn_left.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.turnLeft.setIcon(icon6)
        self.turnLeft.setIconSize(QtCore.QSize(40, 40))
        self.turnLeft.setObjectName("turnLeft")
        self.turnRight = QtWidgets.QPushButton(parent=self.frame_3)
        self.turnRight.setGeometry(QtCore.QRect(550, 0, 70, 60))
        self.turnRight.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("./img/turn-right.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.turnRight.setIcon(icon7)
        self.turnRight.setIconSize(QtCore.QSize(40, 40))
        self.turnRight.setObjectName("turnRight")
        self.widget = QtWidgets.QWidget(parent=self.frame)
        self.widget.setGeometry(QtCore.QRect(0, 60, 700, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMaximumSize(QtCore.QSize(700, 691))
        self.widget.setObjectName("widget")
        self.scrollArea = QtWidgets.QScrollArea(parent=self.widget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 700, 691))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 698, 689))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.imageLabel = QtWidgets.QLabel(parent=self.scrollAreaWidgetContents)
        self.imageLabel.setGeometry(QtCore.QRect(0, 0, 700, 691))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QtCore.QSize(1, 1))
        self.imageLabel.setMaximumSize(QtCore.QSize(700, 691))
        self.imageLabel.setText("")
        self.imageLabel.setScaledContents(False)
        self.imageLabel.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imageLabel.setObjectName("imageLabel")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.frame_2 = QtWidgets.QFrame(parent=self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(700, 0, 1000, 749))
        self.frame_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame_2.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhNone)
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.frame_4 = QtWidgets.QFrame(parent=self.frame_2)
        self.frame_4.setGeometry(QtCore.QRect(0, 0, 1000, 60))
        self.frame_4.setStyleSheet("background-color: rgb(205, 255, 255);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_4.setObjectName("frame_4")
        self.scanImage = QtWidgets.QPushButton(parent=self.frame_4)
        self.scanImage.setGeometry(QtCore.QRect(0, 0, 70, 60))
        self.scanImage.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("./img/scan.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.scanImage.setIcon(icon8)
        self.scanImage.setIconSize(QtCore.QSize(40, 40))
        self.scanImage.setObjectName("scanImage")
        self.removeText = QtWidgets.QPushButton(parent=self.frame_4)
        self.removeText.setGeometry(QtCore.QRect(90, 0, 70, 60))
        self.removeText.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("./img/eraser.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.removeText.setIcon(icon9)
        self.removeText.setIconSize(QtCore.QSize(40, 40))
        self.removeText.setObjectName("removeText")
        self.findText = QtWidgets.QPushButton(parent=self.frame_4)
        self.findText.setGeometry(QtCore.QRect(180, 0, 70, 60))
        self.findText.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("./img/text.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.findText.setIcon(icon10)
        self.findText.setIconSize(QtCore.QSize(40, 40))
        self.findText.setObjectName("findText")
        self.savePDF = QtWidgets.QPushButton(parent=self.frame_4)
        self.savePDF.setGeometry(QtCore.QRect(270, 0, 70, 60))
        self.savePDF.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("./img/pdf-document.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.savePDF.setIcon(icon11)
        self.savePDF.setIconSize(QtCore.QSize(40, 40))
        self.savePDF.setObjectName("savePDF")
        self.textArea = QtWidgets.QPlainTextEdit(parent=self.frame_2)
        self.textArea.setGeometry(QtCore.QRect(0, 60, 830, 691))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(18)
        self.textArea.setFont(font)
        self.textArea.setStyleSheet("border:1px solid rgb(0, 0, 0);")
        self.textArea.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Vietnamese, QtCore.QLocale.Country.Vietnam))
        self.textArea.setObjectName("textArea")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1550, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "ScanImage"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
