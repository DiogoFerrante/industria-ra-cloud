\# Sistema de Apoio à Manutenção Industrial



\## Descrição



Protótipo de um sistema de apoio à manutenção industrial utilizando Realidade Aumentada, API Flask, MQTT, Docker e Docker Compose.



O sistema simula o monitoramento de um torno CNC. Um simulador envia mensagens através do MQTT, o backend recebe essas mensagens e disponibiliza os dados através de uma API.



O frontend apresenta as informações do equipamento e utiliza WebAR com MindAR.



\## Tecnologias utilizadas



\- HTML

\- CSS

\- JavaScript

\- A-Frame

\- MindAR

\- Python

\- Flask

\- MQTT

\- Mosquitto

\- Docker

\- Docker Compose



\## Funcionamento



O sistema funciona da seguinte maneira:



Simulador  

↓  

MQTT / Mosquitto  

↓  

API Flask  

↓  

Frontend Web  

↓  

WebAR / MindAR



O simulador envia os estados:



\- alerta

\- normal



Quando recebe `alerta`, o sistema altera o status do torno para \*\*Alerta\*\*.



Quando recebe `normal`, o sistema altera o status para \*\*Operacional\*\*.



\## Dados monitorados



O sistema apresenta:



\- Nome do equipamento

\- Status

\- Temperatura

\- Vibração

\- Data da última manutenção



\## API



Endpoint:



```text

GET /api/torno

{
    "id": 1,
    "nome": "Torno CNC",
    "status": "Operacional",
    "temperatura": 35,
    "vibracao": 2.1,
    "ultima_manutencao": "2026-09-20"
}
Como executar

Primeiro, abra o CMD na pasta do projeto:

industria-ra-cloud

Execute:

docker compose up -d --build

Para verificar os containers:

docker ps

O frontend pode ser iniciado com:

cd frontend
python -m http.server 8000

Depois abra no navegador:

http://localhost:8000

A API pode ser acessada em:

http://localhost:5000
Testes realizados

Foram realizados testes de:

Comunicação entre o simulador e o MQTT
Comunicação entre MQTT e backend
Funcionamento da API Flask
Alteração automática do status
Funcionamento do frontend
Execução dos serviços com Docker Compose
Objetivo

Demonstrar a integração entre Internet das Coisas, MQTT, serviços web, Docker e Realidade Aumentada para auxiliar no monitoramento e na manutenção de equipamentos industriais.c
