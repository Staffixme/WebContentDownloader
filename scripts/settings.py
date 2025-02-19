# Form implementation generated from reading ui file 'settings.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from path_to_files import PATH


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(651, 461)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{PATH}/WebContent icon 2.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        Form.setWindowIcon(icon)
        Form.setStyleSheet("#titleBar{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-top-right-radius: 12px;\n"
"border-top-left-radius: 12px;\n"
"border-left: 1px solid #C1C1C1;\n"
"border-right: 1px solid #C1C1C1;\n"
"border-top: 1px solid #C1C1C1\n"
"}\n"
"\n"
"#bottomBar{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-bottom-right-radius: 12px;\n"
"border-bottom-left-radius: 12px;\n"
"border-left: 1px solid #C1C1C1;\n"
"border-right: 1px solid #C1C1C1;\n"
"border-bottom: 1px solid #C1C1C1\n"
"}\n"
"\n"
"#background{\n"
"background-color: white;\n"
"border-left: 1px solid #C1C1C1;\n"
"border-right: 1px solid #C1C1C1;\n"
"}")
        self.titleBar = QtWidgets.QFrame(parent=Form)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 651, 55))
        self.titleBar.setStyleSheet(".QToolButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.titleBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titleBar.setObjectName("titleBar")
        self.formTitle = QtWidgets.QLabel(parent=self.titleBar)
        self.formTitle.setGeometry(QtCore.QRect(270, 18, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(13)
        self.formTitle.setFont(font)
        self.formTitle.setStyleSheet("color: #264653")
        self.formTitle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formTitle.setObjectName("formTitle")
        self.CloseButton = QtWidgets.QToolButton(parent=self.titleBar)
        self.CloseButton.setGeometry(QtCore.QRect(608, 12, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
        self.CloseButton.setStyleSheet(".QToolButton{\n"
"    border-radius: 7px;\n"
"    border: 1px solid #C1C1C1;\n"
"}\n"
".QToolButton:hover{\n"
"    background-color: rgb(255, 25, 28);\n"
"}")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(f"{PATH}/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon.addPixmap(QtGui.QPixmap(f"{PATH}/close-white.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon.addPixmap(QtGui.QPixmap(f"{PATH}/close-white.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.CloseButton.setIcon(icon)
        self.CloseButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.CloseButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.CloseButton.setObjectName("CloseButton")
        self.HideButton = QtWidgets.QToolButton(parent=self.titleBar)
        self.HideButton.setGeometry(QtCore.QRect(570, 12, 32, 32))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.HideButton.sizePolicy().hasHeightForWidth())
        self.HideButton.setSizePolicy(sizePolicy)
        self.HideButton.setStyleSheet(".QToolButton{\n"
"    border-radius: 7px;\n"
"    border: 1px solid #C1C1C1;\n"
"}\n"
".QToolButton:hover{\n"
"    background-color: rgba(0, 0, 0, 24);\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{PATH}/hide.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HideButton.setIcon(icon1)
        self.HideButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.HideButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.HideButton.setObjectName("HideButton")
        self.bottomBar = QtWidgets.QFrame(parent=Form)
        self.bottomBar.setGeometry(QtCore.QRect(0, 395, 651, 66))
        self.bottomBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.applyButton = QtWidgets.QPushButton(parent=self.bottomBar)
        self.applyButton.setGeometry(QtCore.QRect(10, 11, 631, 43))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.applyButton.setFont(font)
        self.applyButton.setStyleSheet("QPushButton{\n"
"    background-color: #264653;\n"
"    border-radius: 7;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #1A333D;\n"
"}")
        self.applyButton.setObjectName("applyButton")
        self.background = QtWidgets.QFrame(parent=Form)
        self.background.setGeometry(QtCore.QRect(0, 54, 651, 341))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.background.sizePolicy().hasHeightForWidth())
        self.background.setSizePolicy(sizePolicy)
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 651, 235))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(10)
        self.verticalLayout.setObjectName("verticalLayout")
        self.closingContainer = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.closingContainer.sizePolicy().hasHeightForWidth())
        self.closingContainer.setSizePolicy(sizePolicy)
        self.closingContainer.setMinimumSize(QtCore.QSize(0, 65))
        self.closingContainer.setStyleSheet(".QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-radius: 5px;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QComboBox{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QComboBox::drop-down{\n"
"border: 0px\n"
"}\n"
"\n"
"QComboBox::down-arrow{\n"
f"image: url({PATH}/dropdown_arrow.png);\n"
"height: 24px;\n"
"}\n"
"\n"
"QComboBox QListView{\n"
"border: 1px solid #C1C1C1;\n"
"    background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"}\n"
"\n"
"QComboBox QListView:Item:hover{\n"
"background-color: rgb(14, 149, 148);\n"
"}\n"
"\n"
"QComboBox QListView:Item:selected{\n"
"background-color: rgb(14, 149, 148);\n"
"}")
        self.closingContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.closingContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.closingContainer.setObjectName("closingContainer")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.closingContainer)
        self.horizontalLayout_2.setContentsMargins(24, -1, 12, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(parent=self.closingContainer)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.trayComboBox = QtWidgets.QComboBox(parent=self.closingContainer)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.trayComboBox.setFont(font)
        self.trayComboBox.setEditable(False)
        self.trayComboBox.setFrame(True)
        self.trayComboBox.setObjectName("trayComboBox")
        self.horizontalLayout_2.addWidget(self.trayComboBox)
        self.horizontalLayout_2.setStretch(0, 3)
        self.horizontalLayout_2.setStretch(1, 5)
        self.horizontalLayout_2.setStretch(2, 9)
        self.verticalLayout.addWidget(self.closingContainer)
        self.DirectoryContainer = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DirectoryContainer.sizePolicy().hasHeightForWidth())
        self.DirectoryContainer.setSizePolicy(sizePolicy)
        self.DirectoryContainer.setMinimumSize(QtCore.QSize(0, 65))
        self.DirectoryContainer.setStyleSheet(".QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-radius: 5px;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QPushButton{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 0, 25);\n"
"}\n"
"\n"
"QLineEdit{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"border: 1px solid #C1C1C1\n"
"}")
        self.DirectoryContainer.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.DirectoryContainer.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.DirectoryContainer.setObjectName("DirectoryContainer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.DirectoryContainer)
        self.horizontalLayout_3.setContentsMargins(24, -1, 12, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(parent=self.DirectoryContainer)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.savePath = QtWidgets.QLineEdit(parent=self.DirectoryContainer)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.savePath.setFont(font)
        self.savePath.setReadOnly(True)
        self.savePath.setObjectName("savePath")
        self.horizontalLayout_3.addWidget(self.savePath)
        self.editButton = QtWidgets.QPushButton(parent=self.DirectoryContainer)
        self.editButton.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(f"{PATH}/edit.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.editButton.setIcon(icon2)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout_3.addWidget(self.editButton)
        self.horizontalLayout_3.setStretch(0, 4)
        self.horizontalLayout_3.setStretch(1, 3)
        self.horizontalLayout_3.setStretch(2, 6)
        self.horizontalLayout_3.setStretch(3, 1)
        self.verticalLayout.addWidget(self.DirectoryContainer)
        self.DirectoryContainer_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DirectoryContainer_2.sizePolicy().hasHeightForWidth())
        self.DirectoryContainer_2.setSizePolicy(sizePolicy)
        self.DirectoryContainer_2.setMinimumSize(QtCore.QSize(0, 65))
        self.DirectoryContainer_2.setStyleSheet(".QFrame{\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-radius: 5px;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QPushButton{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"border: 1px solid #C1C1C1\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: rgb(0, 0, 0, 25);\n"
"}\n"
"\n"
"QLineEdit{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: white;\n"
"border: 1px solid #C1C1C1\n"
"}")
        self.DirectoryContainer_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.DirectoryContainer_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.DirectoryContainer_2.setObjectName("DirectoryContainer_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.DirectoryContainer_2)
        self.horizontalLayout_4.setContentsMargins(24, -1, 12, -1)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(parent=self.DirectoryContainer_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.FFmpegPath = QtWidgets.QLineEdit(parent=self.DirectoryContainer_2)
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        self.FFmpegPath.setFont(font)
        self.FFmpegPath.setReadOnly(True)
        self.FFmpegPath.setObjectName("FFmpegPath")
        self.horizontalLayout_4.addWidget(self.FFmpegPath)
        self.editButton2 = QtWidgets.QPushButton(parent=self.DirectoryContainer_2)
        self.editButton2.setText("")
        self.editButton2.setIcon(icon2)
        self.editButton2.setObjectName("editButton2")
        self.horizontalLayout_4.addWidget(self.editButton2)
        self.horizontalLayout_4.setStretch(0, 4)
        self.horizontalLayout_4.setStretch(1, 3)
        self.horizontalLayout_4.setStretch(2, 6)
        self.horizontalLayout_4.setStretch(3, 1)
        self.verticalLayout.addWidget(self.DirectoryContainer_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Настройки"))
        self.formTitle.setText(_translate("Form", "Настройки"))
        self.CloseButton.setToolTip(_translate("Form", "Закрыть"))
        self.CloseButton.setText(_translate("Form", "..."))
        self.HideButton.setToolTip(_translate("Form", "Свернуть"))
        self.HideButton.setText(_translate("Form", "..."))
        self.applyButton.setText(_translate("Form", "Применить"))
        self.label_2.setText(_translate("Form", "При закрытии программы:"))
        self.label_3.setText(_translate("Form", "Сохранять файлы в папку:"))
        self.label_4.setText(_translate("Form", "Путь к FFmpeg:"))
