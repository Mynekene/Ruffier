# напиши модуль для підрахунку кількості присідань
from kivy.uix.label import Label
from kivy.clock import Clock

class Sits(Label):
    
    def __init__(self, total, **kwargs):
        self.total = total
        self.current = 0
        my_text = f'залишилось {self.total}'
        super().__init__(self= my_text, **kwargs)

    def next(self, *args):
        self.current += 1
        tmp = self.total - self.current
        my_text = f'Залишилось {tmp}'
        self.text = my_text