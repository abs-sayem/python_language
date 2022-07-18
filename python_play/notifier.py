# To create a notification we need plyer. Install Plyer using "pip install plyer".
# Also we should know about the parameters of notifier-
#   title       : Title of the notifiction
#   message     : Message of the notification
#   app_name    : Name of the app launching the notifiction
#   app_icon    : Icon to be displayed along with the message
#   timeout     : Time to display the message, by default 10s
#   ticker      : Text to display on the statusbar as the notification arrives
#   toast       : Simple message instead of full nofocation

# Import Libraries
from socket import timeout
from plyer import notification

# Specify the parameters
title = "Notify Me"
message = "This is a notification created in Python"
notification.notify(title = title,
                    message = message,
                    app_name = "PyNotifier",
                    app_icon = None,
                    timeout = 5,
                    ticker = "Python Notifier",
                    toast = False)