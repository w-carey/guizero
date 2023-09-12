##

from guizero import App, TextBox, PushButton, Box, Combo, MenuBar, Text

##

def open_file():
    nameTextBox.value = mainApp.select_file()
    with open(nameTextBox.value, "r") as file:
        editor.value = file.read()
    ####
####

def save_file():
    with open(nameTextBox.value, "w") as file:
        file.write(editor.value)
    ####
####

def changeFont():
    for item in [nameTextBox, editor, font]:
        item.font = font.value
    ####
    editor.text_size = fontsize.value
    editor.resize(1, 1)
    editor.resize("fill", "fill")
    ####
####

##

mainApp = App(title="textEditor", width=500, height=500)
menubar = MenuBar(mainApp, toplevel=["File"],options=[
    [["Open", open_file], ["Save", save_file]] # FILE
])
controlsBox = Box(mainApp, align="top", width="fill")
nameTextBox = Text(controlsBox, text="text_file.txt", width="fill", height="fill", align="left")
editor = TextBox(mainApp, width="fill", height="fill", text="", multiline=True)
accessBox = Box(mainApp, align="bottom")
font = Combo(accessBox, options=["courier", "times new roman", "verdana"], align="left", command=changeFont)
fontsize = Combo(accessBox, options=[10, 30, 60, 100], align="right", command=changeFont)
changeFont()
mainApp.display()

##
