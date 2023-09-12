##

from guizero import App, Text, PushButton, ButtonGroup, Combo, TextBox, Picture

##

def merge():
    output_text1.value = bgroup1.value + other1.value + other2.value
####

##

app1 = App(title="string-joiner", width=300, height=350)
bgroup1 = ButtonGroup(app1, options=["1", "2", "3", "4", "5"], selected="1")
other1 = Combo(app1, options=["hello", "no", "yes", "goodbye"], selected="hello")
other2 = Combo(app1, options=["a", "b", "c", "d"], selected="a")

output_button1 = PushButton(app1, text="joinstr", command=merge)
output_text1 = Text(app1, text="OUTPUT")

picture = Picture(app1, image="mountain.jpg", width=300, height= 250)

app1.display()

##