from datetime import datetime, timedelta
import requests
import hashlib

TOKEN = "mRvd11QSxXs5LUL$CfW1"
USER = "02297349289"
URL = "https://api-horas-extras.onrender.com/consultar-horas-extras"

def gerar_token():
    hoje = datetime.now().strftime("%d/%m/%Y")
    return hashlib.sha256((TOKEN + hoje).encode()).hexdigest()

def gerar_datas(dia_inicio, dia_fim):
    data_atual = dia_inicio
    while data_atual <= dia_fim:
        data_final = data_atual + timedelta(days=29)
        yield (data_atual.strftime("%d/%m/%Y"), min(data_final, dia_fim).strftime("%d/%m/%Y"))
        data_atual = data_final + timedelta(days=1)

def baixar_todos_dados():
    inicio = datetime.strptime("01/01/2025", "%d/%m/%Y")
    fim = datetime.strptime("31/12/2025", "%d/%m/%Y")

    token = gerar_token()
    headers = {
        "Content-Type": "application/json",
        "User": USER,
        "Token": token
    }

    todos_resultados = []
    for dt_ini, dt_fim in gerar_datas(inicio, fim):
        print(f"🔄 Baixando de {dt_ini} até {dt_fim}")
        resp = requests.get(URL, params={"inicio": dt_ini, "fim": dt_fim}, headers=headers)
        dados = resp.json()
        todos_resultados.append(dados)

    return todos_resultados

dados_completos = baixar_todos_dados()
print("✅ Dados totais:", len(dados_completos))
