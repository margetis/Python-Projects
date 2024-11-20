#Python Digital Clock

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer, QTime, Qt
from PyQt5.QtGui import QFont, QFontDatabase


class DigitalClock(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize QLabel for displaying time and QTimer for updating the clock
        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.initUI()  # Set up the UI

    def initUI(self):
        # Set the window title and geometry
        self.setWindowTitle("Digital Clock")
        self.setGeometry(600, 400, 300, 100)  # Corrected from `setGemoetry` typo

        # Set up a vertical layout and add the time label to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)

        # Align the time label to the center
        self.time_label.setAlignment(Qt.AlignCenter)

        # Set the style of the time label (font size, family, and color)
        self.time_label.setStyleSheet("font-size: 100px;"  # Reduced size to fit the label
                                      "font-family: Arial;"
                                      "color: hsl(111, 100%, 50%);")  # Fixed color syntax to `hsl`

        # Set background color for the window
        self.setStyleSheet("background-color: black;")

        # Load custom font if available (optional)
        font_id = QFontDatabase.addApplicationFont("")  # Specify font path if required
        if font_id != -1:  # Ensure font is loaded correctly
            font_family = QFontDatabase.applicationFontFamilies(font_id)[0]
            my_font = QFont(font_family, 100)
            self.time_label.setFont(my_font)
        else:
            # Fall back to default font if loading fails
            self.time_label.setFont(QFont("Arial", 100))

        # Connect the timer to the update_time method and start it for 1-second intervals
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

        # Update the time immediately when the UI loads
        self.update_time()

    def update_time(self):
        # Get the current time and format it as hh:mm:ss AP (AM/PM format)
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        # Display the current time on the label
        self.time_label.setText(current_time)


# Run the application
if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = DigitalClock()
    clock.show()
    sys.exit(app.exec_())