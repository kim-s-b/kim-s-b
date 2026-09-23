#!/usr/bin/env python3
"""criar_motivo_nao_realizada.py — v1 da propriedade `motivo_nao_realizada` no DEAL.

Fecha a lacuna do gate de demo: `demo_aceita = nao_realizada` hoje mistura no-show com
cancelamento. Este campo diz o que aconteceu, no mesmo desenho do `motivo_recusa`
(um motivo por caso; obrigatório quando a demo não aconteceu).

    python3 criar_motivo_nao_realizada.py            # dry-run: mostra o que faria
    python3 criar_motivo_nao_realizada.py --write    # cria (ou completa) a propriedade

Token: env HUBSPOT_TOKEN, senão ~/.carecode_outbound_hstoken (service key
"Carecode Outbound - Automation", mesma do Outbound-Agent). Precisa do scope
crm.schemas.deals.write.

Idempotente: 409 = já existe → compara as opções e acrescenta só o que falta (PATCH).
Nunca remove opção nem altera valor interno — histórico de relatório depende deles.

O que este script NÃO faz (é UI, não API): a lógica condicional "Mostrar e exigir quando
Demo aceita = Não realizada" em Configurações › Objetos › Negócios › Lógica condicional
de propriedade — mesmo lugar onde `motivo_recusa` já está condicionado a `Recusada`.
"""
import argparse, json, os, sys, urllib.error, urllib.request
from pathlib import Path

BASE = "https://api.hubapi.com"
OBJ = "deals"
GRUPO = "gate_demo"          # grupo criado em 14/09 com demo_aceita, motivo_recusa, demo_aceita_em, sdr_originador

PROP = {
    "name": "motivo_nao_realizada",
    "label": "Motivo da não realização",
    "type": "enumeration",
    "fieldType": "select",
    "groupName": GRUPO,
    "description": (
        "Obrigatório quando Demo aceita = Não realizada. Um motivo por demo. "
        "No-show = o lead não apareceu e não avisou. Cancelada pelo lead = avisou antes do horário. "
        "Cancelada por nós = a Carecode desmarcou ou não pôde conduzir. "
        "Remarcou? Não é caso deste campo: atualize a Demo Date e limpe Demo aceita "
        "(regra do CRM_MANUAL §Gate de demo). O no-show fica no histórico e é o que o painel conta. "
        "Definido em 23/09/2026."
    ),
    "options": [
        {"label": "No-show (não apareceu, sem aviso)", "value": "no_show", "displayOrder": 0, "hidden": False},
        {"label": "Cancelada pelo lead (avisou antes)", "value": "cancelada_lead", "displayOrder": 1, "hidden": False},
        {"label": "Cancelada por nós", "value": "cancelada_carecode", "displayOrder": 2, "hidden": False},
        {"label": "Outro (descrever em nota no deal)", "value": "outro", "displayOrder": 3, "hidden": False},
    ],
}


def token() -> str:
    t = os.environ.get("HUBSPOT_TOKEN")
    if t:
        return t.strip()
    f = Path.home() / ".carecode_outbound_hstoken"
    if f.exists():
        return f.read_text().strip()
    sys.exit("token não encontrado: defina HUBSPOT_TOKEN ou crie ~/.carecode_outbound_hstoken")


def call(method, path, body=None):
    req = urllib.request.Request(
        BASE + path, method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token()}", "Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return r.status, json.loads(r.read() or b"{}")
    except urllib.error.HTTPError as e:
        return e.code, json.loads(e.read() or b"{}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="cria/completa de verdade (padrão: dry-run)")
    a = ap.parse_args()

    st, atual = call("GET", f"/crm/v3/properties/{OBJ}/{PROP['name']}")
    if st == 404:
        print(f"[novo] {OBJ}.{PROP['name']} não existe — será criada no grupo {GRUPO} com {len(PROP['options'])} opções")
        if a.write:
            st, body = call("POST", f"/crm/v3/properties/{OBJ}", PROP)
            if st in (200, 201):
                print("[✓] criada")
            else:
                sys.exit(f"[✗] POST falhou: {st} {json.dumps(body, ensure_ascii=False)[:400]}")
    elif st == 200:
        tem = {o["value"] for o in atual.get("options", [])}
        faltam = [o for o in PROP["options"] if o["value"] not in tem]
        print(f"[=] já existe (grupo {atual.get('groupName')}, {len(tem)} opções)")
        if faltam:
            print("    faltam:", ", ".join(o["value"] for o in faltam))
            if a.write:
                st, body = call("PATCH", f"/crm/v3/properties/{OBJ}/{PROP['name']}",
                                {"options": atual["options"] + faltam})
                print("[✓] opções acrescentadas" if st == 200 else f"[✗] PATCH falhou: {st} {body}")
        else:
            print("    nada a fazer")
    else:
        sys.exit(f"[✗] GET falhou: {st} {json.dumps(atual, ensure_ascii=False)[:400]}")

    if not a.write:
        print("\n(dry-run — rode com --write para aplicar)")
    print("\nDepois, na UI: Configurações › Objetos › Negócios › Lógica condicional de propriedade →"
          "\n  quando `Demo aceita` = Não realizada → mostrar e exigir `Motivo da não realização`.")


if __name__ == "__main__":
    main()
