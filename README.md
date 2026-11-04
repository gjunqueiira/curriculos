# Gerador de Currículo

## Por que este projeto existe

Montar currículo em Word/Canva é chato: cada ajuste quebra o layout, manter uma versão em português e outra em inglês sincronizadas dá trabalho, e o resultado raramente sai com cara profissional e consistente.

A ideia aqui é **facilitar a geração do currículo**: você só escreve o conteúdo num arquivo YAML e o script gera HTML e PDF prontos, sempre no mesmo formato. O layout já vem **padronizado com base no template de currículo da Yale** (Yale College General Template) — uma coluna, fonte serifada, seções com linha inferior, sem foto — um formato limpo, aceito em qualquer lugar e fácil de ler por recrutadores e sistemas de triagem (ATS).

Não tem nenhum modelo de IA ou machine learning no meio. Daria pra colocar (gerar texto, adaptar o currículo pra cada vaga etc.), mas *it is not that deep*: é só um template Jinja2 + CSS, preenchido com seus dados e convertido em PDF pelo WeasyPrint. Simples, previsível e sem dependência de API.

## Como usar

Edite `data.yaml` (português) e/ou `data_en.yaml` (inglês) com seus dados e rode:

```powershell
.\.venv\Scripts\python gerar.py
```

Isso sempre gera as duas versões: `curriculo.html`/`curriculo.pdf` (a partir de `data.yaml`) e `curriculo_en.html`/`curriculo_en.pdf` (a partir de `data_en.yaml`).

## Conteúdo por idioma

`data.yaml` e `data_en.yaml` são arquivos independentes, cada um com a estrutura completa (título, perfil, habilidades, experiências, certificações e rótulos das seções). A versão em inglês **não** é gerada por tradução automática do português — o texto de `data_en.yaml` deve ser escrito/revisado diretamente em inglês (idealmente com apoio de um LLM), para não sair uma tradução ao pé da letra.

## Arquivos

- `data.yaml` — conteúdo do currículo em português (edite este).
- `data_en.yaml` — conteúdo do currículo em inglês (edite este, independentemente do PT).
- `template.html` — estrutura HTML (Jinja2), compartilhada pelos dois idiomas.
- `style.css` — visual do currículo.
- `gerar.py` — script que gera o PDF em português e inglês a partir dos dois arquivos de dados.
- `reais_base/` — currículos de referência (layout original em Canva/LinkedIn e template Yale) usados como base de design e conteúdo.

Para pedir ajustes de conteúdo, edite `data.yaml`. Para mudar o visual (cores, fontes, espaçamento), edite `style.css`. Layout atual: modelo Yale (1 coluna, serifada, cabeçalhos de seção com linha inferior, sem foto), baseado em `reais_base/Yale-College-General-Template-v.2.docx`. Sem seção de formação acadêmica.

## Setup (se o venv não existir)

```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\pip install -r requirements.txt
```

## Windows: dependência do WeasyPrint

O WeasyPrint precisa do Pango (GTK). Está instalado via MSYS2 em `D:\msys64` (pacote `mingw-w64-ucrt-x86_64-pango`). O `gerar.py` aponta automaticamente para `D:\msys64\ucrt64\bin`; para outro local, defina a variável `WEASYPRINT_DLL_DIRECTORIES`.
