# Atualização de pipeline a partir dos backups TXT — 27/09/2026

Fontes lidas em 27/09: `Backups-TXT/exports_samskit` (22 reuniões de 11/09 a 25/09) e
`exports_whatsapp` / `exports_whatsapp3c` / conta do bot (34 números de contatos de deals abertos).
Cruzado com o HubSpot ao vivo (pipeline Sales, 36 deals em Demo, Proposta e Negociação).
**Status (27/09, 15h40):** Kim aprovou o Lote 1 só para o Claudio Wulkan e o Lote 2 inteiro. Lote 3 não aprovado. 12 de 14 mudanças gravadas e relidas; Meso Clinic e Dra Fernanda Borba barradas por campo condicional (ver §Execução).

Regras respeitadas: Proposta exige `proximo_fup` + `demo_aceita`; Lost exige `motivo_cold_lost`;
`demo_aceita` segue o gate (5+ médicos ou 500+ atend./mês, decisor, dor); `sdr_originador` não é tocado
onde já existe; dono do deal = quem conduz a demo a partir do handoff.

## Lote 1 — Juízo da demo e handoff (mexe na quota das SDRs)

| Deal | ID | Campo | Atual | Novo | Evidência |
|---|---|---|---|---|---|
| [Indicação] Arthur Safady | 65204384919 | demo_aceita | vazio | aceita | Samskit 25/09: diretor Marcus na sala, ~2.000 contatos/mês, 25 médicos no CRM, dor de atendimento lento e fim de semana |
| | | hubspot_owner_id | Raphael | Mariana | Mariana conduziu; Raphael segue como SDR originador |
| | | proximo_fup | vazio | 2026-09-29 | proposta 2k/3k conversas prometida, sem data |
| Sebastián C | 65062741025 | demo_aceita | vazio | aceita | Samskit 24/09: 5–7 médicos, 3 unidades, decisor, dor de agendamento 24/7 |
| | | hubspot_owner_id | Natalia | Mariana | Mariana conduziu |
| | | proximo_fup | vazio | 2026-09-28 | follow-up combinado para segunda |
| [MQL] Luis Ricardo Teixeira | 65174982706 | demo_aceita | vazio | recusada | Samskit 23/09: 1 médico, 6–7 pacientes/dia |
| | | motivo_recusa | vazio | porte_abaixo_gate | |
| | | sdr_originador | vazio | Raphael | transcrição: "SDR Rafael" |
| | | hubspot_owner_id | vazio | Mariana | Mariana conduziu |
| | | proximo_fup | vazio | 2026-09-29 | cliente ia mandar volume até 25/09 |
| [META] MadelaineHellena | 64823844950 | demo_aceita | vazio | nao_realizada | Samskit 22/09: não compareceu; sem registro da remarcação de 23/09 |
| | | motivo_nao_realizada | vazio | no_show | |
| | | sdr_originador | vazio | Raphael | transcrição: "O Rafa falou alguma coisa" — confiança média |
| Claudio Wulkan | 63161754784 | demo_aceita | vazio | nao_realizada | qualification já diz "NO SHOW" (demo 04/09) |
| | | motivo_nao_realizada | vazio | no_show | |

## Lote 2 — Mudança de estágio

| Deal | ID | Campo | Atual | Novo | Evidência |
|---|---|---|---|---|---|
| Meso Clinic (Meso Medical Group) | 65129794204 | dealstage | SQL | Demo | Samskit 22/09: demo feita com o sócio Elias Rosa |
| | | demo | vazio | 2026-09-22 | |
| | | demo_aceita | vazio | aceita | 25 médicos, decisor, dor de agendamento |
| | | qualification | vazio | "Blumenau/SC, multidisciplinar, 25 médicos, 100–150 conversas/dia, AmpliMed + DigiSAC (API oficial), Unimed + particular. Decisor: Elias Rosa (sócio)." | |
| | | pain_points | vazio | "Bot de menu não agenda; recepção absorve tudo; quer atender e agendar 24h com prontuário integrado. Objeções: financeiro completo (NF, rateio por CNPJ) e receio de fornecedor pequeno." | |
| | | quantidade_de_medicos | vazio | 25 | |
| | | proximo_fup | vazio | 2026-09-28 | proposta prometida para a semana de 28/09 |
| Clínica SOL | 64095736447 | dealstage | Demo | Proposta | WhatsApp: proposta 20/08, revisada 10/09, repassada ao Dr. Carlos |
| | | demo_aceita | vazio | aceita | deal próprio do Kim, sem SDR (não afeta quota) |
| | | proximo_fup | 2026-08-28 | 2026-09-29 | 16 dias sem retorno |
| Instituto Avelino Ferri | 64584433564 | dealstage | Demo | Proposta | WhatsApp: proposta 08/09, gestora ia levar ao Dr. Ricardo |
| | | demo_aceita | vazio | aceita | sem SDR |
| | | proximo_fup | 2026-09-11 | 2026-09-29 | 18 dias sem retorno |
| Unicus Medicina Integrada | 64877506118 | dealstage | Demo | Proposta | WhatsApp (Laís): demo 09/09, proposta 10/09, "não viram a proposta" em 15/09 |
| | | demo_aceita | vazio | recusada | 2 médicos, ~70 atend./mês — abaixo do gate; sem SDR |
| | | motivo_recusa | vazio | porte_abaixo_gate | |
| | | proximo_fup | vazio | 2026-09-30 | |
| Dr. Joel Jacobovicz — Curitiba/PR | 65173406577 | dealstage | Demo | Proposta | WhatsApp: proposta 14/09; em 25/09 pediu "rever a conta"; call seg 28/09 15h |
| | | demo_aceita | vazio | aceita | sem SDR externo (originador Kim) |
| | | proximo_fup | vazio | 2026-09-28 | |
| IRAJ — Instituto Roque de Assis Junior | 64823381514 | dealstage | Demo | Proposta | WhatsApp: condições enviadas 27/08 (400 conv R$ 700, setup R$ 4.000) |
| | | demo_aceita | vazio | aceita | sem SDR |
| | | proximo_fup | 2026-10-05 | mantém | retomada combinada para outubro |
| Nefroclinicas | 62499304574 | dealstage | Lost | Proposta | Samskit 24/09: sócio Neto pediu proposta para comparar; 14 unidades |
| | | hubspot_owner_id | Thomaz (inativo) | Kim | |
| | | demo_aceita | vazio | aceita | porte e dor passam no gate |
| | | proximo_fup | 2026-09-04 | 2026-09-30 | Kim reenvia a proposta copiando Neto |
| Marcelo Queiroz | 64624181317 | dealstage | Proposta | Negociação | WhatsApp 16/09: "Se conseguir manter um valor diferenciado, fechamos os dois" |
| | | proximo_fup | 2026-09-16 | 2026-09-29 | sem resposta aos follow-ups de 21 e 25/09 |
| Dra Fernanda Borba | 65131758341 | dealstage | Proposta | Lost | Samskit 17/09: não troca o iClinic, que não integra; ela encerrou a demo |
| | | motivo_cold_lost | vazio | Integração EHR | |
| Dominica | 65027791220 | dealstage | Proposta | Nutrição | Samskit 17/09: "vou precisar dar um tempo" (orçamento em marketing) |
| | | proximo_fup | 2026-09-18 | 2026-12-01 | revisitar em 60–90 dias |
| Consultório do Dr. Olimpio | 63874344028 | dealstage | Proposta | Nutrição | WhatsApp 16/09: médico "não sabe ainda se irá implementar" |
| | | proximo_fup | 2026-09-21 | 2026-11-02 | |
| Eiger | 62764753578 | dealstage | Negociação | Nutrição | WhatsApp 08/09: "aguardar mais um pouco devido a outros projetos mais urgentes" |
| | | proximo_fup | 2026-09-04 | 2026-11-02 | |
| Clínica Florence | 61606023945 | dealstage | Negociação | Nutrição | WhatsApp (Lucas Andrade): demo 02/06, nada desde junho |
| | | proximo_fup | 2026-09-04 | 2026-11-02 | |
| Claudio Wulkan | 63161754784 | dealstage | Demo | Nutrição | no-show 04/09 (Lote 1); achou a proposta de 06/08 "sem sentido" |
| | | proximo_fup | vazio | 2026-11-02 | |

## Lote 3 — Só próximo follow-up e dono (sem mudar estágio)

| Deal | ID | Campo | Atual | Novo | Evidência |
|---|---|---|---|---|---|
| Hospital de Olhos Sudoeste PR | 65223854884 | proximo_fup | vazio | 2026-09-28 | WhatsApp 24/09: reunião com o call center seg 28/09 14h; proposta formal depois |
| Saúde Sempre | 64375676160 | proximo_fup | 2026-09-11 | 2026-09-28 | WhatsApp 25/09: ZapSign enviado 24/09, "segunda provavelmente já tenho uma posição" |
| Clínica ELA | 65060881988 | proximo_fup | vazio | 2026-09-29 | Samskit 22/09: proposta prometida "esta semana"; pedir taxa de no-show |
| Clínica Vittá | 64575488620 | proximo_fup | 2026-09-11 | 2026-09-30 | WhatsApp: aguardando levantamento de dados desde 08/09 |
| Hospital Allume | 64363898780 | proximo_fup | vazio | 2026-09-30 | Samskit 15/09: licenças de teste; sem sinal do treinamento de 17–18/09 |
| Consultório do Povo | 62950521376 | proximo_fup | 2026-09-04 | 2026-09-30 | WhatsApp: Kim ofereceu 20% em 10/09, sem resposta |
| Oral Unic — Fase 1 | 64488182922 | proximo_fup | 2026-09-21 | 2026-09-30 | Samskit 16/09: pediram POC de custo zero; R$ 60k em risco |
| [MQL] Luiz felipe | 65186978136 | hubspot_owner_id | vazio | Nathally | Nathally conduziu a demo de 23/09 |
| | | proximo_fup | 2026-09-25 | 2026-09-30 | aguarda condição especial da diretoria; teto do cliente R$ 600/mês |

## Fora da proposta — pede decisão do Kim

- **Juliana Melo** ([META], Demo 15/09): nenhuma evidência de que a demo aconteceu. Não realizada, ou voltar para SQL?
- **Alexandre e Eclat Beaute** (dona Mariana): sem gravação nem conversa lida. A Mariana precisa dizer se as demos aconteceram.
- **Letícia Funis**: a demo de 11/09 existe, mas o deal "Leticia Funis" está em Lost e a nota foi para o deal "Letícia" (SQL, Natalia, criado 23/09). Confirmar se é a mesma pessoa antes de mexer.
- **Dra. Vivianne Duarte** (demo 17/09, sem fit, retomar após mentoria em outubro): não há deal. Criar em Nutrição?
- **Oral Unic**: o valor de R$ 60k não se sustenta com o pedido de POC gratuita. Revisar valor ou probabilidade.
- **Susin Clínica Integrada** (Closed Won): fechamento foi verbal em 21/09; conferir se o contrato digital foi assinado.
- **Agape Auditiva, Glauco, Dr. Guilherme Wood, Hospital da Visão, Leila Cedin, Stephan**: sem sinal novo que justifique mudança. Leila e Stephan já têm follow-up coerente (05/10 e 30/09).
- **Seis números** (Glauco, Alexandre, Luis Ricardo, Arthur, Sebastián, Felipe) têm conversas em três pastas do Drive fora do backup documentado. Não foram lidas.

## Execução — 27/09

| Deal | Resultado |
|---|---|
| Clínica SOL, Avelino Ferri, Unicus, Dr. Joel, IRAJ, Nefroclinicas → Proposta | ✅ gravado e relido |
| Marcelo Queiroz → Negociação | ✅ |
| Dominica, Dr. Olimpio, Eiger, Florence → Nutrição | ✅ |
| Claudio Wulkan → não realizada (no-show) + Nutrição | ✅ |
| Meso Clinic → Demo | ❌ portal exige `atendimentos_por_mes` e `qtd_de_recepcionistas` (lógica condicional). Nenhum dos dois foi dito na reunião |
| Dra Fernanda Borba → Lost | ❌ portal exige `closed_lost_reason` além de `motivo_cold_lost`. Proposta: "EHR Integration" |
| Susin Clínica Integrada | já completo: assinatura 22/09, OS 174, Kick-off. Nada a fazer |

Efeito colateral a corrigir: Nefroclinicas voltou para Proposta com `closedate` 09/09 e `closed_lost_reason` "No Response" herdados do Lost.

## Rodada 2 — mapeamento dos demais deals (27/09)

Fontes adicionais: `exports_v2` (Wanda), `exports_ligacoes`, `exports_dermacare` e notas do HubSpot de 08 a 25/09.

| Deal | ID | Evidência | Proposta |
|---|---|---|---|
| Eclat Beaute | 65162352144 | Nota da Natalia 25/09: "No show, tentando nova agenda com a proprietária" | Não realizada (no-show), follow-up 30/09, mantém Demo |
| Alexandre | 65076758064 | Nota do Raphael 24/09: "não compareceu na demonstração e parou de responder"; 40 consultas/mês | Não realizada (no-show) + Nutrição, follow-up 02/11 |
| [META] JulianaMelo | 64793975216 | Sem transcrição da demo de 15/09; lead em silêncio desde 08/09 | Não realizada (outro) + Nutrição, SDR Raphael — confiança média |
| [META] MadelaineHellena | 64823844950 | No-show 22/09 confirmado; remarcação de 23/09 sem registro | Não realizada (no-show) + Nutrição, SDR Raphael |
| [MQL] Luis Ricardo | 65174982706 | Demo 23/09; 1 médico, ~130/mês; não mandou o volume prometido para 25/09 | Recusada (porte) + Nutrição, SDR Raphael, dona Mariana |
| Arthur Safady | 65204384919 | Demo 25/09; diretor quer começar com 2 mil conversas/mês | Aceita · dona Mariana · follow-up 29/09 (igual ao Lote 1) |
| Sebastián C | 65062741025 | Demo 24/09; pediu retorno até 28/09 | Aceita · dona Mariana · follow-up 28/09 (igual ao Lote 1) |
| Leticia Funis | 62634811773 | Demo com Kim 11/09, proposta R$ 900 + R$ 3.000 enviada 14/09, quer implantar até novembro; deal em Lost | Reabrir em Proposta, demo 11/09, follow-up 29/09 |
| Letícia (SQL) | 65204482819 | Notas da Natalia 23–25/09: gestora, irmã atende, clínica indo a 10 médicos | Pessoa diferente da Letícia Funis. Não mexer |
| Dra. Vivianne Duarte | — | Demo 17/09; proposta em pptx de 23/09; decide após mentoria de outubro | Criar deal em Nutrição, follow-up 02/11 |
| Dr. Guilherme Wood | 65077069850 | Nota da Mariana 22/09: demo feita, R$ 700 + R$ 3.000 ofertado | Manter Proposta |
| Glauco | 64986215715 | Demo agendada 16/09; nada depois; follow-up vencido 21/09 | Só follow-up novo — data com o Kim |
| Agape Auditiva | 64215121295 | A resposta da Lilian de 17–23/09 não está no backup | Kim leu a resposta: decide |

### Integridade da quota das SDRs — para a Nathally arbitrar

Quatro deals estão com demo **aceita** abaixo do gate (menos de 5 médicos e menos de 500 atend./mês): Dominica (terapeuta solo, SDR Raphael), Luiz Felipe (2 médicos, 40–50/mês, SDR Natalia), Glauco (~200/mês, SDR Raphael) e Dr. Guilherme Wood (1 médico, ~300 conversas/mês, SDR Natalia). Mudar para recusada tira ponto de quota; por isso fica com a Coordenação.
