import os
import time
import paho.mqtt.client as mqtt

TOPICO = "industria-ra-cloud/torno/monitoramento"

BROKER = os.getenv("MQTT_BROKER", "localhost")

conectado = False


def quando_conectar(client, userdata, flags, reason_code, properties):
    global conectado

    print("================================")
    print("SIMULADOR CONECTADO AO MQTT!")
    print("Código:", reason_code)
    print("================================")

    conectado = True


cliente = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

cliente.on_connect = quando_conectar

print("Conectando ao MQTT:", BROKER)

cliente.connect(
    BROKER,
    1883,
    60
)

cliente.loop_start()

print("Aguardando conexão...")

while not conectado:
    time.sleep(1)

print("Simulador iniciado!")
print("Tópico:", TOPICO)

while True:

    cliente.publish(
        TOPICO,
        "alerta"
    )

    print("Enviado: alerta")

    time.sleep(5)

    cliente.publish(
        TOPICO,
        "normal"
    )

    print("Enviado: normal")

    time.sleep(5)