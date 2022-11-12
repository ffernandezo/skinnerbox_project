from skinnerbox import *

# Programa para realizar pruebas de hardware

IN1.when_pressed = OUT1.pulse

IN1.when_released = OUT1.off

IN2.when_pressed = OUT2.blink

IN2.when_released = OUT2.off

IN3.when_pressed = K1.on

IN3.when_released = K1.off

IN4.when_pressed = K2.on

IN4.when_released = K2.off

pause()