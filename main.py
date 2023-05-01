from kivy.app import App
from kivy.uix.widget import Widget

# from kivy.properties import ObjectProperty
from kivy.lang import Builder
from kivy.core.window import Window

Window.size = (400, 600)
Builder.load_file("stonecalc.kv")


class MyLayout(Widget):
    def clear(self):
        self.ids.calc_input.text = "0"

    def button_press(self, button):
        prior = self.ids.calc_input.text
        if "-E-" in prior:
            prior = ""

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def toggle_dash(self):
        prior = self.ids.calc_input.text
        if "-" in prior[0]:
            self.ids.calc_input.text = prior[1:]
        else:
            self.ids.calc_input.text = f"-{prior}"

    def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[:-1]
        self.ids.calc_input.text = prior

    def dot(self):
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

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"

    def equal(self):
        prior = self.ids.calc_input.text
        try:
            ans = eval(prior)
            self.ids.calc_input.text = str(ans)
        except:
            self.ids.calc_input.text = "-E-"


class CalcApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalcApp().run()
