# Sistema de Apoio à Manutenção Industrial — WebAR + Cloud

Protótipo acadêmico para o ativo **Torno CNC (CNC-01)**. Temperatura, vibração e status são dados fictícios.

## Requisitos
- Docker Desktop instalado e em execução.
- Imagem de target compilada pelo MindAR, salva em `frontend/assets/targets/torno.mind`.
- Imagem usada para gerar esse target salva em `frontend/assets/images/torno.png.png`.

> Os arquivos `torno.mind` e `torno.png` não são incluídos neste pacote: copie os arquivos reais do seu projeto anterior para esses caminhos. O arquivo `.mind` deve corresponder exatamente à imagem usada no target.

## Executar
Na pasta do projeto, rode:

```bash
docker compose up --build
```

- Frontend: http://localhost:8080
- API: http://localhost:5000/
- Saúde da API: http://localhost:5000/api/saude
- Identificação: http://localhost:5000/api/equipamentos/CNC-01
- Telemetria: http://localhost:5000/api/equipamentos/CNC-01/telemetria

Para encerrar: `Ctrl+C`; depois `docker compose down`.

## Testar MQTT
Veja as mensagens do simulador:

```bash
docker compose logs -f simulator
```

Veja os logs da API:

```bash
docker compose logs -f backend
```

O simulador publica no tópico `industria/CNC-01/telemetria` a cada 10 segundos. O Flask guarda o último valor recebido e disponibiliza no endpoint de telemetria.

## Testar indisponibilidade
1. Rode `docker compose stop backend`.
2. Na página WebAR, toque em Monitoramento: a mensagem de indisponibilidade deve aparecer.
3. Rode `docker compose start backend` e tente novamente.

## Observação sobre celular
A câmera normalmente exige HTTPS quando a página é acessada por outro dispositivo. `http://localhost:8080` funciona para testes no mesmo computador, mas não use o IP local via HTTP como solução final para o celular. Para demonstração móvel, publique o frontend em hospedagem HTTPS e configure `API_BASE` em `frontend/js/app.js` para apontar à API publicada com HTTPS e CORS configurado.

## Pastas
- `frontend/`: interface WebAR.
- `backend/`: API Flask e consumidor MQTT.
- `mqtt/`: configuração Mosquitto.
- `simulator/`: simulador de telemetria.
- `docs/`: arquitetura e matriz de testes.
