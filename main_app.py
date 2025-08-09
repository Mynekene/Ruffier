# напиши тут свою програму
from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from instructions import *

class MainWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label1 = Label(text=txt_instruction)
        label_name = Label(text='Введіть ім*я')
        label_age = Label(text='Введіть вік')
        user_name = TextInput(text= '')
        user_age = TextInput(text= '')
        button = Button(text='почати')
        button.on_press = self.next_window
        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 30)
        layout1 = BoxLayout()
        layout2 = BoxLayout()
        main_layout.add_widget(label1)
        main_layout.add_widget(layout1)
        layout1.add_widget(label_name)
        layout1.add_widget(user_name)
        main_layout.add_widget(layout2)
        layout2.add_widget(label_age)
        layout2.add_widget(user_age)
        main_layout.add_widget(button)
        self.add_widget(main_layout)
        
    def next_window(self):
        self.manager.current = 'first_pulse'


class InputPulseFirst(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label1 = Label(text= txt_test1)
        label2 = Label(text='Введіть результат')
        self.first_result = TextInput(multiline= False)
        self.button = Button(text='Продовжити')
        self.button.on_press = self.next_window
        layout1 = BoxLayout()
        layout1.add_widget(label2)
        layout1.add_widget(self.first_result)
        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 30)
        main_layout.add_widget(label1)
        main_layout.add_widget(layout1)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def next_window(self):
        global first_result
        first_result = self.first_result.text
        self.manager.current = "sits"

class SitsWindow(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        label1 = Label(text= txt_sits)
        self.button = Button(text='Продовжити')
        self.button.on_press = self.next_window
        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 30)
        main_layout.add_widget(label1)
        main_layout.add_widget(self.button)
        self.add_widget(main_layout)

    def next_window(self):
        self.manager.current = "second_pulse"

class InputPulseSecond(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        text = Label(text= txt_test3)

        second_result_label = Label(text= "Результат:")
        third_result_label = Label(text= "Результат після відпочінку:")
        self.second_result = TextInput(multiline = False)
        self.third_result = TextInput(multiline = False)
        self.button = Button(text= 'Продовжити')
        self.button.on_press = self.next_window

        layout_first_result = BoxLayout()
        layout_second_result = BoxLayout()
        layout_first_result.add_widget

        main_layout = BoxLayout(orientation = "vertical", padding = 20, spacing = 30)
        main_layout.add_widget(text)
        main_layout.add_widget(layout_first_result)
        main_layout.add_widget(layout_second_result)
        main_layout.add_widget(self.button)

        self.add_widget(main_layout)
    
    def next_window(self):
        global second_result, third_result
        second_result = self.second_result.text
        third_result = self.third_result.text
        self.manager.current = "result"

class result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.result = Label()
        self.on_enter =self.before

        self.add_widget(self.result)

    def before(self):
        self.result.text = f"{first_result} {second_result} {third_result}"

class Ruffier(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(MainWindow(name= "MainWindow"))
        sm.add_widget(InputPulseFirst(name= "first_pulse"))
        sm.add_widget(SitsWindow(name= "sits"))
        sm.add_widget(InputPulseSecond(name= "second_pulse"))
        sm.add_widget(result(name= "result"))
        return sm

ruffier = Ruffier()
ruffier.run()