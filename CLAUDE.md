# Instruções do projeto

- Código-fonte: `src/head.html` (estilos) e `src/body.html` (telas + JavaScript). Inventário base em `dados/inventario.json`.
- Gerar o sistema: `python build.py` → `dist/sistema-extintores-hidrantes.html` (é o arquivo publicado como Artifact no Claude).
- A cada alteração do sistema: atualizar `docs/historico-de-etapas.md`, gerar o `dist`, fazer commit e push na `main` (pedido do Luiz).
- Textos da interface em português do Brasil; números com vírgula decimal; cores ALBRAS (`--accent #2e3192`).
- Dados da equipe (inspeções, pessoas, entregas) ficam no banco do Artifact, não no repositório.
