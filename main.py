"""import pystray
import PIL.Image

image = PIL.Image.open("img/test.png")

def on_clicked(icon,item):
    if str(item) == "Say Hello":
        print("Hello World")
    elif str(item) == "Exit":
        icon.stop()

icon = pystray.Icon("Test", image,menu=pystray.Menu(
    pystray.MenuItem("Say Hello", on_clicked),
    pystray.MenuItem("Exit", on_clicked)
))

icon.run()"""
from datetime import datetime
import psutil

def vocal(text):
    print(text)
    pass
def inquire(pram, add=None):
    match pram:
        case 'weather':
            pass
        case "time":
            now = datetime.now()
            nd = {1: "st", 2: "nd", 3: "rd"}.get(int(now.strftime("%d")), "th")
            current_time = now.strftime(f"It is %H:%M on %B %d{nd} %Y ")
            vocal(current_time)
        case 'nav':
            pass
        case 'news':
            pass
        case 'search':
            pass
        case 'device':
            battery_status = psutil.sensors_battery()
            match battery_status.power_plugged:
                case True:
                    vocal("Device is plugged in and at " + str(battery_status.percent) + " percent")
                case False:
                    vocal("Device is at " + str(battery_status.percent) + " percent and has roughly " + str(round(((battery_status.secsleft/60)/60),2)) + " hours remaining")

inquire("time","yes")