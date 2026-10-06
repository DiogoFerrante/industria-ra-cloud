\# Testes do Sistema



\## 1. Teste do MQTT



Foi realizado um teste de comunicação entre o simulador e o broker MQTT.



O simulador enviou as mensagens:



\- `alerta`

\- `normal`



Resultado: \*\*Aprovado\*\*



\---



\## 2. Teste do Backend



Foi testada a comunicação entre o backend Flask e o broker MQTT.



O backend recebeu as mensagens e alterou o status do torno CNC.



Resultado: \*\*Aprovado\*\*



\---



\## 3. Teste da API



Foi acessado o endpoint:



```text

http://localhost:5000/api/torno



A API retornou os dados do torno CNC em formato JSON.



Resultado: Aprovado



4\. Teste da alteração de status



Quando o simulador envia:



alerta



o status do torno passa para:



Alerta



Quando envia:



normal



o status passa para:



Operacional



Resultado: Aprovado



5\. Teste do Frontend



O frontend foi executado através de um servidor HTTP local.



Endereço utilizado:



http://localhost:8000



A página apresentou os dados recebidos da API e atualizou o status automaticamente.



Resultado: Aprovado



6\. Teste do Docker



Os serviços foram executados utilizando Docker Compose.



Serviços utilizados:



MQTT

Backend

Simulador



Resultado: Aprovado



Resultado final



Os testes realizados demonstraram que os principais componentes do sistema estão funcionando e comunicando corretamente.

