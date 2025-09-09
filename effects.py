from PyQt5.QtCore import QTimer, QPropertyAnimation, QEasingCurve
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QColor, QPalette


class Effects:
    def __init__(self):
        self.timer = None
        self.anim = None

    def clear_effects(self, label: QLabel):
        if self.timer:
            self.timer.stop()
        if self.anim:
            self.anim.stop()

    def typewriter(self, label: QLabel, text: str):
        label.setText("")
        self.index = 0

        def update_text():
            if self.index < len(text):
                label.setText(label.text() + text[self.index])
                self.index += 1
            else:
                self.timer.stop()

        self.timer = QTimer()
        self.timer.timeout.connect(update_text)
        self.timer.start(50)

    def blink(self, label: QLabel):
        def toggle():
            label.setVisible(not label.isVisible())

        self.timer = QTimer()
        self.timer.timeout.connect(toggle)
        self.timer.start(500)

    def glow(self, label: QLabel):
        self.anim = QPropertyAnimation(label, b"windowOpacity")
        self.anim.setDuration(2000)
        self.anim.setStartValue(0.5)
        self.anim.setEndValue(1.0)
        self.anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.anim.setLoopCount(-1)
        self.anim.start()
