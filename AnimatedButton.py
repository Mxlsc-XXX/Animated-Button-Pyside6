from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QEnterEvent
from PySide6.QtWidgets import QPushButton


class AnimatedButton(QPushButton):
    def __init__(self, text):
        super().__init__(text)
        self._animation = QPropertyAnimation(self, b"geometry")
        self._animation.setDuration(150)
        self._original_geometry = None

    def enterEvent(self, event: QEnterEvent):
        if not self._original_geometry:
            self._original_geometry = self.geometry()
        new_rect = self._original_geometry.adjusted(-3, -3, 3, 3)
        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(new_rect)
        self._animation.start()
        super().enterEvent(event)

    def leaveEvent(self, event):
        self._animation.stop()
        self._animation.setStartValue(self.geometry())
        self._animation.setEndValue(self._original_geometry)
        self._animation.start()
        super().leaveEvent(event)
