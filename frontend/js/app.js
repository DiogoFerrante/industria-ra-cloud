document.addEventListener("DOMContentLoaded", () => {

    const scene = document.querySelector("#ar-scene");
    const target = document.querySelector("#target");

    const status = document.querySelector("#status");
    const badge = document.querySelector("#badge");


    // Quando a câmera estiver pronta
    scene.addEventListener("arReady", () => {

        status.textContent =
            "Câmera pronta. Aponte para a imagem do torno.";

        badge.textContent =
            "PROCURANDO ALVO";

    });


    // Quando ocorrer erro
    scene.addEventListener("arError", () => {

        status.textContent =
            "Não foi possível iniciar a câmera.";

        badge.textContent =
            "ERRO";

    });


    // Quando o target for reconhecido
    target.addEventListener("targetFound", () => {

        status.textContent =
            "Torno reconhecido! RA ATIVA.";

        badge.textContent =
            "● RA ATIVA";

        console.log("TARGET ENCONTRADO");

    });


    // Quando perder o target
    target.addEventListener("targetLost", () => {

        status.textContent =
            "Alvo perdido. Aponte novamente para o torno.";

        badge.textContent =
            "PROCURANDO ALVO";

        console.log("TARGET PERDIDO");

    });

});