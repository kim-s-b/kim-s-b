# Painel individual de resultados — SDR

> Sessão de planejamento · 21/09/2026 · doc de uso do Kim.
> Responde duas perguntas: (1) a lista de indicadores proposta faz sentido? (2) em que formato
> acompanhar? Nada foi construído nesta sessão — só decisões e plano.

---

## 0 · O que já existe (e o painel deve reaproveitar)

| Peça | Onde | O que entrega hoje |
|---|---|---|
| **Gate de demo aceita** | HubSpot, deal | `sdr_originador` · `demo` (Demo Date, obrigatória p/ entrar em Demo) · `demo_aceita` (Aceita / Recusada / **Não realizada — no-show ou cancelada**) · `demo_aceita_em` · `motivo_recusa`. Definido em 14 e 21/08 |
| **3 relatórios de SDR** | HubSpot Reports (owner Kim) | `350834064` Demos aceitas por SDR · `350834472` Taxa de aceite (30d) · `350835411` Pendentes há mais de 24h (13 deals hoje) |
| **Quota e rampa por pessoa** | Artifacts "Meta Comercial Set–Nov v2" + "Calculadora · <nome>" (5 SDRs/vendedora) · `GTM/Sales Team structuring/build_calculadoras_v3.py` | Pré-vendedor @100%: 50 leads/dia · **55 agendamentos/mês · 44 realizadas · 35 aceitas (~8/semana)**. Rampa: Natalia/Raphael 50% set · 75% out · 100% nov; Bianca/Viviane 50% out · 75% nov · 100% dez. O que paga: demos aceitas (70%) + receita gerada (30%) |
| **Funil de discagem por agente** | `Ligacao-Agent/metricas.py` (3C Plus `/calls`) | discagens · atendida · conversa ≥30s · decisor · demo, **por agente**, mais `dias_com_discagem` (hoje só agregado) |
| **Rotina semanal de métricas** | `Report-Agents/weekly-metrics/` (launchd seg 07h30, Sheet "Métricas GTM", post `#growth_metrics`) | Cliente HubSpot com retry, `sheets_writer.py` idempotente, `slack_post.py`, padrão `run <motor> <json>` |
| **Desenho do painel diário** | Notion "5 · Automação das métricas de execução e rampa" (30/08) | 4 blocos (execução · pipeline · treino · higiene), alarmes por exceção, decisões em aberto: alvos, canal/nomes, data da virada da taxonomia |
| **Time no CRM** | HubSpot team Sales | SDRs: Natalia Domingues `97347695`, Raphael Reder `97347694`, Bianca Monteiro `99235719`, Viviane Paixão `99235720`. Closer: Mariana `99235153`. Coord.: Nathally `97347696`. Fábio inativo |

**Consequência:** o painel é montagem, não construção. As definições e os campos existem;
falta (a) fechar duas lacunas de dado, (b) escolher o formato, (c) ligar a rampa ao número.

---

## 1 · A proposta, indicador por indicador

| # | Indicador proposto | Veredicto | Fonte hoje | Ajuste |
|---|---|---|---|---|
| 1 | Período selecionado | ✅ | — | **Mês** como unidade principal (é a unidade da carta meta e da rampa), com semanas dentro. Nunca "últimos 30 dias" — a rampa e a comissão são por mês fechado |
| 2 | Dias úteis trabalhados | ✅ mas **sem fonte** | Não existe no HubSpot | Proxy: **dias com ≥1 discagem humana na 3C+** por `agent_id` (o `metricas.py` já lê; falta abrir por agente). Override manual para férias/atestado. Serve também para o ritmo diário: agendamentos ÷ dias trabalhados vs. alvo 2,5/dia |
| 3 | Meta de agendamentos | ✅ com ressalva | Calculadora (55 @100% × fator de rampa) | Mostrar, mas **não é o que paga**. O painel precisa deixar claro: agendamento é meta de execução (1:1); a quota remunerada é demo aceita + receita gerada |
| 4 | Agendamentos realizados | ✅ | Deal com `sdr_originador` + `demo` preenchida, contado pela **data de entrada no estágio Demo** (`hs_v2_date_entered_1354839703`) na janela | Não contar por `createdate` (o mesmo erro que o weekly já corrigiu). Decidir se demo inbound agendada por SDR conta — hoje inbound sai como SDR "Unassigned" |
| 5 | % da meta | ✅ | Calculadora | Meta = quota @100% × **fator de rampa da pessoa no mês**. Sem isso Bianca aparece a 0% em setembro sem ter meta |
| 6 | Reuniões realizadas | ✅ | `demo_aceita ∈ {aceita, recusada}` (= demo aconteceu e o closer julgou) | **Não usar** o objeto Meeting: `hs_meeting_outcome` está vazio em ~100 das 105 reuniões de ago–set, e 55 delas são do Kim. O deal é a unidade |
| 7 | No-show | ⚠️ **sem dado** | `demo_aceita = nao_realizada` existe, **0 usos** até hoje; mistura no-show com cancelamento | Criar `motivo_nao_realizada` (No-show · Cancelada pelo lead · Cancelada por nós · Remarcada) obrigatório quando `demo_aceita = nao_realizada`. Passa a valer no dia em que o closer marcar |
| 8 | Remarcações | ⚠️ **sem dado** | Nada registra | Ler do **histórico da propriedade `demo`** (`propertiesWithHistory`): cada alteração de Demo Date depois da 1ª = 1 remarcação. Zero campo novo, zero disciplina nova, e reconstrói o passado |
| 9 | Oportunidades aceitas | ✅ pronto | `demo_aceita = aceita`, por `sdr_originador`, janela em `demo_aceita_em` | É o relatório `350834064`. Mostrar ao lado: **recusadas** (com motivo) e **pendentes de aceite >24h** — o pendente é SLA do closer e trava o número do SDR |
| 10 | Conversão oportunidade → reunião | ⚠️ ambíguo | — | Dois números distintos, os dois úteis: **show rate** = realizadas ÷ agendadas (premissa 80%) e **taxa de aceite** = aceitas ÷ realizadas (premissa 75%). Mais um degrau acima, da 3C+: **agendamentos ÷ conversas com decisor** — é onde a conta de setembro quebrou (4 decisores, 0 demos) |
| — | **Receita gerada** (falta na lista) | ➕ | Deals Won cuja origem é o SDR (`sdr_originador`), MRR + setup | São 30% da comissão. Sem isso o painel não fecha com a calculadora |
| — | **Leads trabalhados / discagens** (falta) | ➕ | 3C+ por agente | É o gate de atividade (80% dos leads) que libera o acelerador acima de 100%. E é o único indicador diário que a pessoa controla sozinha |

**Leitura geral:** a lista está certa na intenção e alinhada ao modelo de comissão que o time já
recebeu. Faltam três coisas: a régua (rampa), os dois componentes que pagam (aceitas e receita
gerada — só o primeiro estava) e a camada de atividade. E dois indicadores (no-show, remarcação)
não têm dado hoje — um se resolve lendo histórico, o outro pede um campo e um hábito.

---

## 2 · Estado atual dos dados (portal 51359057, consulta 21/09)

| | Natalia | Raphael | Kim (referência) | Inbound (sem SDR) |
|---|---|---|---|---|
| Deals com `sdr_originador` | 117 | 74 | 18 | — |
| Demo Date em setembro | 4 | 6 | 1 | 4 |
| Demo aceita | 2 | 3 | 0 | — |
| Recusada | 1 | 0 | 0 | — |
| Não realizada | 0 | 0 | 0 | — |
| Meta set (rampa 50%) — aceitas | 17,5 | 17,5 | — | — |

- As primeiras demos com Demo Date por SDR aparecem só na semana de **14/09**. Agosto e início de setembro só têm demo inbound.
- **13 deals em Demo com data passada e sem juízo** (`Pendentes há mais de 24h`). Enquanto o closer não marca, o SDR não pontua.
- Bianca e Viviane **não estão no de-para agente 3C+ → owner** (`cfg.OWNER_POR_AGENTE` só tem Natalia, Raphael, Fábio, Kim). Sem isso, nem discagem nem "dias trabalhados" delas existem.
- Meeting outcome: 5 preenchidos em ~105 reuniões. Confirmado: não é fonte.

---

## 3 · Formato — recomendação

Três camadas, cada uma no lugar que já faz esse trabalho. Não é "um ou outro".

### Camada 1 — HubSpot: a verdade ao vivo (esta semana, sem código)
Dashboard **"SDR · Individual"** com filtro de dashboard por `sdr_originador` e por mês de `demo`.
Relatórios (report builder, mesmo padrão dos 3 que existem):

1. Agendamentos por semana — entradas no estágio Demo, por SDR
2. Realizadas × não realizadas (`demo_aceita` preenchida) por SDR
3. Aceitas · recusadas · pendentes — o `350834064` + `350835411` abertos por SDR
4. Taxa de aceite por SDR (aceitas ÷ realizadas)
5. Motivos de recusa por SDR
6. Motivos de não realização (nasce com o campo novo)
7. Receita gerada — Won por `sdr_originador`, MRR e setup (line items)

Serve para: **SDR ver o próprio número a qualquer hora, Nathally na daily, Kim no pipeline review.**
Não serve para: % da meta com rampa, dias trabalhados, remarcação, atividade da 3C+. O HubSpot
não sabe rampa e não vê o discador.

### Camada 2 — Artifact por pessoa: a carta do mês com número real (2–3 dias de build)
As "Calculadora · <nome>" já são o link pessoal de cada SDR. A evolução natural é o mesmo
artifact **pré-preenchido com o realizado**: a pessoa abre e vê atingimento, comissão projetada,
dias trabalhados, ritmo diário e o funil (discagens → conversas → decisor → agendou → realizou →
aceita), com o alvo ao lado de cada número. Um motor novo, `sdr_individual.py`, no padrão do
weekly-metrics:

- lê HubSpot (deals por `sdr_originador`, histórico de `demo` para remarcações, `demo_aceita`,
  Won) e 3C+ (`metricas.py --json`, `por_agente` + dias com discagem por agente)
- aplica quota @100% × rampa (lida de `aba_premissas.py` / calculadoras, não digitada de novo)
- gera um JSON por pessoa → republica os 4 artifacts (+ 1 visão de time para Kim/Nathally)
- roda **segunda 07h30** junto com o weekly (o número chega antes do pipeline review e do 1:1
  de quarta); diário fica para a Camada 3

Serve para: **1:1, carta meta, comissão.** Uma fonte de cálculo — se o artifact e o HubSpot
divergirem, é bug.

### Camada 3 — Slack: alarme por exceção (já desenhado no Notion "5 · Automação")
Não é painel; é o que muda comportamento: zero discagem em dia útil, decisor sem agendamento,
aceite pendente >24h, remarcação em série. Fica para depois da Camada 2, e depende das decisões
de canal e nomes já listadas lá.

### Por que não só HubSpot, e por que não só artifact
- Só HubSpot: entrega 6 dos 10 indicadores e nenhum contra meta rampada. O SDR veria volume sem
  régua — número sem alvo é relatório.
- Só artifact: entrega tudo, mas com atraso de até 7 dias e sem self-service. Setembro não se
  corrige com dado de segunda passada.
- Sheet "Métricas GTM": continua sendo o histórico agregado do time. Uma aba "SDR" pode nascer
  do mesmo JSON, mas não é a interface — o Sheet é para série, não para leitura individual.

---

## 4 · Plano

| Fase | O quê | Dono | Esforço |
|---|---|---|---|
| **0 · Decisões** (antes de qualquer linha) | ver §5 | Kim (+ Nathally em 3) | 1 conversa |
| **1 · Dado** | Criar `motivo_nao_realizada` (enum, obrigatório quando `demo_aceita = nao_realizada`) · incluir Bianca e Viviane em `OWNER_POR_AGENTE` (pegar `agent_id` na 3C+) · limpar os 13 pendentes com a Mariana | Kim / Nathally | ½ dia |
| **2 · HubSpot** | Dashboard "SDR · Individual", 7 relatórios, filtro por `sdr_originador` e mês. Compartilhar com o time Sales | Kim (Claude constrói via MCP) | ½–1 dia |
| **3 · Motor** | `Report-Agents/sdr-individual/sdr_individual.py` + `render_painel.py`; `metricas.py` passa a expor `dias_com_discagem` por agente; teste golden com setembro | Claude Code (Mac, launchd) | 2–3 dias |
| **4 · Artifacts** | "Painel · <nome>" × 4 + "Painel · Time"; substituem o link da calculadora na carta de outubro | Claude Code | dentro da fase 3 |
| **5 · Alarmes** | Motor diário 08h45 + Slack, conforme Notion "5 · Automação" | depois | — |

Fases 1 e 2 fecham **antes do fechamento de setembro** — é o primeiro mês com quota, e a carta de
outubro sai com o link do painel em vez da calculadora vazia.

---

## 5 · Decisões — tomadas pelo Kim em 21/09

| # | Decisão | Escolha | Efeito no plano |
|---|---|---|---|
| 1 | Demo inbound agendada por SDR conta? | **Conta.** Regra única: quem agendou preenche `sdr_originador`, outbound ou inbound | Atualizar a descrição da propriedade e o roteiro do SDR. Painel não separa origem |
| 2 | Fonte de dias trabalhados | **3C Plus + override.** Dia trabalhado = dia com ≥1 discagem humana do agente; planilha de exceções (férias, atestado) | `metricas.py` expõe `dias_com_discagem` por agente; motor lê a planilha de exceções |
| 3 | Remarcação | **Histórico da Demo Date.** Cada mudança depois da 1ª = 1 remarcação | Zero campo novo. Motor lê `propertiesWithHistory` de `demo` |
| 4 | No-show na conta do SDR | **Só informação.** Aparece no painel e no 1:1, não desconta | Cria `motivo_nao_realizada` só para qualificar o dado. Régua da carta não muda |
| 5 | Visibilidade | **Painel pessoal + dashboard do time.** Artifact individual por SDR; dashboard HubSpot aberto ao time Sales com filtro por SDR | Sem permissão por owner no HubSpot. Artifact de time só para Kim e Nathally |
| 6 | Cadência do painel individual | **Diário, 08h45.** Alimenta a daily das 9h | O motor nasce diário, não semanal. Camadas 2 e 3 se fundem: o mesmo run que republica os artifacts dispara os alarmes. Segunda ele também alimenta o weekly |

### O que muda no plano com a cadência diária
- `sdr_individual.py` roda em launchd **seg–sex 08h45**, com lock e caffeinate como o weekly. A janela do dia anterior vem da 3C+ (`/calls` aceita até 31 dias, então o mês corrente cabe numa chamada).
- A leitura do HubSpot é do **mês corrente inteiro** a cada rodada (fluxo por data de entrada em Demo e `demo_aceita_em`), então não há estado a manter: re-rodar é seguro.
- Os alarmes da Camada 3 (zero discagem ontem, decisor sem agendamento, aceite pendente >24h) saem do mesmo JSON, no mesmo run. O canal do Slack e o convite do bot continuam pendentes do Notion "5 · Automação".
- Números pequenos no diário: o painel mostra **acumulado do mês contra a meta rampada pró-rata dos dias úteis decorridos**, não o dia isolado. O dia isolado só aparece no bloco de atividade (discagens, conversas, decisor).

---

**Fontes:** HubSpot portal 51359057 (`query_crm_data` 21/09; relatórios 350834064 / 350834472 /
350835411; propriedades `demo_aceita`, `sdr_originador`, `demo`, `demo_aceita_em`,
`motivo_recusa`, `hs_meeting_outcome`) · artifacts "Meta Comercial Set–Nov v2" (17/09) e
"Calculadora · Bianca" · Notion "4 · Plano de Rampa — Setembro/2026" e "5 · Automação das
métricas de execução e rampa" (31/08) · `Carecode-Agents`: `Report-Agents/weekly-metrics/SPEC.md`,
`Ligacao-Agent/{cfg,metricas}.py`, `GTM/Sales Team structuring/{aba_premissas,build_calculadoras_v3}.py`,
`CRM-Agent/CRM_MANUAL.md`.
