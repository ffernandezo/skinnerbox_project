from gpiozero import Button,PWMOutputDevice,DigitalOutputDevice
import  os, psutil
    
pwmFreq = 1000
# Asignación de entradas/salidas al gpio de la raspberry
IN1=Button(21)
IN2=Button(26)
IN3=Button(20)
IN4=Button(19)
IN5=Button(16)
IN6=Button(13)
IN7=Button(12)
IN8=Button(6)
BUTTON=Button(5, bounce_time=0.15)
OUT1=PWMOutputDevice(25,frequency=pwmFreq)
OUT2=PWMOutputDevice(9,frequency=pwmFreq)
OUT3=PWMOutputDevice(10,frequency=pwmFreq)
OUT4=PWMOutputDevice(24,frequency=pwmFreq)
OUT5=PWMOutputDevice(23,frequency=pwmFreq)
OUT6=PWMOutputDevice(22,frequency=pwmFreq)
OUT7=PWMOutputDevice(27,frequency=pwmFreq)
OUT8=PWMOutputDevice(18,frequency=pwmFreq)
# Salidas auxiliares (relés)
K1=DigitalOutputDevice(2, active_high=False)
K2=DigitalOutputDevice(3, active_high=False)
K3=DigitalOutputDevice(4, active_high=False)
K4=DigitalOutputDevice(17, active_high=False)


""" Raspberry PI GPIO
  3V3  (1) (2)  5V
 GPIO2  (3) (4)  5V
 GPIO3  (5) (6)  GND
 GPIO4  (7) (8)  GPIO14
   GND  (9) (10) GPIO15
GPIO17 (11) (12) GPIO18
GPIO27 (13) (14) GND
GPIO22 (15) (16) GPIO23
   3V3 (17) (18) GPIO24
GPIO10 (19) (20) GND
 GPIO9 (21) (22) GPIO25
GPIO11 (23) (24) GPIO8
   GND (25) (26) GPIO7
 GPIO0 (27) (28) GPIO1
 GPIO5 (29) (30) GND
 GPIO6 (31) (32) GPIO12
GPIO13 (33) (34) GND
GPIO19 (35) (36) GPIO16
GPIO26 (37) (38) GPIO20
   GND (39) (40) GPIO21
"""

def close_all():
    IN1.close()
    IN2.close()
    IN3.close()
    IN4.close()
    IN5.close()
    IN6.close()
    IN7.close()
    IN8.close()
    OUT1.close()
    OUT2.close()
    OUT3.close()
    OUT4.close()
    OUT5.close()
    OUT6.close()
    OUT7.close()
    OUT8.close()
    K1.close()
    K2.close()
    K3.close()
    K4.close()

def shut_down():
    close_all()
    current_system_pid = os.getpid()
    ThisSystem = psutil.Process(current_system_pid)
    ThisSystem.terminate()