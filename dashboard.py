showOnly([booktickets], [orderhistory, helpfeedback, accountsettings])
MAINMENUbookTicketsButton = PushButton(MAINMENUbookTicketsButtonBox, width=17, height="fill", align="left", text="BOOK TICKETS", command=lambda:sortOutButtonColour(MAINMENUbookTicketsButton,MAINMENUbookticketsButtonConnection,showOnly([booktickets], [orderhistory, helpfeedback, accountsettings, bookticketserrortext])))
MAINMENUbookTicketsButton.bg = "light grey"
MAINMENUorderHistoryButton = PushButton(MAINMENUorderHistoryButtonBox, width=17, height="fill", align="left", text="ORDER HISTORY", command=lambda:[sortOutButtonColour(MAINMENUorderHistoryButton,MAINMENUorderHistoryButtonConnection,showOnly([orderhistory], [booktickets, helpfeedback, accountsettings])), viewbookings()])
MAINMENUorderHistoryButton.bg = "light grey"
MAINMENUhelpFeedbackButton = PushButton(MAINMENUhelpFeedbackButtonBox, width=17, height="fill", align="left", text="ACCESSIBILITY/FEEDBACK", command=lambda:sortOutButtonColour(MAINMENUhelpFeedbackButton,MAINMENUhelpFeedbackButtonConnection,showOnly([helpfeedback], [orderhistory, booktickets, accountsettings])))
MAINMENUhelpFeedbackButton.bg = "light grey"
MAINMENUaccountSettingsButton = PushButton(MAINMENUaccountSettngsButtonBox, width=17, height="fill", align="left", text="ACCOUNT SETTINGS", command=lambda:[sortOutButtonColour(MAINMENUaccountSettingsButton,MAINMENUaccountSettingsButtonConnection,showOnly([accountsettings], [orderhistory, helpfeedback, booktickets, accountchangepassworderror, ACCOUNTphoneemailerror])), emailphone()])
MAINMENUaccountSettingsButton.bg = "light grey"
MAINMENUsignOutButton = PushButton(MAINMENUsignOutButtonBox, width=17, height="fill", align="left", text="SIGN OUT", command=lambda:showOnly([LOGINForm], [MAINMENUForm]))
MAINMENUsignOutButton.bg = "light grey"
MAINMENUbookticketsButtonConnection = Box(MAINMENUbookTicketsButtonBox, width="fill", height=10, align="right")
MAINMENUbookticketsButtonConnection.bg = "#FF973D"
MAINMENUorderHistoryButtonConnection = Box(MAINMENUorderHistoryButtonBox, width="fill", height=10, align="right")
MAINMENUorderHistoryButtonConnection.bg = "#FF973D"
MAINMENUhelpFeedbackButtonConnection = Box(MAINMENUhelpFeedbackButtonBox, width="fill", height=10, align="right")
MAINMENUhelpFeedbackButtonConnection.bg = "#FF973D"
MAINMENUaccountSettingsButtonConnection = Box(MAINMENUaccountSettngsButtonBox, width="fill", height=10, align="right")
MAINMENUaccountSettingsButtonConnection.bg = "#FF973D"
sortOutButtonColour(MAINMENUbookTicketsButton, MAINMENUbookticketsButtonConnection, None)
