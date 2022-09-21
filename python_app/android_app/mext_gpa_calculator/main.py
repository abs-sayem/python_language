import kivy
kivy.require('2.0.0')
from kivymd.app import App
from kivymd.uix.label import Label

class MextEGPA(App):
    def build(self):
        #return super().build()
        return(Label(text="MextEquavalentGPA"))

mext_egpa = MextEGPA()
mext_egpa.run()