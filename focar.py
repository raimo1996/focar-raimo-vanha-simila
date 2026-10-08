#focarin fuktiot 
#Raimo Vanha-Similä

#nopeudet
#25% 16383
#50% 32767
#75% 49181
#100% 65535

from machine import Pin, PWM
from time import sleep
#luodaan led olio
led=Pin("LED",Pin.OUT)
# Moottori A
e1 = PWM(Pin(28))
m1 = Pin(27, Pin.OUT)

# Moottori B
e2 = PWM(Pin(26))
m2 = Pin(22, Pin.OUT)

# Aseta PWM-taajuus 1000 Hz
e1.freq(1000)
e2.freq(1000)


#1 eteenpäin funktio 50% teho ja 2s oletusarvot
def eteenpain(nopeus= 32767, aika= 2):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)


#2 taaksepäin funktio 50% teho ja 2s oletusarvot
def taaksepain(nopeus= 32767,aika= 2):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)


#3 vasemalle käännös funktio oikean pyörän oletusarvo 75% ja
# vasen 25% teholla ja 1.5 sekunttia
def vasen(nopeus1=49181,nopeus2=16383,aika=1.5):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus1)
    e2.duty_u16(nopeus2)
    sleep(aika)


#4 oikea käännös funktio  vasemman pyörän oletusarvo 75% ja
# oikea 25% teholla ja 1.5 sekunttia
def oikea(nopeus1=49181,nopeus2=16383,aika=1.5):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus2)
    e2.duty_u16(nopeus1)
    sleep(aika)


#paikallaan kääntymien 180 astetta 50% molemmat pyörät erisuuntiin
# 2 sekunttia oletus arvona
def paikallaan(nopeus=32767,aika=2):
    e1.duty_u16(0)
    e2.duty_u16(0)
#  Odota yksi sekunti moottoreiden pysähtymistä
    sleep(1)
    m1.value(1)
    m2.value(0)
    e1.duty_u16(nopeus)
    e2.duty_u16(nopeus)
    sleep(aika)

#pysähdys fuktio
def pysahdys():
    e1.duty_u16(0)
    e2.duty_u16(0)
    #  Odota yksi sekunti moottoreiden pysähtymistä
    sleep(1)

#käännytään tiukasti vasemmalle 90 astetta
def tiukkavasen(nopeus1=32767, nopeus2= 0,aika=1.5):
    m1.value(1)
    m2.value(1)
    e1.duty_u16(nopeus2)
    e2.duty_u16(nopeus1)
    sleep(aika)

#pakilla käännytään vasemalle
def pvasen(nopeus1=0, nopeus2= 32767,aika=1.5):
    m1.value(0)
    m2.value(0)
    e1.duty_u16(nopeus2)
    e2.duty_u16(nopeus1)
    sleep(aika)

#ledi päälle ja pois 1 sekuntti
def ledi(aika=1):
    led.on()
    sleep(aika)
    led.off()
    sleep(aika)
