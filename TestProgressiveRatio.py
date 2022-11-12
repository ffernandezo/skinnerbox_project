from skinnerbox import *
log = LogFile("logPR.txt")

# Test de razón progresiva
# Al iniciar el programa, se enciende la luz izquierda de estimulo.
# El roedor debera presionar la palanca para obtener una recompensa
# y se añadirá una unidad al numero de veces que deber presionar la palanca
# para obtener otra recompensa.

palancaIz=IN1
palancaDer=IN2
luz_estimulo=OUT1
reward=OUT3

pgratio = 1         # Numero inicial de respuestas requeridas
duracion_exp = 120  # Duración del experimento (segundos)
cnt_incorrectas = 0 # Contador de respuestas incorrectas
cnt_correctas = 0   # Contador de respuestas correctas
cnt = 0             # Contador de razón

def incorrecta():
    global cnt_incorrectas
    cnt_incorrectas += 1
    log.log_event("Respuesta incorrecta")

def correcta():
    global cnt_correctas
    cnt_correctas += 1
    log.log_event("Respuesta correcta")

def recompensa():
    reward.blink(on_time=1,n=1)
    log.log_event("Recompensa")
    luz_estimulo.off()
    sleep(2)
    
def cierre():
    print("Cerrando experimento")
    log.log_event("Fin de experimento\n"+"correctas: "+cnt_correctas+" incorrectas: "+cnt_incorrectas)
    shut_down()

t = Timer(duracion_exp, cierre)
t.start()

palancaDer.when_pressed = incorrecta
palancaIz.when_pressed = correcta 
          
while True:
    luz_estimulo.on()
    if cnt == pgratio:
        recompensa()
        pgratio += 1
        cnt = 0