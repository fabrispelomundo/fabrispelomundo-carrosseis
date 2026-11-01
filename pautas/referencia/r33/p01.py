# -*- coding: utf-8 -*-
# p01 — "O nó no estômago chega antes de você pensar na prova" (marcadores somáticos)
# A = capa escura (pergunta para você) · B = capa clara (enigma) · C = capa clara (A ou B?)
from base import *

def T(theme_first, i):
    """alternância a partir da capa"""
    other = "light" if theme_first == "dark" else "dark"
    return theme_first if i % 2 == 1 else other

KNOT = ("M0,0 C-30,-34 18,-58 34,-30 C48,-6 10,18 -8,0 C-28,-22 2,-50 26,-46 "
        "C54,-40 52,-4 30,8 C10,18 -22,8 -18,-16 C-14,-36 14,-34 16,-20")

def check(x, y, c="var(--pen)", s=1.0):
    return '<path d="M%d,%d l%d,%d l%d,%d" stroke="%s" stroke-width="5"/>' % (x, y, int(10*s), int(12*s), int(22*s), int(-28*s), c)

def cross(x, y, c="var(--mu)", r=12):
    return '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="%s" stroke-width="5"/>' % (x-r, y-r, x+r, y+r, x+r, y-r, x-r, y+r, c)

# ====================================================================== VERSÃO A · pergunta para você · capa escura
def morning(y=150, mark=None, extra=""):
    pts = [(56, "alarme"), (246, "café"), (440, "caminho"), (634, "aquecer"), (822, "largada")]
    s = '<path d="M20,%d L868,%d" stroke="var(--ink)" stroke-width="4"/>' % (y, y)
    for x, lab in pts:
        s += '<circle cx="%d" cy="%d" r="9" style="fill:var(--ink); stroke:none"/>' % (x, y)
        s += '<text x="%d" y="%d" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">%s</text>' % (x, y + 52, lab)
    return s + extra

A = []
A.append('''<div style="margin-top:30px"></div>
<h1>O estômago aperta no dia da prova. Quando? No café? No caminho?</h1>
<p class="mu" style="margin-top:30px">Antes de você pensar no percurso. Antes de qualquer coisa.</p>
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:auto; margin-bottom:70px">
%s
<g transform="translate(246,96)"><path d="%s" stroke="var(--pen)" stroke-width="5"/></g>
<path d="M246,120 L246,140" stroke="var(--pen)" stroke-width="3"/>
<text x="300" y="70" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 300 70)">já aqui?</text>
<path d="M246,250 C246,286 266,290 306,290 L782,290 C812,290 822,286 822,250" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>
<text x="544" y="325" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">e a prova nem começou</text>
</svg>''' % (morning(160), KNOT))

A.append('''<h2>Repara nisso aqui: o aperto chegou primeiro.</h2>
<p style="margin-top:36px">Você nem tinha começado a pensar na prova. O corpo já tinha respondido.</p>
<p>E talvez nem pra esta prova. Talvez pra %s, que esta lembra.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto">
<path d="M300,250 L320,400 C322,412 330,416 342,416 L506,416 C518,416 526,412 528,400 L548,250 Z" stroke="var(--ink)" stroke-width="5"/>
<path d="M548,286 C600,280 610,350 540,360" stroke="var(--ink)" stroke-width="5"/>
<path d="M296,250 L552,250" stroke="var(--ink)" stroke-width="5"/>
<path d="M330,226 C310,190 350,170 340,140 C330,110 370,96 380,70 L440,30 L470,58 L520,10 L560,60 C580,90 600,110 590,140" stroke="var(--pen)" stroke-width="4"/>
<path d="M430,226 C414,200 444,188 436,166" stroke="var(--mu)" stroke-width="3"/>
<path d="M500,226 C486,200 516,190 506,168" stroke="var(--mu)" stroke-width="3"/>
<text x="620" y="54" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 620 54)">aquela subida</text>
<path d="M614,46 C590,36 572,40 562,52" stroke="var(--pen)" stroke-width="3"/>
<text x="0" y="330" font-family="Pen" font-size="36" fill="var(--ink)" transform="rotate(-2 0 330)">você no café.</text>
<text x="0" y="374" font-family="Pen" font-size="36" fill="var(--ink)" transform="rotate(-2 0 374)">o corpo, em</text>
<text x="0" y="418" font-family="Pen" font-size="36" fill="var(--ink)" transform="rotate(-2 0 418)">outra prova.</text>
</svg>''' % hl("uma outra"))

A.append('''<h2>Sabe aquela prova que doeu? Ela deixou uma %s no corpo.</h2>
<p style="margin-top:36px">Um aperto, um frio na barriga. Quando aparece algo parecido com ela, a marca volta sozinha.</p>
<svg class="draw" width="888" height="480" viewBox="0 0 888 480" style="margin-top:auto; margin-bottom:10px">
<circle cx="200" cy="70" r="52" stroke="var(--ink)" stroke-width="4"/>
<path d="M176,124 L176,146 M224,124 L224,146" stroke="var(--ink)" stroke-width="4"/>
<path d="M176,146 C110,156 92,180 96,240 L104,470 M224,146 C290,156 308,180 304,240 L296,470" stroke="var(--ink)" stroke-width="4"/>
<g transform="translate(196,262) scale(.9)"><path d="%s" stroke="var(--pen)" stroke-width="5"/></g>
<path d="M170,370 l14,-12 l14,12 l14,-12 l14,12 l14,-12 M170,394 l14,-12 l14,12 l14,-12 l14,12 l14,-12" stroke="var(--pen)" stroke-width="4"/>
<path d="M250,250 C330,230 360,210 420,206" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 9"/>
<path d="M260,384 C330,384 370,370 420,360" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 9"/>
<text x="436" y="196" font-family="Inter" font-weight="800" font-size="26" fill="var(--ink)">APERTO NO ESTÔMAGO</text>
<text x="436" y="244" font-family="Pen" font-size="40" fill="var(--pen)">de qual prova?</text>
<text x="436" y="350" font-family="Inter" font-weight="800" font-size="26" fill="var(--ink)">FRIO NA BARRIGA</text>
<text x="436" y="398" font-family="Pen" font-size="40" fill="var(--pen)">de qual largada?</text>
</svg>''' % (hl("marca"), KNOT))

A.append('''<h2>Primeiro você sente. Explicar fica pra depois.</h2>
<p style="margin-top:36px">O sinal vem antes. O porquê, quando chega, chega bem depois. E nesse meio-tempo você já está %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,20 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,350 C110,348 140,150 230,110 C330,70 600,80 860,76" stroke="var(--pen)" stroke-width="5"/>
<text x="250" y="70" font-family="Pen" font-size="40" fill="var(--pen)">o aperto</text>
<path d="M700,30 L700,370" stroke="var(--ink)" stroke-width="3" stroke-dasharray="4 10"/>
<text x="690" y="190" text-anchor="end" font-family="Pen" font-size="36" fill="var(--ink)">aqui você entende</text>
<text x="690" y="230" text-anchor="end" font-family="Pen" font-size="36" fill="var(--ink)">o porquê</text>
<path d="M150,290 L690,290 M168,278 L150,290 L168,302 M672,278 L690,290 L672,302" stroke="var(--mu)" stroke-width="3"/>
<text x="420" y="334" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">o corpo sabe, você ainda não</text>
<text x="870" y="414" text-anchor="end" font-family="Inter" font-size="22" fill="var(--mu)">manhã da prova →</text>
</svg>''' % hl("decidindo com ele"))

A.append('''<h2>Calar o sinal não deixa você mais racional.</h2>
<p style="margin-top:36px">Olha isso: pessoas que, por uma lesão, perderam a ligação entre o que sentem e o que decidem continuaram raciocinando bem. Só que passaram a %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<rect x="40" y="40" width="808" height="250" rx="40" stroke="var(--ink)" stroke-width="4"/>
<path d="M120,230 A110,110 0 0 1 340,230" stroke="var(--ink)" stroke-width="4"/>
<path d="M230,230 L170,160" stroke="var(--ink)" stroke-width="4"/>
<path d="M548,230 A110,110 0 0 1 768,230" stroke="var(--ink)" stroke-width="4"/>
<path d="M658,230 L720,170" stroke="var(--ink)" stroke-width="4"/>
<circle cx="444" cy="150" r="40" style="fill:var(--pen); fill-opacity:.85; stroke:none"/>
<text x="444" y="166" text-anchor="middle" font-family="Inter" font-weight="800" font-size="46" fill="#140C06">!</text>
<rect x="380" y="128" width="130" height="30" rx="4" transform="rotate(-18 444 143)" style="fill:var(--mu); fill-opacity:.95; stroke:none"/>
<rect x="378" y="140" width="134" height="30" rx="4" transform="rotate(16 444 155)" style="fill:var(--mu); fill-opacity:.95; stroke:none"/>
<text x="444" y="354" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 354)">o aviso continua aceso. você só parou de ler.</text>
</svg>''' % hl("decidir mal na vida real"))

A.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Calar o aperto é correr com menos informação.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Ler o aperto é descobrir de qual prova ele veio.</h1>''')

A.append(qs("Pega a sua última prova e responde.", [
    ("Quando o estômago apertou? De manhã? Em que momento, exatamente?", "No alarme, no café, no estacionamento, na fila do banheiro, no curral."),
    ("O que tinha ali? O lugar? O horário? Quem estava do lado?", "O mesmo parque, a largada ainda no escuro, o mesmo grupo de treino."),
    ("Isso lembrava qual prova? Qual delas, exatamente?", "Escreve o nome da primeira que vier. E uma linha sobre como ela foi.")]))

A.append(paraquem("Pra quem é, e pra quem não é.",
    "o corpo aperta antes da prova, você treinou pra ela e quer entender de onde vem esse sinal, sem brigar com ele.",
    "o aperto vem com dor no peito, falta de ar ou enjoo que não passa: procure um médico. Se ele aparece todo dia, longe das provas, o caminho é um psicólogo."))

A.append('''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">O aperto não é o adversário.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">É uma prova antiga pedindo para ser lida.</h1>
<p class="mu" style="margin-top:40px">Salva pra reler na manhã da próxima prova, quando o estômago chegar antes de você.</p>
<svg class="draw" width="888" height="250" viewBox="0 0 888 250" style="margin-top:auto; margin-bottom:60px">
%s
<path d="M218,40 L274,40 L274,150 L246,124 L218,150 Z" stroke="var(--pen)" stroke-width="5" style="fill:var(--hl)"/>
<text x="290" y="70" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 290 70)">abrir aqui, no café</text>
</svg>''' % morning(190))

# ====================================================================== VERSÃO B · enigma · capa clara
SNOW = "M0,-30 L0,30 M-26,-15 L26,15 M-26,15 L26,-15 M-8,-24 L0,-16 L8,-24 M-8,24 L0,16 L8,24"

B = []
B.append('''<div style="margin-top:30px"></div>
<h1>Por que a barriga gela numa prova que você nem leva a sério?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:60px">
<path d="M60,330 L60,250" stroke="var(--ink)" stroke-width="3"/>
<path d="M60,250 L130,262 L60,276" stroke="var(--ink)" stroke-width="3"/>
<text x="20" y="370" font-family="Pen" font-size="30" fill="var(--mu)">prova curta,</text>
<text x="20" y="404" font-family="Pen" font-size="30" fill="var(--mu)">sem meta</text>
<path d="M200,300 L360,300 M346,288 L362,300 L346,312" stroke="var(--mu)" stroke-width="3"/>
<circle cx="610" cy="60" r="46" stroke="var(--ink)" stroke-width="4"/>
<path d="M590,108 C470,120 440,170 450,250 L470,430 M630,108 C750,120 780,170 770,250 L750,430" stroke="var(--ink)" stroke-width="4"/>
<g transform="translate(560,250) scale(1.6)"><path d="%s" stroke="var(--pen)" stroke-width="3.5"/></g>
<g transform="translate(680,300) scale(1.25)"><path d="%s" stroke="var(--pen)" stroke-width="3.5"/></g>
<g transform="translate(590,370) scale(1)"><path d="%s" stroke="var(--pen)" stroke-width="3.5"/></g>
<g transform="translate(690,190) scale(.8)"><path d="%s" stroke="var(--pen)" stroke-width="3.5"/></g>
<text x="200" y="250" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 200 250)">tão pequena. por quê?</text>
</svg>''' % (SNOW, SNOW, SNOW, SNOW))

B.append('''<h2>Pois é: o corpo não leu o regulamento.</h2>
<p style="margin-top:36px">Ele não mede o tamanho da prova. Mede o quanto ela %s outra que você já viveu.</p>
<p>E faz essa conta antes de você.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:10px">
<ellipse cx="220" cy="170" rx="120" ry="150" stroke="var(--ink)" stroke-width="4"/>
<path d="M170,140 l0,10 M270,140 l0,10" stroke="var(--ink)" stroke-width="6"/>
<path d="M222,160 L210,210 L232,212" stroke="var(--ink)" stroke-width="4"/>
<path d="M180,250 C210,268 240,268 266,248" stroke="var(--ink)" stroke-width="4"/>
<text x="420" y="130" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 420 130)">“eu conheço essa cara...”</text>
<text x="420" y="220" font-family="Inter" font-weight="800" font-size="26" fill="var(--ink)">NOME:</text>
<path d="M520,222 L840,222" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>
<text x="420" y="300" font-family="Pen" font-size="34" fill="var(--mu)">reconhece antes de saber de onde.</text>
</svg>''' % hl("se parece com"))

B.append('''<h2>Parece exagero. É comparação.</h2>
<p style="margin-top:36px">Se liga nessa parte: o que você viveu deixa uma marca no corpo. Quando algo parecido aparece, a marca volta, mesmo que a prova de hoje seja %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,380 C120,300 200,330 270,250 C330,180 420,190 500,160 C600,120 700,200 840,90" stroke="var(--ink)" stroke-width="5"/>
<circle cx="40" cy="380" r="10" style="fill:var(--ink); stroke:none"/>
<path d="M70,60 C180,90 220,180 270,250 C330,180 420,190 500,160 C560,140 600,260 820,380" stroke="var(--mu)" stroke-width="4" stroke-dasharray="6 12"/>
<path d="M270,250 C330,180 420,190 500,160" stroke="var(--pen)" stroke-width="10" stroke-opacity=".9"/>
<ellipse cx="385" cy="200" rx="150" ry="70" stroke="var(--pen)" stroke-width="3" transform="rotate(-14 385 200)"/>
<text x="560" y="50" font-family="Pen" font-size="34" fill="var(--ink)">— a prova de hoje</text>
<text x="20" y="40" font-family="Pen" font-size="34" fill="var(--mu)">uma prova antiga —</text>
<text x="330" y="330" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 330 330)">o trecho parecido:</text>
<text x="330" y="374" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-3 330 374)">aqui o corpo reconhece</text>
</svg>''' % hl("outra"))

B.append('''<h2>Parece que não tem motivo. Tem. Só chega depois.</h2>
<p style="margin-top:36px">Se você não sabe explicar o frio, ele parece bobeira. Mas o corpo avisa %s de você conseguir dizer por quê.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M40,330 L870,330" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,200 L150,200 L162,186 L172,212 L182,170 L196,240 L210,90 L226,320 L242,120 L256,270 L270,160 L284,232 L298,184 L312,214 L326,194 L340,206 L360,200 L870,200" stroke="var(--pen)" stroke-width="4"/>
<text x="150" y="60" font-family="Pen" font-size="38" fill="var(--pen)">o corpo</text>
<path d="M800,200 L800,140" stroke="var(--ink)" stroke-width="3"/>
<text x="860" y="120" text-anchor="end" font-family="Pen" font-size="38" fill="var(--ink)">“ah, era isso”</text>
<path d="M640,112 C520,60 400,60 300,80 M318,66 L298,80 L318,94" stroke="var(--ink)" stroke-width="3" stroke-dasharray="4 9"/>
<text x="870" y="380" text-anchor="end" font-family="Inter" font-size="22" fill="var(--mu)">tempo →</text>
</svg>''' % hl("antes"))

B.append('''<h2>Parece que pensar resolve. Sozinho, não resolve.</h2>
<p style="margin-top:36px">Pessoas que, por lesão, perderam a ligação entre sensação e decisão seguiram raciocinando bem. E passaram a %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
<path d="M380,410 L400,260 M500,410 L470,260" stroke="var(--ink)" stroke-width="4"/>
<path d="M400,260 C380,200 280,180 120,170 M470,260 C500,200 600,180 780,170" stroke="var(--ink)" stroke-width="4"/>
<path d="M440,240 C420,214 360,206 200,200 M440,240 C460,214 520,206 700,200" stroke="var(--ink)" stroke-width="2" stroke-dasharray="2 10"/>
<path d="M120,170 L60,170 M120,170 L120,230 L60,230" stroke="var(--pen)" stroke-width="5"/>
<path d="M60,170 L60,410" stroke="var(--pen)" stroke-width="4"/>
<path d="M60,230 L40,250 M60,260 L40,280 M60,290 L40,310 M60,320 L40,340" stroke="var(--pen)" stroke-width="3"/>
<text x="20" y="130" font-family="Pen" font-size="34" fill="var(--pen)">a borda</text>
<rect x="560" y="260" width="150" height="130" rx="8" stroke="var(--ink)" stroke-width="4" transform="rotate(6 635 325)"/>
<g transform="rotate(6 635 325)">%s%s%s</g>
<text x="590" y="70" font-family="Pen" font-size="38" fill="var(--ink)" transform="rotate(-2 590 70)">conta certa,</text>
<text x="590" y="112" font-family="Pen" font-size="38" fill="var(--ink)" transform="rotate(-2 590 112)">caminho errado</text>
<path d="M300,200 L160,190 M178,178 L160,190 L178,202" stroke="var(--pen)" stroke-width="4"/>
</svg>''' % (hl("escolher mal na vida real"), check(588, 282, "var(--ink)", .8), check(588, 320, "var(--ink)", .8), check(588, 358, "var(--ink)", .8)))

B.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">O corpo não exagera. Ele compara.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A pergunta não é “por que tanto?”. É “parecido com o quê?”.</h1>''')

B.append(qs("Lembra a última vez que gelou sem motivo?", [
    ("Que prova era? Quando gelou? Na largada? Antes?", "Na retirada do kit, no aquecimento, no curral, no tiro de largada."),
    ("O que nela era igual a outra? O horário? O lugar? O clima?", "A largada de madrugada, o mesmo parque, o calor, a mesma turma."),
    ("E a outra prova, qual era? O que aconteceu lá?", "Escreve o nome dela e uma linha sobre como foi.")]))

B.append(paraquem("Isso é pra você?",
    "você gela antes de provas que nem são importantes e quer descobrir com o que o corpo está comparando.",
    "o frio vem com dor no peito, falta de ar ou mal-estar que não passa: o caminho é um médico. Se ele toma conta dos seus dias, fora das provas, procure um psicólogo."))

B.append('''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">Prova pequena, frio grande?</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">O tamanho está na prova que ela lembra.</h1>
<p class="mu" style="margin-top:40px">Manda pra aquele corredor que gela na largada de prova curta e jura que é bobeira.</p>
<svg class="draw" width="888" height="220" viewBox="0 0 888 220" style="margin-top:auto; margin-bottom:60px">
<path d="M40,150 L250,70 L150,190 Z M150,190 L170,130 L250,70" stroke="var(--pen)" stroke-width="5" style="fill:var(--hl)"/>
<path d="M270,70 C360,40 420,120 500,100 C560,86 580,60 620,70" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 12"/>
<rect x="630" y="40" width="250" height="110" rx="10" stroke="var(--ink)" stroke-width="4" transform="rotate(-3 755 95)"/>
<text x="755" y="86" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--ink)" transform="rotate(-3 755 95)">pra: quem diz</text>
<text x="755" y="126" text-anchor="middle" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-3 755 95)">“é bobeira”</text>
</svg>''')

# ====================================================================== VERSÃO C · A ou B? · capa clara
def radio(x, y, needle_x, cut=False):
    s = ('<rect x="%d" y="%d" width="520" height="230" rx="26" stroke="var(--ink)" stroke-width="5"/>' % (x, y))
    s += '<path d="M%d,%d L%d,%d" stroke="var(--ink)" stroke-width="4"/>' % (x + 420, y, x + 500, y - 90)
    s += '<rect x="%d" y="%d" width="300" height="80" rx="8" stroke="var(--ink)" stroke-width="3"/>' % (x + 30, y + 30)
    for i in range(9):
        s += '<path d="M%d,%d L%d,%d" stroke="var(--mu)" stroke-width="2"/>' % (x + 50 + i * 32, y + 40, x + 50 + i * 32, y + 54)
    s += '<path d="M%d,%d L%d,%d" stroke="var(--pen)" stroke-width="5"/>' % (needle_x, y + 34, needle_x, y + 106)
    s += '<circle cx="%d" cy="%d" r="48" stroke="var(--ink)" stroke-width="4"/>' % (x + 430, y + 120)
    s += '<path d="M%d,%d L%d,%d" stroke="var(--ink)" stroke-width="4"/>' % (x + 430, y + 120, x + 430, y + 80)
    for i in range(4):
        s += '<path d="M%d,%d L%d,%d" stroke="var(--mu)" stroke-width="3"/>' % (x + 40, y + 150 + i * 18, x + 330, y + 150 + i * 18)
    return s

C = []
C.append('''<div style="margin-top:30px"></div>
<h1>A barriga apertou no curral. O que ela tá dizendo: A ou B?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:60px">
<rect x="10" y="40" width="400" height="290" rx="18" stroke="var(--ink)" stroke-width="4" transform="rotate(-2 210 185)"/>
<rect x="478" y="40" width="400" height="290" rx="18" stroke="var(--ink)" stroke-width="4" transform="rotate(2 678 185)"/>
<text x="60" y="110" font-family="Pen" font-size="64" fill="var(--pen)">A</text>
<text x="528" y="110" font-family="Pen" font-size="64" fill="var(--pen)">B</text>
<rect x="140" y="120" width="150" height="70" rx="10" stroke="var(--ink)" stroke-width="4"/>
<path d="M290,142 L304,142 L304,168 L290,168" stroke="var(--ink)" stroke-width="4"/>
<rect x="152" y="132" width="24" height="46" rx="3" style="fill:var(--pen); stroke:none"/>
<text x="210" y="260" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">“não estou</text>
<text x="210" y="300" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">pronto”</text>
<path d="M630,190 L630,150 C630,112 726,112 726,150 L726,190 Z M616,190 L740,190" stroke="var(--ink)" stroke-width="4"/>
<path d="M600,120 L580,100 M756,120 L776,100 M678,96 L678,72 M608,160 L584,160 M748,160 L772,160" stroke="var(--pen)" stroke-width="4"/>
<text x="678" y="260" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">“essa prova</text>
<text x="678" y="300" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">importa”</text>
<text x="444" y="388" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 388)">qual você marcaria?</text>
</svg>''')

C.append('''<h2>Se você escolheu uma das duas, a resposta é outra.</h2>
<p style="margin-top:36px">Repara: o aperto pode não estar falando desta prova. Pode estar falando de uma %s, que esta lembra.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<rect x="10" y="40" width="250" height="150" rx="14" stroke="var(--mu)" stroke-width="3"/>
<rect x="290" y="40" width="250" height="150" rx="14" stroke="var(--mu)" stroke-width="3"/>
<text x="40" y="100" font-family="Pen" font-size="46" fill="var(--mu)">A</text>
<text x="320" y="100" font-family="Pen" font-size="46" fill="var(--mu)">B</text>
<text x="40" y="160" font-family="Pen" font-size="30" fill="var(--mu)">não estou pronto</text>
<text x="320" y="160" font-family="Pen" font-size="30" fill="var(--mu)">a prova importa</text>
<path d="M30,180 L240,56 M310,180 L520,56" stroke="var(--mu)" stroke-width="3"/>
<rect x="580" y="20" width="300" height="190" rx="14" stroke="var(--pen)" stroke-width="5" transform="rotate(-4 730 115)" style="fill:var(--hl)"/>
<text x="610" y="84" font-family="Pen" font-size="52" fill="var(--pen)" transform="rotate(-4 730 115)">C</text>
<text x="610" y="136" font-family="Pen" font-size="34" fill="var(--ink)" transform="rotate(-4 730 115)">uma prova antiga</text>
<text x="610" y="176" font-family="Pen" font-size="34" fill="var(--ink)" transform="rotate(-4 730 115)">voltando no corpo</text>
<path d="M700,240 C680,300 600,330 480,330" stroke="var(--pen)" stroke-width="3"/>
<path d="M500,316 L478,330 L500,344" stroke="var(--pen)" stroke-width="3"/>
<text x="20" y="344" font-family="Pen" font-size="38" fill="var(--ink)">a opção que não estava no papel</text>
</svg>''' % hl("prova antiga"))

C.append('''<h2>Pergunta 1: de onde vem o aperto? Desta prova? De outra?</h2>
<p style="margin-top:36px">De outra. Do que você já viveu. Cada situação deixa uma marca no corpo, e ela volta quando aparece algo %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
%s
<text x="36" y="410" font-family="Pen" font-size="30" fill="var(--mu)">aquela largada</text>
<text x="330" y="410" font-family="Pen" font-size="30" fill="var(--pen)">aquela subida</text>
<text x="600" y="410" font-family="Pen" font-size="30" fill="var(--mu)">aquele km</text>
<path d="M410,380 L262,214" stroke="var(--pen)" stroke-width="3"/>
<text x="640" y="130" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 640 130)">sintoniza</text>
<text x="640" y="172" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 640 172)">sozinho</text>
</svg>''' % (hl("parecido"), radio(40, 130, 262)))

C.append('''<h2>Pergunta 2: ele chega antes de você entender? Ou depois?</h2>
<p style="margin-top:36px">Antes. Olha isso: num jogo de cartas, o corpo das pessoas já reagia aos baralhos ruins quando elas ainda nem sabiam dizer %s.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:10px">
<path d="M40,40 L40,300" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,140 L870,140 M40,250 L870,250" stroke="var(--mu)" stroke-width="2" stroke-dasharray="2 12"/>
<path d="M300,30 L300,300" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 10"/>
<path d="M700,30 L700,300" stroke="var(--ink)" stroke-width="4"/>
<text x="310" y="330" font-family="Pen" font-size="32" fill="var(--pen)">o corpo reage</text>
<text x="710" y="330" font-family="Pen" font-size="32" fill="var(--ink)">você sabe dizer</text>
<path d="M50,100 L292,100 M272,86 L294,100 L272,114" stroke="var(--pen)" stroke-width="6"/>
<text x="60" y="76" font-family="Pen" font-size="38" fill="var(--pen)">o sinal do corpo</text>
<path d="M50,210 L692,210 M672,196 L694,210 L672,224" stroke="var(--ink)" stroke-width="4" stroke-dasharray="6 10"/>
<text x="60" y="186" font-family="Pen" font-size="38" fill="var(--ink)">a explicação</text>
<text x="0" y="350" font-family="Inter" font-size="22" fill="var(--mu)">tempo →</text>
</svg>''' % hl("qual era o ruim"))

C.append('''<h2>Pergunta 3: então é só desligar? Ignorar e largar?</h2>
<p style="margin-top:36px">Não. Quem perdeu essa ligação, por lesão, continuou pensando bem. E passou a %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
<rect x="20" y="120" width="300" height="160" rx="22" stroke="var(--ink)" stroke-width="4"/>
<circle cx="250" cy="200" r="38" stroke="var(--ink)" stroke-width="4"/>
<rect x="50" y="150" width="140" height="50" rx="6" stroke="var(--ink)" stroke-width="3"/>
<path d="M320,220 C380,220 380,300 430,300" stroke="var(--ink)" stroke-width="4"/>
<path d="M470,300 C520,300 520,240 580,240" stroke="var(--ink)" stroke-width="4"/>
<path d="M434,270 L466,330 M466,270 L434,330" stroke="var(--pen)" stroke-width="5"/>
<circle cx="426" cy="262" r="14" stroke="var(--pen)" stroke-width="4"/>
<circle cx="474" cy="262" r="14" stroke="var(--pen)" stroke-width="4"/>
<text x="610" y="190" font-family="Pen" font-size="38" fill="var(--ink)">pensar</text>
%s
<text x="610" y="290" font-family="Pen" font-size="38" fill="var(--ink)">decidir</text>
%s
<text x="40" y="380" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 40 380)">silêncio não é clareza.</text>
</svg>''' % (hl("decidir mal na vida real"), check(790, 170, "var(--ink)"), cross(810, 278, "var(--pen)", 16)))

C.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A pergunta não é “estou pronto?”.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">É “de qual prova é esse aperto?”.</h1>''')

def box_item(text):
    return ('<div style="display:flex; gap:28px; align-items:flex-start; padding:22px 0; border-top:2px dashed var(--line)">'
            '<div style="flex:none; width:46px; height:46px; border:4px solid var(--pen); border-radius:6px; margin-top:4px"></div>'
            '<div style="font-size:38px; font-weight:700; line-height:1.2; letter-spacing:-.01em">%s</div></div>') % text

C.append('''<h2 style="margin-bottom:30px">No curral da próxima prova, marca o que for verdade.</h2>
%s%s%s%s
<p class="mu" style="margin-top:34px">Marcou as duas primeiras e travou nas outras? É aí que está a leitura que falta.</p>''' % (
    box_item("O aperto veio antes de eu pensar na prova."),
    box_item("Algo aqui lembra outra prova. O lugar? O horário? O clima? A turma?"),
    box_item("Eu sei dizer qual prova é. O nome dela."),
    box_item("Eu sei o que aconteceu nela. Em que trecho, em que km.")))

C.append(paraquem("Quem deve ler, e quem não deve.",
    "você chega treinado, a barriga aperta na largada e você quer saber o que esse sinal está lembrando.",
    "o aperto vem com dor no peito, falta de ar ou enjoo forte: vá a um médico. Se ele aparece longe das provas e pesa nos seus dias, converse com um psicólogo."))

C.append('''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">Você ia marcar A ou B?</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">O aperto estava falando de outra prova.</h1>
<p class="mu" style="margin-top:40px">Comenta aqui: A, B ou C? E manda pra quem responderia diferente de você.</p>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto; margin-bottom:60px">
<rect x="20" y="60" width="848" height="96" rx="48" stroke="var(--ink)" stroke-width="4"/>
<text x="70" y="120" font-family="Inter" font-size="28" fill="var(--mu)">Adicione um comentário...</text>
<text x="470" y="128" font-family="Pen" font-size="64" fill="var(--pen)" transform="rotate(-4 490 110)">C</text>
<path d="M524,78 L524,140" stroke="var(--pen)" stroke-width="4"/>
<text x="600" y="40" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-3 600 40)">sua vez</text>
<path d="M590,36 C560,34 540,48 532,66" stroke="var(--pen)" stroke-width="3"/>
</svg>''')

def pack(cover, bodies):
    return [(T(cover, i), b, i in (1, 9)) for i, b in enumerate(bodies, 1)]

VERSOES = {"A": pack("dark", A), "B": pack("light", B), "C": pack("light", C)}

LEGENDAS = {"A": """Faz um teste na próxima prova, ou até no próximo longão de domingo: anota no celular a hora exata em que o estômago apertou. Só a hora e o lugar. Nada de explicação.

Depois, com calma, olha pra essa anotação. O que tinha ali? Era o mesmo trajeto daquela prova que deu errado? O mesmo horário de largada? A mesma camiseta?

O corpo guarda essas coisas sem pedir licença. Ele não precisa que você lembre pra reagir. Por isso o sinal parece vir do nada.

Não vem. Vem de algum lugar que você ainda não nomeou. E enquanto não tem nome, ele decide junto com você, no escuro.

A ideia não é fazer o aperto sumir. É parar de correr com ele como um passageiro desconhecido.

Salva pra abrir na véspera da próxima prova e fazer a anotação no dia.

Quer o diagnóstico inteiro, de graça? Tá no link da bio.""",

"B": """Sabe aquela corridinha de bairro, sem meta, sem pressão nenhuma, e mesmo assim a barriga gela no tiro de largada?

Isso confunde. Se a prova não vale nada, por que o corpo reage como se valesse?

Porque ele não avalia o tamanho do evento. Ele procura semelhança. O horário de madrugada, o barulho do locutor, a muvuca no curral, o cheiro de protetor solar. Qualquer pedaço pode puxar uma prova antiga inteira de volta.

Um exercício pra próxima vez: antes de largar, olha em volta e nomeia três coisas que você já viu em outra prova. Só isso.

Não é pra fazer o frio passar. É pra ele deixar de ser mistério e virar pista.

Manda pra quem treme em prova curta e jura que é frescura. Pode ser que essa pessoa nunca tenha olhado pra isso desse jeito.

O link da bio abre um diagnóstico completo, gratuito.""",

"C": """Esse sinal não aparece só na largada. Ele dá as caras no treino também, bem na hora de decidir.

Repara no próximo intervalado: antes de você escolher apertar o ritmo ou segurar, o corpo já deu um palpite. Às vezes é um aperto. Às vezes, um frio na barriga.

A tendência é passar por cima desse palpite e decidir só pela cabeça: pela planilha, pelo relógio, pelo que você acha que deveria fazer. Só que raciocinar bem não garante escolher bem. O corpo faz parte da escolha.

Isso não quer dizer obedecer cegamente. Quer dizer ouvir, perguntar de onde veio e aí decidir com as duas coisas na mesa.

Experimenta: no próximo treino, toda vez que bater uma sensação forte antes de uma decisão, pergunta em silêncio "isso me lembra o quê?". Não precisa responder na hora.

Comenta aqui embaixo: A ou B? E se você foi de C, conta também.

Diagnóstico completo, zero custo: toque no link do perfil.""",
}
