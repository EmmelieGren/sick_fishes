import sys
import os
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQml import QQmlApplicationEngine
from PyQt6.QtQuick import QQuickWindow
import threading
from time import strftime, sleep
from PyQt6.QtGui import QGuiApplication
from PyQt6.QtQuick import QQuickWindow
from PyQt6.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton, QTextEdit, QComboBox, QFileDialog,
                             QHBoxLayout, QVBoxLayout)

class Backend(QObject):

    def __init__(self):
        QObject.__init__(self)
    
    updated = pyqtSignal(str, arguments=['updater'])

    def updater(self, curr_time):
        self.updated.emit(curr_time)
    
    def bootUp(self):
        t_thread = threading.Thread(target=self._bootUp)
        t_thread.daemon = True
        t_thread.start()

    def _bootUp(self):
        while True:
            curr_time = strftime("%H:%M")
            self.updater(curr_time)
            sleep(0.1)
            #print(curr_time)
            sleep(0.1)
    @pyqtSlot()
    def importPNG(self):
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PNG files (*.png)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)

        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            print("Selected file:", file_path)

QQuickWindow.setSceneGraphBackend('software')

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)
back_end.bootUp()
sys.exit(app.exec())