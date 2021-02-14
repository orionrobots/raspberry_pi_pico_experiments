import machine
import utime
import random

led_external = machine.Pin(15, machine.Pin.OUT)
buzzer = machine.Pin(13, machine.Pin.OUT)
button = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
pwm = machine.PWM(buzzer)
pwm.freq(3000)

B0  = 31
C1  = 33
CS1 = 35
D1  = 37
DS1 = 39
E1  = 41
F1  = 44
FS1 = 46
G1  = 49
GS1 = 52
A1  = 55
AS1 = 58
B1  = 62
C2  = 65
CS2 = 69
D2  = 73
DS2 = 78
E2  = 82
F2  = 87
FS2 = 93
G2  = 98
GS2 = 104
A2  = 110
AS2 = 117
B2  = 123
C3  = 131
CS3 = 139
D3  = 147
DS3 = 156
E3  = 165
F3  = 175
FS3 = 185
G3  = 196
GS3 = 208
A3  = 220
AS3 = 233
B3  = 247
C4  = 262
C7  = 2093
CS7 = 2217
D7  = 2349
DS7 = 2489
E7  = 2637
F7  = 2794
FS7 = 2960
G7  = 3136
GS7 = 3322
A7  = 3520
AS7 = 3729
B7  = 3951

def tune():
    notes = [C7, CS7, E7, G7, E7]
    for note in notes:
        pwm.freq(note)
        utime.sleep(0.25)

def siren():
    for n in range(C3, C7, 50):
        pwm.freq(n)
        utime.sleep(0.005)
        
def siren2():
    for n in range(C7, C3, -25):
        pwm.freq(n)
        utime.sleep(0.005)

def low():
    notes = [FS2, FS1, FS2, FS1]
    for note in notes:
        pwm.freq(note)
        utime.sleep(0.5)
        
def white_noise():
    for n in range(100):
        pwm.freq(random.randint(50, 3000))
        utime.sleep(0.001)
    
noises = [(tune, 1), (siren, 20), (siren2, 10), (low,2), (white_noise, 4)]

while True:
    if button.value() == 1:
        led_external.value(1)
        pwm.duty_u16(32768)
        noise, max_rep = random.choice(noises)
        for n in range(random.randint(1, max_rep)):
            noise()
        #white_noise()
        pwm.duty_u16(0)
        led_external.value(0)
