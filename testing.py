import kivy
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

from kivy.app import App


class MainApp(GridLayout):
    def __init__(self, **kwargs):
        super(MainApp, self).__init__(**kwargs)

        self.cols = 1

        self.firstLabel = Label(text='Rasool')
        self.add_widget(self.firstLabel)


class MyApp(App):
    def build(self):
        return MainApp()


if __name__ == '__main__':
    MyApp().run()