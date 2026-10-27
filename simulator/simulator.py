import json
import os
import random
import time
from datetime import datetime

import paho.mqtt.client as mqtt

HOST = os.getenv("MQTT_HOST", "localhost")
PORT = int(os.getenv("MQTT_PORT", "1883"))
ID = os.getenv("EQUIPAMENTO_ID", "CNC-01")
INTERVALO = int(os.getenv("INTERVALO_SEGUNDOS", "10"))
TOPICO = f"industria/{ID}/telemetria"

cliente = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="simulador-industria")

while True:
    try:
        print(f"Conectando ao broker MQTT em {HOST}:{PORT}...")
        cliente.connect(HOST, PORT, 60)
        break
    except Exception as erro:
        print(f"Broker ainda indisponível: {erro}. Nova tentativa em 3 segundos.")
        time.sleep(3)

cliente.loop_start()
try:
    while True:
        dados = {
            "temperatura": round(random.uniform(32.0, 50.0), 1),
            "vibracao": round(random.uniform(1.0, 4.5), 1),
            "status": random.choice(["Operacional", "Operacional", "Atenção simulada"]),
            "gerado_em": datetime.now().strftime("%H:%M:%S"),
            "dados_didaticos": True
        }
        resultado = cliente.publish(TOPICO, json.dumps(dados), qos=0)
        resultado.wait_for_publish()
        print(f"Publicado em {TOPICO}: {dados}")
        time.sleep(INTERVALO)
except KeyboardInterrupt:
    print("Simulador encerrado.")
finally:
    cliente.loop_stop()
    cliente.disconnect()
