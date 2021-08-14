import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtWidgets import QSlider, QHBoxLayout, QLabel
from PyQt5.QtCore import Qt
from upydevice import Device


class KeyController(QWidget):
    def __init__(self, parent=None, device=None):
        super(KeyController, self).__init__(parent)

        layout = QHBoxLayout()
        self.l1 = QLabel("Press UP,DOWN keys to move servo angle: ")
        self.l1.setAlignment(Qt.AlignCenter)
        self.label = QLabel("0", self)
        self.label.setAlignment(Qt.AlignCenter | Qt.AlignVCenter)
        self.label.setMinimumWidth(80)
        self.angle = 0

        layout.addSpacing(15)
        layout.addWidget(self.l1)
        layout.addWidget(self.label)
        self.setLayout(layout)
        self.setGeometry(10, 10, 350, 250)

        self.device = device

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Up:
                if self.angle < 90:
                    self.angle += 4
                    self.device.wr_cmd("s1.angle({}, 100)".format(self.angle))
                    print(f"Setting angle to {self.angle}")
                    self.label.setText(str(self.angle))

        elif e.key() == Qt.Key_Down:
                if self.angle > -90:
                    self.angle -= 4
                    self.device.wr_cmd("s1.angle({}, 100)".format(self.angle))
                    print(f"Setting angle to {self.angle}")
                    self.label.setText(str(self.angle))


def main():

    # SerialDevice
    print("Connecting to device...")
    mydev = Device("/dev/tty.usbmodem3370377430372", init=True)
    mydev.wr_cmd("from pyb import Servo;s1 = Servo(1)")
    # # WebSocketDevice
    # mydev = Device('192.168.1.73', 'keyespw', init=True)

    # # BleDevice
    # mydev = Device('9998175F-9A91-4CA2-B5EA-482AFC3453B9', init=True)
    print("Connected")

    app = QApplication(sys.argv)

    Keycontroller = KeyController(device=mydev)

    Keycontroller.show()

    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
