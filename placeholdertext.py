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
