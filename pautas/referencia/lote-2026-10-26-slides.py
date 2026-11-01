# -*- coding: utf-8 -*-
# Gera o HTML dos carrosséis do lote 26/10 (C1, C2, C3) no padrão Fabris Pelo Mundo.
import sys, os

FONT_CSS = os.environ.get("FONT_CSS", "")
LOGO_DARK = os.environ.get("LOGO_DARK", "logo_dark.png")
LOGO_LIGHT = os.environ.get("LOGO_LIGHT", "logo_light.png")

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
.logo { position:absolute; left:50%; bottom:42px; transform:translateX(-50%); height:96px; }
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
    lg = '<img class="logo" src="%s">' % (LOGO_DARK if theme == "dark" else LOGO_LIGHT) if logo else ""
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

# ---------------------------------------------------------------- C1
C1 = []
C1.append(("dark", '''<div style="margin-top:70px"></div>
<h1>O que ninguém te conta sobre o pace que cai:</h1>
<h1 class="or" style="margin-top:18px">ele nunca chega sozinho.</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:40px">
<rect x="112" y="20" width="96" height="70" rx="10" stroke="var(--mu)" stroke-width="3"/>
<rect x="112" y="310" width="96" height="70" rx="10" stroke="var(--mu)" stroke-width="3"/>
<rect x="60" y="80" width="200" height="240" rx="42" stroke="var(--ink)" stroke-width="5"/>
<rect x="82" y="104" width="156" height="192" rx="26" stroke="var(--mu)" stroke-width="2"/>
<text x="160" y="170" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="var(--mu)">pace</text>
<path d="M160,196 L160,262 M136,240 L160,264 L184,240" stroke="var(--pen)" stroke-width="7"/>
<path d="M286,206 L370,186 C372,118 452,98 600,98 C770,98 852,122 852,198 C852,276 770,298 600,298 C474,298 398,286 382,236 Z" stroke="var(--pen)" stroke-width="4"/>
<text x="616" y="218" text-anchor="middle" font-family="Pen" font-size="66" fill="var(--ink)">“eu sou fraco”</text>
<text x="470" y="368" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-3 470 368)">chegam juntos. sempre.</text>
</svg>''', True))
C1.append(("light", '''<h2>Junto com o número, chega uma frase.</h2>
<p style="margin-top:40px">Repara: o relógio mostra um pace pior do que você queria e, quase no mesmo instante, aparece um pensamento pronto.</p>
<p>“Eu sou fraco.” “Não nasci pra isso.” “%s.”</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">rápida demais<br>pra ter sido pensada.</div>''' % circ("De novo"), False))
C1.append(("dark", '''<h2>Imagine que essa frase é %s.</h2>
<p style="margin-top:40px">Ela não passa por uma análise da prova. Aparece sozinha, rápida, e chega com cara de fato. Por isso quase ninguém pensa em questionar.</p>
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:56px">
<rect x="0" y="40" width="230" height="110" rx="20" stroke="var(--ink)" stroke-width="4"/>
<text x="115" y="104" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="var(--ink)">o número cai</text>
<path d="M240,95 L318,95 M304,82 L320,95 L304,108" stroke="var(--ink)" stroke-width="4"/>
<rect x="330" y="28" width="230" height="134" rx="22" stroke="var(--pen)" stroke-width="5"/>
<text x="445" y="88" text-anchor="middle" font-family="Pen" font-size="46" fill="var(--pen)">a frase</text>
<text x="445" y="128" text-anchor="middle" font-family="Inter" font-size="22" fill="var(--mu)">pronta, automática</text>
<path d="M570,95 L648,95 M634,82 L650,95 L634,108" stroke="var(--ink)" stroke-width="4"/>
<rect x="660" y="40" width="228" height="110" rx="20" stroke="var(--ink)" stroke-width="4"/>
<text x="774" y="92" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="var(--ink)">a perna</text>
<text x="774" y="126" text-anchor="middle" font-family="Inter" font-weight="700" font-size="28" fill="var(--ink)">responde</text>
<path d="M774,162 C774,250 600,250 520,272" stroke="var(--mu)" stroke-width="3" stroke-dasharray="3 10"/>
<text x="150" y="300" font-family="Pen" font-size="44" fill="var(--ink)">você só percebe o fim.</text>
</svg>''' % hl("automática"), False))
C1.append(("light", '''<h2>O que pesa não é só o número.</h2>
<p style="margin-top:40px">Perceba a ordem: o pace cai um pouco, a frase chega, e o que vem depois já não é só sobre o corpo. %s</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:46px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,110 C300,108 600,112 870,110" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
<text x="660" y="94" font-family="Pen" font-size="36" fill="var(--ink)">o plano</text>
<path d="M40,112 C150,112 220,114 280,124 C320,132 340,150 380,154" stroke="var(--pen)" stroke-width="5"/>
<circle cx="390" cy="156" r="12" style="fill:var(--pen); stroke:none"/>
<path d="M402,160 C470,180 520,250 600,290 C680,326 760,334 860,340" stroke="var(--pen)" stroke-width="5"/>
<text x="210" y="196" font-family="Pen" font-size="38" fill="var(--mu)">o corpo</text>
<text x="420" y="132" font-family="Pen" font-size="42" fill="var(--pen)">a frase</text>
<text x="600" y="250" font-family="Pen" font-size="38" fill="var(--ink)">o resto da prova</text>
<text x="790" y="404" font-family="Inter" font-size="22" fill="var(--mu)">km →</text>
</svg>''' % hl("É sobre o que a frase disse de você."), False))
C1.append(("dark", '''<h2>Embaixo da frase, tem uma regra.</h2>
<p style="margin-top:40px">A frase é a parte que aparece. Por baixo dela costuma estar uma regra antiga, escrita bem antes dessa prova, sobre o que você precisa entregar para ter valor.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:50px">
<text x="0" y="96" font-family="Inter" font-weight="800" font-size="92" fill="var(--ink)" letter-spacing="-3">EU SOU FRACO</text>
<text x="4" y="176" font-family="Inter" font-size="19" fill="var(--mu)">* se eu não render sempre, eu não valho.</text>
<circle cx="120" cy="170" r="62" stroke="var(--pen)" stroke-width="5"/>
<path d="M166,214 L240,270" stroke="var(--pen)" stroke-width="12"/>
<path d="M300,262 C380,250 420,232 470,226" stroke="var(--pen)" stroke-width="3"/>
<path d="M456,214 L472,226 L454,238" stroke="var(--pen)" stroke-width="3"/>
<text x="488" y="236" font-family="Pen" font-size="44" fill="var(--pen)">a letra miúda</text>
<text x="40" y="350" font-family="Pen" font-size="46" fill="var(--ink)">“se eu não render sempre, eu não valho.”</text>
</svg>''', False))
C1.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:72px">O pace que cai conta o que aconteceu no km.</h1>
<h1 class="or" style="font-size:72px; margin-top:26px">A frase conta o que você já acreditava antes da largada.</h1>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">duas leituras, uma prova.</div>''', False))
C1.append(("dark", qs("Na próxima vez que o pace cair, três perguntas.", [
    ("O que o relógio mostrou, exatamente?", "O número. Não o que ele significa."),
    ("O que você concluiu sobre você?", "A conclusão é diferente do número."),
    ("Essa conclusão vale para qualquer prova?", "Se vale, ela não veio desta.")]), False))
C1.append(("light", paraquem("Para quem é isso, e para quem não é.",
    "o pace cai alguns segundos e a cabeça transforma isso num julgamento sobre quem você é.",
    "o pace cai junto com dor, tontura ou falta de ar fora do normal, ou se esse pensamento pesa também fora do esporte. Aí o caminho é um médico ou um psicólogo."), False))
C1.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">O pace que cai é um dado.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">A frase que vem junto é uma história antiga.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para reler antes do próximo treino de ritmo. Ou mande para quem sempre diz “eu sou fraco” depois de olhar o relógio.</p>
<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:40px">
<text x="0" y="70" font-family="Pen" font-size="36" fill="var(--pen)">manda pra quem</text>
<text x="0" y="108" font-family="Pen" font-size="36" fill="var(--pen)">briga com o relógio</text>
<path d="M270,90 L440,96 M426,84 L442,96 L428,108" stroke="var(--pen)" stroke-width="3"/>
<rect x="460" y="40" width="340" height="120" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 630 100)"/>
<text x="630" y="96" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--ink)" transform="rotate(-3 630 100)">“eu sou fraco”</text>
<path d="M500,88 L760,80" stroke="var(--pen)" stroke-width="4"/>
<text x="630" y="140" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-3 630 100)">eu li um número</text>
</svg>''', True))

# ---------------------------------------------------------------- C2
C2 = []
C2.append(("light", '''<div style="margin-top:70px"></div>
<h1>Uma ultrapassagem e você desmontou.</h1>
<h1 class="or" style="margin-top:18px; font-size:70px">Eu descobri que isso acontece em 3 passos.</h1>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:40px">
<rect x="20" y="230" width="44" height="26" rx="6" stroke="var(--ink)" stroke-width="4"/>
<circle cx="42" cy="226" r="8" style="fill:var(--pen); stroke:none"/>
<text x="0" y="300" font-family="Pen" font-size="34" fill="var(--mu)">alguém passou</text>
<path d="M64,244 C160,250 200,180 300,200 C400,220 420,140 520,160" stroke="var(--ink)" stroke-width="3" stroke-dasharray="2 9"/>
<path d="M690,40 L712,120 L790,92 L742,156 L830,190 L740,208 L776,290 L700,236 L660,320 L640,232 L560,268 L604,196 L520,164 L612,150 L590,70 L650,124 Z" stroke="var(--pen)" stroke-width="5"/>
<text x="676" y="190" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)">a prova</text>
<text x="676" y="222" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)">inteira</text>
</svg>''', True))
C2.append(("dark", '''<h2>Não foi a pessoa que passou.</h2>
<p style="margin-top:40px">Ela passou e seguiu a prova dela. O que desmontou a sua continuou com você por quilômetros, e começou em outro lugar.</p>
<p>Imagine os três passos como uma %s. Quando você enxerga a ordem, ela deixa de parecer “do nada”.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">o gatilho é pequeno.<br>a reação, não.</div>''' % hl("sequência"), False))
C2.append(("light", '''<h2>Passo 1: a ultrapassagem toca num %s.</h2>
<p style="margin-top:40px">Imagine que você carrega temas com muita história: ficar para trás, ser comparado, não ser suficiente. Quando algo de fora encosta num deles, ele acorda inteiro.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:44px">
<ellipse cx="520" cy="180" rx="150" ry="80" stroke="var(--pen)" stroke-width="5"/>
<text x="520" y="174" text-anchor="middle" font-family="Inter" font-weight="800" font-size="30" fill="var(--ink)">ponto</text>
<text x="520" y="210" text-anchor="middle" font-family="Inter" font-weight="800" font-size="30" fill="var(--ink)">sensível</text>
<path d="M410,124 L330,60" stroke="var(--ink)" stroke-width="3"/><text x="130" y="52" font-family="Pen" font-size="38" fill="var(--ink)">ficar para trás</text>
<path d="M650,130 L720,70" stroke="var(--ink)" stroke-width="3"/><text x="700" y="56" font-family="Pen" font-size="38" fill="var(--ink)">comparação</text>
<path d="M610,250 L690,312" stroke="var(--ink)" stroke-width="3"/><text x="620" y="346" font-family="Pen" font-size="38" fill="var(--ink)">não ser suficiente</text>
<path d="M30,250 C140,250 260,230 362,206" stroke="var(--pen)" stroke-width="4"/>
<path d="M344,194 L364,206 L346,220" stroke="var(--pen)" stroke-width="4"/>
<text x="20" y="300" font-family="Pen" font-size="40" fill="var(--pen)">a ultrapassagem</text>
</svg>''' % hl("ponto sensível"), False))
C2.append(("dark", '''<h2>Passo 2: a reação vem maior que o fato.</h2>
<p style="margin-top:40px">Perceba a desproporção: um evento pequeno, uma resposta grande e rápida. Coração, respiração e pensamento sobem juntos, antes de você decidir qualquer coisa.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:46px">
<path d="M40,10 L40,350 L870,350" stroke="var(--mu)" stroke-width="3"/>
<rect x="120" y="310" width="70" height="40" stroke="var(--ink)" stroke-width="4"/>
<text x="84" y="390" font-family="Pen" font-size="36" fill="var(--ink)">o fato</text>
<path d="M200,346 C260,346 280,60 360,50 C460,40 520,120 600,190 C680,250 760,280 860,290" stroke="var(--pen)" stroke-width="5"/>
<text x="400" y="40" font-family="Pen" font-size="42" fill="var(--pen)">a reação</text>
<text x="560" y="140" font-family="Pen" font-size="34" fill="var(--mu)">e ela demora a baixar</text>
<text x="780" y="390" font-family="Inter" font-size="22" fill="var(--mu)">km →</text>
</svg>''', False))
C2.append(("light", '''<h2>Passo 3: o ponto assume o %s.</h2>
<p style="margin-top:40px">Por alguns quilômetros, quem corre não é o seu plano. É a reação. Você acelera para responder, ou solta o ritmo para não sentir. Nos dois casos, a prova saiu da sua mão.</p>
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:40px">
<circle cx="250" cy="170" r="140" stroke="var(--ink)" stroke-width="6"/>
<circle cx="250" cy="170" r="34" stroke="var(--ink)" stroke-width="4"/>
<path d="M216,170 L114,170 M284,170 L386,170 M250,204 L250,308" stroke="var(--ink)" stroke-width="5"/>
<rect x="176" y="24" width="148" height="46" rx="8" style="fill:var(--pen); stroke:none"/>
<text x="250" y="57" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="#140C06">O PONTO</text>
<text x="470" y="150" font-family="Pen" font-size="42" fill="var(--mu)">o plano?</text>
<text x="470" y="196" font-family="Pen" font-size="42" fill="var(--mu)">foi pro banco de trás.</text>
</svg>''' % circ("volante"), False))
C2.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A ultrapassagem dura um instante.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">O ponto que ela toca, você leva para todas as provas.</h1>''', False))
C2.append(("light", qs("Três perguntas para a próxima ultrapassagem.", [
    ("O que você fez nos quilômetros seguintes?", "Acelerou para responder, ou soltou o ritmo?"),
    ("Que frase apareceu quando a pessoa passou?", "A primeira, antes de qualquer correção."),
    ("Em que parte da prova isso pesa mais?", "No começo, no meio, ou quando você já está cansado?")]), False))
C2.append(("dark", paraquem("Para quem é isso, e para quem não é.",
    "uma ultrapassagem muda o seu ritmo mais do que o próprio cansaço.",
    "a reação vem com dor no peito, falta de ar ou tontura, ou se esse ponto pesa também no trabalho e nas relações. Aí o caminho é um médico ou um psicólogo."), False))
C2.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">Quem passou por você seguiu a prova dela.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">O que ela acordou ficou correndo com você.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para ler antes da próxima prova. Ou mande para quem sempre acelera quando alguém passa.</p>
<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:40px">
<text x="0" y="70" font-family="Pen" font-size="36" fill="var(--pen)">manda pra quem corre</text>
<text x="0" y="108" font-family="Pen" font-size="36" fill="var(--pen)">a prova dos outros</text>
<path d="M300,90 L450,96 M436,84 L452,96 L438,108" stroke="var(--pen)" stroke-width="3"/>
<rect x="470" y="40" width="330" height="120" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 635 100)"/>
<text x="635" y="96" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)" transform="rotate(-3 635 100)">a prova dele</text>
<path d="M520,88 L755,80" stroke="var(--pen)" stroke-width="4"/>
<text x="635" y="140" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 635 100)">a sua</text>
</svg>''', True))

# ---------------------------------------------------------------- C3
C3 = []
C3.append(("dark", '''<div style="margin-top:70px"></div>
<h1>Se eu estivesse começando a correr hoje,</h1>
<h1 class="or" style="margin-top:18px">eu faria exatamente isto:</h1>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:40px">
<rect x="250" y="20" width="420" height="300" rx="10" stroke="var(--ink)" stroke-width="4" transform="rotate(-3 460 170)"/>
<g transform="rotate(-3 460 170)"><path d="M290,100 L630,100 M290,160 L630,160 M290,220 L630,220" stroke="var(--mu)" stroke-width="2"/>
<text x="300" y="150" font-family="Pen" font-size="50" fill="var(--ink)">km</text>
<path d="M370,150 L500,150" stroke="var(--ink)" stroke-width="3"/>
<ellipse cx="436" cy="134" rx="84" ry="38" stroke="var(--pen)" stroke-width="4"/></g>
<path d="M700,60 L560,250" stroke="var(--pen)" stroke-width="8"/>
<path d="M560,250 L552,272 L572,258" stroke="var(--pen)" stroke-width="5"/>
<text x="700" y="320" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-4 700 320)">próxima tela</text>
</svg>''', True))
C3.append(("light", '''<h2>Anotaria o km em que eu não me reconheci.</h2>
<p style="margin-top:40px">Aquele trecho em que você virou alguém que não costuma mostrar: irritado, assustado, com vontade de parar, falando sozinho.</p>
<p>Imagine anotar esse km, em vez de %s.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">esse km tem informação.</div>''' % hl("apagar ele da memória"), False))
C3.append(("dark", '''<h2>Imagine que você corre com uma %s.</h2>
<p style="margin-top:40px">Forte, disciplinado, sempre bem. É a versão que aparece no treino, no grupo, na foto de chegada. Ela não é falsa. Só não é tudo.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:46px">
<text x="80" y="40" font-family="Inter" font-weight="800" font-size="24" fill="var(--pen)">O QUE APARECE</text>
<text x="80" y="100" font-family="Pen" font-size="44" fill="var(--ink)">forte</text>
<text x="80" y="150" font-family="Pen" font-size="44" fill="var(--ink)">disciplinado</text>
<text x="80" y="200" font-family="Pen" font-size="44" fill="var(--ink)">sempre bem</text>
<path d="M420,10 C424,120 416,240 422,350" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>
<text x="500" y="40" font-family="Inter" font-weight="800" font-size="24" fill="var(--mu)">O QUE FICA DE FORA</text>
<text x="500" y="100" font-family="Pen" font-size="44" fill="var(--mu)">cansaço</text>
<text x="500" y="150" font-family="Pen" font-size="44" fill="var(--mu)">medo</text>
<text x="500" y="200" font-family="Pen" font-size="44" fill="var(--mu)">dúvida</text>
<text x="300" y="320" font-family="Pen" font-size="38" fill="var(--pen)">a linha do que pode aparecer</text>
</svg>''' % hl("versão oficial"), False))
C3.append(("light", '''<h2>Perceba o que acontece quando o cansaço sobe.</h2>
<p style="margin-top:40px">Enquanto a prova está fácil, a versão oficial dá conta. Conforme o cansaço cresce, sustentar a imagem custa mais, e o que estava guardado %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:46px">
<path d="M40,10 L40,350 L870,350" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,320 C240,310 440,260 600,170 C700,110 780,60 860,40" stroke="var(--ink)" stroke-width="4"/>
<text x="700" y="140" font-family="Pen" font-size="38" fill="var(--ink)">cansaço</text>
<path d="M40,200 C300,200 520,204 620,212 C700,220 760,250 860,330" stroke="var(--pen)" stroke-width="5"/>
<text x="120" y="186" font-family="Pen" font-size="38" fill="var(--pen)">a imagem segura</text>
<circle cx="606" cy="190" r="22" stroke="var(--pen)" stroke-width="4"/>
<text x="520" y="300" font-family="Pen" font-size="38" fill="var(--mu)">aqui começa a vazar</text>
<text x="780" y="390" font-family="Inter" font-size="22" fill="var(--mu)">km →</text>
</svg>''' % hl("começa a vazar"), False))
C3.append(("dark", '''<h2>E aí vem o km do estranhamento.</h2>
<p style="margin-top:40px">Repara: não é outra pessoa correndo. É uma parte sua que ficou sem espaço. Como nunca treinou junto, ela aparece sem aviso e no pior momento.</p>
<svg class="draw" width="888" height="380" viewBox="0 0 888 380" style="margin-top:40px">
<path d="M380,8 L380,50" stroke="var(--mu)" stroke-width="3"/>
<path d="M160,60 L600,60 L600,250 L520,330 L160,330 Z" stroke="var(--ink)" stroke-width="5"/>
<rect x="340" y="44" width="80" height="22" rx="8" stroke="var(--ink)" stroke-width="3"/>
<text x="190" y="140" font-family="Inter" font-weight="800" font-size="34" fill="var(--ink)">FORTE</text>
<text x="190" y="190" font-family="Inter" font-weight="800" font-size="34" fill="var(--ink)">DISCIPLINADO</text>
<text x="190" y="240" font-family="Inter" font-weight="800" font-size="34" fill="var(--ink)">SEMPRE BEM</text>
<path d="M600,250 L640,318 L520,330" stroke="var(--pen)" stroke-width="4"/>
<path d="M600,250 L520,330" stroke="var(--pen)" stroke-width="2" stroke-dasharray="3 6"/>
<text x="660" y="270" font-family="Pen" font-size="40" fill="var(--pen)">no verso:</text>
<text x="660" y="314" font-family="Pen" font-size="40" fill="var(--pen)">cansado.</text>
<text x="660" y="358" font-family="Pen" font-size="40" fill="var(--pen)">com medo.</text>
</svg>''', False))
C3.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Você não deixou de ser você naquele km.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Você encontrou a parte que nunca leva para correr.</h1>''', False))
C3.append(("dark", qs("Três perguntas depois da sua próxima prova.", [
    ("Em que km você não se reconheceu?", "Anote o número, mesmo que pareça bobo."),
    ("Quem apareceu ali?", "Descreva com três palavras, sem julgar."),
    ("Essa parte tem espaço no seu treino?", "Ou só aparece quando você não aguenta mais segurar?")]), False))
C3.append(("light", paraquem("Para quem é isso, e para quem não é.",
    "existe um trecho da prova em que você vira alguém que não reconhece, e depois prefere não lembrar.",
    "esse estranhamento aparece também fora da corrida, com frequência, ou vem com tontura, dor ou falta de ar. Aí o caminho é um médico ou um psicólogo."), False))
C3.append(("dark", '''<div style="margin-top:100px"></div>
<h1 style="font-size:70px">A versão que te leva até a largada nem sempre é a que termina a prova.</h1>
<h1 class="or" style="font-size:70px; margin-top:18px">As duas correm com você.</h1>
<p class="mu" style="margin-top:46px; max-width:860px">Salve para reler depois da próxima prova. Ou mande para quem sempre diz que está tudo bem.</p>
<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:36px">
<text x="0" y="70" font-family="Pen" font-size="36" fill="var(--pen)">manda pra quem</text>
<text x="0" y="108" font-family="Pen" font-size="36" fill="var(--pen)">nunca está cansado</text>
<path d="M270,90 L440,96 M426,84 L442,96 L428,108" stroke="var(--pen)" stroke-width="3"/>
<rect x="460" y="40" width="340" height="120" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 630 100)"/>
<text x="630" y="96" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--ink)" transform="rotate(-3 630 100)">“tô sempre bem”</text>
<path d="M500,88 L760,80" stroke="var(--pen)" stroke-width="4"/>
<text x="630" y="140" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-3 630 100)">hoje, não muito</text>
</svg>''', True))

LOTE = [("C1", "pace-que-cai", C1), ("C2", "uma-ultrapassagem", C2), ("C3", "naquele-km", C3)]

def build(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    for code, slug, slides in LOTE:
        html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><style>%s</style></head><body>' % CSS
        for i, (theme, body, logo) in enumerate(slides, 1):
            html += slide(theme, i, body, logo=logo, swipe=(i != 9))
        html += "</body></html>"
        open(os.path.join(out_dir, "%s_%s.html" % (code, slug)), "w").write(html)

if __name__ == "__main__":
    build(sys.argv[1] if len(sys.argv) > 1 else "html")
