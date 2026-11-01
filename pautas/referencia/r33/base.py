# -*- coding: utf-8 -*-
# Gera o HTML dos carrosséis do lote 28/10/2026 (C1, C2, C3) no padrão Fabris Pelo Mundo.
# Categoria de gancho do lote: praticidade. Pautas 7, 8 e 9.
import sys, os

PEN = os.environ.get("PEN_FONT", "pen.woff2")
PEN_EXT = os.environ.get("PEN_FONT_EXT", "pen-ext.woff2")
LOGO = os.environ.get("LOGO", "logo.png")

FONT_CSS = ("@font-face { font-family:'Pen'; src:url('%s') format('woff2'); font-weight:600; unicode-range:U+0000-00FF,U+0131,U+0152-0153,U+02BB-02BC,U+02C6,U+02DA,U+02DC,U+0304,U+0308,U+0329,U+2000-206F,U+2074,U+20AC,U+2122,U+2191,U+2193,U+2212,U+2215,U+FEFF,U+FFFD; }\n"
            "@font-face { font-family:'Pen'; src:url('%s') format('woff2'); font-weight:600; unicode-range:U+0100-02AF,U+0304,U+0308,U+0329,U+1E00-1E9F,U+1EF2-1EFF,U+2020,U+20A0-20AB,U+20AD-20C0,U+2113,U+2C60-2C7F,U+A720-A7FF; }\n"
            "@font-face { font-family:'Pen'; src:url('%s') format('woff2'); font-weight:400; }\n") % (PEN, PEN_EXT, PEN)

CSS = FONT_CSS + r"""
* { margin:0; padding:0; box-sizing:border-box; }
body { background:#555; padding:40px; display:flex; flex-direction:column; gap:40px; align-items:center; }
.slide { width:1080px; height:1350px; overflow:hidden; position:relative; flex:none; font-family:'Inter', sans-serif; }
.light { --bg:#F1ECE3; --ink:#151413; --mu:#5E5951; --pen:#F0640F; --line:rgba(21,20,19,.10); --hl:rgba(240,100,15,.30); background:var(--bg); color:var(--ink); }
.dark  { --bg:#111111; --ink:#F3EFE8; --mu:#A39D94; --pen:#FF7A1A; --line:rgba(255,255,255,.07); --hl:rgba(255,122,26,.34); background:radial-gradient(120% 90% at 50% 35%, #1E1E1F 0%, #0C0C0C 100%); color:var(--ink); }
.grain { position:absolute; inset:0; pointer-events:none; opacity:.55; }
.light .grain { opacity:.35; }
.rules { position:absolute; inset:0; background-image:linear-gradient(var(--line) 1px, transparent 1px); background-size:100% 64px; background-position:0 30px; opacity:.55; }
.top { position:absolute; top:64px; left:96px; right:96px; display:flex; justify-content:space-between; align-items:center; font-size:20px; font-weight:600; letter-spacing:.22em; color:var(--mu); }
.bottom { position:absolute; bottom:60px; left:96px; right:96px; display:flex; justify-content:space-between; align-items:center; }
.swipe { font-family:'Pen'; font-size:44px; color:var(--pen); transform:rotate(-3deg); }
.content { position:absolute; top:170px; left:96px; right:96px; bottom:150px; display:flex; flex-direction:column; }
h1 { font-weight:800; font-size:84px; line-height:1.04; letter-spacing:-.03em; }
h2 { font-weight:800; font-size:62px; line-height:1.08; letter-spacing:-.025em; }
p { font-size:35px; line-height:1.42; font-weight:400; color:var(--ink); }
p.mu { color:var(--mu); }
p + p { margin-top:24px; }
.or { color:var(--pen); }
.hl { background:linear-gradient(180deg, transparent 58%, var(--hl) 58%, var(--hl) 92%, transparent 92%); padding:0 4px; -webkit-box-decoration-break:clone; box-decoration-break:clone; }
.circ { position:relative; white-space:nowrap; }
.circ svg { position:absolute; left:-22px; top:-16px; width:calc(100% + 44px); height:calc(100% + 32px); overflow:visible; }
.note { font-family:'Pen'; color:var(--pen); font-size:48px; line-height:1.05; }
svg.draw path, svg.draw line, svg.draw polyline, svg.draw ellipse, svg.draw rect, svg.draw circle { fill:none; stroke-linecap:round; stroke-linejoin:round; }
svg text { stroke:none; }
.q { display:flex; gap:26px; align-items:flex-start; padding:30px 0; border-top:2px dashed var(--line); }
.q:first-of-type { border-top:none; }
.q .n { font-family:'Pen'; font-size:76px; line-height:.8; color:var(--pen); width:60px; flex:none; }
.q .t { font-size:42px; font-weight:700; line-height:1.15; letter-spacing:-.01em; }
.q .d { font-size:30px; line-height:1.38; color:var(--mu); margin-top:10px; }
.lab { font-size:22px; font-weight:700; letter-spacing:.2em; text-transform:uppercase; margin-bottom:14px; }
.sep { border-top:2px dashed var(--line); margin:38px 0; }
.content > .lab:first-child { font-size:46px; font-weight:800; letter-spacing:-.02em; text-transform:none; color:var(--mu) !important; margin-bottom:4px; line-height:1.1; }
.logo { position:absolute; left:474px; top:1206px; width:138px; height:106px; }
"""

GRAIN = '<svg class="grain" width="1080" height="1350"><filter id="n"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 0 0.5  0 0 0 .09 0"/></filter><rect width="100%" height="100%" filter="url(#n)"/></svg>'

def circ(word, rot=-2):
    return ('<span class="circ">%s<svg viewBox="0 0 100 40" preserveAspectRatio="none" style="transform:rotate(%ddeg)">'
            '<path d="M8,22 C6,8 40,2 62,4 C88,6 98,14 96,24 C94,36 60,39 36,37 C14,35 2,28 10,14 C14,8 22,6 30,5" '
            'fill="none" stroke="var(--pen)" vector-effect="non-scaling-stroke" style="stroke-width:4px" stroke-linecap="round"/></svg></span>') % (word, rot)

def hl(t): return '<span class="hl">%s</span>' % t

def slide(theme, n, body, logo=False, swipe=True):
    rules = '<div class="rules"></div>' if theme == "light" else ""
    sw = '<div class="swipe">arraste →</div>' if swipe else '<div></div>'
    lg = '<img class="logo" src="%s">' % LOGO if logo else ""
    return ('<section class="slide %s">%s%s<div class="top"><span></span><span>%02d / 09</span></div>'
            '<div class="content">%s</div><div class="bottom"><span></span>%s</div>%s</section>') % (theme, rules, GRAIN, n, body, sw, lg)

def qs(title, items):
    out = '<h2 style="margin-bottom:34px">%s</h2>' % title
    for i, (t, d) in enumerate(items, 1):
        out += '<div class="q"><div class="n">%d</div><div><div class="t">%s</div><div class="d">%s</div></div></div>' % (i, t, d)
    return out

SIGNPOST = '''<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto">
<line x1="444" y1="20" x2="444" y2="196" stroke="var(--ink)" stroke-width="4"/>
<path d="M452,40 L640,40 L668,62 L640,84 L452,84 Z" stroke="var(--pen)" stroke-width="4"/>
<text x="476" y="74" font-family="Pen" font-size="38" fill="var(--pen)">aqui</text>
<path d="M436,104 L170,104 L142,126 L170,148 L436,148 Z" stroke="var(--mu)" stroke-width="3"/>
<text x="182" y="137" font-family="Pen" font-size="32" fill="var(--mu)">outro profissional</text>
</svg>'''

def paraquem(title, sim, nao):
    return ('<h2 style="margin-bottom:46px">%s</h2><div class="lab or">É para você se</div><p>%s</p>'
            '<div class="sep"></div><div class="lab" style="color:var(--mu)">Não é para você se</div><p>%s</p>%s') % (title, sim, nao, SIGNPOST)

def cta_box(l1, l2, tag, fix, x0=460, w=340):
    cx = x0 + w // 2
    return '''<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:40px">
<text x="0" y="70" font-family="Pen" font-size="36" fill="var(--pen)">%s</text>
<text x="0" y="108" font-family="Pen" font-size="36" fill="var(--pen)">%s</text>
<path d="M%d,90 L%d,96 M%d,84 L%d,96 L%d,108" stroke="var(--pen)" stroke-width="3"/>
<rect x="%d" y="40" width="%d" height="120" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 %d 100)"/>
<text x="%d" y="96" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)" transform="rotate(-3 %d 100)">%s</text>
<path d="M%d,88 L%d,80" stroke="var(--pen)" stroke-width="4"/>
<text x="%d" y="140" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-3 %d 100)">%s</text>
</svg>''' % (l1, l2, x0 - 190, x0 - 20, x0 - 34, x0 - 18, x0 - 32, x0, w, cx, cx, cx, tag, x0 + 34, x0 + w - 34, cx, cx, fix)

HEART = "M0,30 C0,0 40,-6 50,22 C60,-6 100,0 100,30 C100,62 62,82 50,104 C38,82 0,62 0,30 Z"

def ecg(x0):
    return ("M%d,60 L%d,60 L%d,30 L%d,98 L%d,10 L%d,74 L%d,60 L%d,60 L%d,30 L%d,98 L%d,10 L%d,74 L%d,60 L%d,60"
            % (x0, x0+60, x0+76, x0+92, x0+108, x0+124, x0+138, x0+210, x0+226, x0+242, x0+258, x0+274, x0+288, x0+360))


# ------------------------------------------------------------------ helpers do projeto 33
import glob as _glob
_HERE = os.path.dirname(os.path.abspath(__file__))

def build_html(slides, path):
    """slides: lista de 9 tuplas (theme, body_html, logo_bool). Logo obrigatória nos slides 1 e 9."""
    assert len(slides) == 9, "precisa de 9 slides"
    html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS
    for i, (theme, body, logo) in enumerate(slides, 1):
        html += slide(theme, i, body, logo=logo, swipe=(i != 9 and not logo))
    html += "</body></html>"
    open(path, "w").write(html)
