# Painel individual de SDR — execução end-to-end (sessão no Mac)

Sou o Kim. Vamos executar o plano do painel individual de resultados dos SDRs, ponta a ponta,
nesta máquina (Mac com as rotinas launchd, tokens em `~/.carecode_*` e a clone de
`Carecode-Agents`). Você tem Claude in Chrome para a parte que só existe na UI do HubSpot.

## Contexto que você precisa antes de tocar em qualquer coisa

1. Leia o plano e os anexos — estão no repo `kim-s-b`, branch
   `claude/sdr-individual-results-dashboard-6hpes2`, pasta `painel-sdr/`:
   - `PLANO_painel-individual-sdr_2026-09-21.md` (§5 decisões · §6 alvos e bloqueios · §7 conferência de 23/09)
   - `hubspot/criar_motivo_nao_realizada.py` (v1 do campo, dry-run por padrão)
   - `cfg_owner_por_agente.patch` (agentes Viviane/Mariana + `DATA_VIRADA_TAXONOMIA`)
   - `COMO-MARCAR-demo-nao-realizada.md` (texto para o time)
   Se o repo não estiver clonado: `git clone -b claude/sdr-individual-results-dashboard-6hpes2 https://github.com/kim-s-b/kim-s-b ~/kim-s-b`.
2. Leia no `Carecode-Agents`: `CLAUDE.md`, `Report-Agents/weekly-metrics/SPEC.md` e `RUNBOOK.md`,
   `Ligacao-Agent/{README.md,cfg.py,metricas.py}`, `CRM-Agent/CRM_MANUAL.md` §"Gate de demo",
   `GTM/Sales Team structuring/{aba_premissas.py,build_calculadoras_v3.py}`.
3. Regras da casa: **dry-run por padrão, `--write` explícito**; pergunte antes de modificar arquivo
   ou registro; RUNLOG ao fim de cada fase; nada de número inventado — leia HubSpot e 3C+ ao vivo.

## Decisões já tomadas (não reabrir)

Inbound agendado por SDR conta · dias trabalhados = dia com discagem humana na 3C+ (+ planilha de
exceções) · remarcação = mudança de Demo Date no histórico · no-show só informação · painel pessoal
por SDR + dashboard do time no HubSpot · cadência **diária 08h45** (segunda também alimenta o
weekly) · alarmes no `#update_routines` (privado, `C0BKDE4UQTX`) com o token do bot **Carecode
Backups** (`~/.carecode_slack_bot_token`), nomeando pessoas · virada da taxonomia **01/10** ·
alvos: 50 discagens/dia meta e 40 piso · 2,5 agendamentos/dia · 80% show · 75% aceite · 35 aceitas
@100% × rampa · 100% de ligações com código, alarme <90%.

## Fases — nesta ordem, com gate entre elas

### Fase 1 · Dado (30 min)
1. `git apply ~/kim-s-b/painel-sdr/cfg_owner_por_agente.patch` no `Carecode-Agents`. Antes,
   confirme na 3C+ (`GET /agents` via `tcplus.py`) que `252924` = Viviane e `249600` = Mariana, e se
   a **Bianca** já tem agente — se tiver, acrescente a linha dela (owner `99235719`).
2. `python3 ~/kim-s-b/painel-sdr/hubspot/criar_motivo_nao_realizada.py` (dry-run) → me mostre →
   `--write`. Token: `~/.carecode_outbound_hstoken`; se faltar scope `crm.schemas.deals.write`,
   me avise em vez de contornar.
3. Confirme os owners no HubSpot: Viviane `99235720`, Bianca `99235719`, Mariana `99235153`.
**Gate:** `metricas.py --start <seg> --end <hoje>` mostra Viviane em `por_agente`; a propriedade
aparece no `GET /crm/v3/properties/deals/motivo_nao_realizada`.

### Fase 2 · HubSpot pela UI, com Claude in Chrome (1h)
Portal 51359057. Antes de cada bloco, me mostre o que vai clicar; depois, printe o resultado.
1. **Lógica condicional** (Configurações › Objetos › Negócios › Lógica condicional de propriedade):
   quando `Demo aceita` = Não realizada → mostrar e **exigir** `Motivo da não realização`. Mesmo
   padrão que já existe para `motivo_recusa` quando Recusada.
2. **Ligar os 3 workflows do gate**, pausados desde 14/09: `1884131449` (SLA 24h: tarefa ao dono na
   Demo Date, aviso à Nathally 34h depois), `1884148564` (carimba `demo_aceita_em`),
   `1884451698` (carimba `sdr_originador` = owner na criação). Ligar **sem inscrever registros
   existentes**.
3. **Dashboard "SDR · Individual"** — filtros de dashboard: `sdr_originador` e mês de `demo`.
   Sete relatórios, no report builder, todos em DEAL, pipeline Sales:
   1. Agendamentos por semana — entradas no estágio Demo (`hs_v2_date_entered_1354839703`), por `sdr_originador`
   2. Realizadas × não realizadas — `demo_aceita` ∈ {aceita, recusada} vs `nao_realizada`, por SDR
   3. Aceitas · recusadas · pendentes — clonar `350834064` e `350835411` abertos por SDR (pendente = Demo com `demo` < hoje e `demo_aceita` vazio)
   4. Taxa de aceite por SDR — aceitas ÷ (aceitas + recusadas)
   5. Motivos de recusa por SDR (`motivo_recusa`)
   6. Motivos de não realização por SDR (`motivo_nao_realizada`)
   7. Receita gerada — deals Closed Won por `sdr_originador`, MRR e setup via line items (regra do SPEC §5)
   Compartilhar com o time Sales (leitura). Me mande o link.
4. **Pendentes de aceite (16 deals)** — lista no §7 do plano. Não decida por mim: monte a tabela
   deal · dono · Demo Date · o que sugere (mover para Proposta/Nutrição/Lost os 7 anteriores ao gate;
   aceite/recusa nos 3 do gate; trocar dono nos 3 de SDR; atribuir os 2 [META]) e **espere meu OK**
   por lote.
**Gate:** um deal de teste passa por Demo → Não realizada → o campo aparece e exige motivo; o
workflow cria a tarefa.

### Fase 3 · Motor diário `sdr_individual.py` (2–3 dias)
Em `Report-Agents/sdr-individual/`, padrão do weekly (`run <motor> <json>`, `_bootstrap.py`, lock,
caffeinate, `sheets_writer` só se eu pedir).
1. **`Ligacao-Agent/metricas.py`**: expor em `por_agente` os campos `dias_com_discagem` e a lista de
   dias; aplicar `DATA_VIRADA_TAXONOMIA` (antes traduz LEGADO, depois conta como sem código). Teste
   com a janela 01/09–hoje; os totais agregados não podem mudar.
2. **`sdr_individual.py`** — lê, por SDR do time Sales (owners acima + Natalia `97347695`, Raphael `97347694`):
   - HubSpot, **mês corrente inteiro a cada rodada** (sem estado): agendamentos = entrada em Demo
     por `sdr_originador`; realizadas/aceitas/recusadas/não realizadas = histórico de `demo_aceita`
     (`propertiesWithHistory`), atribuído por `sdr_originador`, janela em `demo_aceita_em`;
     remarcações = nº de mudanças de `demo` após a primeira; no-show = `motivo_nao_realizada =
     no_show`; pendentes >24h; receita gerada = Won do mês por SDR (line items, regra do SPEC).
   - 3C+ (`metricas.py --json`): discagens humanas, conversas ≥30s, decisor, demo, % com código,
     dias com discagem — por agente → owner.
   - Quota: 55 / 44 / 35 / 50 leads-dia @100% × **fator de rampa da pessoa no mês** (Natalia e
     Raphael 50% set · 75% out · 100% nov; Bianca e Viviane 50% out · 75% nov · 100% dez) — ler de
     `aba_premissas.py`/calculadoras, não digitar. Meta pró-rata = quota × dias úteis decorridos ÷
     dias úteis do mês. Dias trabalhados = dias com discagem − planilha de exceções (criar
     `exclusoes_sdr.json` ao lado do `exclusoes.json` do weekly, vazio).
   - Saída: `sdr_individual_<AAAA-MM-DD>.json` com um bloco por pessoa + bloco time; todo indicador
     com `alvo` ao lado.
3. **`render_painel.py`**: (a) 4 artifacts "Painel · <nome>" (mesmo visual da "Calculadora ·
   <nome>", pré-preenchida com o realizado: atingimento, comissão projetada, funil, dias
   trabalhados, ritmo) + "Painel · Time" (Kim e Nathally); (b) post no `#update_routines` às 08h45
   com o bloco de execução de ontem por pessoa e os **alarmes por exceção**: zero discagem em dia
   útil · decisor sem agendamento · aceite pendente >24h · código <90% · remarcação em série (≥2 no
   mesmo deal). Usar `slack_post.py` apontando para o token do Backups.
4. **launchd** `com.carecode.sdr-individual.plist`, seg–sex 08h45, mesmo padrão dos outros; segunda
   o JSON também alimenta o weekly (colunas novas **no fim** do `SEMANAL_HDR`).
5. Testes: golden com setembro (os números de aceitas devem bater com o relatório `350834064`:
   Raphael 3, Natalia 2 em 21/09 — refaça a leitura ao vivo), `test_render_painel.py`.
**Gate:** rodada manual de ponta a ponta com `--write` só depois de eu ver o dry-run (JSON + post +
artifact) e dar OK.

### Fase 4 · Fechamento
RUNLOG em `Report-Agents/sdr-individual/RUNLOG.md` e no `PLANO` do `kim-s-b`; atualizar
`_ops/rotinas_map.py` e o watchdog para a rotina nova; texto do `COMO-MARCAR-demo-nao-realizada.md`
pronto para eu postar no hub do time; carta de outubro passa a apontar para "Painel · <nome>".

## O que NÃO fazer
Não reabrir decisões da §5 · não criar deal, mover estágio ou trocar dono sem meu OK por lote ·
não rodar nada com `--write` sem me mostrar o dry-run · não tocar em `demo_aceita`,
`motivo_recusa`, `sdr_originador` (definições fechadas em 14/09) · não postar no Slack fora do
`#update_routines` · não inventar alvo: se um indicador não tiver alvo decidido, ele fica fora do
painel até eu decidir.

Comece pela Fase 1 e me mostre o dry-run do script antes de qualquer `--write`.
