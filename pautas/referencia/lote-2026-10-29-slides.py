# -*- coding: utf-8 -*-
# Gera o HTML dos carrosséis do lote 29/10/2026 (C1, C2, C3) no padrão Fabris Pelo Mundo.
# Categoria de gancho do lote: alerta / erro (resultado / prova social pulada por falta de material). Pautas 10, 11 e 12.
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

def trophy(cx, top, s=1.0, label=None, label_rot=-8, peel=False):
    # troféu desenhado à caneta, centrado em cx
    def X(v): return cx + v * s
    def Y(v): return top + v * s
    out = ('<path d="M%d,%d L%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" stroke="var(--ink)" stroke-width="4"/>'
           % (X(-100), Y(0), X(100), Y(0), X(100), Y(110), X(56), Y(160), X(0), Y(170), X(-56), Y(160), X(-100), Y(110), X(-100), Y(0)))
    out += ('<path d="M%d,%d C%d,%d %d,%d %d,%d M%d,%d C%d,%d %d,%d %d,%d" stroke="var(--ink)" stroke-width="4"/>'
            % (X(-100), Y(30), X(-156), Y(30), X(-156), Y(100), X(-92), Y(110), X(100), Y(30), X(156), Y(30), X(156), Y(100), X(92), Y(110)))
    out += '<path d="M%d,%d L%d,%d" stroke="var(--ink)" stroke-width="4"/>' % (X(0), Y(170), X(0), Y(220))
    out += '<rect x="%d" y="%d" width="%d" height="%d" rx="4" stroke="var(--ink)" stroke-width="4"/>' % (X(-60), Y(220), 120 * s, 26 * s)
    out += '<rect x="%d" y="%d" width="%d" height="%d" rx="4" stroke="var(--ink)" stroke-width="4"/>' % (X(-90), Y(246), 180 * s, 40 * s)
    if label:
        lx, ly = X(0), Y(78)
        out += ('<g transform="rotate(%d %d %d)"><rect x="%d" y="%d" width="%d" height="%d" rx="6" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3"/>'
                '<text x="%d" y="%d" text-anchor="middle" font-family="Pen" font-size="%d" fill="var(--ink)">%s</text>'
                % (label_rot, lx, ly, lx - 82 * s, ly - 30 * s, 164 * s, 62 * s, lx, ly + 13 * s, int(42 * s), label))
        if peel:
            out = out.replace('<g transform="rotate(%d %d %d)"><rect x="%d" y="%d" width="%d" height="%d" rx="6" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3"/>'
                              % (label_rot, lx, ly, lx - 82 * s, ly - 30 * s, 164 * s, 62 * s),
                              '<g transform="rotate(%d %d %d)"><path d="M%d,%d L%d,%d L%d,%d L%d,%d L%d,%d Z" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" stroke-linejoin="round"/>'
                              % (label_rot, lx, ly, lx - 82 * s, ly - 30 * s, lx + 82 * s, ly - 30 * s, lx + 82 * s, ly + 2 * s, lx + 50 * s, ly + 32 * s, lx - 82 * s, ly + 32 * s))
            out += ('<path d="M%d,%d L%d,%d L%d,%d Z" style="fill:var(--pen)" stroke="var(--pen)" stroke-width="3" stroke-linejoin="round"/>'
                    % (lx + 82 * s, ly + 2 * s, lx + 50 * s, ly + 32 * s, lx + 96 * s, ly + 50 * s))
        out += '</g>'
    return out

# ---------------------------------------------------------------- C1 · pauta 10 · capa escura
C1 = []
C1.append(("dark", '''<div style="margin-top:40px"></div>
<h1>Pare de chamar a sua melhor prova de sorte</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">se você quer que ela se repita.</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:40px">
%s
<path d="M640,110 C600,96 570,104 548,122 M560,108 L546,124 L566,128" stroke="var(--pen)" stroke-width="3"/>
<text x="650" y="96" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 650 96)">o que tem</text>
<text x="650" y="136" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 650 136)">embaixo?</text>
</svg>''' % trophy(444, 50, 1.15, "sorte", -9, True), True))

C1.append(("light", '''<h2>Sorte é uma explicação que não volta.</h2>
<p style="margin-top:40px">Perceba o que essa palavra faz: ela coloca a causa fora de você e diz que ela só valeu para aquele dia.</p>
<p>E o que só valeu para aquele dia não tem por que %s.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">a prova boa<br>vira acidente.</div>''' % hl("aparecer na próxima largada"), False))

def cell(x, y, l1, l2, color="var(--ink)"):
    return ('<text x="%d" y="%d" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="%s">%s</text>'
            '<text x="%d" y="%d" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="%s">%s</text>'
            % (x, y, color, l1, x, y + 40, color, l2))

C1.append(("dark", '''<h2>Toda explicação responde duas %s.</h2>
<p style="margin-top:36px">A causa está em você ou fora? E ela fica, ou muda de um dia para o outro?</p>
<svg class="draw" width="888" height="520" viewBox="0 0 888 520" style="margin-top:36px">
<text x="300" y="40" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--mu)">em você</text>
<text x="680" y="40" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--mu)">fora de você</text>
<text x="0" y="176" font-family="Pen" font-size="40" fill="var(--mu)">fica</text>
<text x="0" y="376" font-family="Pen" font-size="40" fill="var(--mu)">muda</text>
<rect x="490" y="270" width="380" height="200" style="fill:var(--hl); stroke:none"/>
<path d="M110,70 L870,70 L870,470 L110,470 Z M490,70 L490,470 M110,270 L870,270" stroke="var(--ink)" stroke-width="3"/>
%s%s%s
<text x="680" y="386" text-anchor="middle" font-family="Pen" font-size="64" fill="var(--pen)">sorte</text>
<text x="300" y="512" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--pen)" transform="rotate(-2 300 512)">a única que não depende de você nem fica</text>
</svg>''' % (circ("perguntas"), cell(300, 160, "o que você", "já sabe fazer"), cell(680, 160, "a prova", "era fácil"), cell(300, 360, "o esforço", "daquele dia")), False))

C1.append(("light", '''<h2>A explicação muda o que você espera da próxima.</h2>
<p style="margin-top:36px">Repara: quando a causa fica, faz sentido esperar que aconteça de novo. Quando a causa muda, a próxima prova %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<text x="56" y="30" font-family="Inter" font-size="22" fill="var(--mu)">o que você espera</text>
<path d="M40,120 C240,110 500,100 860,92" stroke="var(--ink)" stroke-width="4"/>
<text x="470" y="78" font-family="Pen" font-size="38" fill="var(--ink)">explicou com o que fica</text>
<path d="M40,120 C200,150 360,230 520,262 C640,286 760,290 860,292" stroke="var(--pen)" stroke-width="5"/>
<text x="470" y="334" font-family="Pen" font-size="40" fill="var(--pen)">explicou com sorte</text>
<circle cx="40" cy="120" r="10" style="fill:var(--pen); stroke:none"/>
<text x="58" y="100" font-family="Pen" font-size="32" fill="var(--mu)">a prova boa</text>
<text x="640" y="410" font-family="Inter" font-size="22" fill="var(--mu)">próximas provas →</text>
</svg>''' % hl("fica em aberto"), False))

C1.append(("dark", '''<h2>E a sorte esconde o que estava nas suas mãos.</h2>
<p style="margin-top:36px">Imagine olhar para aquela prova e perguntar: o que eu fiz ali que dependia de mim? É essa resposta que dá para %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:30px">
%s%s
<text x="220" y="384" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--mu)">não dá para treinar</text>
<text x="668" y="384" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)">dá para treinar</text>
<text x="444" y="432" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 432)">mesmo troféu. só um vem com manual.</text>
</svg>''' % (hl("levar para o próximo treino"), trophy(220, 40, 1.0, "sorte", -6), trophy(668, 40, 1.0, "o que eu fiz", -4)), False))

C1.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A prova boa aconteceu uma vez.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A explicação que você dá decide se ela pode voltar.</h1>''', False))

C1.append(("dark", qs("Três perguntas sobre a sua melhor prova.", [
    ("Como você explica essa prova quando alguém pergunta?", "A frase exata, do jeito que sai."),
    ("Essa causa está em você ou fora de você?", "Clima, percurso e “o dia” ficam fora."),
    ("O que ali dependia de você e dá para fazer de novo?", "Uma coisa só. Concreta.")]), False))

C1.append(("light", paraquem("Para quem é isso, e para quem não é.",
    "você já fez uma prova muito boa e, desde então, trata ela como um acaso que não volta.",
    "a dúvida sobre você aparece em tudo, não só na corrida, ou se pensar nas provas te deixa mal por dias. Aí o caminho é um psicólogo."), False))

C1.append(("dark", '''<div style="margin-top:100px"></div>
<h1 style="font-size:78px">Sorte não se treina.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">O que você fez naquele dia, sim.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para reler depois da sua próxima prova boa. Ou mande para quem sempre diz que foi sorte.</p>
%s''' % cta_box("manda pra quem", "diz que foi sorte", "“foi sorte”", "fui eu"), True))

# ---------------------------------------------------------------- C2 · pauta 11 · capa clara
def bubble(x, w, color, l1, l2, tail_left=True):
    tx = x + 70 if tail_left else x + w - 70
    return ('<rect x="%d" y="30" width="%d" height="190" rx="40" stroke="%s" stroke-width="4"/>'
            '<path d="M%d,218 L%d,280 L%d,218" style="fill:var(--bg)" stroke="%s" stroke-width="4"/>'
            '<path d="M%d,216 L%d,216" stroke="var(--bg)" stroke-width="6"/>'
            '<text x="%d" y="110" text-anchor="middle" font-family="Pen" font-size="44" fill="%s">%s</text>'
            '<text x="%d" y="166" text-anchor="middle" font-family="Pen" font-size="44" fill="%s">%s</text>'
            % (x, w, color, tx - 22, tx - 30 if tail_left else tx + 30, tx + 22, color, tx - 19, tx + 19,
               x + w // 2, color, l1, x + w // 2, color, l2))

C2 = []
C2.append(("light", '''<div style="margin-top:40px"></div>
<h1>Por que a prova ruim não vira aprendizado?</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">O motivo real está na tela 4.</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:40px">
%s%s
<text x="70" y="320" font-family="Inter" font-weight="700" font-size="24" fill="var(--mu)">PARA UM AMIGO</text>
<text x="818" y="320" text-anchor="end" font-family="Inter" font-weight="700" font-size="24" fill="var(--pen)">PARA VOCÊ</text>
<text x="444" y="388" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 388)">mesma prova. mesmo tempo no relógio.</text>
</svg>''' % (bubble(0, 420, "var(--ink)", "dia difícil.", "o que você aprendeu?"), bubble(468, 420, "var(--pen)", "de novo?", "que vergonha.", False)), True))

C2.append(("dark", '''<h2>Comece por esta conversa.</h2>
<p style="margin-top:40px">Imagine um amigo cruzando a chegada bem acima do tempo que queria. Você diria a ele que é fraco? Que não leva jeito?</p>
<p>Provavelmente não. Agora repara no que você diz para %s depois da sua.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">a mesma prova.<br>duas vozes.</div>''' % hl("você mesmo"), False))

def ring(x, n, l1, l2, l3, color):
    return ('<circle cx="%d" cy="100" r="66" stroke="%s" stroke-width="4"/>'
            '<text x="%d" y="128" text-anchor="middle" font-family="Pen" font-size="84" fill="%s">%s</text>'
            '<text x="%d" y="230" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="var(--ink)">%s</text>'
            '<text x="%d" y="270" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="var(--ink)">%s</text>'
            '<text x="%d" y="310" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="var(--ink)">%s</text>'
            % (x, color, x, color, n, x, l1, x, l2, x, l3))

C2.append(("light", '''<h2>Com um amigo, você faz três coisas sem %s.</h2>
<p style="margin-top:36px">Perceba que nenhuma delas é fingir que a prova foi boa.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
%s%s%s
<path d="M222,100 L370,100 M518,100 L666,100" stroke="var(--mu)" stroke-width="3" stroke-dasharray="3 10"/>
<text x="444" y="410" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 410)">com você, quase sempre o contrário.</text>
</svg>''' % (circ("pensar"), ring(148, "1", "gentileza", "no lugar", "do ataque", "var(--pen)"),
            ring(444, "2", "lembrar que", "acontece com", "quem corre", "var(--pen)"),
            ring(740, "3", "olhar do", "tamanho", "que foi", "var(--pen)")), False))

C2.append(("dark", '''<h2>O motivo: a gentileza faz você voltar.</h2>
<p style="margin-top:36px">Repara: quem trata o próprio erro com gentileza não larga o assunto. Volta para ele e %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<text x="56" y="30" font-family="Inter" font-size="22" fill="var(--mu)">tempo dedicado a melhorar</text>
<path d="M40,300 C220,290 380,200 520,150 C640,110 760,96 860,90" stroke="var(--pen)" stroke-width="5"/>
<text x="420" y="62" font-family="Pen" font-size="38" fill="var(--pen)">tratou o erro com gentileza</text>
<path d="M40,300 C240,296 520,290 860,288" stroke="var(--mu)" stroke-width="4"/>
<text x="520" y="330" font-family="Pen" font-size="38" fill="var(--mu)">não tratou</text>
<text x="560" y="410" font-family="Inter" font-size="22" fill="var(--mu)">depois da prova ruim →</text>
</svg>''' % hl("se dedica mais a melhorar"), False))

C2.append(("light", '''<h2>Quando a conversa é ataque, olhar dói.</h2>
<p style="margin-top:36px">E o que dói, você para de olhar. A prova ruim vai inteira para a gaveta, junto com %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:36px">
<path d="M60,40 C200,20 330,30 444,52 C558,30 688,20 828,40 L828,330 C688,312 558,320 444,344 C330,320 200,312 60,330 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M444,52 L444,344" stroke="var(--ink)" stroke-width="3"/>
<text x="110" y="110" font-family="Pen" font-size="36" fill="var(--ink)">longão: ok</text>
<text x="110" y="170" font-family="Pen" font-size="36" fill="var(--ink)">tiros: ok</text>
<text x="110" y="230" font-family="Pen" font-size="36" fill="var(--ink)">regenerativo: ok</text>
<path d="M480,70 L800,62 L800,300 L480,316 Z" style="fill:var(--bg)" stroke="var(--mu)" stroke-width="3" transform="rotate(4 640 190)"/>
<text x="640" y="196" text-anchor="middle" font-family="Pen" font-size="48" fill="var(--mu)" transform="rotate(4 640 190)">a prova</text>
<path d="M520,96 L560,96 M720,92 L760,92 M520,286 L560,286 M720,282 L760,282" stroke="var(--pen)" stroke-width="6" transform="rotate(4 640 190)"/>
<text x="444" y="404" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 404)">a única página grampeada do caderno.</text>
</svg>''' % hl("o que ela tinha para ensinar"), False))

C2.append(("dark", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">O tempo da prova é o mesmo nas duas conversas.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Só uma delas te leva de volta ao treino.</h1>''', False))

C2.append(("light", qs("Três perguntas para depois da próxima prova ruim.", [
    ("O que você disse para si mesmo na chegada?", "A frase inteira, sem suavizar."),
    ("Você diria isso para alguém que treina com você?", "Se não, a frase não é análise."),
    ("O que um amigo te perguntaria sobre essa prova?", "Responda essa pergunta, e não a outra.")]), False))

C2.append(("dark", paraquem("Para quem é isso, e para quem não é.",
    "depois de uma prova ruim, você passa dias se cobrando e evita até abrir os dados do relógio.",
    "a fala dura com você mesmo não sai da cabeça, aparece em tudo e pesa no seu dia a dia. Aí o caminho é um psicólogo."), False))

C2.append(("light", '''<div style="margin-top:100px"></div>
<h1 style="font-size:76px">Você já sabe conversar sobre uma prova ruim.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">Só nunca fez isso com a sua.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Salve para abrir depois da próxima prova que não sair como você queria. Ou mande para quem só é duro consigo mesmo.</p>
%s''' % cta_box("manda pra quem", "se cobra sozinho", "“que vergonha”", "o que eu aprendi?", x0=480, w=360), True))

# ---------------------------------------------------------------- C3 · pauta 12 · capa escura
C3 = []
C3.append(("dark", '''<div style="margin-top:40px"></div>
<h1>O erro bobo que estraga o seu longão:</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">dar uma sentença para a perna pesada.</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:30px">
<path d="M520,40 L520,170 M600,40 L600,170 M520,40 C540,20 580,20 600,40" stroke="var(--mu)" stroke-width="4"/>
<rect x="420" y="170" width="300" height="140" rx="6" stroke="var(--ink)" stroke-width="4"/>
<path d="M420,200 L720,200" stroke="var(--ink)" stroke-width="3"/>
<path d="M600,160 L676,160" stroke="var(--pen)" stroke-width="7"/><rect x="674" y="138" width="26" height="44" rx="5" style="fill:var(--pen)" stroke="var(--pen)" stroke-width="3"/>
<text x="570" y="270" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">juiz</text>
<rect x="30" y="200" width="280" height="140" rx="6" stroke="var(--ink)" stroke-width="4"/>
<path d="M140,30 C134,70 150,96 172,118 C160,140 146,170 140,200 M184,30 C186,64 198,96 214,116 C200,146 188,172 184,200" stroke="var(--ink)" stroke-width="4"/>
<path d="M140,30 C152,20 172,20 184,30" stroke="var(--ink)" stroke-width="4"/>
<path d="M168,104 C180,112 196,114 212,110" stroke="var(--mu)" stroke-width="3"/>
<text x="170" y="262" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--ink)">RÉ:</text>
<text x="170" y="300" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--ink)">PERNA PESADA</text>
<text x="760" y="110" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-4 760 110)">cadeira</text>
<text x="760" y="150" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-4 760 150)">vazia.</text>
<text x="444" y="392" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 392)">então quem bateu o martelo?</text>
</svg>''', True))

C3.append(("light", '''<h2>Repara no que vem logo depois da sensação.</h2>
<p style="margin-top:40px">Imagine: a perna pesa no começo do longão. Em segundos, chega a frase: “hoje não é meu dia”.</p>
<p>A perna só deu um sinal. %s foi você quem escreveu.</p>
<div class="note" style="margin-top:70px; transform:rotate(-2deg)">o sinal é um.<br>o veredito é outro.</div>''' % hl("A sentença"), False))

C3.append(("dark", '''<h2>Dentro de você, são duas %s.</h2>
<p style="margin-top:36px">O que o corpo sente. E o que a cabeça conclui em cima disso.</p>
<svg class="draw" width="888" height="480" viewBox="0 0 888 480" style="margin-top:36px">
<rect x="0" y="30" width="330" height="300" rx="24" stroke="var(--ink)" stroke-width="4"/>
<text x="165" y="80" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--ink)">O QUE VOCÊ SENTE</text>
<text x="165" y="150" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">pesada</text>
<text x="165" y="210" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">dura na coxa</text>
<text x="165" y="270" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">quente</text>
<rect x="558" y="30" width="330" height="300" rx="24" stroke="var(--pen)" stroke-width="4"/>
<text x="723" y="80" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--pen)">O QUE VOCÊ CONCLUI</text>
<text x="723" y="150" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)">vou quebrar</text>
<text x="723" y="210" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)">não treinei</text>
<text x="723" y="270" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)">não é meu dia</text>
<path d="M344,180 L544,180 M528,166 L546,180 L528,194" stroke="var(--mu)" stroke-width="4"/>
<path d="M444,200 L444,380" stroke="var(--pen)" stroke-width="3" stroke-dasharray="3 10"/>
<text x="444" y="430" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 430)">é aqui, no meio, que dá para olhar.</text>
</svg>''' % circ("coisas"), False))

C3.append(("light", '''<h2>A sensação muda. A sentença não acompanha.</h2>
<p style="margin-top:36px">Perceba: o que você sente sobe, desce e muda de lugar ao longo do treino. A frase colada no primeiro pico %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,300 C90,260 120,120 170,110 C220,100 240,250 300,260 C360,270 380,180 440,190 C500,200 520,300 580,290 C640,280 660,200 720,214 C780,228 800,280 860,270" stroke="var(--pen)" stroke-width="5"/>
<text x="560" y="350" font-family="Pen" font-size="38" fill="var(--pen)">o que a perna sente</text>
<path d="M170,92 L860,92" stroke="var(--ink)" stroke-width="3" stroke-dasharray="6 10"/>
<circle cx="170" cy="110" r="10" style="fill:var(--ink); stroke:none"/>
<text x="330" y="70" font-family="Pen" font-size="38" fill="var(--ink)">“hoje não é meu dia”</text>
<text x="660" y="410" font-family="Inter" font-size="22" fill="var(--mu)">tempo de treino →</text>
</svg>''' % hl("fica parada no mesmo lugar"), False))

C3.append(("dark", '''<h2>Olhar sem julgar não é ignorar.</h2>
<p style="margin-top:36px">Imagine descrever a perna como quem lê o relógio: pesada, mais na coxa, um pouco menos agora. Sem %s. Só o que está ali.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:40px">
<text x="0" y="110" font-family="Inter" font-weight="800" font-size="62" fill="var(--ink)">perna pesada</text>
<text x="450" y="110" font-family="Inter" font-weight="800" font-size="62" fill="var(--mu)">= dia perdido</text>
<path d="M440,92 C560,70 720,100 870,76 M450,104 C580,86 730,112 866,90" stroke="var(--pen)" stroke-width="6"/>
<text x="450" y="210" font-family="Pen" font-size="66" fill="var(--pen)" transform="rotate(-3 450 210)">= perna pesada.</text>
<path d="M600,230 C600,280 560,300 500,310" stroke="var(--pen)" stroke-width="3"/>
<text x="40" y="350" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 40 350)">só isso. o resto você escreveu.</text>
</svg>''' % hl("“bom” nem “ruim”"), False))

C3.append(("light", '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Perna pesada é informação.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">“Hoje não é meu dia” é uma sentença que você deu.</h1>''', False))

C3.append(("dark", qs("Três perguntas para o próximo longão.", [
    ("Em que trecho a perna pesou?", "O trecho, não o treino inteiro."),
    ("Qual frase veio logo depois?", "Anote do jeito que ela apareceu."),
    ("Como a perna estava um pouco mais à frente?", "Igual, pior ou diferente. Só observe.")]), False))

C3.append(("light", paraquem("Para quem é isso, e para quem não é.",
    "a perna pesa, a cabeça já decreta o treino perdido e o resto vira só cumprir tabela.",
    "o peso vem com dor que aumenta, inchaço ou um cansaço que se arrasta por semanas. Aí o caminho é um médico ou um fisioterapeuta."), False))

C3.append(("dark", '''<div style="margin-top:100px"></div>
<h1 style="font-size:78px">A perna pesada não é ré.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">E você não precisa ser o juiz.</h1>
<p class="mu" style="margin-top:50px; max-width:860px">Salve para lembrar no próximo longão. Ou mande para quem decreta o dia perdido no primeiro quilômetro.</p>
%s''' % cta_box("manda pra quem", "condena o treino cedo", "“não é meu dia”", "só está pesada", x0=480, w=360), True))

LOTE = [("C1", "foi-sorte", C1), ("C2", "conversa-com-amigo", C2), ("C3", "perna-pesada", C3)]

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
