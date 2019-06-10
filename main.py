from m5stack import *
from m5ui import *
import tool
import json

def buttonC_wasPressed():
  import wakeonlan
  with open('/sd/config.json') as json_file:  
    data = json.load(json_file)
    for p in data["hosts"]:
        h = data["hosts"][p]
        wakeonlan.wake(h["mac_address"])
buttonC.wasPressed(buttonC_wasPressed)

tool.mount_sd()
with open('/sd/config.json') as json_file:  
    data = json.load(json_file)
    for p in data["hosts"]:
        h = data["hosts"][p]
        print(h["mac_address"])
    n = tool.connect_wifi(data["wifi"]["SSID"],data["wifi"]["password"])

w = M5TextBox(208, 204, "wakeonlan", lcd.FONT_Default,0xFFFFFF, rotate=0)
