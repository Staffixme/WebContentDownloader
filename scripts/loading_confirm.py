# Form implementation generated from reading ui file 'loading_confirm.ui'
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
"}\n"
"\n"
"#preview{\n"
"border-radius: 5px\n"
"}")
        self.bottomBar = QtWidgets.QFrame(parent=Form)
        self.bottomBar.setGeometry(QtCore.QRect(0, 395, 651, 66))
        self.bottomBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.bottomBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.bottomBar.setObjectName("bottomBar")
        self.downloadButton = QtWidgets.QPushButton(parent=self.bottomBar)
        self.downloadButton.setGeometry(QtCore.QRect(493, 11, 146, 43))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.downloadButton.setFont(font)
        self.downloadButton.setStyleSheet("QPushButton{\n"
"    background-color: #264653;\n"
"    border-radius: 7;\n"
"    color: white;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #1A333D;\n"
"}")
        self.downloadButton.setObjectName("downloadButton")
        self.savePath = QtWidgets.QLabel(parent=self.bottomBar)
        self.savePath.setGeometry(QtCore.QRect(20, 11, 401, 43))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.savePath.setFont(font)
        self.savePath.setObjectName("savePath")
        self.background = QtWidgets.QFrame(parent=Form)
        self.background.setGeometry(QtCore.QRect(0, 55, 651, 341))
        self.background.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.background.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.background.setObjectName("background")
        self.preview = QtWidgets.QLabel(parent=self.background)
        self.preview.setGeometry(QtCore.QRect(35, 35, 269, 150))
        self.preview.setStyleSheet("background-color: rgb(200, 200, 200);")
        self.preview.setText("")
        self.preview.setScaledContents(True)
        self.preview.setObjectName("preview")
        self.fileName = QtWidgets.QLineEdit(parent=self.background)
        self.fileName.setGeometry(QtCore.QRect(35, 200, 269, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.fileName.setFont(font)
        self.fileName.setStyleSheet("background-color: rgba(255, 255, 255, 0);\n"
"border-radius: 5px;")
        self.fileName.setObjectName("fileName")
        self.formatText = QtWidgets.QLabel(parent=self.background)
        self.formatText.setGeometry(QtCore.QRect(35, 240, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.formatText.setFont(font)
        self.formatText.setStyleSheet("color: #5D6669")
        self.formatText.setObjectName("formatText")
        self.durationText = QtWidgets.QLabel(parent=self.background)
        self.durationText.setGeometry(QtCore.QRect(35, 265, 271, 20))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(10)
        self.durationText.setFont(font)
        self.durationText.setStyleSheet("color: #5D6669")
        self.durationText.setObjectName("durationText")
        self.verticalLayoutWidget = QtWidgets.QWidget(parent=self.background)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(360, 30, 251, 211))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 52))
        self.frame_2.setStyleSheet("QComboBox{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
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
        self.frame_2.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(parent=self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 249, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.formatBox = QtWidgets.QComboBox(parent=self.frame_2)
        self.formatBox.setGeometry(QtCore.QRect(0, 20, 249, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        self.formatBox.setFont(font)
        self.formatBox.setObjectName("formatBox")
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(0, 52))
        self.frame.setStyleSheet("QComboBox{\n"
"height: 30px;\n"
"border-radius: 3px;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
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
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.label_2 = QtWidgets.QLabel(parent=self.frame)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 249, 16))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Mono")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.extensionBox = QtWidgets.QComboBox(parent=self.frame)
        self.extensionBox.setGeometry(QtCore.QRect(0, 20, 249, 31))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        self.extensionBox.setFont(font)
        self.extensionBox.setObjectName("extensionBox")
        self.verticalLayout.addWidget(self.frame)
        self.frame_3 = QtWidgets.QFrame(parent=self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMinimumSize(QtCore.QSize(0, 62))
        self.frame_3.setStyleSheet("QCheckBox:indicator{\n"
"Width: 22px;\n"
"Height: 22px;\n"
"border: 1px solid #C1C1C1;\n"
"background-color: qlineargradient(spread:pad, x1:0.5, y1:0, x2:0.5, y2:1, stop:0 rgba(243, 243, 243, 255), stop:1 rgba(239, 239, 239, 255));\n"
"border-radius: 3px;\n"
"}\n"
"\n"
"QCheckBox:indicator:checked{\n"
f"image: url({PATH}/checked.png);\n"
"}\n"
"")
        self.frame_3.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_5 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_5.setGeometry(QtCore.QRect(38, 0, 211, 21))
        font = QtGui.QFont()
        font.setFamily("Ubuntu Medium")
        font.setPointSize(11)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.sponsorBlockBox = QtWidgets.QCheckBox(parent=self.frame_3)
        self.sponsorBlockBox.setGeometry(QtCore.QRect(0, 0, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sponsorBlockBox.setFont(font)
        self.sponsorBlockBox.setText("")
        self.sponsorBlockBox.setIconSize(QtCore.QSize(16, 16))
        self.sponsorBlockBox.setChecked(False)
        self.sponsorBlockBox.setTristate(False)
        self.sponsorBlockBox.setObjectName("sponsorBlockBox")
        self.label_6 = QtWidgets.QLabel(parent=self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(40, 10, 211, 51))
        font = QtGui.QFont()
        font.setFamily("Ubuntu")
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: #717171")
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.frame_3)
        self.titleBar = QtWidgets.QFrame(parent=Form)
        self.titleBar.setGeometry(QtCore.QRect(0, 0, 651, 55))
        self.titleBar.setStyleSheet(".QToolButton{\n"
"background-color: rgba(255, 255, 255, 0);\n"
"}")
        self.titleBar.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.titleBar.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.titleBar.setObjectName("titleBar")
        self.formTitle = QtWidgets.QLabel(parent=self.titleBar)
        self.formTitle.setGeometry(QtCore.QRect(200, 18, 251, 21))
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
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(f"{PATH}/close.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        icon1.addPixmap(QtGui.QPixmap(f"{PATH}/close-white.png"), QtGui.QIcon.Mode.Active, QtGui.QIcon.State.On)
        icon1.addPixmap(QtGui.QPixmap(f"{PATH}/close-white.png"), QtGui.QIcon.Mode.Selected, QtGui.QIcon.State.On)
        self.CloseButton.setIcon(icon1)
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
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(f"{PATH}/hide.png"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        self.HideButton.setIcon(icon2)
        self.HideButton.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.DelayedPopup)
        self.HideButton.setToolButtonStyle(QtCore.Qt.ToolButtonStyle.ToolButtonIconOnly)
        self.HideButton.setObjectName("HideButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Подтверждение загрузки"))
        self.downloadButton.setText(_translate("Form", "Скачать"))
        self.savePath.setText(_translate("Form", "Файл будет сохранен в:"))
        self.fileName.setText(_translate("Form", "Название файла"))
        self.fileName.setPlaceholderText(_translate("Form", "Введите название файла"))
        self.formatText.setText(_translate("Form", "Оригинальное расширение:"))
        self.durationText.setText(_translate("Form", "Длительность:"))
        self.label_3.setText(_translate("Form", "Формат"))
        self.label_2.setText(_translate("Form", "Расширение"))
        self.label_5.setText(_translate("Form", "Удалить рекламные вставки"))
        self.label_6.setText(_translate("Form", "Удаление рекламных фрагментов из видео на базе SponsorBlock."))
        self.formTitle.setText(_translate("Form", "Подтверждение загрузки"))
        self.CloseButton.setToolTip(_translate("Form", "Закрыть"))
        self.CloseButton.setText(_translate("Form", "..."))
        self.HideButton.setToolTip(_translate("Form", "Свернуть"))
        self.HideButton.setText(_translate("Form", "..."))
