#Python Weather App
import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import Qt
import os

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        # Initialize UI components
        self.city_label = QLabel("Enter City Name: ", self)
        self.city_input = QLineEdit(self)
        self.get_weather_button = QPushButton("Get Weather", self)
        self.temperature_label = QLabel(self)
        self.emoji_label = QLabel(self)
        self.description_label = QLabel(self)
        self.initUI()

    def initUI(self):
        # Set up the window title and layout
        self.setWindowTitle("Weather App")


        vbox = QVBoxLayout()

        # Add widgets to the layout
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        vbox.addWidget(self.emoji_label)
        vbox.addWidget(self.description_label)

        self.setLayout(vbox)

        # Align components to center
        self.city_label.setAlignment(Qt.AlignCenter)
        self.city_input.setAlignment(Qt.AlignCenter)
        self.get_weather_button.setAlignment(Qt.AlignCenter)
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.emoji_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)

        # Set custom object names for styling
        self.city_label.setObjectName("city_label")
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")

        # Apply custom styles using a stylesheet
        self.setStyleSheet("""
            QLabel, QPushButton {
                font-family: calibre;
            }
            QLabel#city_label {
                font-size: 40px;
                font-style: italic;
            }
            QLineEdit#city_input {
                font-size: 40px;
            }
            QPushButton#get_weather_button {
                font-size: 30px;
                font-weight: bold;
            }
            QLabel#temperature_label {
                font-size: 75px;
            }
            QLabel#emoji_label {
                font-size: 100px;
                font-family: Segue UI emoji;
            }
            QLabel#description_label {
                font-size: 50px;
            } 
        """)

        # Connect button click to the get_weather method
        self.get_weather_button.clicked.connect(self.get_weather)

    def get_weather(self):
        # Define the API key and construct the request URL
        api_key = os.getenv("c9af90715cdc20aff19e9526037b499f")
        if not api_key:
            self.display_error("API key not found! Please set the API key.")
            return
        city = self.city_input.text().strip()  # Remove any extra spaces
        if not city:
            self.display_error("City name cannot be empty")
            return
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

        try:
            # Make the API request
            response = requests.get(url)
            response.raise_for_status()  # Raise HTTP errors if any
            try:
                data = response.json()
            except ValueError:
                self.display_error("Error parsing server response:\nInvalid JSON")
                return

            if data["cod"] == 200:  # Success case
                self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:
            # Handle specific HTTP errors based on the response status code
            if response.status_code == 400:
                self.display_error("Bad Request:\nPlease check your input")
            elif response.status_code == 401:
                self.display_error("Unauthorized:\nInvalid API key")
            elif response.status_code == 403:
                self.display_error("Forbidden:\nAccess Denied")
            elif response.status_code == 404:
                self.display_error("Not Found:\nCity not found")
            elif response.status_code == 500:
                self.display_error("Internal Server Error:\nPlease try again later")
            elif response.status_code == 502:
                self.display_error("Bad Gateway:\nInvalid response from the server")
            elif response.status_code == 503:
                self.display_error("Service Unavailable:\nServer is down")
            elif response.status_code == 504:
                self.display_error("Gateway Timeout:\nNo response from the server")
            else:
                self.display_error(f"HTTP error occurred:\n{http_error}")

        except requests.exceptions.ConnectionError:
            self.display_error("Connection Error:\nCheck your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout Error:\nThe request timed out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too Many Redirects Error:\nCheck URL")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")

    def display_error(self, message):
        # Display error message in the temperature label
        self.temperature_label.setStyleSheet("QLabel { font-size: 30px; }")
        self.temperature_label.setText(message)
        self.emoji_label.clear()  # Clear other labels
        self.description_label.clear()

    def display_weather(self, data):
        # Convert temperature from Kelvin to Celsius
        self.temperature_label.setStyleSheet("QLabel { font-size: 75px; }")
        temperature_c = data["main"]["temp"] - 273.15
        weather_id = data["weather"][0]["id"]
        weather_description = data["weather"][0]["description"].capitalize()

        # Update labels with weather data
        self.temperature_label.setText(f"{temperature_c:.0f}°C")
        self.emoji_label.setText(get_weather_emoji(weather_id))
        self.description_label.setText(weather_description)


def get_weather_emoji(weather_id):
    # Map weather conditions to emojis
    if 200 <= weather_id <= 232:
        return "⛈️"
    elif 300 <= weather_id <= 321:
        return "🌦️"
    elif 500 <= weather_id <= 531:
        return "🌧️"
    elif 600 <= weather_id <= 622:
        return "🌨️"
    elif 701 <= weather_id <= 741:
        return "🌫️"
    elif weather_id == 762:
        return "🌋"
    elif weather_id == 771:
        return "💨"
    elif weather_id == 781:
        return "🌪️"
    elif weather_id == 800:
        return "☀️"
    elif 801 <= weather_id <= 804:
        return "☁️"
    else:
        return ""

if __name__ == '__main__':
    # Run the application
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
