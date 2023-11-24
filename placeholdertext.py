def placeholdertextbox(textbox, event, placeholder, password):
    # This procedure, creates the placeholder text for buttons, makes it easier to see what the textbox is meant to contain
    if event == "<FocusIn event>":
        if textbox.value == placeholder:
            textbox.value = ""
            textbox.text_color = "black"
            textbox.tk.config(font=('Calibri', 14))
            textbox.hide_text = password
        ####
    elif event == "<FocusOut event>":
        if textbox.value == "":
            textbox.value = placeholder
            textbox.text_color = "dark grey"
            textbox.tk.config(font=('Calibri', 14, "italic"))
            textbox.hide_text = False
        ####
    elif event == "reset":
        textbox.value = placeholder
        textbox.text_color = "dark grey"
        textbox.tk.config(font=('Calibri', 14, "italic"))
        textbox.hide_text = False
    ####
####
SIGNUPforenameBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPforenameBox, str(type), PLACEHOLDERforename, False))
SIGNUPforenameBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPforenameBox, str(type), PLACEHOLDERforename, False))
SIGNUPsurnameBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPsurnameBox, str(type), PLACEHOLDERsurname, False))
SIGNUPsurnameBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPsurnameBox, str(type), PLACEHOLDERsurname, False))
SIGNUPusernameBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPusernameBox, str(type), PLACEHOLDERrusername, False))
SIGNUPusernameBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPusernameBox, str(type), PLACEHOLDERrusername, False))
SIGNUPpasswordBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPpasswordBox, str(type), PLACEHOLDERpassword, True))
SIGNUPpasswordBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPpasswordBox, str(type), PLACEHOLDERpassword, True))
SIGNUPconfirmpasswordBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPconfirmpasswordBox, str(type), PLACEHOLDERconfirmpassword, True))
SIGNUPconfirmpasswordBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPconfirmpasswordBox, str(type), PLACEHOLDERconfirmpassword, True))
SIGNUPemailBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPemailBox, str(type), PLACEHOLDERemail, False))
SIGNUPemailBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPemailBox, str(type), PLACEHOLDERemail, False))
SIGNUPmobilenumberBox.tk.bind("<FocusIn>", lambda type: placeholdertextbox(SIGNUPmobilenumberBox, str(type), PLACEHOLDERmobile, False))
SIGNUPmobilenumberBox.tk.bind("<FocusOut>", lambda type: placeholdertextbox(SIGNUPmobilenumberBox, str(type), PLACEHOLDERmobile, False))
