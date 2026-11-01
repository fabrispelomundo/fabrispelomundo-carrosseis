# -*- coding: utf-8 -*-
# p06 — Coração acelerado na largada: tentar se acalmar não é o caminho.
# A = capa clara (pergunta para você) · B = capa clara (enigma) · C = capa escura (A ou B?)
import math
from base import *

L, D = "light", "dark"

def alt(first):
    other = D if first == L else L
    return [first if i % 2 == 0 else other for i in range(9)]

def pen(x, y, txt, size=40, color="var(--pen)", anchor="start", rot=0):
    r = ' transform="rotate(%s %d %d)"' % (rot, x, y) if rot else ""
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Pen" font-size="%d" fill="%s"%s>%s</text>' % (x, y, anchor, size, color, r, txt)

def inter(x, y, txt, size=26, color="var(--ink)", weight=700, anchor="start"):
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Inter" font-weight="%d" font-size="%d" fill="%s">%s</text>' % (x, y, anchor, weight, size, color, txt)

def svg(h, inner, style="margin-top:40px"):
    return '<svg class="draw" width="888" height="%d" viewBox="0 0 888 %d" style="%s">%s</svg>' % (h, h, style, inner)

def arrow(x1, y1, x2, y2, color="var(--ink)", w=4, head=16):
    a = math.atan2(y2 - y1, x2 - x1)
    hx1 = x2 - head * math.cos(a - 0.5); hy1 = y2 - head * math.sin(a - 0.5)
    hx2 = x2 - head * math.cos(a + 0.5); hy2 = y2 - head * math.sin(a + 0.5)
    return '<path d="M%d,%d L%d,%d M%.0f,%.0f L%d,%d L%.0f,%.0f" stroke="%s" stroke-width="%d"/>' % (x1, y1, x2, y2, hx1, hy1, x2, y2, hx2, hy2, color, w)

def checklist(title, items, note):
    out = '<h2 style="margin-bottom:30px">%s</h2>' % title
    for t in items:
        out += ('<div style="display:flex; gap:28px; align-items:flex-start; padding:24px 0; border-top:2px dashed var(--line)">'
                '<svg class="draw" width="52" height="52" viewBox="0 0 52 52" style="flex:none; margin-top:4px">'
                '<rect x="4" y="4" width="44" height="44" rx="6" stroke="var(--pen)" stroke-width="4" transform="rotate(-3 26 26)"/></svg>'
                '<div style="font-size:36px; line-height:1.3; font-weight:600">%s</div></div>') % t
    out += '<div class="note" style="margin-top:36px; transform:rotate(-2deg)">%s</div>' % note
    return out

# =================================================================== VERSÃO A
# Pergunta para você · cena: curral de largada · 3 alavancas · CTA salvar

# A1 — a frase em branco
A1_SVG = svg(420, (
    pen(60, 70, "calmo?", 40, "var(--mu)", rot=-6) + pen(300, 50, "nervoso?", 40, "var(--mu)", rot=4) + pen(740, 120, "pronto?", 40, "var(--mu)", rot=-3)
    + inter(0, 200, "No curral, eu estou", 44, "var(--ink)", 800)
    + '<path d="M470,206 L860,206" stroke="var(--ink)" stroke-width="4"/>'
    # lápis encostado na linha
    + '<g transform="rotate(-38 520 190)"><rect x="520" y="176" width="190" height="30" rx="4" stroke="var(--pen)" stroke-width="4"/>'
      '<path d="M520,176 L486,191 L520,206" stroke="var(--pen)" stroke-width="4"/><path d="M680,176 L680,206" stroke="var(--pen)" stroke-width="3"/></g>'
    + pen(0, 320, "é por essa palavra que o cérebro", 42, rot=-2)
    + pen(0, 372, "vai ler o seu corpo.", 42, rot=-2)
), style="margin-top:auto; margin-bottom:60px")

A1 = '''<div style="margin-top:30px"></div>
<h1>O que você fala pra si mesmo no curral? Antes do tiro? Que frase, exatamente?</h1>
%s''' % A1_SVG

# A2 — botão de volume gigante, pedido de "calma"
def knob():
    cx, cy, r = 250, 220, 150
    s = '<circle cx="%d" cy="%d" r="%d" stroke="var(--ink)" stroke-width="5"/>' % (cx, cy, r)
    s += '<circle cx="%d" cy="%d" r="%d" stroke="var(--mu)" stroke-width="2"/>' % (cx, cy, r - 22)
    for i in range(11):
        ang = math.radians(225 - i * 27)
        x1 = cx + (r + 12) * math.cos(ang); y1 = cy - (r + 12) * math.sin(ang)
        x2 = cx + (r + 30) * math.cos(ang); y2 = cy - (r + 30) * math.sin(ang)
        col = "var(--pen)" if i >= 8 else "var(--mu)"
        s += '<path d="M%.0f,%.0f L%.0f,%.0f" stroke="%s" stroke-width="4"/>' % (x1, y1, x2, y2, col)
    ang = math.radians(225 - 10 * 27)
    s += '<path d="M%d,%d L%.0f,%.0f" stroke="var(--pen)" stroke-width="8"/>' % (cx, cy, cx + (r - 30) * math.cos(ang), cy - (r - 30) * math.sin(ang))
    s += inter(cx - 150, cy + 200, "BAIXO", 22, "var(--mu)") + inter(cx + 150, cy + 200, "ALTO", 22, "var(--pen)", anchor="end")
    return s

A2_SVG = svg(440, (
    knob()
    # setinha minúscula tentando girar de volta
    + '<path d="M150,70 C120,92 104,116 98,146" stroke="var(--ink)" stroke-width="3"/>'
    + '<path d="M90,132 L98,148 L110,136" stroke="var(--ink)" stroke-width="3"/>'
    + pen(118, 56, "“calma”", 30, "var(--ink)")
    + pen(500, 150, "o que já subiu:", 40, "var(--ink)")
    + pen(500, 200, "coração, respiração,", 40, "var(--ink)")
    + pen(500, 250, "mãos frias.", 40, "var(--ink)")
    + pen(500, 340, "girar tudo de volta", 42, rot=-2)
    + pen(500, 392, "antes do tiro?", 42, rot=-2)
), style="margin-top:50px")

A2 = '''<h2>Se a frase começa com “calma”, repara no tamanho do pedido.</h2>
<p style="margin-top:36px">O corpo já subiu. “Calma” pede pra ele descer %s, nos poucos minutos antes do tiro.</p>
%s''' % (hl("tudo de uma vez"), A2_SVG)

# A3 — mapa: sinais -> contexto + nome -> leitura
def pill(x, y, w, txt):
    return ('<rect x="%d" y="%d" width="%d" height="64" rx="32" stroke="var(--ink)" stroke-width="3"/>' % (x, y, w)
            + inter(x + w // 2, y + 42, txt, 26, "var(--ink)", 700, "middle"))

A3_SVG = svg(430, (
    pill(0, 40, 270, "coração rápido") + pill(0, 170, 270, "respiração curta") + pill(0, 300, 270, "mãos frias")
    + arrow(280, 72, 352, 170) + arrow(280, 202, 352, 202) + arrow(280, 332, 352, 236)
    + '<rect x="364" y="120" width="250" height="170" rx="18" stroke="var(--pen)" stroke-width="5" transform="rotate(-2 489 205)"/>'
    + pen(489, 186, "contexto", 40, "var(--ink)", "middle") + pen(489, 228, "+", 34, "var(--ink)", "middle")
    + pen(489, 268, "o nome que você dá", 30, "var(--pen)", "middle")
    + arrow(626, 180, 700, 110, "var(--mu)", 3) + arrow(626, 230, 700, 300, "var(--pen)", 4)
    + pen(712, 108, "ameaça", 44, "var(--mu)") + pen(712, 318, "prontidão", 44)
), style="margin-top:44px")

A3 = '''<h2>O corpo só manda os sinais. Quem diz o que eles significam é o %s.</h2>
<p style="margin-top:36px">Olha isso: ele decide pelo contexto. E o nome que você dá ao que sente entra nesse contexto.</p>
%s''' % (circ("cérebro"), A3_SVG)

# A4 — gráfico: ativação até a largada, calma longe, empolgação ao lado
A4_SVG = svg(430, (
    '<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>'
    + inter(54, 30, "ativação ↑", 22, "var(--mu)", 400)
    + inter(866, 420, "até a largada →", 22, "var(--mu)", 400, "end")
    + '<path d="M40,330 C220,320 340,180 480,130 C580,96 660,96 720,96" stroke="var(--ink)" stroke-width="5"/>'
    + '<circle cx="720" cy="96" r="10" style="fill:var(--ink); stroke:none"/>'
    + pen(330, 110, "o seu corpo", 38, "var(--ink)")
    + '<path d="M600,64 L860,64" stroke="var(--pen)" stroke-width="4" stroke-dasharray="4 12"/>'
    + pen(860, 50, "empolgação", 36, anchor="end")
    + '<path d="M500,350 L860,350" stroke="var(--mu)" stroke-width="4" stroke-dasharray="4 12"/>'
    + pen(860, 336, "calma", 36, "var(--mu)", "end")
    + arrow(760, 110, 760, 340, "var(--mu)", 3)
    + pen(578, 250, "longe daqui", 34, "var(--mu)")
), style="margin-top:44px")

A4 = '''<h2>A calma tá longe. A empolgação tá do lado.</h2>
<p style="margin-top:36px">No corpo, medo e empolgação são parecidos. Trocar um pelo outro %s. Muda só a leitura.</p>
%s''' % (hl("não pede pra baixar nada"), A4_SVG)

# A5 — pista: o ensaio antes do tiro difícil
A5_SVG = svg(440, (
    '<ellipse cx="300" cy="230" rx="280" ry="150" stroke="var(--ink)" stroke-width="4"/>'
    + '<ellipse cx="300" cy="230" rx="210" ry="92" stroke="var(--mu)" stroke-width="2"/>'
    + '<path d="M300,380 L300,322" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 8"/>'
    + '<path d="M86,214 L86,120 M86,120 L140,134 L86,150" stroke="var(--pen)" stroke-width="4"/>'
    + '<circle cx="86" cy="214" r="8" style="fill:var(--pen); stroke:none"/>'
    + '<path d="M150,128 C260,60 470,40 600,70" stroke="var(--pen)" stroke-width="3"/>'
    + pen(612, 70, "antes do tiro", 38) + pen(612, 116, "mais difícil:", 38)
    + pen(612, 176, "“estou", 44, "var(--ink)") + pen(612, 222, "empolgado”", 44, "var(--ink)")
    + pen(612, 300, "em voz alta.", 36, "var(--mu)")
    + pen(300, 436, "na largada, só a frase que o treino já testou.", 38, "var(--pen)", "middle", -1)
), style="margin-top:36px")

A5 = '''<h2>Teste o nome novo antes do tiro difícil do treino.</h2>
<p style="margin-top:36px">Sabe aquela série que você mais teme? Antes dela, diga em voz alta: “estou empolgado”. Você não precisa fingir nada. Só observe o que muda na leitura.</p>
%s''' % A5_SVG

A6 = '''<div style="margin-top:120px"></div>
<h1 style="font-size:76px">“Calma” pede para o corpo descer.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">“Empolgado” deixa o corpo onde está e muda o que ele quer dizer.</h1>'''

A7 = qs("Responde agora, de cabeça.", [
    ("Que frase você fala no curral? A primeira? E a última, antes do tiro?", "“calma”, “relaxa”, “não sai forte”, “segura”. A de verdade."),
    ("Ela pede pro corpo descer? Ou deixa ele onde está?", "Se tem “calma” ou “relaxa” no meio, ela pede descer."),
    ("Em qual treino você testa a frase nova? O de tiros? Antes de qual série?", "Na primeira, na mais dura, ou no aquecimento do longão.")])

A8 = paraquem("Para quem é isso, e para quem não é.",
    "o corpo dispara na largada e você gasta os últimos minutos brigando pra se acalmar.",
    "o coração dispara junto com dor no peito, tontura ou falta de ar, ou se esse disparo aparece fora do esporte e atrapalha a sua rotina. Aí o caminho é um médico ou um psicólogo.")

A9 = '''<div style="margin-top:80px"></div>
<h1 style="font-size:76px">O seu corpo chega pronto na largada.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">Só falta chamar isso pelo nome certo.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Salva pra testar no próximo treino de tiro. E pra reler no curral da próxima prova.</p>
%s''' % cta_box("salva pra ler", "no curral", "“fica calmo”", "“estou empolgado”", x0=440, w=380)

# =================================================================== VERSÃO B
# Pergunta-enigma · o que parece × o que acontece · CTA mandar para outro corredor

B1_SVG = svg(430, (
    # foguete na plataforma
    '<path d="M250,280 L250,110 C250,60 280,24 300,10 C320,24 350,60 350,110 L350,280 Z" stroke="var(--ink)" stroke-width="5"/>'
    + '<circle cx="300" cy="140" r="24" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M250,220 L206,290 L250,280 M350,220 L394,290 L350,280" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M180,330 L420,330" stroke="var(--ink)" stroke-width="5"/>'
    + '<path d="M270,290 C262,310 270,322 280,328 M300,292 C292,312 300,322 304,328 M330,290 C340,310 332,322 322,328" stroke="var(--pen)" stroke-width="4"/>'
    + '<path d="M150,330 C120,300 160,280 180,300 C190,270 230,280 230,310 M450,330 C480,300 440,280 420,300 C410,270 370,280 370,310" stroke="var(--mu)" stroke-width="3"/>'
    # tremor
    + '<path d="M214,80 L196,72 M214,120 L190,120 M214,160 L196,170 M386,80 L404,72 M386,120 L410,120 M386,160 L404,170" stroke="var(--pen)" stroke-width="4"/>'
    + pen(500, 100, "tremendo.", 44, "var(--ink)") + pen(500, 160, "barulhento.", 44, "var(--ink)") + pen(500, 220, "quente.", 44, "var(--ink)")
    + pen(500, 296, "e ele não tenta", 40) + pen(500, 342, "se acalmar.", 40)
), style="margin-top:auto; margin-bottom:60px")

B1 = '''<div style="margin-top:30px"></div>
<h1>Por que “respira e se acalma” quase nunca acalma na largada?</h1>
%s''' % B1_SVG

B2_SVG = svg(420, (
    '<path d="M0,400 L300,40 L620,400 L888,400" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M300,40 L300,10 M300,10 L338,18 L300,28" stroke="var(--pen)" stroke-width="4"/>'
    + '<circle cx="300" cy="40" r="9" style="fill:var(--pen); stroke:none"/>'
    + pen(0, 40, "você, aqui em cima", 32, "var(--ink)")
    + '<path d="M312,60 C360,120 300,150 360,190 C420,230 360,270 440,300 C510,326 480,370 560,388 L760,392" stroke="var(--pen)" stroke-width="4" stroke-dasharray="4 12"/>'
    + '<circle cx="780" cy="392" r="10" stroke="var(--mu)" stroke-width="4"/>'
    + pen(780, 360, "calmo", 44, "var(--mu)", "middle")
    + pen(480, 110, "o caminho até lá", 36, rot=-2) + pen(480, 154, "é longo.", 36, rot=-2)
), style="margin-top:60px")

B2 = '''<h2>Pois é: o corpo não está com defeito. Ele está se preparando.</h2>
<p style="margin-top:36px">E “se acalma” pede pra ele desfazer tudo isso antes do tiro. Então o que fazer com o que já subiu?</p>
%s''' % B2_SVG

B3_SVG = svg(440, (
    '<rect x="20" y="20" width="848" height="330" rx="8" stroke="var(--ink)" stroke-width="4" transform="rotate(-1.5 444 185)"/>'
    + '<g transform="rotate(-1.5 444 185)">'
    + inter(70, 96, "mãos frias", 46, "var(--ink)", 800) + inter(330, 96, "(s.f., na largada)", 26, "var(--mu)", 400)
    + '<path d="M70,120 L820,120" stroke="var(--mu)" stroke-width="2"/>'
    + pen(70, 180, "1. medo.", 44, "var(--ink)")
    + pen(70, 240, "2. vontade de ir.", 44, "var(--ink)")
    + pen(70, 310, "o sentido depende do contexto.", 34, "var(--mu)")
    + '</g>'
    + pen(444, 420, "quem escolhe a definição é o cérebro.", 40, anchor="middle", rot=-2)
), style="margin-top:36px")

B3 = '''<h2>Parece que o corpo avisa: “é medo”.</h2>
<p style="margin-top:36px">O que acontece: coração rápido, respiração curta e mãos frias são quase iguais no medo e na empolgação. %s.</p>
%s''' % (hl("O sentido vem do contexto"), B3_SVG)

B4_SVG = svg(460, (
    '<path d="M444,20 L444,420 M30,220 L858,220" stroke="var(--mu)" stroke-width="3"/>'
    + inter(454, 40, "ativação alta", 22, "var(--mu)", 400) + inter(454, 414, "ativação baixa", 22, "var(--mu)", 400)
    + inter(30, 256, "ameaça", 22, "var(--mu)", 400) + inter(858, 256, "prontidão", 22, "var(--mu)", 400, "end")
    + '<circle cx="150" cy="80" r="14" style="fill:var(--ink); stroke:none"/>' + pen(130, 140, "você no curral", 34, "var(--ink)")
    + '<circle cx="740" cy="80" r="14" style="fill:var(--pen); stroke:none"/>' + pen(740, 48, "empolgado", 40, anchor="middle")
    + '<circle cx="740" cy="360" r="14" stroke="var(--mu)" stroke-width="4"/>' + pen(700, 400, "calmo", 40, "var(--mu)", "end")
    + arrow(172, 80, 716, 80, "var(--pen)", 5, 20)
    + '<path d="M170,96 L718,346" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>' + arrow(700, 338, 720, 347, "var(--mu)", 3)
    + pen(300, 300, "longe", 36, "var(--mu)", rot=24)
    + pen(500, 120, "perto", 36)
), style="margin-top:36px")

B4 = '''<h2>Parece que se acalmar é o caminho mais curto.</h2>
<p style="margin-top:36px">O que acontece: é o mais longo. Ele pede pra baixar uma ativação alta. Chamar de empolgação %s e muda só a leitura.</p>
%s''' % (hl("mantém a ativação"), B4_SVG)

B5_SVG = svg(400, (
    # máscara de "tranquilo", riscada
    '<path d="M60,90 C60,30 300,30 300,90 C300,210 240,290 180,290 C120,290 60,210 60,90 Z" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M100,130 C116,116 140,116 154,130 M206,130 C220,116 244,116 260,130" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M120,210 C150,232 210,232 240,210" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M30,40 L330,320 M330,40 L30,320" stroke="var(--pen)" stroke-width="6"/>'
    + pen(180, 370, "cara de tranquilo", 36, "var(--mu)", "middle")
    + arrow(380, 180, 460, 180, "var(--ink)", 4)
    + pen(490, 110, "em voz alta:", 38, "var(--mu)")
    + pen(490, 190, "“estou", 56, "var(--ink)") + pen(490, 252, "empolgado.”", 56, "var(--ink)")
    + '<path d="M770,160 C790,180 790,210 770,230 M796,140 C826,174 826,216 796,250" stroke="var(--pen)" stroke-width="4"/>'
    + pen(490, 330, "o corpo segue igual.", 36) + pen(490, 372, "a leitura, não.", 36)
), style="margin-top:36px")

B5 = '''<h2>Parece que você teria de fingir tranquilidade.</h2>
<p style="margin-top:36px">O que acontece: você não precisa fingir nada. Basta dizer a frase. E ela se testa antes, no treino do tiro difícil, %s.</p>
%s''' % (hl("não pela primeira vez no pórtico"), B5_SVG)

B6 = '''<div style="margin-top:120px"></div>
<h1 style="font-size:78px">Se acalmar pede para o corpo recuar.</h1>
<h1 class="or" style="font-size:78px; margin-top:22px">Empolgação usa o que ele já preparou.</h1>'''

B7 = qs("Na próxima largada, repara nisso aqui.", [
    ("Quando o coração acelera? No café? No aquecimento? Só no curral?", "Anote o momento: no estacionamento, na fila do banheiro, no curral."),
    ("Que nome você dá pra isso? Qual palavra, exatamente?", "“nervoso”, “travado”, “com medo”, “pronto”. A primeira que aparecer."),
    ("Esse nome pede pro corpo recuar? Ou deixa ele ir?", "Se pede recuar, você achou o ponto onde a largada pesa.")])

B8 = paraquem("Para quem é isso, e para quem não é.",
    "você chega treinado e passa os minutos antes do tiro tentando baixar o coração na marra.",
    "o coração acelerado vem com dor no peito, tontura ou desmaio, ou se esse disparo toma conta de outras horas do seu dia, longe da corrida. Aí o caminho é um médico ou um psicólogo.")

B9 = '''<div style="margin-top:80px"></div>
<h1 style="font-size:78px">O corpo não precisa voltar atrás.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Precisa de outro nome.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Manda pra aquele amigo que, no curral, fica repetindo “calma, calma, calma” com o dedo no relógio.</p>
%s''' % cta_box("manda pra quem", "pede calma no curral", "“calma, calma”", "“estou empolgado”", x0=460, w=380)

# =================================================================== VERSÃO C
# A ou B? · quiz · CTA comentar + mandar

def card(x, letter, l1, l2, l3, color):
    return ('<rect x="%d" y="20" width="410" height="270" rx="16" stroke="%s" stroke-width="4" transform="rotate(%s %d 155)"/>' % (x, color, "-2" if letter == "A" else "1.5", x + 205)
            + pen(x + 36, 100, letter, 80, color)
            + inter(x + 36, 170, l1, 30, "var(--ink)", 700) + inter(x + 36, 212, l2, 30, "var(--ink)", 700) + inter(x + 36, 254, l3, 30, "var(--ink)", 700))

C1_SVG = svg(400, (
    card(0, "A", "respirar fundo", "até o coração", "baixar", "var(--ink)")
    + card(470, "B", "dizer em voz alta:", "“estou", "empolgado”", "var(--pen)")
    + pen(444, 380, "qual você escolhe?", 46, "var(--pen)", "middle", -2)
), style="margin-top:auto; margin-bottom:60px")

C1 = '''<div style="margin-top:30px"></div>
<h1>Coração disparado no curral, minutos antes do tiro. O que você faz?</h1>
%s''' % C1_SVG

C2_SVG = svg(430, (
    '<path d="M40,400 L360,400" stroke="var(--ink)" stroke-width="5"/>'
    + '<path d="M200,400 L200,384 L120,370 L280,352 L120,334 L280,316 L120,298 L280,280 L200,266 L200,252" stroke="var(--ink)" stroke-width="4"/>'
    + '<rect x="90" y="226" width="220" height="26" rx="6" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M200,70 L200,210 M182,190 L200,214 L218,190" stroke="var(--pen)" stroke-width="5"/>'
    + pen(200, 52, "“acalma”", 44, anchor="middle")
    + '<path d="M300,320 C360,320 400,300 440,270" stroke="var(--mu)" stroke-width="3"/>'
    + pen(456, 260, "tudo o que já subiu,", 40, "var(--ink)")
    + pen(456, 308, "apertado de volta", 40, "var(--ink)")
    + pen(456, 356, "em poucos minutos.", 40, "var(--ink)")
), style="margin-top:44px")

C2 = '''<h2>Se você escolheu A, fez o pedido mais difícil que dá pra fazer ao corpo.</h2>
<p style="margin-top:36px">Faz sentido querer baixar. Mas repara: a pergunta certa %s.</p>
%s''' % (hl("não é como baixar"), C2_SVG)

C3_SVG = svg(460, (
    inter(0, 30, "RETRATO FALADO", 24, "var(--mu)", 800)
    + '<circle cx="210" cy="110" r="52" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M210,162 L210,320 M210,200 L130,280 M210,200 L290,280 M210,320 L150,430 M210,320 L270,430" stroke="var(--ink)" stroke-width="4"/>'
    + '<circle cx="230" cy="220" r="12" style="fill:var(--pen); stroke:none"/>'
    + '<circle cx="290" cy="280" r="10" stroke="var(--pen)" stroke-width="4"/>'
    + '<path d="M196,140 C200,150 220,150 224,140" stroke="var(--pen)" stroke-width="4"/>'
    + arrow(470, 146, 236, 144, "var(--mu)", 3) + pen(486, 156, "respiração curta", 38, "var(--ink)")
    + arrow(470, 226, 250, 220, "var(--mu)", 3) + pen(486, 236, "coração rápido", 38, "var(--ink)")
    + arrow(470, 306, 306, 284, "var(--mu)", 3) + pen(486, 316, "mãos frias", 38, "var(--ink)")
    + pen(486, 400, "suspeito: medo?", 40) + pen(486, 446, "ou empolgação?", 40)
), style="margin-top:36px")

C3 = '''<h2>Pergunta 1: o que separa medo de empolgação no corpo? O coração?</h2>
<p style="margin-top:30px">Resposta: quase nada. Os sinais são os mesmos. Quem decide qual é qual é o cérebro, %s.</p>
%s''' % (hl("olhando o contexto"), C3_SVG)

C4_SVG = svg(430, (
    '<path d="M60,10 L60,360 L860,360" stroke="var(--mu)" stroke-width="3"/>'
    + inter(76, 30, "o quanto você pede ao corpo ↑", 22, "var(--mu)", 400)
    + '<rect x="180" y="80" width="200" height="280" stroke="var(--ink)" stroke-width="4"/>'
    + ''.join('<path d="M%d,%d L%d,%d" stroke="var(--mu)" stroke-width="2"/>' % (180, y, 380, y - 40) for y in range(120, 361, 40))
    + '<rect x="540" y="290" width="200" height="70" stroke="var(--pen)" stroke-width="5" style="fill:var(--hl)"/>'
    + pen(280, 410, "baixar a ativação", 36, "var(--ink)", "middle")
    + pen(640, 410, "trocar o nome", 36, anchor="middle")
    + pen(640, 260, "a ativação fica.", 34, anchor="middle", rot=-2)
), style="margin-top:36px")

C4 = '''<h2>Pergunta 2: e se você trocar o nome? O coração desacelera?</h2>
<p style="margin-top:30px">Resposta: não. A ativação fica onde está. Só a leitura muda. Por isso dizer “estou empolgado” %s do que tentar ficar calmo.</p>
%s''' % (hl("pede menos ao corpo"), C4_SVG)

C5_SVG = svg(430, (
    # caixa de tênis
    '<path d="M40,190 L360,190 L360,360 L40,360 Z" stroke="var(--ink)" stroke-width="4"/>'
    + '<path d="M28,150 L372,150 L372,190 L28,190 Z" stroke="var(--ink)" stroke-width="4" transform="rotate(-6 200 170)"/>'
    + inter(200, 290, "FRASE NOVA", 30, "var(--ink)", 800, "middle")
    # não: dia da prova
    + pen(440, 120, "estrear no dia da prova", 38, "var(--mu)")
    + '<path d="M432,108 L860,100" stroke="var(--pen)" stroke-width="5"/>'
    # sim: treino
    + arrow(380, 270, 440, 270, "var(--pen)", 4)
    + pen(456, 260, "amaciar no treino,", 42) + pen(456, 310, "antes do tiro", 42) + pen(456, 360, "mais difícil.", 42)
), style="margin-top:36px")

C5 = '''<h2>Pergunta 3: dá pra estrear a frase na largada? Ou antes? Em qual treino?</h2>
<p style="margin-top:30px">Resposta: sabe tênis novo no dia da prova? Com a frase é igual. %s</p>
%s''' % (hl("Teste antes, no treino."), C5_SVG)

C6 = '''<div style="margin-top:120px"></div>
<h1 style="font-size:78px">A pergunta não é como baixar o coração.</h1>
<h1 class="or" style="font-size:78px; margin-top:22px">É que nome você dá para ele.</h1>'''

C7 = checklist("Marque o que é com você.", [
    "No curral, você repete “calma” ou “relaxa”.",
    "Você chama o coração acelerado de nervoso, não de pronto.",
    "Você nunca disse outra frase antes de um tiro difícil no treino.",
    "Você larga já brigando com o próprio corpo."],
    "cada marca é um lugar onde<br>a leitura pode mudar.")

C8 = paraquem("Para quem é isso, e para quem não é.",
    "você marcou A no começo e larga gastando a cabeça pra segurar o coração.",
    "o coração disparado vem com dor no peito, tontura ou falta de ar, ou se esse disparo aparece sem prova nenhuma e atrapalha o seu dia. Aí o caminho é um médico ou um psicólogo.")

C9_SVG = svg(220, (
    '<rect x="40" y="60" width="110" height="110" rx="12" stroke="var(--ink)" stroke-width="4" transform="rotate(-3 95 115)"/>'
    + pen(95, 140, "A", 70, "var(--ink)", "middle")
    + '<rect x="200" y="60" width="110" height="110" rx="12" stroke="var(--pen)" stroke-width="4" style="fill:var(--hl)" transform="rotate(2 255 115)"/>'
    + pen(255, 140, "B", 70, "var(--ink)", "middle")
    + arrow(340, 120, 420, 120, "var(--pen)", 4)
    + pen(440, 100, "comente a sua letra.", 40)
    + pen(440, 150, "e manda pra quem", 40)
    + pen(440, 200, "marcaria a outra.", 40)
), style="margin-top:36px")

C9 = '''<div style="margin-top:70px"></div>
<h1 style="font-size:76px">O coração dispara do mesmo jeito.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">O que muda é o nome que você dá.</h1>
<p class="mu" style="margin-top:40px; max-width:860px">A ou B: o que você faz hoje no curral? Comenta aqui embaixo.</p>
%s''' % C9_SVG

def pack(first, bodies):
    th = alt(first)
    return [(th[i], b, i in (0, 8)) for i, b in enumerate(bodies)]

VERSOES = {
    "A": pack(L, [A1, A2, A3, A4, A5, A6, A7, A8, A9]),
    "B": pack(L, [B1, B2, B3, B4, B5, B6, B7, B8, B9]),
    "C": pack(D, [C1, C2, C3, C4, C5, C6, C7, C8, C9]),
}

LEGENDAS = {"A": """Repara numa coisa: a frase do curral quase sempre começa antes. No café da manhã da prova, no carro, na fila do banheiro químico. Quando você chega no curral, ela já está rodando sozinha.

Coração rápido, respiração curta, mão gelada. Isso aparece no medo e aparece na vontade de ir. O que separa um do outro é o contexto que o cérebro usa pra ler esses sinais, e a palavra que você escolhe faz parte desse contexto.

Um teste pra esta semana: no treino de tiros, antes da série que você mais evita, fala em voz alta "estou empolgado". Sem forçar sorriso, sem mexer na respiração. Depois, anota duas coisas: em que momento o coração subiu e que palavra veio primeiro na sua cabeça.

Repete isso em dois ou três treinos antes da prova. Assim, no curral, a frase não é estreia.

Salva pra lembrar do teste na semana dos tiros e pra reler na manhã da prova.

Tem um diagnóstico completo, sem custo, que mapeia o seu jeito de competir de ponta a ponta: link na bio.""",
"B": """Pensa no último aquecimento antes de uma prova importante. Você trotando, olhando o relógio, sentindo o coração mais alto do que gostaria. E a cabeça mandando o corpo voltar ao normal.

Esse pedido parece razoável, mas olha o tamanho dele: baixar uma ativação que já subiu, em poucos minutos, com gente apertada do lado e a contagem regressiva rolando.

Agora repara em outra coisa. Quando você está empolgado de verdade, numa largada que esperou meses, o coração também dispara. As mãos também esfriam. O corpo faz quase a mesma coisa. A diferença está no nome que vai junto.

Por isso a troca de palavra não pede pra você sentir outra coisa. Pede só que você diga em voz alta "estou empolgado" e deixe a leitura mudar. Sem teatro.

Manda pra quem passa o aquecimento inteiro tentando baixar o coração. Aquele amigo que chega no curral pedindo calma pra si mesmo.

Vale um raio-x completo e gratuito do seu lado mental em competição: acessa pela bio.""",
"C": """Escolheu A? Faz sentido. Respirar fundo é aquele conselho que você já ouviu em toda véspera de prova.

O ponto é outro. Nos minutos antes do tiro, o corpo já subiu. Pedir pra ele descer até a calma é pedir muito, bem na hora em que você queria pensar só no primeiro quilômetro.

Já a frase "estou empolgado" deixa o coração onde está. Ela muda a leitura, não o batimento. E a leitura é o que o cérebro usa pra decidir se aquilo é ameaça ou prontidão.

Um jeito de testar sem risco: escolhe um treino com o tiro que você mais teme. Antes da primeira repetição, fala a frase em voz alta. Na volta pra casa, responde pra você mesmo: a sensação no peito mudou ou só o jeito de olhar pra ela?

Comenta aqui embaixo: A ou B? E marca aquele amigo que escolheria a letra contrária.

Pra enxergar o restante do seu jogo mental, existe uma análise inteira, de graça, esperando no link do perfil."""}
