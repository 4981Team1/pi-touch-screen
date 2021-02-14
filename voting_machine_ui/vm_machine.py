import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.bubble import Bubble, BubbleButton
from kivy.uix.screenmanager import ScreenManager, Screen
from functools import partial
from kivy.lang import Builder

import requests

import json

#Home Login/Pin Screen
#---------------------------------------
class VM_Home(Screen):
    pin = ObjectProperty(None)
    msg = ObjectProperty(None)
    def process_pin(self):
        #response = requests.get("http://good-team.herokuapp.com/ballots")
        #print(response.json())
        #print(response.status_code)
        
        checkPin = requests.get("http://good-team.herokuapp.com/voters/" + self.pin.text)
        
        #1 - TODO: DB Connection required here
        #Check whether the pin is valid
        if checkPin.status_code == 200:
            self.manager.current = "election_list"
        else:
            self.msg.text = "Pin " + self.pin.text + " is not accepted"
            self.pin.text = ""
            
#Elections List Screen
#---------------------------------------
class VM_Election_List(Screen):
    #2 - TODO: DB Connection required here
    #Get the list of allowed elections for the user
    def process_elec(self, *args):
        print(args[0])
        self.manager.current = "election_det"
        
    
    def on_enter(self):
        electionsStr = '{"num_elections": 3, "elections": {"election0": {"prompt":"desc1", "num_candidates": "2", "candidate_1": "1_A", "candidate_2": "1_B"}, "election1": {"prompt":"desc2", "num_candidates": "3", "candidate_1": "2_A", "candidate_2": "2_B", "candidate_3": "2_C"}, "election2": {"prompt": "desc3", "num_candidates": "4", "candidate_1": "3_A", "candidate_2": "3_B", "candidate_3": "3_C", "candidate_4": "3_D"}}}'
        electionsObj = json.loads(electionsStr)
        num_elec = electionsObj["num_elections"]
        for i in range(num_elec):
            button = Button(text=electionsObj["elections"]["election" + str(i)]["prompt"],
                            size_hint=(None, None),
                            size=(self.width, self.height / (num_elec)))
            button.bind(on_press=partial(self.process_elec, electionsObj["elections"]["election" + str(i)]))
            self.ids.grid.add_widget(button)
               

#Election Details Screen
#---------------------------------------
class VM_Election_Det(Screen):
    def tmp(self):
        print("Hi")

#Manager to handle all possible screens
#---------------------------------------
class WindowManager(ScreenManager):
    vm_home = ObjectProperty(None)
    vm_election_list = ObjectProperty(None)
    vm_election_det = ObjectProperty(None)

kv = Builder.load_file("vm_home.kv")

#Loads the Home Screen
#---------------------------------------
class VM_HomeApp(App):
    def build(self):
        return kv

if __name__ == "__main__":
    VM_HomeApp().run()