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


class CalcApp(App):
    def build(self):
        return MyLayout()


if __name__ == "__main__":
    CalcApp().run()
