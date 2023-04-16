#$buildozer init == File buildozer.spec created,ready to customize!
#$buildozer android debug or $buildozer android release
# author = VVICTORIOUS© Copyright Info
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class Hello(App):
    def build(self):
        self.windows = GridLayout()
        self.windows.cols = 1 #number of grids by column
        #add widgets to windows(self.windows.add_widget())
        self.windows.size_hint = (0.6, 0.7)
        self.windows.pos_hint = {'center_x' : 0.5, 'center_y' : 0.5}

        #Image widget
        self.windows.add_widget(Image(source='1.JPG'))
        
        #Label widget
        self.greeting = Label(
            text='What is your name ?',
            font_size= 20
            )
        
        #adding Label widget to the list of widgets
        self.windows.add_widget(self.greeting)

        #text input widget
        self.user = TextInput(
            multiline=False,
            padding_y = (20,20),#Distance between inputted text\
                                #and the allocated border(up & down)
            size_hint = (1,0.5),
            padding_x = (20,30)#Distance between inputted text\
                                #and the allocated border(left & right)
            )
        self.windows.add_widget(self.user)

        #button widget
        self.button = Button(
            text='GREET',
            size_hint = (1,0.5),#reducing the height by half with 0.5
            bold = True,
            background_color = '#cece00'
            )
        self.button.bind(on_press=self.callback)
        self.windows.add_widget(self.button)

        return self.windows


    def callback(self, instance):
        self.greeting.text = 'Hey ' + self.user.text + '!'


if __name__ == '__main__':
    Hello().run()
