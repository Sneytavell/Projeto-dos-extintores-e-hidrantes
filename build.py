"""Monta o sistema.
- dist/sistema-extintores-hidrantes.html: versão para o Artifact do Claude (banco do Claude).
- dist/index.html: versão para hospedagem (Vercel), com banco Firebase configurado em firebase-config.js.
"""
from pathlib import Path
import shutil
raiz = Path(__file__).parent
CORPO = (raiz / 'src/body.html').read_text(encoding='utf-8'); CORPO_INI = CORPO[:CORPO.index('</style>') + len('</style>')]  # o snippet entra logo depois do bloco de estilos
html = (raiz / 'src/head.html').read_text(encoding='utf-8') + CORPO
html = html.replace('__DATA__', (raiz / 'dados/inventario.json').read_text(encoding='utf-8'), 1)
dist = raiz / 'dist'; dist.mkdir(exist_ok=True)
(dist / 'sistema-extintores-hidrantes.html').write_text(html, encoding='utf-8')
FB = '10.12.2'
scripts = ''.join(f'<script src="https://www.gstatic.com/firebasejs/{FB}/firebase-{m}-compat.js"></script>\n' for m in ('app', 'auth', 'firestore'))
# tela "404" (fora do ar): ligada/desligada em site-status.js
fora = (raiz / 'src/fora-do-ar.html').read_text(encoding='utf-8')
(dist / 'index.html').write_text('<!doctype html>\n<html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">\n'
    + '<script src="site-status.js"></script>\n' + scripts + '<script src="firebase-config.js"></script>\n' + html.replace(CORPO_INI, CORPO_INI + '\n' + fora, 1) + '\n</html>', encoding='utf-8')
shutil.copy(raiz / 'firebase-config.js', dist / 'firebase-config.js')
shutil.copy(raiz / 'site-status.js', dist / 'site-status.js')
print('OK: dist/index.html e dist/sistema-extintores-hidrantes.html')
