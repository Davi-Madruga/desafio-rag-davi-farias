from pathlib import Path

pasta_documentos = Path("httpx/docs")
arquivos = pasta_documentos.rglob("*.md")
documentos = []

for arquivo in arquivos:
    texto = arquivo.read_text(encoding="utf-8")

    documento = {
        "arquivo": arquivo.name,
        "caminho":str(arquivo),
        "texto":texto
    }
    documentos.append(documento)
