##

from guizero import App, Text, PushButton, ButtonGroup, Combo, TextBox, Picture, Box

##


##

app1 = App(title="title1", width=300, height=300)
box1 = Box(app1, width="fill", height=int(app1.height/2))
box2 = Box(app1, width="fill", height=int(app1.height/2))
box1.bg = "light blue"
box2.bg = "dark blue"
txt1 = Text(box1, text="hello")

app1.display()

##