##

from guizero import App, TextBox, PushButton, Text, info

##

def button1_clicked():
    info("HELLO", textbox1.value)
    exit()
####

def textbox1_highlight_lowlight():
    if textbox1.bg == "light blue":
        textbox1.bg = None
        return
    ####
    textbox1.bg = "light blue"
####

##

app1 = App(title="test gui")
question1 = Text(app1, text="Hello. What's your name?")
textbox1 = TextBox(app1)
button1 = PushButton(app1, command = button1_clicked, text = "Done")

textbox1.when_mouse_enters = textbox1_highlight_lowlight
textbox1.when_mouse_leaves = textbox1_highlight_lowlight
app1.display()

##