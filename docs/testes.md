# Matriz de testes — Torno CNC

| ID | Ação | Resultado esperado | Resultado obtido |
|---|---|---|---|
| T01 | Abrir a aplicação pelo navegador | Página abre e solicita câmera | Preencher durante o teste |
| T02 | Apontar para o target correto | MindAR reconhece o target | Preencher durante o teste |
| T03 | Mover câmera/dispositivo | Hotspots acompanham o target | Preencher durante o teste |
| T04 | Tocar em Identificação | Informações do equipamento aparecem | Preencher durante o teste |
| T05 | Tocar em Monitoramento | API retorna status, temperatura e vibração | Preencher durante o teste |
| T06 | Ver logs do simulador | Valores são publicados via MQTT | Preencher durante o teste |
| T07 | Consultar novamente | Valores recentes aparecem na RA | Preencher durante o teste |
| T08 | Parar o container backend | Interface exibe indisponibilidade | Preencher durante o teste |
| T09 | Reiniciar o backend | Consulta volta a funcionar | Preencher durante o teste |
| T10 | Executar `docker compose up --build` | Serviços iniciam coordenadamente | Preencher durante o teste |

Todos os dados operacionais são simulados e não representam limites reais de segurança.
