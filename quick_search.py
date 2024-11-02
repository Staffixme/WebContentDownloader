# Form implementation generated from reading ui file 'quick_search.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(551, 41)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/downloader_icon.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setWindowOpacity(1.0)
        Form.setStyleSheet("#background{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-radius: 7px;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
".QToolButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}\n"
"\n"
".QLineEdit{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"border: none;\n"
"}\n"
"")
        self.background = QtWidgets.QFrame(parent=Form)
        self.background.setGeometry(QtCore.QRect(0, 0, 551, 41))
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.searchButton = QtWidgets.QToolButton(parent=self.background)
        self.searchButton.setGeometry(QtCore.QRect(10, 9, 24, 24))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("icons/search.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.searchButton.setIcon(icon1)
        self.searchButton.setObjectName("searchButton")
        self.closeButton = QtWidgets.QToolButton(parent=self.background)
        self.closeButton.setGeometry(QtCore.QRect(520, 9, 24, 24))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("icons/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.closeButton.setIcon(icon2)
        self.closeButton.setObjectName("closeButton")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.background)
        self.lineEdit.setGeometry(QtCore.QRect(40, 0, 471, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lineEdit.setFont(font)
        self.lineEdit.setClearButtonEnabled(False)
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.searchButton.setText(_translate("Form", "..."))
        self.closeButton.setText(_translate("Form", "..."))
        self.lineEdit.setPlaceholderText(_translate("Form", "Введите URL"))
