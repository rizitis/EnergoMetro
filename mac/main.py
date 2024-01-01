# Your Python script (color_web_app.py)

from PyQt5.QtWidgets import QApplication, QVBoxLayout, QLabel, QPushButton
import sys
import webbrowser

class ColorWebApp:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        # Add a banner at the top
        banner = QLabel('ΠΑTΑΣ ΣΤΟ ΧΡΩΜΜΑ & ΒΛΕΠΕΙΣ ΤΙΜΕΣ')
        banner.setFixedHeight(40)
        layout.addWidget(banner)

        # Define labels and corresponding web pages
        labels_and_urls = {
            'ΠΡΑΣΙΝΟ': 'https://rizitis.github.io/green.html',
            'ΜΠΛΕ': 'https://rizitis.github.io/blue.html',
            'ΠΟΡΤΟΚΑΛΙ': 'https://rizitis.github.io/orange.html',
            'ΚΙΤΡΙΝΟ': 'https://rizitis.github.io/yellow.html',
        }

        # Create buttons for each color with custom text labels
        for label, url in labels_and_urls.items():
            button = QPushButton(label)
            button.clicked.connect(lambda state, url=url: webbrowser.open(url))
            layout.addWidget(button)

        # Add a button as a link to terms and conditions
        terms_button = QPushButton("Oροι και Προϋποθέσεις χρήσης")
        terms_button.clicked.connect(lambda: webbrowser.open("https://rizitis.github.io/privacy_policy.html"))
        layout.addWidget(terms_button)

        self.app.setLayout(layout)

    def run(self):
        sys.exit(self.app.exec_())

if __name__ == '__main__':
    app = ColorWebApp()
    app.run()
