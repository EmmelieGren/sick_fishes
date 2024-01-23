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
import numpy as np
from tensorflow.keras.preprocessing.image import img_to_array, load_img
from tensorflow.keras.models import load_model

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
        cnn_model = load_model("C:\Skola\Applicerad AI\sick_fishes\saved_models\cnn_model_more_data_17-1-24.h5")
        print("Model Loaded")
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("PNG files (*.png)")
        file_dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        
        if file_dialog.exec() == QFileDialog.DialogCode.Accepted:
            file_path = file_dialog.selectedFiles()[0]
            print("Selected file:", file_path)
            test_image = self.prepare_images([file_path])
            prediction = cnn_model.predict(test_image)

            predicted_class_index = np.argmax(prediction[0])
            confidence_score = prediction[0][predicted_class_index]

            class_labels = ["Diseased", "Healthy"]
            predicted_class_label = class_labels[predicted_class_index]

            print(f"Predicted Class: {predicted_class_label}")
            print(f"Confidence Score: {confidence_score}")

    @staticmethod
    def prepare_images(file_paths, target_size=(64, 64)):
        images = []
        for path in file_paths:
            img = load_img(path, target_size=target_size)
            img_array = img_to_array(img)
            images.append(img_array)
        return np.array(images)


QQuickWindow.setSceneGraphBackend('software')

app = QApplication(sys.argv)
engine = QQmlApplicationEngine()
engine.quit.connect(app.quit)
engine.load('./UI/main.qml')
back_end = Backend()
engine.rootObjects()[0].setProperty('backend', back_end)
back_end.bootUp()
sys.exit(app.exec())