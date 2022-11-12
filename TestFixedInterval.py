from skinnerbox import *
log = LogFile("logFI.txt")

# Test de intervalo fijo
# Al iniciar el programa, se enciende la luz izquierda (estimulo).
# El roedor debera presionar la palanca para iniciar un contador de tiempo
# que al finalizar le otorgará una recompensa. Mientras se espera el tiempo
# se guarda cada activacion de las palancas.

palancaIz=IN1
palancaDer=IN2
ledIz=OUT1
ledDer=OUT2
reward=OUT3

intervalo = 5       # Tiempo a esperar entre respuesta correcta y recompensa
duracionExp = 120   # Duración del experimento (segundos)
cnt_incorrectas = 0 # Contador de respuestas incorrectas
cnt_correctas = 0   # Contador de respuestas correctas

def incorrecta():
    global cnt_incorrectas
    cnt_incorrectas += 1
    log.log_event("Respuesta incorrecta ")

def correcta():
    global cnt_correctas
    cnt_correctas += 1
    log.log_event("Respuesta correcta ")
    
def cierre():
    print("Cerrando experimento")
    log.log_event("Fin de experimento\n"+"correctas: "+cnt_correctas+" incorrectas: "+cnt_incorrectas)
    shut_down()
    
def recompensa():
    ledIz.off()
    reward.blink(on_time=1,n=1)
    log.log_event("Recompensa")
    

t = Timer(duracionExp, cierre)
t.start()

palancaDer.when_pressed = incorrecta
palancaIz.when_pressed = correcta
          
while True:
    ledIz.on()
    palancaIz.wait_for_press()
    sleep(intervalo)
    recompensa()