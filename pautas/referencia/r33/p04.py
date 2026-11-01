# -*- coding: utf-8 -*-
# p04 — O trecho da prova que pesa antes de você chegar nele.
# A = pergunta para você (capa clara) · B = pergunta-enigma (capa clara) · C = A ou B? (capa escura)
from base import *

def T(x, y, s, size=36, fill="var(--pen)", anchor="start", rot=0, fam="Pen", weight=None):
    w = ' font-weight="%s"' % weight if weight else ""
    r = ' transform="rotate(%s %s %s)"' % (rot, x, y) if rot else ""
    return '<text x="%s" y="%s" text-anchor="%s" font-family="%s"%s font-size="%s" fill="%s"%s>%s</text>' % (x, y, anchor, fam, w, size, fill, r, s)

def runner(x, y, c="var(--ink)", s=1.0):
    # boneco correndo com pés em (x, y)
    return ('<g transform="translate(%s,%s) scale(%s)"><circle cx="4" cy="-82" r="13" stroke="%s" stroke-width="4"/>'
            '<path d="M2,-68 L-4,-34 L-20,-2 M-4,-34 L16,-6 L24,-6 M0,-58 L-20,-44 M0,-58 L20,-50" stroke="%s" stroke-width="4"/></g>') % (x, y, s, c, c)

# ======================================================================= VERSÃO A
A = []
A.append(("light", '''<div style="margin-top:30px"></div>
<h1>Qual trecho da sua prova pesa antes de você chegar nele?</h1>
<h1 class="or" style="margin-top:22px; font-size:54px; line-height:1.1">A subida? Qual delas? Em que ponto ela começa a pesar?</h1>
<svg class="draw" width="888" height="400" viewBox="0 20 888 400" style="margin-top:auto; margin-bottom:30px">
<path d="M100,336 L520,336 L520,354 L100,354 Z" style="fill:var(--hl); stroke:none"/>
<path d="M650,128 L100,340" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 14"/>
<path d="M650,128 L520,340" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 14"/>
<path d="M20,336 L470,336 C540,336 560,140 650,124 C740,108 770,270 868,312" stroke="var(--ink)" stroke-width="5"/>
%s
%s
%s
%s
</svg>''' % (runner(160, 334), T(660, 94, "a subida", 40, "var(--ink)", "middle"),
             T(144, 220, "você, ainda no plano", 36, "var(--mu)"),
             T(60, 404, "a sombra dela já chegou em você.", 44, "var(--pen)", rot=-2)), True))

A.append(("dark", '''<h2>A perna ainda responde. Você ainda está no plano.</h2>
<p style="margin-top:36px">Mas repara: o fôlego encurtou, o olho foi lá pra frente. O corpo está aqui. A cabeça %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M20,320 L520,320 C600,320 620,170 700,160 C780,150 820,260 868,290" stroke="var(--ink)" stroke-width="4"/>
<path d="M150,300 C150,262 196,262 196,300 C196,330 173,350 173,350 C173,350 150,330 150,300 Z" stroke="var(--mu)" stroke-width="4" transform="translate(0,-60)"/>
%s
<path d="M680,140 C680,96 740,96 740,140 C740,176 710,198 710,198 C710,198 680,176 680,140 Z" stroke="var(--pen)" stroke-width="5" transform="translate(-10,-110)"/>
%s
<path d="M200,200 C330,40 520,20 640,50" stroke="var(--pen)" stroke-width="3" stroke-dasharray="6 12"/>
<path d="M618,32 L644,52 L614,66" stroke="var(--pen)" stroke-width="3"/>
%s
</svg>''' % (hl("já está subindo"), T(173, 386, "pernas: aqui", 36, "var(--mu)", "middle"),
             T(800, 70, "cabeça: lá", 38, "var(--pen)", "middle"),
             T(300, 384, "esse pedaço você corre duas vezes.", 38, "var(--pen)", rot=-2)), False))

A.append(("light", '''<h2>Subida é só inclinação. Até o dia em que ela %s.</h2>
<p style="margin-top:32px">Olha isso: quando um trecho vem junto com um momento forte, os dois ficam colados. E o que veio com emoção grava mais fundo que o resto da prova.</p>
<svg class="draw" width="888" height="430" viewBox="0 0 888 430" style="margin-top:auto">
<rect x="10" y="20" width="868" height="400" rx="10" stroke="var(--mu)" stroke-width="3"/>
%s
%s
%s
<path d="M60,154 L540,154" stroke="var(--pen)" stroke-width="4"/>
%s
%s
%s
%s
</svg>''' % (circ("pesou"),
             T(50, 86, "subida", 46, "var(--ink)", fam="Inter", weight="800"),
             T(220, 86, "s.f.", 30, "var(--mu)", fam="Inter"),
             T(50, 146, "trecho do percurso com inclinação.", 32, "var(--ink)", fam="Inter"),
             T(80, 222, "+ a perna que travou", 42, "var(--pen)", rot=-2),
             T(80, 282, "+ o ar que faltou", 42, "var(--pen)", rot=-2),
             T(80, 342, "+ a vontade de andar", 42, "var(--pen)", rot=-2),
             T(860, 400, "definição reescrita por um dia só", 30, "var(--mu)", "end")), False))

rows = ""
for i, (lab, st) in enumerate([("uma prova", 640), ("a seguinte", 520), ("mais uma", 390), ("hoje", 250)]):
    y = 70 + i * 92
    rows += T(0, y + 8, lab, 34, "var(--pen)" if lab == "hoje" else "var(--mu)")
    rows += '<path d="M%d,%d L%d,%d" stroke="var(--pen)" stroke-width="12" stroke-opacity="%s"/>' % (st, y, 700, y, ".9" if lab == "hoje" else ".55")
    rows += '<path d="M200,%d L700,%d C730,%d 740,%d 770,%d C800,%d 820,%d 868,%d" stroke="var(--ink)" stroke-width="4"/>' % (y, y, y, y - 44, y - 44, y - 44, y, y)
A.append(("dark", '''<h2>E a cada prova, o peso chega mais cedo.</h2>
<p style="margin-top:32px">Pois é. Cada vez que a mesma subida leva à mesma conclusão, a ligação fica mais forte e mais automática. Vira %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto">
%s
<path d="M690,410 L250,410 M274,394 L250,410 L274,426" stroke="var(--pen)" stroke-width="3"/>
%s
%s
</svg>''' % (hl("atalho"), rows, T(770, 370, "a subida", 30, "var(--mu)", "middle"),
             T(300, 396, "onde o peso começa", 32, "var(--pen)")), False))

lit = ""
for i, (s, on) in enumerate([("perna pesando", True), ("ritmo em dia", False), ("fôlego no lugar", False), ("treino feito", False)]):
    y = 70 + i * 92
    if on:
        lit += T(500, y, s, 44, "var(--ink)") + '<path d="M820,%d L834,%d L860,%d" stroke="var(--pen)" stroke-width="5"/>' % (y - 16, y - 2, y - 34)
    else:
        lit += T(500, y, s, 40, "var(--mu)")
A.append(("light", '''<h2>Antes da subida, o cérebro já fez a previsão.</h2>
<p style="margin-top:32px">Ele usa o que você já viveu ali. Se a previsão é sofrimento, o corpo se adianta. E a atenção sai caçando %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto">
<path d="M150,30 L486,20 L486,110 L150,92 Z" style="fill:var(--hl); stroke:none"/>
<rect x="30" y="34" width="110" height="56" rx="10" stroke="var(--ink)" stroke-width="4"/>
<path d="M140,40 L160,30 L160,96 L140,86" stroke="var(--ink)" stroke-width="4"/>
<path d="M60,90 L60,104" stroke="var(--ink)" stroke-width="4"/>
%s
%s
</svg>''' % (hl("a prova de que ele tava certo"), lit,
             T(30, 220, "a lanterna só", 40, "var(--pen)", rot=-2) + T(30, 270, "aponta pra um lado.", 40, "var(--pen)", rot=-2)), False))

A.append(("dark", '''<div style="margin-top:150px"></div>
<h1 style="font-size:78px">A subida pesa nas pernas uma vez.</h1>
<h1 class="or" style="font-size:78px; margin-top:24px">Na lembrança, ela pesa desde a largada.</h1>''', False))

A.append(("light", '''<h2>Pega a sua última prova.</h2>
<p style="margin-top:28px">Qual trecho pesou? A subida? Qual delas? E onde você começou a pensar nela: no km antes, na largada, no café da manhã? Marque os dois pontos.</p>
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:24px">
<path d="M20,220 L868,220" stroke="var(--ink)" stroke-width="4"/>
<path d="M20,206 L20,234 M868,206 L868,234" stroke="var(--ink)" stroke-width="4"/>
%s%s
<path d="M220,150 C220,108 280,108 280,150 C280,180 250,206 250,206 C250,206 220,180 220,150 Z" stroke="var(--pen)" stroke-width="4" stroke-dasharray="6 9"/>
<path d="M620,150 C620,108 680,108 680,150 C680,180 650,206 650,206 C650,206 620,180 620,150 Z" stroke="var(--ink)" stroke-width="4" stroke-dasharray="6 9"/>
%s%s
<path d="M256,270 L644,270 M272,258 L256,270 L272,282 M628,258 L644,270 L628,282" stroke="var(--pen)" stroke-width="3"/>
%s
</svg>
<p style="margin-top:20px">O espaço entre eles é o pedaço da prova que você correu %s.</p>''' % (
    T(20, 270, "largada", 28, "var(--mu)", fam="Inter"), T(868, 270, "chegada", 28, "var(--mu)", "end", fam="Inter"),
    T(250, 80, "comecei a pensar", 34, "var(--pen)", "middle"), T(650, 80, "o trecho de verdade", 34, "var(--ink)", "middle"),
    T(450, 316, "esse número é o seu diagnóstico", 32, "var(--pen)", "middle"),
    hl("carregando um trecho que ainda não tinha chegado")), False))

A.append(("dark", '''<h2 style="margin-bottom:40px">Pra quem é isso, e pra quem não é.</h2>
<div class="lab or">É para você se</div>
<p>um trecho específico da prova pesa antes de você chegar nele, mesmo com o treino em dia.</p>
<div class="sep"></div>
<div class="lab" style="color:var(--mu)">Não é para você se</div>
<p>a perna dói até em repouso ou piora a cada treino: médico ou fisioterapeuta. Se aquela prova tira o seu sono: psicólogo.</p>
<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:auto">
<path d="M20,140 L400,140 C450,140 470,70 520,66 C570,62 590,130 640,140 L868,140" stroke="var(--ink)" stroke-width="4"/>
<path d="M300,96 C300,64 340,64 340,96 C340,118 320,136 320,136 C320,136 300,118 300,96 Z" stroke="var(--pen)" stroke-width="4"/>
%s
<rect x="690" y="30" width="170" height="70" rx="8" stroke="var(--mu)" stroke-width="3"/>
<path d="M775,100 L775,140" stroke="var(--mu)" stroke-width="3"/>
%s
%s
</svg>''' % (T(320, 182, "pesa antes: aqui", 32, "var(--pen)", "middle"),
             T(775, 74, "consultório", 30, "var(--mu)", "middle"),
             T(775, 182, "dói parado: lá", 32, "var(--mu)", "middle")), False))

A.append(("light", '''<div style="margin-top:70px"></div>
<h1 style="font-size:76px">A subida vai estar no mesmo lugar.</h1>
<h1 class="or" style="font-size:76px; margin-top:20px">A leitura que você leva até ela, não.</h1>
<p class="mu" style="margin-top:44px">Salva pra reler na véspera da próxima prova que tem aquela subida.</p>
<svg class="draw" width="888" height="210" viewBox="0 0 888 210" style="margin-top:auto; margin-bottom:40px">
<path d="M20,180 L420,180 C500,180 520,70 600,64 C680,58 720,160 868,176" stroke="var(--ink)" stroke-width="4"/>
<path d="M570,0 L630,0 L630,110 L600,88 L570,110 Z" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
%s
</svg>''' % T(560, 40, "salvo pra véspera", 38, "var(--pen)", "end", rot=-2), True))

# ======================================================================= VERSÃO B
B = []
ANVIL = 'M0,0 L120,0 L120,14 C96,16 86,24 84,40 L96,64 L24,64 L36,40 C34,24 20,18 -30,12 Z'
FEATHER = ('M0,0 C30,-40 90,-60 130,-56 C110,-20 60,8 0,0 Z M0,0 L120,-50 '
           'M30,-14 L30,-36 M60,-24 L64,-48 M90,-34 L96,-54')
B.append(("light", '''<div style="margin-top:30px"></div>
<h1>Como um km plano pode pesar mais do que uma subida?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:30px">
<path d="M20,340 L470,340 C560,340 590,150 680,140 C760,132 800,280 868,316" stroke="var(--ink)" stroke-width="5"/>
<path d="M140,340 L380,340" stroke="var(--pen)" stroke-width="10"/>
<g transform="translate(200,232) scale(1.25)"><path d="%s" style="fill:var(--ink)" stroke="var(--ink)" stroke-width="3"/></g>
<path d="M190,330 L184,346 M396,330 L400,346" stroke="var(--pen)" stroke-width="4"/>
<g transform="translate(624,126)"><path d="%s" stroke="var(--mu)" stroke-width="3"/></g>
%s%s
</svg>''' % (ANVIL, FEATHER, T(260, 400, "km plano", 40, "var(--pen)", "middle"),
             T(690, 40, "subida", 40, "var(--mu)", "middle")), True))

B.append(("dark", '''<h2>Porque esse km não se mede em metros.</h2>
<p style="margin-top:32px">Sabe aquele km em que você quebrou da última vez? No mapa, ele é igual aos outros. Na sua cabeça, carrega %s.</p>
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:auto">
%s
<path d="M60,90 L828,90" stroke="var(--ink)" stroke-width="5"/>
<path d="M60,74 L60,106 M828,74 L828,106" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M60,230 L828,230" stroke="var(--ink)" stroke-width="5"/>
<path d="M60,214 L60,246 M828,214 L828,246" stroke="var(--ink)" stroke-width="4"/>
<path d="M90,230 C160,180 220,280 300,226 C380,180 420,290 520,222 C600,176 660,286 800,230" stroke="var(--pen)" stroke-width="4"/>
%s
</svg>
<div class="note" style="margin-top:20px; transform:rotate(-2deg)">e essa lembrança ainda aprende.</div>''' % (
    hl("aquele dia inteiro"),
    T(60, 46, "no mapa: 1 km plano", 38, "var(--mu)"),
    T(60, 186, "na sua cabeça: o km em que você parou", 38, "var(--pen)"),
    T(444, 310, "mesmo comprimento.", 34, "var(--mu)", "middle")), False))

route = ('<path d="M60,40 C200,10 300,90 240,150 C180,210 340,250 470,200 C600,150 640,60 760,90 C860,116 840,220 720,250 C620,274 560,300 600,330" '
         'stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>'
         '<path d="M470,200 C560,166 600,110 660,82" stroke="var(--pen)" stroke-width="12"/>')
B.append(("light", '''<div class="lab" style="color:var(--mu)">O que parece</div>
<h2>Você lembra da prova inteira.</h2>
<div class="lab or" style="margin-top:36px">O que acontece</div>
<p>Se liga nessa parte: o trecho que veio com emoção forte grava mais fundo que todo o resto. E fica preso %s.</p>
<svg class="draw" width="888" height="370" viewBox="0 0 888 370" style="margin-top:auto">
%s
<circle cx="60" cy="40" r="8" style="fill:var(--mu); stroke:none"/>
<circle cx="600" cy="330" r="8" style="fill:var(--mu); stroke:none"/>
%s%s
</svg>''' % (hl("ao lugar onde aconteceu"), route,
             T(560, 60, "isso ficou", 38, "var(--pen)", "end", rot=-3),
             T(20, 330, "o resto: pontilhado", 34, "var(--mu)")), False))

road = ""
for i in range(6):
    x = 110 + i * 126
    w = 4 + i * 9
    road += '<path d="M%d,370 L%d,370" stroke="var(--ink)" stroke-width="%d" stroke-opacity="%s"/>' % (x, x + 100, w, ".35" if i < 2 else ".8")
B.append(("dark", '''<div class="lab" style="color:var(--mu)">O que parece</div>
<h2>“Sempre acontece comigo.”</h2>
<div class="lab or" style="margin-top:36px">O que acontece</div>
<p>Cada vez que o mesmo sinal leva à mesma conclusão, a ligação fica mais forte e mais rápida. É %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto">
<path d="M60,10 L60,310 L868,310" stroke="var(--mu)" stroke-width="3"/>
<path d="M60,290 C300,284 520,220 660,120 C720,80 780,50 860,40" stroke="var(--pen)" stroke-width="5"/>
%s%s%s
%s
%s%s
</svg>''' % (hl("caminho repetido, não sentença"),
             T(76, 34, "o quanto custa ler diferente ↑", 30, "var(--mu)"),
             T(860, 300, "vezes que se repetiu →", 30, "var(--mu)", "end"),
             T(560, 110, "vira estrada", 36, "var(--pen)", "end"),
             road, T(110, 424, "trilha", 30, "var(--mu)"), T(850, 424, "asfalto", 30, "var(--ink)", "end")), False))

B.append(("light", '''<div class="lab" style="color:var(--mu)">O que parece</div>
<h2>A perna pesou porque hoje não é o seu dia.</h2>
<div class="lab or" style="margin-top:32px">O que acontece</div>
<p>Repara: o cérebro prevê o que você vai sentir pelo que já viveu ali. Previu sofrimento, o corpo se prepara antes. E a atenção vai atrás %s.</p>
<svg class="draw" width="888" height="300" viewBox="0 0 888 300" style="margin-top:auto">
<g transform="rotate(-3 444 150)">
<path d="M120,30 L760,30 L760,120 C736,120 736,180 760,180 L760,270 L120,270 L120,180 C144,180 144,120 120,120 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M600,40 L600,260" stroke="var(--mu)" stroke-width="3" stroke-dasharray="6 10"/>
%s%s%s%s
</g>
</svg>''' % (hl("da confirmação"),
             T(170, 96, "REPRISE", 56, "var(--ink)", fam="Inter", weight="800"),
             T(170, 160, "sessão: o km da quebra", 40, "var(--pen)"),
             T(170, 222, "comprado antes de você chegar", 34, "var(--mu)"),
             T(680, 166, "você", 36, "var(--ink)", "middle")), False))

B.append(("dark", '''<div style="margin-top:150px"></div>
<h1 style="font-size:78px">O peso na perna é igual para todo mundo.</h1>
<h1 class="or" style="font-size:78px; margin-top:24px">O que ele significa, você aprendeu. E dá pra treinar.</h1>''', False))

B.append(("light", qs("Pega a sua última prova e responde.", [
    ("Qual km pesou antes de chegar? Qual, exatamente?", "O da subida, o do retorno, o último antes da reta, aquele em que você parou da outra vez."),
    ("Quando começou a pensar nele? Na largada? Antes?", "No café da manhã, no carro, na fila do banheiro, no km anterior."),
    ("E quando a perna pesou, o que passou na cabeça?", "“Eu sabia”, “começou”, “é sempre aqui”. Essa frase é o seu diagnóstico.")]), False))

B.append(("dark", paraquem("Pra quem é isso, e pra quem não é.",
    "um km específico pesa antes mesmo de chegar, e nos treinos a perna responde bem.",
    "a perna dói também em casa ou o peso não passa com descanso: médico ou fisioterapeuta. Se aquela prova volta à cabeça e atrapalha o dia: psicólogo."), False))

PLANE = 'M0,60 L300,0 L120,90 Z M120,90 L140,140 L170,80 M300,0 L170,80'
B.append(("light", '''<div style="margin-top:70px"></div>
<h1 style="font-size:78px">Você não está fraco naquele km.</h1>
<h1 class="or" style="font-size:78px; margin-top:20px">Está lembrando.</h1>
<p class="mu" style="margin-top:44px">Manda pra aquele corredor que já avisa, antes da largada, em que km vai quebrar.</p>
<svg class="draw" width="888" height="230" viewBox="0 0 888 230" style="margin-top:auto; margin-bottom:40px">
<path d="M40,190 C140,200 240,150 330,110" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 12"/>
<g transform="translate(340,30)"><path d="%s" stroke="var(--ink)" stroke-width="4"/></g>
<rect x="520" y="120" width="360" height="80" rx="8" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 710 160)"/>
<path d="M560,140 L500,110" stroke="var(--pen)" stroke-width="3"/>
%s
</svg>''' % (PLANE, T(700, 172, "para: quem já sabe onde quebra", 28, "var(--ink)", "middle", rot=-3)), True))

# ======================================================================= VERSÃO C
def opt(y, letter, label, st, en, rest):
    return ('%s<path d="M90,%d L860,%d" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M%d,%d L%d,%d" stroke="var(--pen)" stroke-width="14" stroke-opacity=".85"/>'
            '<path d="M90,%d L90,%d M860,%d L860,%d" stroke="var(--ink)" stroke-width="4"/>%s%s') % (
        T(0, y + 14, letter, 62, "var(--pen)", fam="Inter", weight="800"), y, y, st, y, en, y,
        y - 14, y + 14, y - 14, y + 14, T(90, y + 58, label, 38, "var(--ink)"), rest)
C = []
C.append(("dark", '''<div style="margin-top:30px"></div>
<h1>Onde o último terço da sua prova começa a pesar?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:30px">
%s
%s
</svg>''' % (opt(80, "A", "no último terço", 600, 860, T(860, 40, "chegada", 26, "var(--mu)", "end", fam="Inter")),
             opt(270, "B", "na largada", 90, 860, T(90, 230, "largada", 26, "var(--mu)", fam="Inter"))), True))

C.append(("light", '''<h2>Se ele já te derrubou uma vez, pode ser B.</h2>
<p style="margin-top:32px">Ou antes: na véspera, quando você abre o percurso e o olho vai direto pro fim. Então a pergunta não é onde pesa. É %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto">
<path d="M120,20 L768,20 L768,380 L120,380 Z" stroke="var(--mu)" stroke-width="3" transform="rotate(2 444 200)"/>
<path d="M190,320 C240,240 200,160 300,140 C400,120 380,260 480,250 C560,242 560,120 640,100" stroke="var(--ink)" stroke-width="4"/>
<circle cx="190" cy="320" r="8" style="fill:var(--ink); stroke:none"/>
<ellipse cx="600" cy="150" rx="110" ry="88" stroke="var(--pen)" stroke-width="4" transform="rotate(-8 600 150)"/>
<ellipse cx="596" cy="156" rx="124" ry="96" stroke="var(--pen)" stroke-width="3" transform="rotate(6 600 150)"/>
<ellipse cx="604" cy="146" rx="100" ry="104" stroke="var(--pen)" stroke-width="3" transform="rotate(-20 600 150)"/>
%s%s
</svg>''' % (hl("por que pesa antes"), T(160, 360, "largada", 28, "var(--mu)", fam="Inter"),
             T(740, 340, "a véspera", 40, "var(--pen)", "end", rot=-3)), False))

def watch(x, y, buzz=True):
    s = ('<g transform="translate(%d,%d)"><rect x="-34" y="-40" width="68" height="80" rx="16" stroke="var(--ink)" stroke-width="4"/>'
         '<path d="M-22,-40 L-18,-70 L18,-70 L22,-40 M-22,40 L-18,70 L18,70 L22,40" stroke="var(--ink)" stroke-width="4"/>') % (x, y)
    if buzz:
        s += '<path d="M-48,-20 C-56,-6 -56,6 -48,20 M48,-20 C56,-6 56,6 48,20" stroke="var(--pen)" stroke-width="3"/>'
    return s + '</g>'
C.append(("dark", '''<div class="lab or">Pergunta 1</div>
<h2>O trecho pesa antes de chegar? Quanto antes? Por quê?</h2>
<p style="margin-top:28px">Ele ficou ligado a um momento forte. Daí, só o aviso de que ele tá chegando já %s a resposta daquele dia.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto">
%s%s%s
%s%s%s
<path d="M300,30 L300,370 M590,30 L590,370" stroke="var(--line)" stroke-width="3"/>
%s%s%s
%s%s%s
</svg>''' % (hl("dispara sozinho"),
             watch(140, 150), watch(440, 150), watch(740, 150),
             T(140, 40, "antes", 34, "var(--mu)", "middle"), T(444, 40, "aquele dia", 34, "var(--ink)", "middle"),
             T(740, 40, "depois", 34, "var(--pen)", "middle"),
             T(140, 290, "bzz →", 36, "var(--mu)", "middle"), T(444, 290, "bzz + quebra", 36, "var(--ink)", "middle"),
             T(740, 290, "bzz →", 36, "var(--pen)", "middle"),
             T(140, 340, "nada", 36, "var(--mu)", "middle"), T(444, 340, "ficam juntos", 36, "var(--ink)", "middle"),
             T(740, 340, "já pesa", 40, "var(--pen)", "middle")), False))

C.append(("light", '''<div class="lab or">Pergunta 2</div>
<h2>Pesou na última prova? Na anterior também? Então é destino?</h2>
<p style="margin-top:28px">Não. É repetição. Cada vez que o mesmo sinal leva à mesma conclusão, a ligação fica mais forte e %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto">
<path d="M60,10 L60,340 L868,340" stroke="var(--mu)" stroke-width="3"/>
<path d="M60,60 C260,80 420,200 560,260 C680,306 780,316 860,318" stroke="var(--ink)" stroke-width="4" stroke-dasharray="3 12"/>
<path d="M60,320 C260,310 420,200 560,130 C680,74 780,60 860,56" stroke="var(--pen)" stroke-width="5"/>
%s%s%s%s
</svg>''' % (hl("mais automática"),
             T(860, 100, "parece fato", 38, "var(--pen)", "end"),
             T(520, 300, "tempo para pensar", 32, "var(--ink)", "end"),
             T(860, 384, "vezes que se repetiu →", 30, "var(--mu)", "end"),
             T(80, 410, "é hábito, não destino.", 38, "var(--pen)", rot=-2)), False))

def tag(x, y, s, rot):
    return ('<g transform="rotate(%d %d %d)"><rect x="%d" y="%d" width="240" height="56" rx="8" stroke="var(--pen)" stroke-width="3"/>'
            '<circle cx="%d" cy="%d" r="6" stroke="var(--pen)" stroke-width="3"/>%s</g>') % (
        rot, x, y, x, y, x + 18, y + 28, T(x + 132, y + 38, s, 30, "var(--ink)", "middle"))
C.append(("dark", '''<div class="lab or">Pergunta 3</div>
<h2>Quando o corpo reage? No trecho? Ou antes?</h2>
<p style="margin-top:28px">Antes. O cérebro prevê pelo que já viveu. Se prevê sofrimento, o corpo já se prepara. E a atenção vai procurar %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto">
<rect x="80" y="120" width="420" height="250" rx="22" stroke="var(--ink)" stroke-width="5"/>
<path d="M210,120 L210,80 C210,64 220,58 236,58 L344,58 C360,58 370,64 370,80 L370,120" stroke="var(--ink)" stroke-width="5"/>
<path d="M80,190 L500,190" stroke="var(--ink)" stroke-width="3"/>
<path d="M500,170 L560,120 M500,250 L560,230 M500,320 L560,330" stroke="var(--pen)" stroke-width="3"/>
%s%s%s
%s
</svg>''' % (hl("o que confirma"),
             tag(560, 92, "ombro duro", -3), tag(560, 202, "fôlego curto", 2), tag(560, 304, "olho no relógio", -2),
             T(290, 290, "pronta na largada", 36, "var(--pen)", "middle", rot=-3)), False))

C.append(("light", '''<div style="margin-top:150px"></div>
<h1 style="font-size:78px">O sinal na perna é igual para todo mundo.</h1>
<h1 class="or" style="font-size:78px; margin-top:24px">A leitura que ele recebe é sua. E se treina.</h1>''', False))

def check(s):
    return ('<div style="display:flex; gap:28px; align-items:flex-start; padding:20px 0; border-top:2px dashed var(--line)">'
            '<svg class="draw" width="44" height="44" viewBox="0 0 44 44" style="flex:none; margin-top:4px"><rect x="3" y="3" width="38" height="38" rx="6" stroke="var(--pen)" stroke-width="4"/></svg>'
            '<div style="font-size:36px; line-height:1.3">%s</div></div>') % s
C.append(("dark", '''<h2 style="margin-bottom:24px">Pensa no seu último terço. O que rolou antes dele?</h2>
%s%s%s%s%s
<p style="margin-top:30px">Conte as marcas. Esse número é o seu diagnóstico: quantas vezes %s.</p>''' % (
    check("Olhou o relógio a cada poucos minutos, não a cada km."),
    check("Sentiu o ombro subir antes de o terreno mudar."),
    check("Já tinha a desculpa pronta: o calor, o tênis, a noite mal dormida."),
    check("Pensou: “sempre comigo”."),
    check("Lembrou o ponto exato: a placa, a curva, o posto de água."),
    hl("a lembrança chegou antes de você")), False))

C.append(("light", '''<h2 style="margin-bottom:40px">Pra quem é isso, e pra quem não é.</h2>
<div class="lab or">É para você se</div>
<p>o fim da prova começa a pesar cedo, mesmo quando o treino mostra que a perna aguenta.</p>
<div class="sep"></div>
<div class="lab" style="color:var(--mu)">Não é para você se</div>
<p>o peso vem com dor que não passa, inchaço ou falta de ar: médico ou fisioterapeuta. Se a prova ocupa a cabeça fora do esporte: psicólogo.</p>
<svg class="draw" width="888" height="170" viewBox="0 0 888 170" style="margin-top:auto">
<path d="M40,30 L400,30 L430,70 L400,110 L40,110 Z" stroke="var(--pen)" stroke-width="4"/>
<path d="M848,60 L488,60 L458,100 L488,140 L848,140 Z" stroke="var(--mu)" stroke-width="3"/>
%s%s
</svg>''' % (T(60, 84, "pesa por lembrança", 34, "var(--pen)"), T(830, 114, "pesa por outro motivo", 32, "var(--mu)", "end")), False))

C.append(("dark", '''<div style="margin-top:60px"></div>
<h1 style="font-size:74px">O último terço fica no fim do percurso.</h1>
<h1 class="or" style="font-size:74px; margin-top:18px">Na sua cabeça, ele pode começar na largada.</h1>
<p class="mu" style="margin-top:40px">Comenta aí: A ou B? E qual trecho pesa antes de chegar. Depois manda pra quem marcaria a outra.</p>
<svg class="draw" width="888" height="150" viewBox="0 0 888 150" style="margin-top:auto; margin-bottom:40px">
<rect x="20" y="30" width="848" height="90" rx="45" stroke="var(--ink)" stroke-width="3"/>
%s
<path d="M380,96 L620,96" stroke="var(--pen)" stroke-width="3"/>
<path d="M632,52 L632,104" stroke="var(--pen)" stroke-width="4"/>
%s
</svg>''' % (T(60, 90, "A ou B? o meu é", 40, "var(--ink)"), T(840, 90, "publicar", 30, "var(--pen)", "end", fam="Inter", weight="700")), True))

VERSOES = {"A": A, "B": B, "C": C}

LEGENDAS = {
"A": """Faz um teste no próximo treino que tiver subida.

Antes de chegar nela, repara no que acontece com você. O ombro sobe? O olho vai pro relógio? A respiração muda antes de o terreno mudar?

Depois do treino, anota. Não o pace. Anota o ponto em que a subida começou a pesar e o ponto em que ela começava de verdade.

Esse registro vale muito. O que a sua cabeça faz antes da subida é bem previsível: ela repete o que já viveu ali. E o que é previsível dá pra treinar.

A subida não fica mais leve porque você decidiu. Ela fica diferente quando você chega nela lendo o mesmo sinal de outro jeito.

Salva pra fazer esse teste no próximo treino com subida, e pra reler na véspera da prova.

Diagnóstico completo e sem custo? Tá no link da bio.""",

"B": """Você conhece esse corredor. Na concentração, antes da largada, ele já avisa em que km vai quebrar.

E aí quebra. Ali mesmo.

Ele não tem bola de cristal. Tem memória. Cada vez que repete essa frase, deixa a ligação entre aquele trecho e a quebra um pouco mais forte. A previsão vira roteiro.

Repara que o km em si não mudou. O sinal que chega na perna é o mesmo de sempre. O que mudou foi o significado que aquele lugar acende nele.

Uma coisa simples pra próxima prova: em vez de anunciar onde vai quebrar, descrever o que sentiu da última vez ali, sem conclusão. A perna pesou, o fôlego encurtou. Só isso. Descrever é diferente de prever.

Manda pra quem você sabe que já larga com esse km marcado na cabeça.

Seu diagnóstico, completo e gratuito, mora no endereço do perfil.""",

"C": """Véspera de prova. Você abre a altimetria. Pra onde o olho vai primeiro?

Se foi direto pro trecho que já te pegou uma vez, é dessa cena que eu tô falando. O corpo reage à lembrança antes de reagir ao terreno. Na véspera, você já está ensaiando.

Repara no que vem junto quando você olha: aperto, pressa de fechar o mapa, uma conta de quanto vai perder ali. É a previsão trabalhando, montada com o que você viveu, não com o que você treinou.

Um exercício pra próxima véspera: passa pelo percurso trecho por trecho e, pra cada um, lembra de um treino em que você passou por algo parecido. Inclusive o último terço. A lembrança forte não some, mas ganha companhia.

Comenta aqui embaixo: A ou B? E, se quiser, diz qual trecho é o seu.

Pra ir além do comentário, o diagnóstico inteiro sai de graça pelo link da bio.""",
}
