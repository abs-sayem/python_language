import kivy
#kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout

class MextEGPA(App):
    def build(self):
        #return super().build()
        return(BoxLayout())

mext_egpa = MextEGPA()
mext_egpa.run()