# Assets dos carrosséis Fabris Pelo Mundo

Arquivos fixos para gerar os slides sem depender de nada externo.

- `logo.png` — bonequinho cobre/prata, fundo transparente, 138×106 px (já no tamanho final, com margem). Posição exata no slide 1080×1350: `position:absolute; left:474px; top:1206px; width:138px; height:106px;` (equivale à logo de 96 px centralizada a 42 px do rodapé). Vai no slide 1 e no slide 9.
- `pen.woff2` + `pen-ext.woff2` — fonte manuscrita (Caveat 600, latin e latin-ext). Use como `font-family:'Pen'` com dois `@font-face` (o segundo com `unicode-range:U+0100-02AF,...`). Ver `../2026-10-28/lote-2026-10-28-slides.py`.
- `render.py` — `python3 render.py arquivo.html pasta_saida prefixo` exporta cada `section.slide` em PNG 1080×1350 com Playwright/Chromium.
- Inter vem do sistema (fonte instalada no ambiente); se faltar, instale `@fontsource/inter` e declare o `@font-face`.

Script de referência mais recente: `2026-10-28/lote-2026-10-28-slides.py`.
