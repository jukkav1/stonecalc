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

        if prior == "0":
            self.ids.calc_input.text = ""
            self.ids.calc_input.text = f"{button}"

        else:
            self.ids.calc_input.text = f"{prior}{button}"

    def dot(self):
        prior = self.ids.calc_input.text
        if "." in prior:
            pass
        else:
            prior = f"{prior}."
            self.ids.calc_input.text = prior

    def math_sign(self, sign):
        prior = self.ids.calc_input.text
        self.ids.calc_input.text = f"{prior}{sign}"

    def equal(self):
        prior = self.ids.calc_input.text
        ans = 0
        if "+" in prior:
            num_list = prior.split("+")
            for _ in num_list:
                ans += int(_)
        elif "-" in prior:
            num_list = prior.split("-")
            for _ in num_list:
                ans -= int(_)
        elif "*" in prior:
            num_list = prior.split("*")
            for _ in num_list:
                ans *= int(_)
        elif "/" in prior:
            num_list = prior.split("/")
            for _ in num_list:
                ans /= int(_)

        self.ids.calc_input.text = str(ans)


class CalcApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalcApp().run()
