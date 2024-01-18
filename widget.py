# This Python file uses the following encoding: utf-8
import sys
from pygame import mixer
from PySide6.QtWidgets import QApplication, QWidget, QListWidgetItem
from PySide6.QtCore import QTimer, QDateTime, QTime
from PySide6.QtGui import QIcon
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_Widget
mixer.init()
class Widget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_Widget()
        self.ui.setupUi(self)
        self.setWindowTitle("Alarm Clock")
        self.setWindowIcon(QIcon("alarm-clock.png"))

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateTime)
        self.timer.start(1000)
        self.updateTime()

        self.ui.setButton.clicked.connect(self.addAlarm)
        self.ui.removeButton.clicked.connect(self.removeAlarm)
        self.ui.stopButton.clicked.connect(self.stopAlarm)

        self.checkAlarmTimer = QTimer(self)
        self.checkAlarmTimer.timeout.connect(self.checkAlarm)
        self.checkAlarmTimer.start(1000)

    def updateTime(self):
        current_time = QDateTime.currentDateTime().toString('hh:mm:ss')
        self.ui.labelTime.setText(f'Current Time: {current_time}')

    def checkAlarm(self):
        currentTime = QTime.currentTime()
        flag = False
        for index in range(self.ui.listWidget.count()):
            item = self.ui.listWidget.item(index)
            alarm_time = item.data(1)
            hourTime = int(alarm_time[:2])
            minTime = int(alarm_time[3:5])
            currentHour = currentTime.hour()
            currentMin = currentTime.minute()
            currentSec = currentTime.second()
            if hourTime == currentHour and minTime == currentMin and currentSec == 0:
                flag = True
                print(f"Alarm Time: {alarm_time}")

        if flag:
            mixer.music.load("sound.mp3")
            mixer.music.play(loops=0)

    def addAlarm(self):
        # Get the selected hour and minute from the dropdown lists
        selected_hour = self.ui.hourcomboBox.currentText()
        selected_minute = self.ui.mincomboBox.currentText()

        # Create a QDateTime object with the selected time
        alarm_datetime = QDateTime.currentDateTime()
        alarm_datetime.setTime(QTime(int(selected_hour), int(selected_minute)))

        # Convert QDateTime to string for display
        alarm_time = alarm_datetime.toString('hh:mm:ss')
        alarm_text = f"Set Alarm: {alarm_time}"

        # Create a QListWidgetItem and set the text
        item = QListWidgetItem(alarm_text)

        # Store the alarm time as data in the item for future use
        item.setData(1, alarm_time)

        # Add the item to the QListWidget
        self.ui.listWidget.addItem(item)

    def removeAlarm(self):
        # Get the selected item from the QListWidget
        selected_item = self.ui.listWidget.currentItem()

        if selected_item:
            # Remove the selected item from the QListWidget
            self.ui.listWidget.takeItem(self.ui.listWidget.row(selected_item))

    def stopAlarm(self):
        mixer.music.stop()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Widget()
    widget.show()
    sys.exit(app.exec())
