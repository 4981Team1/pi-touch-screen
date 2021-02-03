import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.lang import Builder

class NumericKeyboard(Bubble):
    layout = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(NumericKeyboard, self).__init__(**kwargs)
        self.create_bubble_button()

    def create_bubble_button(self):
        numeric_keypad = ['7', '8', '9', '4', '5', '6', '1', '2', '3', '', '0', '']
        for x in numeric_keypad:
            if len(x) == 0:
                self.layout.add_widget(Label(text=""))
            else:
                bubb_btn = CustomBubbleButton(text=str(x))
                self.layout.add_widget(bubb_btn)

class MyFloat(Widget):
    pin = ObjectProperty(None)
    msg = ObjectProperty(None)
    
    def btn(self):
        if self.pin.text == "1234":
            self.msg.text = "Successful - " + self.pin.text
            self.pin.text = ""
        else:
            self.msg.text = "Pin " + self.pin.text + " is not accepted"
            self.pin.text = ""
        
    def show_bubble(self, *l):
        if not hasattr(self, 'bubb'):
            self.bubb = bubb = NumericKeyboard()
            self.bubb.arrow_pos = "bottom_mid"
            self.add_widget(bubb)
        
class CustomBubbleButton(BubbleButton):
    pass

class MyFloatApp(App):
    def build(self):
        return MyFloat()

if __name__ == "__main__":
    Window.fullscreen = False
    MyFloatApp().run()