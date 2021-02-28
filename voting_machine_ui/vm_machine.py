import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
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

API_URL = "http://good-team.herokuapp.com"

#Home Login/Pin Screen
#---------------------------------------
class VM_Home(Screen):
    pin = ObjectProperty(None)
    msg = ObjectProperty(None)
    def process_pin(self):
        #response = requests.get("http://good-team.herokuapp.com/ballots")
        #print(response.json())
        #print(response.status_code)
        #self.pin.text = "60234cec2a45ae3eec0a77bf"
        checkPin = requests.get(API_URL + "/voters/" + self.pin.text)

        if checkPin.status_code == 200:
            self.manager.current = "election_list"
            pin = checkPin
        else:
            self.msg.text = "Pin\n" + self.pin.text + "\nis not accepted"
            self.pin.text = ""
            
#Elections List Screen
#---------------------------------------
class VM_Election_List(Screen):
    #2 - TODO: DB Connection required here
    #Get the list of allowed elections for the user
    def process_elec(self, *args):
        print(args[0])
        self.manager.current = "election_det"
    
    def backBtn(self, instance):
        self.manager.screens[0].ids.pin.text = ""
        self.ids.grid.clear_widgets()
        self.manager.current = "election_home"
    
    def on_enter(self):
        pin = self.manager.screens[0].ids.pin.text
        
        titleLbl = Label(text="Eligible Elections",
                      font_size='30sp',
                      size_hint=(None,None),
                      size=(self.width, self.height/8))
        self.ids.grid.add_widget(titleLbl)
        
        election_list = requests.get(API_URL + "/eligible/" + pin)
        if election_list.status_code == 200:
            electionsStr = election_list.json()
            for i in range(len(electionsStr)):
                button = Button(text="electionId" + str(i) + ":" + electionsStr[i],
                                size_hint=(None, None),
                                size=(self.width, self.height/4))
                button.bind(on_press=partial(self.process_elec, electionsStr[i]))
                self.ids.grid.add_widget(button)
        
        #below code is just to place the finish button on the far bottom right of the grid
        padLbl = Label(text="",
                       size_hint=(None,None),
                       size=(self.width, self.height/16))
        self.ids.grid.add_widget(padLbl)
    
        tmpGridLayout = GridLayout(cols=4)
        
        padLbl = Label(text="",
                       size_hint=(None,None),
                       size=(self.width/4, self.height/8))
        tmpGridLayout.add_widget(padLbl)
        padLbl = Label(text="",
                       size_hint=(None,None),
                       size=(self.width/4, self.height/8))
        tmpGridLayout.add_widget(padLbl)
        padLbl = Label(text="",
                       size_hint=(None,None),
                       size=(self.width/4, self.height/8))
        tmpGridLayout.add_widget(padLbl)
        
        finishBtn = Button(text="Finish",
                           size_hint=(None,None),
                           size=(self.width/4, self.height/8))
        finishBtn.bind(on_press=self.backBtn)
        tmpGridLayout.add_widget(finishBtn)
        self.ids.grid.add_widget(tmpGridLayout)
        
        #else:
        
        #electionsStr = '{"num_elections": 3, "elections": {"election0": {"prompt":"desc1", "num_candidates": "2", "candidate_1": "1_A", "candidate_2": "1_B"}, "election1": {"prompt":"desc2", "num_candidates": "3", "candidate_1": "2_A", "candidate_2": "2_B", "candidate_3": "2_C"}, "election2": {"prompt": "desc3", "num_candidates": "4", "candidate_1": "3_A", "candidate_2": "3_B", "candidate_3": "3_C", "candidate_4": "3_D"}}}'
        #electionsObj = json.loads(electionsStr)
        #num_elec = electionsObj["num_elections"]
        #for i in range(num_elec):
            #button = Button(text=electionsObj["elections"]["election" + str(i)]["prompt"],
            #                size_hint=(None, None),
            #                size=(self.width, self.height / (num_elec)))
            #button.bind(on_press=partial(self.process_elec, electionsObj["elections"]["election" + str(i)]))
            #self.ids.grid.add_widget(button)
               

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