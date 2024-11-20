#Python Stopwatch

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt


class StopWatch(QWidget):
    def __init__(self):
        super().__init__()

        # Initialize timer and QTime for counting elapsed time
        self.timer = QTimer(self)
        self.time = QTime(0, 0, 0, 0)

        # Initialize GUI components
        self.time_label = QLabel("00:00:00.00", self)
        self.start_button = QPushButton("Start", self)
        self.stop_button = QPushButton("Stop", self)
        self.reset_button = QPushButton("Reset", self)

        # Set up the user interface
        self.initUI()

    def initUI(self):
        # Set the window title
        self.setWindowTitle("StopWatch")

        # Main vertical layout
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        vbox.addWidget(self.start_button)
        vbox.addWidget(self.stop_button)
        vbox.addWidget(self.reset_button)
        self.setLayout(vbox)

        # Center-align the time label
        self.time_label.setAlignment(Qt.AlignCenter)

        # Horizontal layout for the buttons
        hbox = QHBoxLayout()
        hbox.addWidget(self.start_button)
        hbox.addWidget(self.stop_button)
        hbox.addWidget(self.reset_button)
        vbox.addLayout(hbox)

        # Apply styles to buttons and labels
        self.setStyleSheet("""
            QPushButton, QLabel {
                padding: 20px;
                font-weight: bold;
                font-family: Calibri;
            }
            QPushButton {
                font-size: 50px;
            }
            QLabel {
                font-size: 120px;
                background-color: hsl(200, 100%, 85%);
                border-radius: 20px;
            }
        """)

        # Connect buttons to their respective functions
        self.start_button.clicked.connect(self.start)
        self.stop_button.clicked.connect(self.stop)
        self.reset_button.clicked.connect(self.reset)

        # Connect timer timeout to update_display for updating time
        self.timer.timeout.connect(self.update_display)

    def start(self):
        # Start the timer with 10 ms intervals for precise time updates
        self.timer.start(10)

    def stop(self):
        # Stop the timer
        self.timer.stop()

    def reset(self):
        # Stop the timer and reset the time to zero
        self.timer.stop()
        self.time = QTime(0, 0, 0, 0)
        self.time_label.setText(self.format_time(self.time))

    def format_time(self, time):
        """
        Formats the time to display hours, minutes, seconds, and milliseconds.
        """
        hours = time.hour()
        minutes = time.minute()
        seconds = time.second()
        milliseconds = int(time.msec() / 10)  # Divide milliseconds for two decimal places
        return f"{hours:02}:{minutes:02}:{seconds:02}.{milliseconds:02}"

    def update_display(self):
        # Increment time by 10 ms and update the time label
        self.time = self.time.addMSecs(10)
        self.time_label.setText(self.format_time(self.time))


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    stopwatch = StopWatch()
    stopwatch.show()
    sys.exit(app.exec_())