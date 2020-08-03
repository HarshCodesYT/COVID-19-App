from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

import requests
from bs4 import BeautifulSoup

class MyGrid(GridLayout):
    def __init__(self , **kwargs):
        super().__init__(**kwargs)

        self.cols = 1
        self.inside = GridLayout()
        self.inside.cols = 2

        self.inside.add_widget(Label(text='Country Name: '))
        self.country = TextInput(multiline=False)
        self.inside.add_widget(self.country)
        self.add_widget(self.inside)

        self.inside.add_widget(Label(text='Stats: '))
        self.stats = TextInput(multiline=False)
        self.inside.add_widget(self.stats)

        self.enter = Button(text='Enter' , font_size = 40)
        self.enter.bind(on_press=self.pressed)
        self.add_widget(self.enter)


    def pressed(self , instance):
        try:

            name = self.country.text
            name = str.casefold(name)
            if name == "united states of america":

                name = 'us'  
            if name == "usa":

                name = 'us' 

            if name == "united kingdom":
                name = 'uk'


            name = name.replace('.' , '')
            name = name.replace(' ' , '-') 


            url = ('https://www.worldometers.info/coronavirus/country/' + name + '/')

            d = requests.get(url)
            soup = BeautifulSoup(d.content , 'html.parser')
            number = soup.find_all(class_ = 'maincounter-number')   
            h = number[0].get_text()  
            i = number[1].get_text()
            j = number[2].get_text()

            statistics = self.stats.text = ('CoronaVirus Cases' + h + 'Deaths' + i + 'Recovered' + j)
        except:
            self.stats.text = 'No Data or Wrong Spelling'






class MyApp(App):
    def build(self):
        return MyGrid()

if __name__ == '__main__':
    MyApp().run()