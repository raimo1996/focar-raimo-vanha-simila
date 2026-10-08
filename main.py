# focar 3 pisteen käännös
#Raimo Vanha-Similä

#tuodaan tarvittavia asioita ja fuktioita
from machine import Pin, PWM
from time import sleep
from focar import eteenpain
from focar import pysahdys
from focar import tiukkavasen
from focar import pvasen
from focar import ledi

# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)

#odotetaan 10 sekunttia
sleep(10)

#ledin vilkutus
ledi()

#eteenpäin 1m
eteenpain(aika=4)

#pysähdytään
pysahdys()

#käännös vasempaan 90 astetta
tiukkavasen()

#pysähdytään
pysahdys()

#pakitetaan 90 astetta vasemalle
pvasen()

#eteenpäin 1m 
eteenpain(aika=4)

#pysähdytään
pysahdys()

