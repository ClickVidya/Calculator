from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
import pygame
import os, sys

# This is mapped to a widget in .kv file 
class CalculatorScreen(Screen):
    def update_input(self, text):
        self.ids.exp_input.text += text

    def clear(self):
        self.ids.exp_input.text = ""

    def clear_last_character(self):
        length = len(self.ids.exp_input.text)
        self.ids.exp_input.text = self.ids.exp_input.text[0:length-1]
   
    def calculate(self):
        expression = self.ids.exp_input.text
        result = eval(expression)
        self.ids.exp_input.text = str(result)
        
        history_screen = self.manager.get_screen("history")

        history = history_screen.ids.history_label.text
        history += "\n"
        history += f"{expression} = {result}"
        history_screen.ids.history_label.text = history


class HistoryScreen(Screen):
    def clear_history(self):
        self.ids.history_label.text = ""

class AppScreen(ScreenManager):
    def toggle_screen(self):
        """Switch between calculator <-> history"""
        if self.current == "calculator":
            self.current = "history"
        else:
            self.current = "calculator"       


class CalculatorApp(App):
    def build(self):
        pygame.mixer.init()
        sm = AppScreen()
        sm.current = "calculator"
        return sm

if __name__ == '__main__':
    CalculatorApp().run()

