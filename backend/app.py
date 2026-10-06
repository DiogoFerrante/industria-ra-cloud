from flask import Flask, jsonify
from flask_cors import CORS
import paho.mqtt.client as mqtt

app = Flask(__name__)

CORS(app)

dados_torno = {
    "id": 1,
    "nome": "Torno CNC",
    "status": "Operacional",
    "temperatura": 35,
    "vibracao": 2.1,
    "ultima_manutencao": "2026-09-20"
}

TOPICO = "industria-ra-cloud/torno/monitoramento"


def quando_conectar(client, userdata, flags, reason_code, properties):
    print("================================")
    print("MQTT CONECTADO!")
    print("Código:", reason_code)
    print("================================")

    client.subscribe(TOPICO)

    print("Inscrito em:", TOPICO)


def quando_receber(client, userdata, msg):
    mensagem = msg.payload.decode()

    print("================================")
    print("MENSAGEM MQTT RECEBIDA!")
    print("Mensagem:", mensagem)
    print("================================")

    if mensagem == "alerta":
        dados_torno["status"] = "Alerta"

    elif mensagem == "normal":
        dados_torno["status"] = "Operacional"


mqtt_client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION2
)

mqtt_client.on_connect = quando_conectar
mqtt_client.on_message = quando_receber

print("Tentando conectar ao MQTT local...")

mqtt_client.connect(
    "mqtt",
    1883,
    60
)

mqtt_client.loop_start()


@app.route("/")
def inicio():
    return jsonify({
        "mensagem": "API do Sistema de Manutenção Industrial funcionando!"
    })


@app.route("/api/torno")
def torno():
    return jsonify(dados_torno)


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=False
    )