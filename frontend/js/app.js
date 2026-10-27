const API_BASE = `${window.location.protocol}//${window.location.hostname}:5000`;
const ID_EQUIPAMENTO = 'CNC-01';
const painel = document.getElementById('painel');
const tituloPainel = document.getElementById('titulo-painel');
const conteudoPainel = document.getElementById('conteudo-painel');
const avisoCamera = document.getElementById('carregando');
const targetTorno = document.getElementById('target-torno');

function mostrarPainel(titulo, html) {
  tituloPainel.textContent = titulo;
  conteudoPainel.innerHTML = html;
  painel.scrollIntoView({ behavior: 'smooth', block: 'nearest' });
}

async function buscarJson(url) {
  const resposta = await fetch(url, { headers: { Accept: 'application/json' }, cache: 'no-store' });
  if (!resposta.ok) throw new Error(`A API respondeu com HTTP ${resposta.status}`);
  return resposta.json();
}

async function mostrarIdentificacao() {
  mostrarPainel('Identificação', '<p>Consultando os dados do equipamento…</p>');
  try {
    const d = await buscarJson(`${API_BASE}/api/equipamentos/${ID_EQUIPAMENTO}`);
    mostrarPainel('Identificação do equipamento', `<p><strong>${d.nome}</strong></p><p><strong>ID:</strong> ${d.id}<br><strong>Tipo:</strong> ${d.tipo}<br><strong>Setor:</strong> ${d.setor}<br><strong>Função:</strong> ${d.funcao}<br><strong>Última manutenção registrada:</strong> ${d.ultima_manutencao}</p><p class="nota">Informações para demonstração acadêmica.</p>`);
  } catch (erro) { mostrarErro(); }
}

function mostrarComponentes() {
  mostrarPainel('Componentes principais', '<ul><li><strong>Placa e cabeçote:</strong> prendem e movimentam a peça durante a usinagem.</li><li><strong>Torre de ferramentas:</strong> sustenta e seleciona a ferramenta de corte.</li><li><strong>Proteção:</strong> separa a área de usinagem do operador.</li><li><strong>Painel de comando:</strong> interface de operação do equipamento.</li></ul><p>Conteúdo técnico geral, que deve ser conferido com a documentação da máquina real.</p>');
}

function mostrarManutencao() {
  mostrarPainel('Orientações de manutenção', '<ul><li>Consulte o procedimento oficial antes de qualquer intervenção.</li><li>Realize inspeções somente conforme autorização e treinamento aplicáveis.</li><li>Antes de manutenção física, siga os procedimentos de bloqueio e etiquetagem da indústria.</li><li>Registre ocorrências e encaminhe anomalias ao responsável.</li></ul><p><strong>Importante:</strong> este protótipo não substitui manual, análise de risco ou procedimento de segurança.</p>');
}

async function mostrarMonitoramento() {
  mostrarPainel('Monitoramento simulado', '<p>Consultando a API Flask…</p>');
  try {
    const d = await buscarJson(`${API_BASE}/api/equipamentos/${ID_EQUIPAMENTO}/telemetria`);
    mostrarPainel('Monitoramento simulado', `<div class="dados"><div class="dado"><span>Status</span><strong>${escapar(d.status)}</strong></div><div class="dado"><span>Temperatura</span><strong>${Number(d.temperatura).toFixed(1)} °C</strong></div><div class="dado"><span>Vibração</span><strong>${Number(d.vibracao).toFixed(1)}</strong></div><div class="dado"><span>Última atualização</span><strong>${escapar(d.atualizacao)}</strong></div></div><p>Origem: ${escapar(d.origem || 'API Flask')}.</p><p class="nota">Valores fictícios para fins didáticos. Não são limites reais de segurança.</p><button id="atualizar-dados" type="button" class="botao-secundario">Consultar novamente</button>`);
    document.getElementById('atualizar-dados').addEventListener('click', mostrarMonitoramento);
  } catch (erro) { mostrarErro(); }
}

function escapar(valor) {
  return String(valor).replace(/[&<>"']/g, (c) => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
}

function mostrarErro() {
  mostrarPainel('Serviço indisponível', '<p class="erro"><strong>Não foi possível consultar os dados do equipamento.</strong></p><p>Verifique se a API Flask está em execução e tente novamente.</p><button id="tentar-novamente" class="botao-secundario" type="button">Tentar novamente</button>');
  const botao = document.getElementById('tentar-novamente');
  if (botao) botao.addEventListener('click', mostrarMonitoramento);
}

document.querySelectorAll('.hotspot').forEach((hotspot) => {
  const acao = () => {
    switch (hotspot.dataset.ponto) {
      case 'identificacao': mostrarIdentificacao(); break;
      case 'componentes': mostrarComponentes(); break;
      case 'manutencao': mostrarManutencao(); break;
      case 'monitoramento': mostrarMonitoramento(); break;
    }
  };
  hotspot.addEventListener('pointerup', acao);
});

document.getElementById('fechar-painel').addEventListener('click', () => {
  mostrarPainel('Como utilizar', '<p>Toque em um dos quatro pontos da Realidade Aumentada para abrir as informações.</p>');
});

targetTorno.addEventListener('targetFound', () => {
  avisoCamera.textContent = 'Target reconhecido! Toque em um dos quatro pontos.';
  avisoCamera.classList.add('sucesso');
});
targetTorno.addEventListener('targetLost', () => {
  avisoCamera.textContent = 'Target não está visível. Aponte novamente para a imagem cadastrada.';
  avisoCamera.classList.remove('sucesso');
});

fetch(`${API_BASE}/api/saude`).then((r) => {
  if (r.ok) avisoCamera.textContent = 'Permita o acesso à câmera e aponte para a imagem target.';
}).catch(() => {
  avisoCamera.textContent = 'A câmera pode funcionar, mas a API está indisponível no momento.';
});
