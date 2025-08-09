# напиши модуль для роботи з анімацією
from kivy.uix.boxlayout import BoxLayout
from kivy.animation import Animation
from kivy.uix.button import Button
from kivy.properties import NumericProperty, BooleanPropety

class Runner(BoxLayout):
    value = NumericProperty
    finished = BooleanPropety(False)
    def __init__(self, total, **kwargs):
        self.total = total
        self.animation = (Animation(pos_hint={'top': 0.1},duration=0.75) +
                          Animation(pos_hint={'top': 0.1},duration=0.75))
        self.animation.repeat = True
        self.animation.on_progress = self.total
        self.button = Button(size_hint = (1, 0.1), pos_hint ={'top': 1}), background_color=(55/255,255/255,155/255,1)
        self.add_widget(self.button)

    def start(self):
        self.value = 0
        self.finished = False
        self.animation.repeat = True
        self.animation.start(self.button)

    def next(self, widget, step):
        self.value += 1
        if self.button >= self.total:
            self.animation.repeat = False
            self.finished = True