# This work, created by Anagnostakis Ioannis GR (rizitis@gmail.com), is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License.
# License details: https://creativecommons.org/licenses/by-nc-nd/4.0/legalcode

# You are free to:
# - Share — copy and redistribute the material in any medium or format. The licensor cannot revoke these freedoms as long as you follow the license terms.

# Under the following terms:
# - Attribution — You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
#   You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.
# - NonCommercial — You may not use the material for commercial purposes.
# - NoDerivatives — If you remix, transform, or build upon the material, you may not distribute the modified material.
# - No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

# Notices:
# - You do not have to comply with the license for elements of the material in the public domain or where your use is permitted by an applicable exception or limitation.
# - No warranties are given. The license may not give you all of the permissions necessary for your intended use. For example, other rights such as publicity, privacy, or moral rights may limit how you use the material.


from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import webbrowser

class ColorWebApp(App):
    def build(self):
        # Create a BoxLayout with a vertical orientation
        layout = BoxLayout(orientation='vertical', spacing=10)

        # Add a banner at the top
        banner = Label(
            text='ΠΑTΑΣ ΣΤΟ ΧΡΩΜΜΑ & ΒΛΕΠΕΙΣ ΤΙΜΕΣ',
            size_hint_y=None,
            height=40
        )
        layout.add_widget(banner)

        # Define labels and corresponding web pages
        labels_and_urls = {
            'ΠΡΑΣΙΝΟ': 'https://rizitis.github.io/green.html',
            'ΜΠΛΕ': 'https://rizitis.github.io/blue.html',
            'ΠΟΡΤΟΚΑΛΙ': 'https://rizitis.github.io/orange.html',
            'ΚΙΤΡΙΝΟ': 'https://rizitis.github.io/yellow.html',
            'ΕΠΑΓΓΕΛΜΑΤΙΚΑ ΤΙΜΟΛΟΓΙΑ': 'https://invoices.rae.gr/epaggelmatiko-2/',
        }

        # Create buttons for each color with custom text labels
        for label, url in labels_and_urls.items():
            button = Button(
                text=label,
                background_color=self.get_color_by_label(label),
                on_press=self.on_button_press(url)
            )
            layout.add_widget(button)

        # Add a button as a link to terms and conditions
        terms_button = Button(
            text="Oροι και Προϋποθέσεις χρήσης",
            markup=True,
            background_color=(1, 1, 1, 0),  # Transparent background
            border=(0, 0, 0, 0)  # No border
        )
        terms_button.bind(on_press=self.on_terms_button_press)
        layout.add_widget(terms_button)

        return layout

    def get_color_by_label(self, label):
        # Return the corresponding color based on the label
        color_mapping = {
            'ΠΡΑΣΙΝΟ': (0, 1, 0),
            'ΜΠΛΕ': (0, 0, 1),
            'ΠΟΡΤΟΚΑΛΙ': (255, 0, 0),  # RGB for orange
            'ΚΙΤΡΙΝΟ': (100, 100, 0),  # RGB for yellow
        }
        return color_mapping.get(label, (1, 1, 1))

    def on_button_press(self, url):
        # Callback function for button press
        def callback(instance):
            # Open the web page in the default web browser
            webbrowser.open(url)
        return callback

    def on_terms_button_press(self, instance):
        # Callback function for terms button press
        webbrowser.open("https://rizitis.github.io/privacy_policy.html")

if __name__ == '__main__':
    ColorWebApp().run()

