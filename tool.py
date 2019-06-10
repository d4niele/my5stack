import uos
import machine
import network
import time

def mount_sd():
    uos.sdconfig(uos.SDMODE_SPI, clk=18, mosi=23, miso=19, cs=4)
    uos.mountsd()

def clear_ledbar():
    ledbar = machine.Neopixel(machine.Pin(15), 10)
    ledbar.clear()

def connect_wifi(ssid,password):
    n = network.WLAN(network.STA_IF)
    n.active(True)
    n.connect(ssid,password)
    time.sleep(5000)
    return n.ifconfig()
