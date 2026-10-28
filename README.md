# Sistema de Extintores e Hidrantes — ALBRAS

Controle de extintores e hidrantes da brigada: painel de status, inspeção mensal, cronograma e distribuição de planilhas por equipe, indicadores (validade, inspeção mensal, realizado x planejado, comparativo de grupos), cadastro de pessoas e perfis, login por matrícula + PIN e geração das planilhas de campo do mês.

O sistema roda como um Artifact no Claude (os dados compartilhados ficam no banco do Artifact). Link de uso: https://claude.ai/artifact/XsYzLbr8YPrFSrCTczdhzJ

## Estrutura
- `src/head.html` — título, fontes e estilos (cores ALBRAS).
- `src/body.html` — telas e todo o JavaScript.
- `dados/inventario.json` — inventário base (1.191 extintores, 168 hidrantes) e grupos de inspeção.
- `build.py` — junta tudo em `dist/sistema-extintores-hidrantes.html`.
- `docs/historico-de-etapas.md` — o que foi feito em cada versão.

## Gerar o arquivo
```
python build.py
```
