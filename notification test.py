pip install win10toast
from win10toast import ToastNotifier
toast = ToastNotifier()
toast.show_toast("Notification","You have an event!",duration=20,icon_path="icon.ico")
