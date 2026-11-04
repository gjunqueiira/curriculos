#!/usr/bin/env python3
"""Gera curriculo.html/.pdf (data.yaml) e curriculo_en.html/.pdf (data_en.yaml)."""

import os
import sys
from pathlib import Path

# No Windows o WeasyPrint precisa das DLLs do Pango/GTK (instaladas via MSYS2).
# Pode sobrescrever com a variável de ambiente WEASYPRINT_DLL_DIRECTORIES.
if sys.platform == "win32":
    os.environ.setdefault("WEASYPRINT_DLL_DIRECTORIES", r"D:\msys64\ucrt64\bin")

import yaml
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

BASE_DIR = Path(__file__).parent

# (arquivo de dados, sufixo dos arquivos gerados, código de idioma)
FONTES = [
    ("data.yaml", "", "pt-br"),
    ("data_en.yaml", "_en", "en"),
]


def main():
    env = Environment(loader=FileSystemLoader(BASE_DIR))
    template = env.get_template("template.html")

    for arquivo, sufixo, lang in FONTES:
        data = yaml.safe_load((BASE_DIR / arquivo).read_text(encoding="utf-8"))
        html_out = template.render(**data, lang=lang)

        html_path = BASE_DIR / f"curriculo{sufixo}.html"
        html_path.write_text(html_out, encoding="utf-8")

        pdf_path = BASE_DIR / f"curriculo{sufixo}.pdf"
        HTML(filename=str(html_path), base_url=str(BASE_DIR)).write_pdf(str(pdf_path))

        print(f"Gerado: {html_path.name} e {pdf_path.name}")


if __name__ == "__main__":
    main()
