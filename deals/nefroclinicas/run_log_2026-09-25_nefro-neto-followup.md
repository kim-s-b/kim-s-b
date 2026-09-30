# Run Log — Nefroclínicas × Neto (follow-up da call de 24/09) — 2026-09-25

**Deal HubSpot `62499304574` "Nefroclinicas"** (portal 51359057). Sessão Claude Code (cloud). Objetivo: analisar a call de 24/09 entre Thomaz e José Neto, filtrar o que fazer e preparar o follow-up. Kim pediu cautela: o Thomaz tem errado em deals, e a proposta que ele citou não está com o Kim.

## Fontes lidas
- Transcrição Samskit `2026-09-24_Neto-NefroClinicas_a2557873.txt` (Drive `1u3eoh6iiQnalHoTFBvgahwDGYxGW014c`). 60 min, Thomaz Srougi × José Neto.
- 2 áudios de WhatsApp do Thomaz pós-call (pasta `Leads/Nefroclinicas`, Drive `178ti-4GibP-0AguuAYYhP3S53sHs_fmE`):
  - `17.02.46.opus` (69 s) e `17.03.33.opus` (11 s).
  - Transcritos com Whisper medium (ONNX via sherpa-onnx), porque HF e OpenAI estão bloqueados no proxy. **Transcrição automática, sem revisão humana.** O trecho 0:00–0:05 do primeiro áudio ficou ininteligível.
- `deal62499304574.json` (histórico de calls consolidado): 29/04, 04/05, 22/06 e 07/07.
- WhatsApp com Kamilla (`+5521998675477.txt`).
- HubSpot: deal em **Proposta**, amount **R$60.000**, closedate **09/09/2026 (vencido)**.
- Gmail: nenhuma proposta enviada à Nefro encontrada. Convite da call veio do Thomaz em 23/09.

## Histórico reconstruído
| Data | Com quem | O que aconteceu |
|---|---|---|
| 29/04 | Robert Santos (gerente Brasília) | Demo. Interesse em piloto em Brasília. Próximo passo: call com Tiago (TI) sobre NefroCIS. |
| 04/05 | Nefro | Carecode faria proposta de piloto WhatsApp. Dependência: resposta da Nefrosys sobre API. Nefro comparava com outro piloto. |
| 22/06 | Kamilla (gerente regional Rio) + Robert | Interesse em piloto no Rio. Robert topa romper contrato com a NET2. Kamilla recebeu uma proposta ("ele me mandou, só não abri"). |
| 26/06 | Kamilla (WA) | Nefrosys roda em nuvem, pago por licença. |
| 07/07 | Tiago Azevedo (TI) | API Nefrosys só retorna as **próximas 10 agendas**, não cria paciente e não expõe catálogo. Nefrosys quer **cobrar** pela API. CEO **Luiz Marcial** ia negociar. Kim enviou a lista de APIs necessárias. |
| ~12/08 | Tiago | Faltou à call e parou de responder (WA com Kamilla, 14/08). |
| 24/09 | **José Neto** (sócio do Daniel Calazans; dir. marketing e comunicação) | Call com o Thomaz (ver abaixo). |

Não achei registro do resultado da negociação Luiz Marcial × Nefrosys.

## Leitura da call de 24/09
**Dados do Neto:**
- 14 unidades.
- BH, Brasília e Rio somam cerca de 80%.
- BH: Blip + secretária virtual, R$12–15 mil/mês, 1.500–2.000 consultas/mês.
- Brasília: NET2, de 200–300 para 750 atendimentos, com leads desqualificados.
- Campanha teste em Brasília: CPC ~R$20.

**Dor:**
- Qualificar renal crônico. O ideal seria ter a TFG a partir da creatinina do prontuário.
- Não consegue escalar o marketing porque o atendimento não aguenta.
- Não existe dono nacional do atendimento.

**Positivo:**
- Pediu proposta e vai comparar com as que já tem: "ouro vs. coisa que só brilha".
- Sugeriu começar por BH e depois ir para o Rio.
- Quer pressionar a Nefrocis.

**Riscos:**
1. Sem dono do atendimento no lado deles. Tanto Neto quanto Thomaz citaram.
2. API da Nefrocis.
3. Overclaim do Thomaz: "Ferrari", Meta/Microsoft, 90M pacientes nos EUA, 2 semanas de implantação, 85% de resolutividade, ROI de 10–40x.
4. Thomaz citou preços na call: voz R$6/conversa, WA R$1,75, semiconversa R$0,17. Também disse que "já fizemos proposta, teria que revisar".

**Áudios do Thomaz:**
- Pede que o Kim se apresente como sócio comercial, copie ele e mande "a última proposta".
- "Vai ser um puta case."
- Eles vão receber um investimento grande de um fundo apresentado pelo Thomaz, investidor do Dr. Consulta.
- Fala em **"flexibilizar a proposta"**.

## Decisões
- **Não reenviar a proposta antiga.** O escopo era outro (agendamento ops Brasília/Rio) e o Kim não tem o documento. Pedida ao Thomaz só como referência de preço.
- **Nova proposta em 2 fases.**
  - Fase 1: qualificação de renal crônico por WA em BH. **Sem dependência da API Nefrosys.**
  - Fase 2: integração, agendamento, voz e outras unidades.
- **Dono nomeado do lado Nefro como pré-condição.**
- **Sem desconto antecipado.** Investimento/fundo não justifica baixar preço.
- **Kim assume a thread.** Thomaz fica em cópia, sem mensagens paralelas de preço ou prazo.
- Não copiar Robert, Kamilla ou Tiago agora.

## Ações executadas
1. **25/09 10:34 — email enviado pelo Kim** ao Neto, cc Thomaz (t@) e Eduardo (e@).
   - Assunto: "NefroClínicas & Carecode". Thread Gmail `1a0d8ab43b291ee1`.
   - Conteúdo: apresentação, histórico (visita ao Robert em Brasília, Kamilla, Tiago), Fase 1 sem API e 3 perguntas (volume BH, dono do piloto, indicadores).
   - **Sem data de entrega da proposta** (Kim removeu do rascunho).
2. **25/09 — rascunho da proposta criado** como Google Doc na pasta `Leads/Nefroclinicas`.
   - "Proposta Carecode × Nefroclínicas — Piloto BH (RASCUNHO)", Doc `1rb8MjLYJC8-6Ey1z68cCyT2YllgHg7zS6sid6RobxbY`.
   - Versão .md: `Proposta_Nefroclinicas_Piloto_BH_RASCUNHO.md`.

## Status em 30/09
- **Neto não respondeu** (Gmail, últimos 7 dias). 3 dias úteis sem resposta.
- HubSpot **não alterado** nesta sessão.

## Pendências
- [ ] Preencher na proposta:
  - setup;
  - mínimo mensal;
  - metas [X]% de qualificação e acurácia;
  - canal (número atual Blip vs. dedicado);
  - prazo de go-live (rascunho: 4 semanas);
  - simulação de volume.
- [ ] Receber do Thomaz a proposta antiga, só como referência de preço.
- [ ] Sem resposta do Neto: enviar a proposta até ~02/10 com premissas explícitas.
- [ ] Apagar o bloco "NOTAS INTERNAS" do Doc antes de enviar. Conferir a formatação dessa caixa (pode ter vindo com `**` literais).
- [ ] HubSpot `62499304574`:
  - closedate (vencido em 09/09);
  - contato principal → José Neto;
  - amount conforme a nova proposta;
  - nota com o resumo da call de 24/09.
- [ ] Alinhar com o Thomaz: Kim é dono da thread e não haverá desconto antecipado.

## Registrado em
- Esta run log (Drive `Leads/Nefroclinicas` + repo `deals/nefroclinicas/`).
