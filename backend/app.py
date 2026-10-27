import json
import os
from datetime import datetime
from threading import Lock

import paho.mqtt.client as mqtt
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

EQUIPAMENTO_ID = os.getenv("EQUIPAMENTO_ID", "CNC-01")
MQTT_HOST = os.getenv("MQTT_HOST", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", "1883"))
TOPICO = f"industria/{EQUIPAMENTO_ID}/telemetria"

lock = Lock()
telemetria = {
    "temperatura": 35.0,
    "vibracao": 2.1,
    "status": "Operacional",
    "atualizacao": datetime.now().strftime("%H:%M:%S"),
    "origem": "valor inicial didático"
}


def ao_conectar(cliente, userdata, flags, reason_code, properties):
    print(f"MQTT conectado: {reason_code}")
    cliente.subscribe(TOPICO)
    print(f"Inscrito no tópico: {TOPICO}")


def ao_receber(cliente, userdata, mensagem):
    global telemetria
    try:
        dados = json.loads(mensagem.payload.decode("utf-8"))
        with lock:
            telemetria = {
                "temperatura": float(dados["temperatura"]),
                "vibracao": float(dados["vibracao"]),
                "status": str(dados["status"]),
                "atualizacao": datetime.now().strftime("%H:%M:%S"),
                "origem": "MQTT (simulado)"
            }
        print(f"Telemetria atualizada: {telemetria}")
    except (ValueError, KeyError, json.JSONDecodeError) as erro:
        print(f"Mensagem MQTT ignorada: {erro}")


cliente_mqtt = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id="api-flask-industria")
cliente_mqtt.on_connect = ao_conectar
cliente_mqtt.on_message = ao_receber


def conectar_mqtt():
    try:
        cliente_mqtt.connect(MQTT_HOST, MQTT_PORT, 60)
        cliente_mqtt.loop_start()
    except Exception as erro:
        # A API continua ativa mesmo que o broker ainda não esteja disponível.
        print(f"Não foi possível conectar ao MQTT agora: {erro}")


@app.get("/")
def inicio():
    return jsonify({"mensagem": "API do Torno CNC funcionando", "equipamento_id": EQUIPAMENTO_ID})


@app.get("/api/saude")
def saude():
    return jsonify({"status": "ok"})


@app.get("/api/equipamentos/<id_equipamento>")
def equipamento(id_equipamento):
    if id_equipamento != EQUIPAMENTO_ID:
        return jsonify({"erro": "Equipamento não encontrado"}), 404
    return jsonify({
        "id": EQUIPAMENTO_ID,
        "nome": "Torno CNC",
        "tipo": "Torno CNC",
        "setor": "Usinagem",
        "funcao": "Usinagem de peças por remoção de material",
        "ultima_manutencao": "2026-09-20",
        "dados_didaticos": True
    })


@app.get("/api/equipamentos/<id_equipamento>/telemetria")
def consultar_telemetria(id_equipamento):
    if id_equipamento != EQUIPAMENTO_ID:
        return jsonify({"erro": "Equipamento não encontrado"}), 404
    with lock:
        resposta = dict(telemetria)
    resposta["id"] = EQUIPAMENTO_ID
    resposta["dados_didaticos"] = True
    return jsonify(resposta)


if __name__ == "__main__":
    conectar_mqtt()
    app.run(host="0.0.0.0", port=5000, debug=False)
