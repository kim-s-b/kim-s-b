> **NOTAS INTERNAS — apagar antes de enviar**
> - Tudo marcado **[A DEFINIR]** ou **[X]** é premissa e precisa ser validado.
> - **Preços por conversa:** WA R$1,75; semiconversa R$0,17; voz R$6. São os valores que o Thomaz citou na call de 24/09. Mantidos para não contradizer.
>   - Conferir com a proposta antiga do Thomaz antes de fixar setup e mínimo.
> - **Prazo:** o Thomaz falou em "duas semanas". O rascunho usa 4 semanas até o go-live.
> - **Números de BH** (1.500–2.000 consultas/mês; secretária virtual R$12–15 mil/mês): vieram do Neto na call. O volume de contatos ainda não foi informado.
> - **Tom:** sem superlativos, sem ROI genérico, sem % de resolução prometida sem baseline.
> - **Sem desconto nesta versão.** Se ele pedir, a alavanca é a duração do piloto ou o mínimo mensal, não o preço por conversa.
> - HubSpot 62499304574: amount R$60 mil, closedate vencido em 09/09. Ajustar depois.

# Carecode × Nefroclínicas
## Proposta de piloto: qualificação de pacientes renais crônicos via WhatsApp em Belo Horizonte
*Preparado para José Neto, Nefroclínicas · [DATA] · Versão para discussão*

## 1. O que entendemos
- **Negócio:** o modelo da Nefroclínicas é centrado no paciente **renal crônico**.
  - Parte relevante de quem procura a rede chega por "consulta de nefrologia" e não está no estágio da doença que interessa ao negócio.
- **Atendimento descentralizado:** cada região (BH, Brasília, Rio) resolve à sua maneira.
  - Não há visão nacional nem dono único do atendimento.
- **BH (maior operação):** Blip + secretária virtual terceirizada.
  - Custo de ~**R$12–15 mil/mês**, para ~**1.500–2.000 consultas/mês**.
  - Tempo de resposta e uso da ferramenta atual abaixo do necessário.
- **Marketing travado:** não dá para acelerar a captação.
  - Sem qualificar e atender bem quem chega, mais volume vira custo e risco de reputação.
  - Hoje não é possível saber **que perfil de paciente** cada campanha trouxe.
- **API da Nefrosys limitada:**
  - só consulta as próximas agendas;
  - não cria paciente;
  - não expõe o catálogo de procedimentos.
  - Isso bloqueia qualquer automação que dependa do prontuário.

## 2. Objetivo do piloto
Provar, em uma unidade e em um fluxo, que a Carecode consegue:
1. **Responder todo contato** que chega por WhatsApp em BH em segundos, 24/7.
2. **Classificar o perfil clínico** de cada contato, segundo critérios definidos pela equipe médica da Nefroclínicas:
   - renal crônico dialítico;
   - renal crônico não dialítico;
   - outras demandas de nefrologia;
   - não paciente.
3. **Encaminhar** cada perfil ao destino certo, com prioridade para o renal crônico.
4. **Medir** tudo por campanha e por canal.

O piloto **não depende da API da Nefrosys**. A qualificação é feita na conversa com o paciente.

## 3. Escopo da Fase 1
### 3.1 Canal
- WhatsApp de BH. **[A DEFINIR com o Neto]:** usar o número atual (hoje no Blip) ou um número dedicado às campanhas.
- Recomendamos o **número dedicado às campanhas**:
  - não mexe na operação atual;
  - isola o resultado;
  - reduz o risco.

### 3.2 O que o agente faz
- **Acolhimento e triagem:** identifica a necessidade do contato (consulta, diálise, transplante, exames, dúvidas, familiar buscando informação).
- **Qualificação clínica:** faz perguntas padronizadas, por exemplo:
  - se já faz diálise;
  - se tem diagnóstico de DRC;
  - se tem creatinina ou TFG recente (com opção de enviar foto do exame);
  - se veio encaminhado por outro médico;
  - qual é o convênio.
  - Critérios e textos são **validados pela equipe médica** antes do go-live.
- **Regras de atendimento:** aplica as regras de convênio e de médico que hoje estão em planilha (particular, Unimed, primeira consulta etc.).
- **Encaminhamento:**
  - renal crônico: transferência prioritária para a equipe humana, com o resumo da conversa;
  - demais perfis: orientação conforme regra da Nefroclínicas.
- **Dúvidas frequentes:** endereço, horários, convênios, preparo, documentos.
- **Transferência para humanos:** a qualquer momento, com o histórico completo. Nada fica sem resposta.

### 3.3 Painel de indicadores
- Contatos por dia, canal e campanha (UTM ou mensagem de origem).
- Distribuição por perfil clínico, por campanha.
- Custo por lead qualificado (renal crônico), cruzado com o investimento em mídia.
- Tempo de primeira resposta, taxa de transferência para humanos e motivos.
- Acesso a cada conversa, para auditoria e ajuste fino.

## 4. Fora do escopo da Fase 1 (Fase 2)
- Integração com a Nefrosys:
  - agenda;
  - cadastro de paciente;
  - dados do prontuário, como creatinina e TFG.
- Agendamento automático.
- Voz.
- Outras unidades (Rio, Brasília, SP, São Luís, Curitiba).

A Fase 2 depende do resultado do piloto e da abertura da API pela Nefrosys. Podemos apoiar essa conversa com uma especificação das APIs necessárias:
- consulta e criação de paciente;
- consulta de agenda e disponibilidade;
- catálogo de procedimentos e médicos;
- marcação, cancelamento e confirmação;
- lista de agendamentos por dia e status.

## 5. O que precisamos da Nefroclínicas
- **Um dono do piloto**, com ~2–4 h/semana. É o fator que mais pesa no resultado. Essa pessoa:
  - valida conteúdos;
  - revisa conversas;
  - decide ajustes.
- **Validação médica** dos critérios de qualificação (~1 h).
- **Materiais:**
  - regras de atendimento (planilha de convênios e médicos);
  - informações das unidades;
  - materiais existentes.
- **Quem recebe** as conversas transferidas em BH.
- **Do marketing:**
  - identificação das campanhas;
  - investimento por campanha.

## 6. Cronograma
| Etapa | Período | Entregas |
|---|---|---|
| Kickoff e coleta | Semana 1 | Regras, conteúdos, critérios clínicos, canal |
| Configuração | Semanas 2–3 | Agente e painel |
| Testes com a equipe | Semanas 3–4 | Testes intensivos pela Nefroclínicas e ajustes |
| Go-live | [Semana 4] | Atendimento real |
| Operação assistida | 60 dias após o go-live | Revisões semanais, ajuste fino e relatório |

## 7. Critérios de sucesso
Definidos juntos no kickoff, com o baseline de BH. Proposta inicial:
- **Primeira resposta:** < 1 min em 95% dos contatos.
- **Cobertura:** 100% dos contatos respondidos.
- **Qualificação:** ≥ [X]% dos contatos com perfil identificado.
- **Acurácia:** ≥ [X]% de classificação correta em amostra auditada pela Nefroclínicas.
- **Negócio:** custo por lead renal crônico por campanha, disponível no painel.

Ao fim dos 60 dias, decisão conjunta de **seguir, ajustar ou encerrar**.

## 8. Investimento
| Item | Valor |
|---|---|
| Implantação (setup, configuração e testes) | [A DEFINIR] |
| Conversa WhatsApp | R$ 1,75 |
| Semiconversa (até 3 trocas) | R$ 0,17 |
| Mínimo mensal | [A DEFINIR] |
| Painel e transferência para humanos | Incluídos |

**Simulação ilustrativa** [ajustar com o volume real]:
- ~3.000 conversas/mês ≈ **R$ 5.250/mês** de custo variável.
- A secretária virtual de BH custa hoje R$ 12–15 mil/mês.
- A Fase 1 não substitui a equipe humana. A comparação dá só a ordem de grandeza.

*Valores sem impostos. Validade de 30 dias.* [confirmar condições padrão]

## 9. Próximos passos
1. Call de 30 min para revisar a proposta e ajustar o escopo.
2. Definir o dono do piloto e o canal.
3. Assinatura e kickoff.

Kim Seung Beom · Growth & Revenue · Carecode
kim@carecode.com.br · +55 11 93619-0404
