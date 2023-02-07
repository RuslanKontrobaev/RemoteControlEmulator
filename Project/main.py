import sys
import time

from PyQt5 import QtWidgets
from PyQt5.QtCore import QIODevice
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtWidgets import qApp

from codes import Code
from design import Ui_MainWindow


class SerialPort:
    def __init__(self, name, baundrate, parity, stopbits, databits, flowcontrol):
        self.serialPort = QSerialPort()
        self.serialPort.setPortName(name)
        self.serialPort.setBaudRate(baundrate)
        self.serialPort.setParity(parity)
        self.serialPort.setStopBits(stopbits)
        self.serialPort.setDataBits(databits)
        self.serialPort.setFlowControl(flowcontrol)

    def open_port(self):
        self.serialPort.open(QIODevice.WriteOnly)
        time.sleep(1)

    def close_port(self): self.serialPort.close()

    def serial_send(self, data):
        self.serialPort.write(bytes(str(data), 'ascii'))
        # time.sleep(1)


class RemoteControl(QtWidgets.QMainWindow, Ui_MainWindow):
    port = None
    firstaction = None

    def __init__(self):
        super(RemoteControl, self).__init__()
        self.setupUi(self)

        self.init_interface()

        self.refresh_available_ports()
        self.port = SerialPort(QSerialPortInfo.availablePorts()[0].portName(), QSerialPort.BaudRate.Baud9600,
                               QSerialPort.NoParity, QSerialPort.OneStop, QSerialPort.Data8, QSerialPort.NoFlowControl)
        self.port.open_port()

        self.firstaction.setChecked(True)

    def init_interface(self):
        self.setFixedSize(312, 855)

        self.actionExit.triggered.connect(qApp.quit)

        self.b_POWER.clicked.connect(self.power_btn)
        self.b_GEQ.clicked.connect(self.geq_btn)
        self.b_SOUND.clicked.connect(self.sound_btn)
        self.b_ENTER.clicked.connect(self.enter_btn)

        self.b_REC_MODE.clicked.connect(self.rec_mode_btn)
        self.b_REC_REC_MUTE.clicked.connect(self.rec_rec_mute_btn)

        self.b_PRESET_UP.clicked.connect(self.preset_up_btn)
        self.b_PRESET_DOWN.clicked.connect(self.preset_down_btn)

        self.b_VOLUME_UP.clicked.connect(self.volume_up_btn)
        self.b_VOLUME_DOWN.clicked.connect(self.volume_down_btn)

        self.b_NUM_1.clicked.connect(self.num1_btn)
        self.b_NUM_2.clicked.connect(self.num2_btn)
        self.b_NUM_3.clicked.connect(self.num3_btn)
        self.b_NUM_4.clicked.connect(self.num4_btn)
        self.b_NUM_5.clicked.connect(self.num5_btn)
        self.b_NUM_6.clicked.connect(self.num6_btn)
        self.b_NUM_7.clicked.connect(self.num7_btn)
        self.b_NUM_8.clicked.connect(self.num8_btn)
        self.b_NUM_9.clicked.connect(self.num9_btn)
        self.b_CD_DIRECT.clicked.connect(self.cd_direct_btn)
        self.b_NUM_0.clicked.connect(self.num0_btn)
        self.b_NUM_10.clicked.connect(self.num10_btn)

        self.b_DECK_1_2.clicked.connect(self.deck_1_2_btn)
        self.b_BAND.clicked.connect(self.band_btn)

        self.b_PLAY.clicked.connect(self.play_btn)
        self.b_PREV.clicked.connect(self.prev_btn)
        self.b_NEXT.clicked.connect(self.next_btn)
        self.b_SET.clicked.connect(self.set_pause_btn)
        self.b_STOP.clicked.connect(self.stop_btn)

        self.b_SHIFT.setCheckable(True)
        self.b_SHIFT.setChecked(False)
        self.b_SHIFT.clicked.connect(self.shift_btn)
        self.b_FUNCTION.clicked.connect(self.function_btn)

    def refresh_available_ports(self):
        portlist = []
        for port in QSerialPortInfo.availablePorts():
            portlist.append(port.portName())

        actiongroup = QtWidgets.QActionGroup(self)
        actiongroup.setExclusive(True)

        i = 0
        self.menu_COM.clear()
        for name in portlist:
            action = QtWidgets.QAction(self)
            action.setText(name)
            action.setCheckable(True)
            action.setChecked(False)
            action.setData(name)
            action.triggered.connect(self.change_port)
            actiongroup.addAction(action)
            if i == 0:
                self.firstaction = action
            i += 1
            self.menu_COM.addAction(action)

    def change_port(self):
        self.port.close_port()
        self.port = SerialPort(str(self.sender().data()), QSerialPort.BaudRate.Baud9600, QSerialPort.NoParity,
                               QSerialPort.OneStop, QSerialPort.Data8, QSerialPort.NoFlowControl)
        self.port.open_port()
        self.statusbar.showMessage("Порт успешно изменен на " + str(self.sender().data()), 5000)

    def show_pressed_btn_in_statusbar(self, data):
        self.statusbar.showMessage(data.name + " = " + data.value, 5000)

    def power_btn(self):
        self.port.serial_send(Code.POWER.value)
        self.show_pressed_btn_in_statusbar(Code.POWER)

    def geq_btn(self):
        self.port.serial_send(Code.GEQ.value)
        self.show_pressed_btn_in_statusbar(Code.GEQ)

    def sound_btn(self):
        self.port.serial_send(Code.SOUND.value)
        self.show_pressed_btn_in_statusbar(Code.SOUND)

    def enter_btn(self):
        self.port.serial_send(Code.ENTER.value)
        self.show_pressed_btn_in_statusbar(Code.ENTER)

    def rec_mode_btn(self):
        self.port.serial_send(Code.REC_MODE.value)
        self.show_pressed_btn_in_statusbar(Code.REC_MODE)

    def rec_rec_mute_btn(self):
        self.port.serial_send(Code.REC_REC_MUTE.value)
        self.show_pressed_btn_in_statusbar(Code.REC_REC_MUTE)

    def preset_up_btn(self):
        self.port.serial_send(Code.PRESET_UP.value)
        self.show_pressed_btn_in_statusbar(Code.PRESET_UP)

    def preset_down_btn(self):
        self.port.serial_send(Code.PRESET_DOWN.value)
        self.show_pressed_btn_in_statusbar(Code.PRESET_DOWN)

    def volume_up_btn(self):
        self.port.serial_send(Code.VOLUME_UP.value)
        self.show_pressed_btn_in_statusbar(Code.VOLUME_UP)

    def volume_down_btn(self):
        self.port.serial_send(Code.VOLUME_DOWN.value)
        self.show_pressed_btn_in_statusbar(Code.VOLUME_DOWN)

    def num1_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT1.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT1)
        else:
            self.port.serial_send(Code.NUM_1.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_1)

    def num2_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT2.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT2)
        else:
            self.port.serial_send(Code.NUM_2.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_2)

    def num3_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT3.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT3)
        else:
            self.port.serial_send(Code.NUM_3.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_3)

    def num4_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT4.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT4)
        else:
            self.port.serial_send(Code.NUM_4.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_4)

    def num5_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT5.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT5)
        else:
            self.port.serial_send(Code.NUM_5.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_5)

    def num6_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT6.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT6)
        else:
            self.port.serial_send(Code.NUM_6.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_6)

    def num7_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT7.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT7)
        else:
            self.port.serial_send(Code.NUM_7.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_7)

    def num8_btn(self):
        if self.b_SHIFT.isChecked():
            self.port.serial_send(Code.SHIFT8.value)
            self.show_pressed_btn_in_statusbar(Code.SHIFT8)
        else:
            self.port.serial_send(Code.NUM_8.value)
            self.show_pressed_btn_in_statusbar(Code.NUM_8)

    def num9_btn(self):
        self.port.serial_send(Code.NUM_9.value)
        self.show_pressed_btn_in_statusbar(Code.NUM_9)

    def cd_direct_btn(self):
        self.port.serial_send(Code.CD_DIRECT.value)
        self.show_pressed_btn_in_statusbar(Code.CD_DIRECT)

    def num0_btn(self):
        self.port.serial_send(Code.NUM_0.value)
        self.show_pressed_btn_in_statusbar(Code.NUM_0)

    def num10_btn(self):
        self.port.serial_send(Code.NUM_10.value)
        self.show_pressed_btn_in_statusbar(Code.NUM_10)

    def deck_1_2_btn(self):
        self.port.serial_send(Code.DECK_1_2.value)
        self.show_pressed_btn_in_statusbar(Code.DECK_1_2)

    def band_btn(self):
        self.port.serial_send(Code.BAND.value)
        self.show_pressed_btn_in_statusbar(Code.BAND)

    def play_btn(self):
        self.port.serial_send(Code.PLAY.value)
        self.show_pressed_btn_in_statusbar(Code.PLAY)

    def prev_btn(self):
        self.port.serial_send(Code.PREV.value)
        self.show_pressed_btn_in_statusbar(Code.PREV)

    def next_btn(self):
        self.port.serial_send(Code.NEXT.value)
        self.show_pressed_btn_in_statusbar(Code.NEXT)

    def set_pause_btn(self):
        self.port.serial_send(Code.SET_PAUSE.value)
        self.show_pressed_btn_in_statusbar(Code.SET_PAUSE)

    def stop_btn(self):
        self.port.serial_send(Code.STOP.value)
        self.show_pressed_btn_in_statusbar(Code.STOP)

    def shift_btn(self):
        if self.b_SHIFT.isChecked():
            self.b_SHIFT.setStyleSheet("background: rgba(199, 168, 114, 170)")
        else:
            self.b_SHIFT.setStyleSheet("background-color: transparent")
        self.port.serial_send(Code.SHIFT.value)
        self.show_pressed_btn_in_statusbar(Code.SHIFT)

    def function_btn(self):
        self.port.serial_send(Code.FUNCTION.value)
        self.show_pressed_btn_in_statusbar(Code.FUNCTION)


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = RemoteControl()
    window.show()
    app.exec_()
    sys.exit(window.port.close_port())


if __name__ == "__main__":
    main()
