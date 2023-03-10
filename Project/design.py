# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(311, 855)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./resources/Icon.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet(open("./css/style.css", "r").read())
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_5.setGeometry(QtCore.QRect(66, 156, 34, 85))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.Rec = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.Rec.setContentsMargins(0, 0, 0, 0)
        self.Rec.setSpacing(23)
        self.Rec.setObjectName("Rec")
        self.b_REC_MODE = QtWidgets.QPushButton(self.layoutWidget_5)
        self.b_REC_MODE.setMinimumSize(QtCore.QSize(0, 0))
        self.b_REC_MODE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_REC_MODE.setStyleSheet("")
        self.b_REC_MODE.setText("")
        self.b_REC_MODE.setObjectName("b_REC_MODE")
        self.Rec.addWidget(self.b_REC_MODE)
        self.b_REC_REC_MUTE = QtWidgets.QPushButton(self.layoutWidget_5)
        self.b_REC_REC_MUTE.setMinimumSize(QtCore.QSize(0, 0))
        self.b_REC_REC_MUTE.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_REC_REC_MUTE.setStyleSheet("")
        self.b_REC_REC_MUTE.setText("")
        self.b_REC_REC_MUTE.setObjectName("b_REC_REC_MUTE")
        self.Rec.addWidget(self.b_REC_REC_MUTE)
        self.layoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_3.setGeometry(QtCore.QRect(146, 154, 41, 91))
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.Preset = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.Preset.setContentsMargins(0, 0, 0, 0)
        self.Preset.setSpacing(18)
        self.Preset.setObjectName("Preset")
        self.b_PRESET_UP = QtWidgets.QPushButton(self.layoutWidget_3)
        self.b_PRESET_UP.setMinimumSize(QtCore.QSize(0, 0))
        self.b_PRESET_UP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_PRESET_UP.setStyleSheet("")
        self.b_PRESET_UP.setText("")
        self.b_PRESET_UP.setObjectName("b_PRESET_UP")
        self.Preset.addWidget(self.b_PRESET_UP)
        self.b_PRESET_DOWN = QtWidgets.QPushButton(self.layoutWidget_3)
        self.b_PRESET_DOWN.setMinimumSize(QtCore.QSize(0, 0))
        self.b_PRESET_DOWN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_PRESET_DOWN.setStyleSheet("")
        self.b_PRESET_DOWN.setText("")
        self.b_PRESET_DOWN.setObjectName("b_PRESET_DOWN")
        self.Preset.addWidget(self.b_PRESET_DOWN)
        self.layoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_2.setGeometry(QtCore.QRect(231, 154, 41, 91))
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.Volume = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.Volume.setContentsMargins(0, 0, 0, 0)
        self.Volume.setSpacing(18)
        self.Volume.setObjectName("Volume")
        self.b_VOLUME_UP = QtWidgets.QPushButton(self.layoutWidget_2)
        self.b_VOLUME_UP.setMinimumSize(QtCore.QSize(0, 0))
        self.b_VOLUME_UP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_VOLUME_UP.setStyleSheet("")
        self.b_VOLUME_UP.setText("")
        self.b_VOLUME_UP.setObjectName("b_VOLUME_UP")
        self.Volume.addWidget(self.b_VOLUME_UP)
        self.b_VOLUME_DOWN = QtWidgets.QPushButton(self.layoutWidget_2)
        self.b_VOLUME_DOWN.setMinimumSize(QtCore.QSize(0, 0))
        self.b_VOLUME_DOWN.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_VOLUME_DOWN.setStyleSheet("")
        self.b_VOLUME_DOWN.setText("")
        self.b_VOLUME_DOWN.setObjectName("b_VOLUME_DOWN")
        self.Volume.addWidget(self.b_VOLUME_DOWN)
        self.b_STOP = QtWidgets.QPushButton(self.centralwidget)
        self.b_STOP.setGeometry(QtCore.QRect(111, 592, 100, 37))
        self.b_STOP.setMinimumSize(QtCore.QSize(0, 0))
        self.b_STOP.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_STOP.setStyleSheet("")
        self.b_STOP.setText("")
        self.b_STOP.setObjectName("b_STOP")
        self.b_SHIFT = QtWidgets.QPushButton(self.centralwidget)
        self.b_SHIFT.setGeometry(QtCore.QRect(59, 650, 47, 27))
        self.b_SHIFT.setMinimumSize(QtCore.QSize(0, 0))
        self.b_SHIFT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_SHIFT.setStyleSheet("")
        self.b_SHIFT.setText("")
        self.b_SHIFT.setObjectName("b_SHIFT")
        self.b_FUNCTION = QtWidgets.QPushButton(self.centralwidget)
        self.b_FUNCTION.setGeometry(QtCore.QRect(219, 650, 47, 27))
        self.b_FUNCTION.setMinimumSize(QtCore.QSize(0, 0))
        self.b_FUNCTION.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_FUNCTION.setStyleSheet("")
        self.b_FUNCTION.setText("")
        self.b_FUNCTION.setObjectName("b_FUNCTION")
        self.b_SET = QtWidgets.QPushButton(self.centralwidget)
        self.b_SET.setGeometry(QtCore.QRect(137, 548, 53, 29))
        self.b_SET.setMinimumSize(QtCore.QSize(0, 0))
        self.b_SET.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_SET.setStyleSheet("")
        self.b_SET.setText("")
        self.b_SET.setObjectName("b_SET")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(59, 422, 211, 41))
        self.layoutWidget.setObjectName("layoutWidget")
        self.Other_numbers = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.Other_numbers.setContentsMargins(0, 0, 0, 0)
        self.Other_numbers.setSpacing(42)
        self.Other_numbers.setObjectName("Other_numbers")
        self.b_CD_DIRECT = QtWidgets.QPushButton(self.layoutWidget)
        self.b_CD_DIRECT.setMinimumSize(QtCore.QSize(0, 0))
        self.b_CD_DIRECT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_CD_DIRECT.setStyleSheet("")
        self.b_CD_DIRECT.setText("")
        self.b_CD_DIRECT.setObjectName("b_CD_DIRECT")
        self.Other_numbers.addWidget(self.b_CD_DIRECT)
        self.b_NUM_0 = QtWidgets.QPushButton(self.layoutWidget)
        self.b_NUM_0.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_0.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_0.setStyleSheet("")
        self.b_NUM_0.setText("")
        self.b_NUM_0.setObjectName("b_NUM_0")
        self.Other_numbers.addWidget(self.b_NUM_0)
        self.b_NUM_10 = QtWidgets.QPushButton(self.layoutWidget)
        self.b_NUM_10.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_10.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_10.setStyleSheet("")
        self.b_NUM_10.setText("")
        self.b_NUM_10.setObjectName("b_NUM_10")
        self.Other_numbers.addWidget(self.b_NUM_10)
        self.layoutWidget_7 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_7.setGeometry(QtCore.QRect(61, 368, 209, 41))
        self.layoutWidget_7.setObjectName("layoutWidget_7")
        self.Numbers_7_9 = QtWidgets.QHBoxLayout(self.layoutWidget_7)
        self.Numbers_7_9.setContentsMargins(0, 0, 0, 0)
        self.Numbers_7_9.setSpacing(42)
        self.Numbers_7_9.setObjectName("Numbers_7_9")
        self.b_NUM_7 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.b_NUM_7.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_7.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_7.setStyleSheet("")
        self.b_NUM_7.setText("")
        self.b_NUM_7.setObjectName("b_NUM_7")
        self.Numbers_7_9.addWidget(self.b_NUM_7)
        self.b_NUM_8 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.b_NUM_8.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_8.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_8.setStyleSheet("")
        self.b_NUM_8.setText("")
        self.b_NUM_8.setObjectName("b_NUM_8")
        self.Numbers_7_9.addWidget(self.b_NUM_8)
        self.b_NUM_9 = QtWidgets.QPushButton(self.layoutWidget_7)
        self.b_NUM_9.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_9.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_9.setStyleSheet("")
        self.b_NUM_9.setText("")
        self.b_NUM_9.setObjectName("b_NUM_9")
        self.Numbers_7_9.addWidget(self.b_NUM_9)
        self.layoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_4.setGeometry(QtCore.QRect(61, 260, 209, 41))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.Numbers_1_3 = QtWidgets.QHBoxLayout(self.layoutWidget_4)
        self.Numbers_1_3.setContentsMargins(0, 0, 0, 0)
        self.Numbers_1_3.setSpacing(42)
        self.Numbers_1_3.setObjectName("Numbers_1_3")
        self.b_NUM_1 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.b_NUM_1.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_1.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_1.setStyleSheet("")
        self.b_NUM_1.setText("")
        self.b_NUM_1.setObjectName("b_NUM_1")
        self.Numbers_1_3.addWidget(self.b_NUM_1)
        self.b_NUM_2 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.b_NUM_2.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_2.setStyleSheet("")
        self.b_NUM_2.setText("")
        self.b_NUM_2.setObjectName("b_NUM_2")
        self.Numbers_1_3.addWidget(self.b_NUM_2)
        self.b_NUM_3 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.b_NUM_3.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_3.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_3.setStyleSheet("")
        self.b_NUM_3.setText("")
        self.b_NUM_3.setObjectName("b_NUM_3")
        self.Numbers_1_3.addWidget(self.b_NUM_3)
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(1, 0, 321, 829))
        self.background.setStyleSheet("")
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("./resources/Remote Controller.jpg"))
        self.background.setObjectName("background")
        self.layoutWidget_8 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_8.setGeometry(QtCore.QRect(61, 314, 211, 41))
        self.layoutWidget_8.setObjectName("layoutWidget_8")
        self.Numbers_4_6 = QtWidgets.QHBoxLayout(self.layoutWidget_8)
        self.Numbers_4_6.setContentsMargins(0, 0, 0, 0)
        self.Numbers_4_6.setSpacing(43)
        self.Numbers_4_6.setObjectName("Numbers_4_6")
        self.b_NUM_4 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.b_NUM_4.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_4.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_4.setStyleSheet("")
        self.b_NUM_4.setText("")
        self.b_NUM_4.setObjectName("b_NUM_4")
        self.Numbers_4_6.addWidget(self.b_NUM_4)
        self.b_NUM_5 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.b_NUM_5.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_5.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_5.setStyleSheet("")
        self.b_NUM_5.setText("")
        self.b_NUM_5.setObjectName("b_NUM_5")
        self.Numbers_4_6.addWidget(self.b_NUM_5)
        self.b_NUM_6 = QtWidgets.QPushButton(self.layoutWidget_8)
        self.b_NUM_6.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NUM_6.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NUM_6.setStyleSheet("")
        self.b_NUM_6.setText("")
        self.b_NUM_6.setObjectName("b_NUM_6")
        self.Numbers_4_6.addWidget(self.b_NUM_6)
        self.b_PLAY = QtWidgets.QPushButton(self.centralwidget)
        self.b_PLAY.setGeometry(QtCore.QRect(113, 496, 100, 37))
        self.b_PLAY.setMinimumSize(QtCore.QSize(0, 0))
        self.b_PLAY.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_PLAY.setStyleSheet("")
        self.b_PLAY.setText("")
        self.b_PLAY.setObjectName("b_PLAY")
        self.b_PREV = QtWidgets.QPushButton(self.centralwidget)
        self.b_PREV.setGeometry(QtCore.QRect(73, 518, 45, 87))
        self.b_PREV.setMinimumSize(QtCore.QSize(0, 0))
        self.b_PREV.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_PREV.setStyleSheet("")
        self.b_PREV.setText("")
        self.b_PREV.setObjectName("b_PREV")
        self.b_POWER = QtWidgets.QPushButton(self.centralwidget)
        self.b_POWER.setGeometry(QtCore.QRect(56, 94, 41, 41))
        self.b_POWER.setMinimumSize(QtCore.QSize(0, 0))
        self.b_POWER.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_POWER.setStyleSheet("")
        self.b_POWER.setText("")
        self.b_POWER.setObjectName("b_POWER")
        self.b_NEXT = QtWidgets.QPushButton(self.centralwidget)
        self.b_NEXT.setGeometry(QtCore.QRect(209, 520, 45, 87))
        self.b_NEXT.setMinimumSize(QtCore.QSize(0, 0))
        self.b_NEXT.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_NEXT.setStyleSheet("")
        self.b_NEXT.setText("")
        self.b_NEXT.setObjectName("b_NEXT")
        self.b_DECK_1_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_DECK_1_2.setGeometry(QtCore.QRect(57, 484, 31, 30))
        self.b_DECK_1_2.setMinimumSize(QtCore.QSize(0, 0))
        self.b_DECK_1_2.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_DECK_1_2.setStyleSheet("")
        self.b_DECK_1_2.setText("")
        self.b_DECK_1_2.setObjectName("b_DECK_1_2")
        self.b_BAND = QtWidgets.QPushButton(self.centralwidget)
        self.b_BAND.setGeometry(QtCore.QRect(239, 486, 31, 30))
        self.b_BAND.setMinimumSize(QtCore.QSize(0, 0))
        self.b_BAND.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_BAND.setStyleSheet("")
        self.b_BAND.setText("")
        self.b_BAND.setObjectName("b_BAND")
        self.layoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget_6.setGeometry(QtCore.QRect(116, 109, 161, 27))
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.Control = QtWidgets.QHBoxLayout(self.layoutWidget_6)
        self.Control.setContentsMargins(0, 0, 0, 0)
        self.Control.setSpacing(18)
        self.Control.setObjectName("Control")
        self.b_GEQ = QtWidgets.QPushButton(self.layoutWidget_6)
        self.b_GEQ.setMinimumSize(QtCore.QSize(0, 0))
        self.b_GEQ.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_GEQ.setStyleSheet("")
        self.b_GEQ.setText("")
        self.b_GEQ.setObjectName("b_GEQ")
        self.Control.addWidget(self.b_GEQ)
        self.b_SOUND = QtWidgets.QPushButton(self.layoutWidget_6)
        self.b_SOUND.setMinimumSize(QtCore.QSize(0, 0))
        self.b_SOUND.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_SOUND.setStyleSheet("")
        self.b_SOUND.setText("")
        self.b_SOUND.setObjectName("b_SOUND")
        self.Control.addWidget(self.b_SOUND)
        self.b_ENTER = QtWidgets.QPushButton(self.layoutWidget_6)
        self.b_ENTER.setMinimumSize(QtCore.QSize(0, 0))
        self.b_ENTER.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.b_ENTER.setStyleSheet("")
        self.b_ENTER.setText("")
        self.b_ENTER.setObjectName("b_ENTER")
        self.Control.addWidget(self.b_ENTER)
        self.Control.setStretch(0, 5)
        self.Control.setStretch(1, 5)
        self.Control.setStretch(2, 5)
        self.background.raise_()
        self.layoutWidget_5.raise_()
        self.layoutWidget_3.raise_()
        self.layoutWidget_2.raise_()
        self.b_STOP.raise_()
        self.b_SHIFT.raise_()
        self.b_FUNCTION.raise_()
        self.b_SET.raise_()
        self.layoutWidget.raise_()
        self.layoutWidget_7.raise_()
        self.layoutWidget_4.raise_()
        self.layoutWidget_8.raise_()
        self.b_PLAY.raise_()
        self.b_PREV.raise_()
        self.b_POWER.raise_()
        self.b_NEXT.raise_()
        self.b_DECK_1_2.raise_()
        self.b_BAND.raise_()
        self.layoutWidget_6.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 311, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_COM = QtWidgets.QMenu(self.menu)
        self.menu_COM.setObjectName("menu_COM")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setShortcut('Ctrl+Q')
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.menu_COM.menuAction())
        self.menu.addSeparator()
        self.menu.addAction(self.actionExit)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Remote AIWA RC-CAS01"))
        self.menu.setTitle(_translate("MainWindow", "????????"))
        self.menu_COM.setTitle(_translate("MainWindow", "?????????????? COM"))
        self.actionExit.setText(_translate("MainWindow", "??????????"))
