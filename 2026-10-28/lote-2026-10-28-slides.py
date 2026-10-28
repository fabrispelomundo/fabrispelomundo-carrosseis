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

# ---------------------------------------------------------------- C1 · pauta 7 · capa clara
C1 = []
C1.append(("light", '''<div style="margin-top:40px"></div>
<h1>Guarde este carrossel</h1>
<h1 class="or" style="margin-top:18px; font-size:64px; line-height:1.08">se antes da largada você pensa: “vou mostrar que eu aguento”.</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:40px">
<path d="%s" stroke="var(--pen)" stroke-width="4"/>
<path d="%s" stroke="var(--pen)" stroke-width="4"/>
<g transform="translate(150,130) scale(1.25)"><path d="%s" stroke="var(--ink)" stroke-width="4"/></g>
<g transform="translate(610,130) scale(1.25)"><path d="%s" stroke="var(--ink)" stroke-width="4"/></g>
<path d="M200,262 L200,300 C200,330 220,340 250,340 L420,340" stroke="var(--ink)" stroke-width="4"/>
<path d="M262,262 L262,280 C262,290 268,296 280,296 L420,296" stroke="var(--ink)" stroke-width="4"/>
<path d="M666,262 L666,318 C666,322 670,324 676,324 L860,324" stroke="var(--ink)" stroke-width="4"/>
<path d="M680,262 L680,306 C680,310 684,312 690,312 L860,312" stroke="var(--ink)" stroke-width="4"/>
<text x="444" y="404" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)" transform="rotate(-2 444 404)">mesmo batimento. qual dos dois corre melhor?</text>
</svg>''' % (ecg(30), ecg(498), HEART, HEART), True))

C1.append(("dark", '''<h2>Essa frase parece força.</h2>
<p style="margin-top:40px">Mas repara no que ela traz junto: alguém duvidando de você. E uma prova que vai decidir quem tem razão.</p>
<p>A partir daí, você não larga só para correr. Larga para %s.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">a prova virou<br>um julgamento.</div>''' % hl("se defender"), False))

C1.append(("light", '''<h2>Antes da largada, a cabeça faz uma %s.</h2>
<p style="margin-top:36px">De um lado, o que a prova pede. Do outro, o que você tem para ela. Essa conta é rápida e quase nunca é consciente.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<path d="M444,40 L444,250 M380,250 L508,250" stroke="var(--ink)" stroke-width="5"/>
<path d="M150,70 L738,70" stroke="var(--ink)" stroke-width="5"/>
<circle cx="444" cy="40" r="10" style="fill:var(--ink); stroke:none"/>
<path d="M190,70 L130,170 M190,70 L250,170 M110,170 C130,200 250,200 270,170 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M698,70 L638,170 M698,70 L758,170 M618,170 C638,200 758,200 778,170 Z" stroke="var(--ink)" stroke-width="4"/>
<text x="190" y="234" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">o que a prova pede</text>
<text x="698" y="234" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">o que eu tenho</text>
<path d="M300,300 L230,360 M588,300 L658,360" stroke="var(--mu)" stroke-width="3"/>
<text x="20" y="400" font-family="Inter" font-weight="800" font-size="26" fill="var(--mu)">PEDE MAIS DO QUE TENHO</text>
<text x="20" y="436" font-family="Pen" font-size="40" fill="var(--mu)">→ ameaça</text>
<text x="510" y="400" font-family="Inter" font-weight="800" font-size="26" fill="var(--pen)">TENHO O SUFICIENTE</text>
<text x="510" y="436" font-family="Pen" font-size="40" fill="var(--pen)">→ desafio</text>
</svg>''' % circ("conta"), False))

C1.append(("dark", '''<h2>O coração acelera nos dois casos.</h2>
<p style="margin-top:36px">Perceba onde está a diferença: no desafio, os vasos se abrem e o sangue circula com mais facilidade. Na ameaça, eles se fecham um pouco, e o coração %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:40px">
<path d="M40,10 L40,350 L870,350" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,300 C200,298 260,200 360,190 C500,178 700,180 860,178" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
<text x="560" y="218" font-family="Pen" font-size="34" fill="var(--ink)">batimento: igual nos dois</text>
<path d="M40,320 C200,318 280,160 400,110 C520,64 700,52 860,46" stroke="var(--pen)" stroke-width="5"/>
<text x="860" y="116" text-anchor="end" font-family="Pen" font-size="38" fill="var(--pen)">sangue que chega: desafio</text>
<path d="M40,320 C220,318 300,270 420,262 C560,254 720,262 860,266" stroke="var(--mu)" stroke-width="4"/>
<text x="520" y="306" font-family="Pen" font-size="38" fill="var(--mu)">sangue que chega: ameaça</text>
<text x="740" y="392" font-family="Inter" font-size="22" fill="var(--mu)">largada →</text>
</svg>''' % hl("trabalha mais para entregar menos"), False))

C1.append(("light", '''<h2>“Vou mostrar” coloca um peso a mais na balança.</h2>
<p style="margin-top:36px">Imagine: além dos quilômetros, agora a prova também precisa provar quem você é. O que você tem continua igual. O que ela pede ficou enorme.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:36px">
<path d="M444,40 L444,250 M380,250 L508,250" stroke="var(--ink)" stroke-width="5"/>
<circle cx="444" cy="40" r="10" style="fill:var(--ink); stroke:none"/>
<path d="M150,140 L738,0" stroke="var(--ink)" stroke-width="5"/>
<path d="M190,130 L130,230 M190,130 L250,230 M110,230 C130,260 250,260 270,230 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M698,12 L648,100 M698,12 L748,100 M628,100 C648,124 748,124 768,100 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M60,228 L320,228 L300,120 L80,120 Z" style="fill:var(--pen); fill-opacity:.9; stroke:none" transform="rotate(-1 190 170)"/>
<text x="190" y="166" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="#140C06">PROVAR QUE</text>
<text x="190" y="200" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="#140C06">EU AGUENTO</text>
<text x="698" y="160" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--ink)">o seu treino</text>
<text x="120" y="320" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 120 320)">a prova continua a mesma.</text>
<text x="120" y="370" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 120 370)">a conta, não.</text>
</svg>''', False))

C1.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Mesmo coração. Mesmo batimento.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A conta que você faz antes da largada decide o caminho do sangue.</h1>''', False))

C1.append(("light", qs("Três perguntas para a véspera da próxima prova.", [
    ("O que essa prova pede de você, de verdade?", "Distância, ritmo, percurso. Só o que está no papel."),
    ("O que você já tem para ela?", "Os longões feitos, as semanas cumpridas, as provas que já terminou."),
    ("O que você está tentando provar, e para quem?", "Se a resposta tem um nome, ele entrou na balança.")]), False))

C1.append(("dark", paraquem("Para quem é isso, e para quem não é.",
    "você chega bem treinado na largada, mas com algo a provar, e o corpo responde travado.",
    "o coração dispara junto com dor no peito, tontura ou falta de ar, ou se essa pressão aparece também fora do esporte. Aí o caminho é um médico ou um psicólogo."), False))

C1.append(("light", '''<div style="margin-top:100px"></div>
<h1 style="font-size:78px">Aguentar não é o problema.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">O problema é largar para provar.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para reler na véspera da próxima prova. Ou mande para quem sempre diz que vai mostrar que aguenta.</p>
%s''' % cta_box("manda pra quem", "larga pra provar", "“vou mostrar”", "vou correr a minha"), True))

# ---------------------------------------------------------------- C2 · pauta 8 · capa escura
def week(x, label, w, h, y_base=330):
    return ('<text x="%d" y="40" font-family="Inter" font-weight="700" font-size="22" fill="var(--mu)">%s</text>'
            '<path d="M%d,56 L%d,56" stroke="var(--mu)" stroke-width="2"/>'
            '<rect x="%d" y="%d" width="%d" height="%d" rx="8" stroke="var(--pen)" stroke-width="4"/>'
            % (x, label, x, x + 190, x + (190 - w) // 2, y_base - h, w, h))

C2 = []
C2.append(("dark", '''<div style="margin-top:40px"></div>
<h1>O checklist essencial</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">para quem sempre diz: “essa semana não dá, semana que vem eu faço”.</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:40px">
%s%s%s%s
<text x="95" y="304" text-anchor="middle" font-family="Pen" font-size="30" fill="var(--ink)">longão</text>
<text x="319" y="290" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--ink)">longão</text>
<text x="543" y="262" text-anchor="middle" font-family="Pen" font-size="46" fill="var(--ink)">longão</text>
<text x="767" y="220" text-anchor="middle" font-family="Pen" font-size="60" fill="var(--ink)">longão</text>
<path d="M150,300 C180,270 210,270 240,286 M228,276 L242,288 L224,292" stroke="var(--mu)" stroke-width="3"/>
<path d="M378,280 C404,250 430,250 452,262 M440,252 L454,264 L436,268" stroke="var(--mu)" stroke-width="3"/>
<path d="M610,240 C632,200 650,196 672,204 M660,194 L674,206 L656,212" stroke="var(--mu)" stroke-width="3"/>
<text x="444" y="390" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 390)">o mesmo treino, empurrado. e maior a cada vez.</text>
</svg>''' % (week(0, "SEMANA 1", 90, 60), week(224, "SEMANA 2", 120, 90), week(448, "SEMANA 3", 160, 140), week(672, "SEMANA 4", 200, 230)), True))

C2.append(("light", '''<h2>Item 1: descubra qual treino é sempre o adiado.</h2>
<p style="margin-top:40px">Repara: quase nunca é qualquer treino. É o mesmo, semana após semana. O tiro, o longão, o ritmo de prova.</p>
<p>Aquele que pode mostrar algo que você %s.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">o treino adiado<br>tem nome.</div>''' % hl("prefere não ver"), False))

C2.append(("dark", '''<h2>Item 2: perceba o %s.</h2>
<p style="margin-top:36px">Na hora em que você decide adiar, vem um alívio. Ele é real e é imediato. E é ele que ensina a cabeça a adiar de novo na semana seguinte.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:40px">
<rect x="0" y="40" width="250" height="110" rx="20" stroke="var(--ink)" stroke-width="4"/>
<text x="125" y="88" text-anchor="middle" font-family="Inter" font-weight="700" font-size="26" fill="var(--ink)">o treino difícil</text>
<text x="125" y="122" text-anchor="middle" font-family="Inter" font-weight="700" font-size="26" fill="var(--ink)">se aproxima</text>
<path d="M262,95 L330,95 M316,82 L332,95 L316,108" stroke="var(--ink)" stroke-width="4"/>
<rect x="342" y="40" width="200" height="110" rx="20" stroke="var(--ink)" stroke-width="4"/>
<text x="442" y="106" text-anchor="middle" font-family="Pen" font-size="46" fill="var(--ink)">adiar</text>
<path d="M554,95 L622,95 M608,82 L624,95 L608,108" stroke="var(--ink)" stroke-width="4"/>
<rect x="634" y="28" width="250" height="134" rx="22" stroke="var(--pen)" stroke-width="5"/>
<text x="759" y="108" text-anchor="middle" font-family="Pen" font-size="54" fill="var(--pen)">alívio</text>
<path d="M759,176 C759,330 600,340 442,340 C250,340 125,320 125,166" stroke="var(--pen)" stroke-width="4"/>
<path d="M110,184 L125,162 L140,184" stroke="var(--pen)" stroke-width="4"/>
<text x="260" y="400" font-family="Pen" font-size="40" fill="var(--pen)">na semana que vem, adiar fica mais fácil</text>
</svg>''' % circ("alívio"), False))

C2.append(("light", '''<h2>Item 3: repare no tamanho.</h2>
<p style="margin-top:36px">Perceba: quanto mais semanas o treino fica sem ser feito, maior ele parece. Como ele nunca acontece, nada aparece para %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,250 C300,248 600,252 860,250" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
<text x="560" y="290" font-family="Pen" font-size="38" fill="var(--ink)">o treino de verdade</text>
<path d="M40,250 C220,240 380,200 520,140 C640,90 760,50 860,30" stroke="var(--pen)" stroke-width="5"/>
<text x="150" y="150" font-family="Pen" font-size="40" fill="var(--pen)">o treino na sua cabeça</text>
<text x="640" y="410" font-family="Inter" font-size="22" fill="var(--mu)">semanas adiando →</text>
</svg>''' % hl("contradizer o medo"), False))

C2.append(("dark", '''<h2>Item 4: escreva a previsão antes.</h2>
<p style="margin-top:36px">Imagine anotar o que você acha que vai acontecer: “vou quebrar no terceiro tiro”. Depois do treino, você compara. O que a cabeça aprende está na diferença entre as duas colunas.</p>
<svg class="draw" width="888" height="380" viewBox="0 0 888 380" style="margin-top:36px">
<rect x="40" y="20" width="808" height="300" rx="10" stroke="var(--ink)" stroke-width="4" transform="rotate(-1.5 444 170)"/>
<g transform="rotate(-1.5 444 170)">
<path d="M444,20 L444,320 M40,90 L848,90" stroke="var(--ink)" stroke-width="3"/>
<text x="242" y="68" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" fill="var(--ink)">EU ACHEI</text>
<text x="646" y="68" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" fill="var(--pen)">ACONTECEU</text>
<text x="70" y="160" font-family="Pen" font-size="42" fill="var(--ink)">“quebro no 3º tiro”</text>
<text x="70" y="226" font-family="Pen" font-size="42" fill="var(--ink)">“não termino”</text>
<path d="M480,170 L800,170 M480,236 L800,236" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>
<text x="646" y="292" text-anchor="middle" font-family="Pen" font-size="64" fill="var(--pen)">?</text>
</g>
<text x="440" y="370" font-family="Pen" font-size="38" fill="var(--pen)">só o treino feito preenche</text>
</svg>''', False))

C2.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:74px">Cada semana adiada ensina que o treino era perigoso.</h1>
<h1 class="or" style="font-size:74px; margin-top:22px">Só o treino feito pode ensinar outra coisa.</h1>''', False))

C2.append(("dark", qs("Três perguntas antes de adiar de novo.", [
    ("Qual treino você adiou mais de uma vez este mês?", "O nome dele. Sem justificativa."),
    ("O que você espera que aconteça nele?", "A frase inteira, do jeito que ela vem."),
    ("Qual é a menor parte dele que você faria esta semana?", "Não o treino todo. Só a parte que dá medo.")]), False))

C2.append(("light", paraquem("Para quem é isso, e para quem não é.",
    "você cumpre a planilha inteira, menos o mesmo treino, que vive ficando para a semana que vem.",
    "você adia por dor, lesão ou cansaço que não passa, ou se esse jeito de fugir já tomou conta de outras áreas da vida. Aí o caminho é um médico, um fisioterapeuta ou um psicólogo."), False))

C2.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">O treino que você adia não fica parado.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Ele cresce.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para abrir na próxima vez que pensar em deixar para a semana que vem. Ou mande para quem vive empurrando o mesmo treino.</p>
%s''' % cta_box("manda pra quem", "empurra o longão", "“semana que vem”", "terça, 6h"), True))

# ---------------------------------------------------------------- C3 · pauta 9 · capa clara
def lever(x, y, r, stick, label, color, size, strong=True):
    sw = 4 if strong else 2
    return ('<circle cx="%d" cy="%d" r="%d" stroke="%s" stroke-width="%d"/>'
            '<path d="M%d,%d L%d,%d" stroke="%s" stroke-width="%d"/>'
            '<circle cx="%d" cy="%d" r="%d" style="fill:%s; stroke:none"/>'
            '<text x="%d" y="%d" text-anchor="middle" font-family="Pen" font-size="%d" fill="%s">%s</text>'
            % (x, y, r, color, sw, x, y, x + stick // 3, y - stick, color, sw,
               x + stick // 3, y - stick, max(3, r // 3), color, x, y + r + size + 6, size, color, label))

C3 = []
C3.append(("light", '''<div style="margin-top:40px"></div>
<h1>5 atalhos para quando a cabeça pesa na prova.</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">Quase todo mundo só conhece o último.</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:30px">
<path d="M10,220 L878,220" stroke="var(--ink)" stroke-width="4"/>
<path d="M862,208 L880,220 L862,232" stroke="var(--ink)" stroke-width="4"/>
<text x="10" y="300" font-family="Inter" font-size="22" fill="var(--mu)">semanas antes</text>
<text x="350" y="300" font-family="Inter" font-size="22" fill="var(--mu)">largada</text>
<text x="740" y="300" font-family="Inter" font-size="22" fill="var(--mu)">km 15</text>
%s%s%s%s%s
<path d="M800,130 C760,100 720,90 680,92" stroke="var(--pen)" stroke-width="3"/>
<path d="M800,130 L792,112 M800,130 L782,128" stroke="var(--pen)" stroke-width="3"/>
<text x="380" y="72" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 380 72)">o que quase todo mundo usa</text>
<text x="444" y="380" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--ink)" transform="rotate(-2 444 380)">a menor alavanca é a mais puxada.</text>
</svg>''' % (lever(90, 190, 30, 90, "1", "var(--ink)", 34), lever(250, 190, 30, 90, "2", "var(--ink)", 34),
              lever(430, 190, 30, 90, "3", "var(--ink)", 34), lever(610, 190, 30, 90, "4", "var(--ink)", 34),
              lever(800, 208, 8, 24, "5", "var(--pen)", 30, False)), True))

C3.append(("dark", '''<h2>O último é segurar.</h2>
<p style="margin-top:40px">Engolir a frase, disfarçar a cara, apertar o dente e seguir. Perceba quando ele entra: no km em que a emoção já chegou inteira.</p>
<p>Funciona por fora. Por dentro, ela continua lá, e o corpo %s.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">chega tarde.<br>e cobra caro.</div>''' % hl("gasta mais para manter a tampa fechada"), False))

def step(y, n, title, desc, color, small=False):
    fs = 30 if small else 40
    return ('<circle cx="40" cy="%d" r="%d" style="fill:%s; stroke:none"/>'
            '<text x="40" y="%d" text-anchor="middle" font-family="Inter" font-weight="800" font-size="%d" fill="var(--bg)">%s</text>'
            '<text x="100" y="%d" font-family="Inter" font-weight="800" font-size="%d" fill="%s">%s</text>'
            '<text x="100" y="%d" font-family="Pen" font-size="%d" fill="var(--mu)">%s</text>'
            % (y, 14 if small else 24, color, y + 9, 18 if small else 26, n, y + 10, fs - 6, color, title, y + 50, fs - 4, desc))

C3.append(("light", '''<h2>Antes de segurar, existem %s lugares.</h2>
<svg class="draw" width="888" height="740" viewBox="0 0 888 740" style="margin-top:40px">
<path d="M40,40 L40,660" stroke="var(--mu)" stroke-width="3" stroke-dasharray="3 10"/>
%s%s%s%s%s
</svg>''' % (circ("quatro"),
            step(40, "1", "ESCOLHER", "a prova, a onda de largada, com quem você corre", "var(--ink)"),
            step(180, "2", "AJUSTAR", "chegar antes, a posição, a tela do relógio", "var(--ink)"),
            step(320, "3", "OLHAR", "para onde vai a atenção quando o trecho aperta", "var(--ink)"),
            step(460, "4", "LER", "o que aquele sinal do corpo significa para você", "var(--pen)"),
            step(610, "5", "SEGURAR", "quando todo o resto já passou", "var(--mu)", True)), False))

C3.append(("dark", '''<h2>Quanto mais cedo você mexe, menos ela cresce.</h2>
<p style="margin-top:36px">Repara na diferença: mudar a atenção ou a leitura muda o caminho da emoção. Segurar só muda o que %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,330 C200,320 300,220 420,150 C520,96 620,70 860,60" stroke="var(--ink)" stroke-width="4"/>
<path d="M640,40 L860,40" stroke="var(--ink)" stroke-width="10"/>
<text x="660" y="26" font-family="Pen" font-size="34" fill="var(--ink)">a tampa</text>
<text x="500" y="160" font-family="Pen" font-size="38" fill="var(--ink)">só segurou</text>
<path d="M40,330 C180,320 240,280 300,270 C420,252 640,250 860,252" stroke="var(--pen)" stroke-width="5"/>
<circle cx="300" cy="270" r="12" style="fill:var(--pen); stroke:none"/>
<text x="330" y="320" font-family="Pen" font-size="38" fill="var(--pen)">mexeu antes</text>
<text x="690" y="410" font-family="Inter" font-size="22" fill="var(--mu)">dia da prova →</text>
</svg>''' % hl("aparece por fora"), False))

def button(x, label, worn=False):
    if worn:
        return ('<rect x="%d" y="150" width="130" height="90" rx="20" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="5"/>'
                '<path d="M%d,170 C%d,190 %d,200 %d,226 M%d,166 C%d,200 %d,214 %d,232" stroke="var(--pen)" stroke-width="2"/>'
                '<text x="%d" y="208" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">%s</text>'
                % (x, x + 14, x + 30, x + 50, x + 70, x + 80, x + 96, x + 110, x + 120, x + 65, label))
    return ('<rect x="%d" y="150" width="130" height="90" rx="20" stroke="var(--ink)" stroke-width="3"/>'
            '<text x="%d" y="206" text-anchor="middle" font-family="Pen" font-size="32" fill="var(--mu)">%s</text>' % (x, x + 65, label))

C3.append(("light", '''<h2>Repara qual botão você aperta.</h2>
<p style="margin-top:36px">Os quatro primeiros quase nunca são treinados. Então, no dia, a mão vai direto no único que sobrou.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:44px">
<rect x="4" y="110" width="880" height="170" rx="60" stroke="var(--ink)" stroke-width="5"/>
<circle cx="50" cy="195" r="10" style="fill:var(--pen); stroke:none"/>
%s%s%s%s%s
<text x="200" y="66" font-family="Pen" font-size="36" fill="var(--mu)" transform="rotate(-2 200 66)">esses ainda estão com plástico</text>
<path d="M300,80 C300,110 260,120 230,140" stroke="var(--mu)" stroke-width="3"/>
<text x="520" y="350" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-3 520 350)">gasto de tanto apertar</text>
<path d="M780,310 C790,290 790,270 790,250" stroke="var(--pen)" stroke-width="3"/>
<path d="M778,262 L790,246 L802,262" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % (button(90, "escolher"), button(240, "ajustar"), button(390, "olhar"), button(540, "ler"), button(718, "segurar", True)), False))

C3.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Segurar é o último lugar onde dá para mexer.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Os outros quatro começam antes da largada.</h1>''', False))

C3.append(("light", qs("Três perguntas para a próxima prova.", [
    ("Em que trecho você já sabe que vai pesar?", "O km, a subida, o momento. Antes de largar."),
    ("Para onde vai a sua atenção ali?", "Escolha agora, não no meio do trecho."),
    ("Que leitura você vai dar quando o corpo acelerar?", "Uma frase curta, decidida com calma.")]), False))

C3.append(("dark", paraquem("Para quem é isso, e para quem não é.",
    "no trecho difícil da prova, a única ferramenta que você tem é engolir e aguentar.",
    "a emoção na prova vem com dor no peito, tontura ou falta de ar, ou se segurar tudo virou regra também fora do esporte. Aí o caminho é um médico ou um psicólogo."), False))

C3.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">Engolir é o último recurso.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Não precisa ser o único.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para montar o seu plano antes da próxima prova. Ou mande para quem corre de dente travado.</p>
%s''' % cta_box("manda pra quem", "corre de dente travado", "“aguenta calado”", "escolhe antes", x0=500, w=320), True))

LOTE = [("C1", "vou-mostrar-que-aguento", C1), ("C2", "semana-que-vem", C2), ("C3", "cinco-atalhos", C3)]

def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for code, slug, slides in LOTE:
        assert len(slides) == 9
        html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS
        for i, (theme, body, logo) in enumerate(slides, 1):
            html += slide(theme, i, body, logo=logo, swipe=(i != 9))
        html += "</body></html>"
        open(os.path.join(out_dir, "%s_%s.html" % (code, slug)), "w").write(html)

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "html")
