##

from guizero import Box, Text, PushButton, TextBox, MenuBar, App

##


##

mainApp = App(title="menubar-test")
menuOpt1 = MenuBar(mainApp, toplevel=["File", "Edit"],options=[
    [["File option 1", None]], # FILE
    [["Edit option 1", None]]  # EDIT
])

mainApp.display()

##
