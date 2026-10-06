async function carregarTorno() {
    try {
        const resposta = await fetch(
            `http://${window.location.hostname}:5000/api/torno`
        );

        const torno = await resposta.json();

        document.getElementById("nome").textContent = torno.nome;
        document.getElementById("status").textContent = torno.status;
        document.getElementById("temperatura").textContent =
            torno.temperatura + " °C";
        document.getElementById("vibracao").textContent =
            torno.vibracao;
        document.getElementById("manutencao").textContent =
            torno.ultima_manutencao;

    } catch (erro) {
        console.error("Erro ao consultar a API:", erro);
    }
}

carregarTorno();

setInterval(carregarTorno, 5000);