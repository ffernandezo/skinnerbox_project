from skinnerbox import *

log = LogFile("logFR.txt")

# Test de razón fija
# Al iniciar el programa, se enciende la luz de estimulo.
# El roedor debera presionar la palanca durante determinada cantidad de
# veces para obtener una recompensa.

palancaIz=IN1
palancaDer=IN2
luz_estimulo=OUT1
reward=OUT3

fixedratio=5        # Razón fija
duracion_exp = 120  # Duración del experimento (segundos)

cnt_incorrectas = 0 # Contador de respuestas incorrectas
cnt_correctas = 0   # Contador de respuestas correctas
cnt=0               # Contador de razon

def incorrecta():
    global cnt_incorrectas
    cnt_incorrectas += 1
    log.log_event("Respuesta incorrecta")

def correcta():
    global cnt_correctas
    global cnt
    cnt_correctas += 1
    cnt += 1
    log.log_event("Respuesta correcta")
    
def recompensa():
    luz_estimulo.off()
    reward.blink(on_time=1,n=1)
    log.log_event("Recompensa")

def apagado():
    print("Cerrando experimento")
    log.log_event("Fin de experimento\n"+"correctas: "+cnt_correctas+" incorrectas: "+cnt_incorrectas)
    shut_down()

t = Timer(duracion_exp, apagado)
t.start()

palancaDer.when_pressed = incorrecta
palancaIz.when_pressed = correcta

while True:
    luz_estimulo.on()
    if cnt == fixedratio:
        recompensa()
        cnt=0
        