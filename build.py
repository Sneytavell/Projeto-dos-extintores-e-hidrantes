"""Monta o sistema em um único arquivo: dist/sistema-extintores-hidrantes.html"""
from pathlib import Path
raiz = Path(__file__).parent
html = (raiz / 'src/head.html').read_text(encoding='utf-8') + (raiz / 'src/body.html').read_text(encoding='utf-8')
html = html.replace('__DATA__', (raiz / 'dados/inventario.json').read_text(encoding='utf-8'), 1)
(raiz / 'dist').mkdir(exist_ok=True)
(raiz / 'dist/sistema-extintores-hidrantes.html').write_text(html, encoding='utf-8')
# página inicial para hospedagem estática (Vercel)
(raiz / 'dist/index.html').write_text('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n' + html + '\n</html>', encoding='utf-8')
print('OK: dist/sistema-extintores-hidrantes.html')
