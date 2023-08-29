"""
Simple calculator app on Python&Kivy
credits to codemy.com.
How ever, we probly should avoid eval() ?
"""
# from ast import literal_eval
from kivy.app import App
from kivy.uix.widget import Widget
from kivy import require as kivyreq
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 600)
Builder.load_file("stonecalc.kv")
kivyreq("2.2.0")


class MyLayout(Widget):
    """creates a layout"""

    def clear(self):
        """zero as first text"""
        self.ids.calc_input.text = "0"

    def button_press(self, button: str):
        """set input to what ever is pressed"""
        prior = self.ids.calc_input.text
        if "-E-" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def toggle_dash(self):
        """toggle wether the number is negative"""
        prior = self.ids.calc_input.text
        if "-" in prior[0]:
            self.ids.calc_input.text = prior[1:]
        else:
            self.ids.calc_input.text = f"-{prior}"

    def remove(self):
        """remove last number"""
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def dot(self):
        """handle dot"""
        prior = self.ids.calc_input.text
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

        elif "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    def math_sign(self, sign: str):
        """insert math sign"""
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"

    def equal(self):
        """What happen when = is hit."""
        prior = self.ids.calc_input.text

        # This block should be written more professionally.
        try:
            ans = eval(str(prior))
            self.ids.calc_input.text = str(ans)
        except:
            self.ids.calc_input.text = "-E-"


class CalcApp(App):
    """The main app"""

    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalcApp().run()
