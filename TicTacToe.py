from kivy.app import App
import random
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.modalview import ModalView
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.label import Label
from time import sleep

Config.set("graphics", "resizable", "0")
Config.set("graphics", "width", "300")
Config.set("graphics", "height", "300")


class MainApp(App):
    def __init__(self):
        super().__init__()
        self.switch = True

    def tic_tac_toe(self, arg):
        arg.disabled = True
        arg.text = 'X' if self.switch else 'O'
        self.switch = not self.switch
        if not self.switch:
            while True:
                ai_choise = random.randint(0, 99)
                if not self.buttons[ai_choise].disabled:
                    self.tic_tac_toe(self.buttons[ai_choise])
                    break

        coordinate = []
        for i in range(10):
            for j in range(6):
                coordH = (i*10+j, i*10+j+1, i*10+j+2, i*10+j+3, i*10+j+4)
                coordV = (j*10+i, (j+1)*10+i, (j+2)*10+i, (j+3)*10+i, (j+4)*10+i)
                coordinate.append(coordH)
                coordinate.append(coordV)
        for i in range(2, 8):
            for j in range(2, 8):
                coordD1 = ((i-2)*10+(j-2), (i-1)*10+(j-1), i*10+j, (i+1)*10+(j+1), (i+2)*10+(j+2))
                coordD2 = ((i-2)*10+(j+2), (i-1)*10+(j+1), i*10+j, (i+1)*10+(j-1), (i+2)*10+(j-2))
                coordinate.append(coordD1)
                coordinate.append(coordD2)

        vector = lambda item: [self.buttons[x].text for x in item]

        color = [1, 0, 0, 1]

        for item in coordinate:
            if vector(item).count('X') == 5 or vector(item).count('O') == 5:
                if vector(item).count('X') == 5:
                    winner = 'OS win!'
                else:
                    winner = 'You win!'
                for i in item:
                    self.buttons[i].color = color
                for button in self.buttons:
                    button.disabled = True
                popup = ModalView(size_hint=(0.75, 0.5))
                victory_label = Label(text=winner, font_size=50)
                popup.add_widget(victory_label)
                popup.bind(on_dismiss=self.restart)
                popup.open()
                break

    def restart(self, arg):
        self.switch = True

        for button in self.buttons:
            button.text = ""
            button.disabled = False

    def build(self):
        self.title = "Tic-Tac-Toe"

        root = BoxLayout(orientation="vertical", padding=5)

        grid = GridLayout(cols=10)
        self.buttons = []
        for _ in range(100):
            button = Button(
                background_color=(1, 1, 1, 1),
                font_size=24,
                disabled=False,
                on_press=self.tic_tac_toe
            )
            self.buttons.append(button)
            grid.add_widget(button)

        root.add_widget(grid)

        root.add_widget(
            Button(
               text="Restart",
               size_hint=[1, .1],
               on_press=self.restart
            )
        )

        return root


if __name__ == "__main__":
    MainApp().run()