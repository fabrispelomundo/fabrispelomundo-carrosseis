# -*- coding: utf-8 -*-
# Pauta p02 — recriação de "Uma ultrapassagem e você desmontou" em 3 versões.
from base import *

def themes(first):
    other = "dark" if first == "light" else "light"
    return [first if i % 2 == 0 else other for i in range(9)]

def build(first, bodies):
    th = themes(first)
    return [(th[i], b, i in (0, 8)) for i, b in enumerate(bodies)]

def svg(h, inner, style="margin-top:40px"):
    return f'<svg class="draw" width="888" height="{h}" viewBox="0 0 888 {h}" style="{style}">{inner}</svg>'

def pen(x, y, t, size=38, color="var(--pen)", anchor="start", rot=0):
    tr = f' transform="rotate({rot} {x} {y})"' if rot else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Pen" font-size="{size}" fill="{color}"{tr}>{t}</text>'

def lab(t, color="var(--mu)"):
    return f'<text font-family="Inter" font-weight="800" font-size="22" fill="{color}" letter-spacing="3">{t}</text>'

# um "nó": rabisco emaranhado centrado em (cx, cy)
def knot(cx, cy, s=1.0, color="var(--pen)", w=4):
    d = ("M-60,0 C-60,-50 40,-60 55,-10 C70,40 -20,60 -45,25 C-70,-10 -10,-55 30,-35 "
         "C70,-15 40,45 0,40 C-40,35 -50,-20 -10,-25 C30,-30 35,20 5,22 C-20,24 -25,-5 0,-5")
    return f'<g transform="translate({cx},{cy}) scale({s})"><path d="{d}" stroke="{color}" stroke-width="{w / s:.1f}"/></g>'

def runner(x, y, lean=0, color="var(--ink)", w=4):
    # boneco simples correndo; (x,y) = pés
    return (f'<g transform="translate({x},{y}) rotate({lean})">'
            f'<circle cx="0" cy="-118" r="16" stroke="{color}" stroke-width="{w}"/>'
            f'<path d="M0,-100 L0,-46 M0,-46 L-22,0 M0,-46 L20,-6 L34,-2 M0,-86 L-24,-62 M0,-86 L24,-70 L36,-86" stroke="{color}" stroke-width="{w}"/></g>')

# =============================================================== VERSÃO A — capa clara — "pergunta para você"
A = []
A.append('''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">Em que km do longão você parou de pensar no tempo do seu amigo?</h1>
<h1 class="or" style="margin-top:18px; font-size:52px; line-height:1.1">No primeiro? Na volta? Só no banho, depois?</h1>''' + svg(400, f'''
<rect x="10" y="40" width="74" height="120" rx="12" stroke="var(--ink)" stroke-width="4"/>
<path d="M26,72 L68,72 M26,92 L58,92 M26,112 L64,112" stroke="var(--mu)" stroke-width="3"/>
<circle cx="47" cy="140" r="5" style="fill:var(--ink); stroke:none"/>
{pen(0, 210, "abri o app", 32, "var(--ink)")}
<path d="M100,140 C200,140 220,300 340,300 C470,300 470,160 600,160 C720,160 700,320 860,320" stroke="var(--mu)" stroke-width="4" stroke-dasharray="2 12"/>
<path d="M112,140 C200,140 220,300 340,300 C470,300 470,160 600,160 C720,160 700,320 852,320" stroke="var(--pen)" stroke-width="9" opacity=".85"/>
<circle cx="104" cy="140" r="9" style="fill:var(--ink); stroke:none"/>
<path d="M852,320 L852,250 L890,264 L852,278" stroke="var(--ink)" stroke-width="4"/>
{pen(880, 370, "fim do treino", 32, "var(--ink)", "end")}
{pen(250, 120, "ainda nele", 44, "var(--pen)", rot=-4)}
{pen(560, 120, "ainda nele", 44, "var(--pen)", rot=3)}
{pen(444, 432, "ler: segundos. o resto: o treino inteiro.", 40, "var(--ink)", "middle", -2)}
''', "margin-top:auto; margin-bottom:40px"))

A.append(f'''<h2>Ler levou segundos. Soltar levou o treino.</h2>
<p style="margin-top:36px">Repara nisso aqui: o número dele não pesa nada sozinho. Pesou porque encostou em algo que {hl("já era seu")}.</p>''' + svg(470, f'''
<ellipse cx="444" cy="250" rx="420" ry="130" stroke="var(--mu)" stroke-width="2" stroke-dasharray="3 10"/>
<ellipse cx="444" cy="250" rx="320" ry="98" stroke="var(--mu)" stroke-width="3"/>
<ellipse cx="444" cy="250" rx="210" ry="64" stroke="var(--ink)" stroke-width="3"/>
<ellipse cx="444" cy="250" rx="110" ry="34" stroke="var(--ink)" stroke-width="4"/>
<circle cx="444" cy="250" r="7" style="fill:var(--pen); stroke:none"/>
<path d="M444,60 L444,226 M432,212 L444,230 L456,212" stroke="var(--pen)" stroke-width="3"/>
{pen(460, 70, "o tempo dele", 36, "var(--pen)")}
{pen(444, 440, "o resto da sua manhã", 38, "var(--ink)", "middle", -2)}
''', "margin-top:auto"))

A.append(f'''<h2>Por trás tem um&nbsp; {circ("nó")} &nbsp;antigo.</h2>
<p style="margin-top:36px">Lembranças e emoções amarradas em volta de um tema seu. Ele fica quieto até alguém de fora puxar uma ponta.</p>''' + svg(440, f'''
{knot(300, 220, 1.7)}
<path d="M200,190 C150,140 120,120 70,110" stroke="var(--ink)" stroke-width="3"/>
<path d="M240,290 C200,340 150,360 90,370" stroke="var(--ink)" stroke-width="3"/>
<path d="M330,130 C340,90 360,60 400,40" stroke="var(--ink)" stroke-width="3"/>
{pen(0, 96, "lembranças", 34, "var(--ink)")}
{pen(10, 412, "emoções", 34, "var(--ink)")}
{pen(410, 46, "um tema seu", 34, "var(--ink)")}
<path d="M398,236 C500,240 560,226 680,224" stroke="var(--pen)" stroke-width="4"/>
<path d="M662,210 L686,224 L662,238" stroke="var(--pen)" stroke-width="4"/>
<rect x="700" y="164" width="76" height="124" rx="12" stroke="var(--pen)" stroke-width="4"/>
<path d="M716,196 L760,196 M716,218 L748,218" stroke="var(--pen)" stroke-width="3"/>
{pen(738, 340, "o tempo", 34, "var(--pen)", "middle")}
{pen(738, 376, "do amigo", 34, "var(--pen)", "middle")}
{pen(540, 214, "puxou", 34, "var(--pen)", "middle", -3)}
''', "margin-top:auto"))

A.append(f'''<h2>O app fecha. A reação continua aberta.</h2>
<p style="margin-top:36px">Olha isso: ela demora a baixar mesmo depois que o motivo saiu da tela. Esse {hl("rastro")} mostra onde o nó está.</p>''' + svg(450, f'''
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,370 L120,370 L120,280 L210,280 L210,370 L860,370" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 12"/>
{pen(120, 266, "na tela", 34, "var(--ink)")}
<path d="M40,370 C90,368 110,120 160,90 C260,40 340,120 460,190 C600,270 740,320 860,340" stroke="var(--pen)" stroke-width="5"/>
{pen(250, 60, "o que você sente", 38, "var(--pen)")}
<path d="M260,140 L260,370 M340,150 L340,370 M420,170 L420,370 M500,212 L500,370 M580,250 L580,370 M660,276 L660,370 M740,300 L740,370" stroke="var(--pen)" stroke-width="2" opacity=".55"/>
{pen(520, 160, "o rastro", 44, "var(--pen)", rot=-3)}
<text x="740" y="420" font-family="Inter" font-size="22" fill="var(--mu)">tempo →</text>
''', "margin-top:auto"))

A.append(f'''<h2>Muda a cena. O nó é o mesmo.</h2>
<p style="margin-top:36px">O ranking do app, a foto de chegada de alguém, o amigo que baixou o tempo. Se os três mexem igual, não são {hl("três problemas")}. É um só.</p>''' + svg(460, f'''
<rect x="30" y="20" width="180" height="120" rx="12" stroke="var(--ink)" stroke-width="4"/>
<path d="M54,50 L186,50 M54,78 L186,78 M54,106 L186,106" stroke="var(--mu)" stroke-width="3"/>
<text x="40" y="58" font-family="Inter" font-weight="800" font-size="18" fill="var(--ink)">1</text>
{pen(120, 182, "ranking", 32, "var(--ink)", "middle")}
<rect x="354" y="20" width="180" height="120" rx="6" stroke="var(--ink)" stroke-width="4"/>
{runner(444, 132, 0, "var(--ink)", 3).replace('translate(444,132)', 'translate(444,132) scale(.8)')}
<path d="M372,96 L516,96" stroke="var(--mu)" stroke-width="2" stroke-dasharray="6 6"/>
{pen(444, 182, "foto de chegada", 32, "var(--ink)", "middle")}
<rect x="700" y="20" width="96" height="140" rx="14" stroke="var(--ink)" stroke-width="4"/>
<path d="M748,50 L748,120 M728,100 L748,124 L768,100" stroke="var(--ink)" stroke-width="4"/>
{pen(748, 202, "baixou o tempo", 32, "var(--ink)", "middle")}
<path d="M120,210 C140,300 260,340 380,360" stroke="var(--mu)" stroke-width="3"/>
<path d="M444,212 L444,300" stroke="var(--mu)" stroke-width="3"/>
<path d="M748,226 C720,300 620,340 510,360" stroke="var(--mu)" stroke-width="3"/>
{knot(444, 376, 0.9)}
{pen(560, 420, "um só", 42, "var(--pen)", rot=-3)}
''', "margin-top:auto"))

A.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">O tempo dele some quando você fecha o app.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">O rastro que fica mostra onde está o seu nó.</h1>''')

A.append(qs("Pensa na sua última semana.", [
    ("De quem foi o resultado? O que exatamente você viu?", "O tempo no app, a foto no grupo, a posição no ranking de domingo."),
    ("Quando passou? Na hora? No meio do treino? Só à noite?", "Lembra onde você estava quando parou de pensar nisso. Esse trecho é o rastro."),
    ("Já sentiu isso antes? Com quem? Em que cena?", "Uma prova, um treino em grupo, um comentário. Escreve numa palavra o que se repete.")]) +
    '<div class="note" style="margin-top:auto; transform:rotate(-2deg)">dar nome não desata o nó.<br>mas ele passa a mandar menos.</div>')

A.append(paraquem("Pra quem é isso, e pra quem não é.",
    "o resultado dos outros tira você do seu treino ou da sua prova, e você quer entender o que está sendo tocado.",
    "o incômodo invade o sono, o trabalho ou as relações, ou se o que vem à tona pesa demais para olhar sozinho. Aí o caminho é um psicólogo."))

A.append('''<div style="margin-top:60px"></div>
<h1 style="font-size:78px">Você não precisa desatar o nó para correr.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Precisa saber onde ele está.</h1>
<p class="mu" style="margin-top:44px">Salva pra reler na próxima vez que o tempo de alguém entrar no seu treino.</p>''' + svg(250, f'''
<path d="M600,10 L760,10 L760,230 L680,180 L600,230 Z" stroke="var(--pen)" stroke-width="5" style="fill:var(--hl)"/>
{knot(680, 92, 0.6, "var(--ink)", 4)}
{pen(0, 90, "guarda antes", 40, "var(--pen)", rot=-2)}
{pen(0, 140, "do próximo ranking", 40, "var(--pen)", rot=-2)}
<path d="M380,110 C450,110 520,110 580,112 M562,98 L582,112 L562,126" stroke="var(--pen)" stroke-width="4"/>
''', "margin-top:30px"))

# =============================================================== VERSÃO B — capa escura — "pergunta-enigma"
def parece(t):
    return f'<div class="lab" style="color:var(--mu)">Parece</div><h2 style="color:var(--mu); font-size:54px">{t}</h2>'
def acontece(t):
    return f'<div class="lab or" style="margin-top:34px">Acontece</div><p>{t}</p>'

B = []
B.append('''<div style="margin-top:20px"></div>
<h1 style="font-size:78px">Por que o mesmo ranking deixa seu parceiro de treino de boa e tira você do eixo?</h1>''' + svg(410, f'''
<rect x="384" y="10" width="120" height="190" rx="16" stroke="var(--ink)" stroke-width="4"/>
<path d="M404,50 L484,50 M404,82 L484,82 M404,114 L484,114 M404,146 L470,146" stroke="var(--mu)" stroke-width="3"/>
<path d="M378,110 C300,120 250,160 220,220 M206,200 L218,224 L240,208" stroke="var(--ink)" stroke-width="3"/>
<path d="M510,110 C588,120 638,160 668,220 M648,208 L670,224 L682,200" stroke="var(--ink)" stroke-width="3"/>
<circle cx="200" cy="300" r="62" stroke="var(--ink)" stroke-width="4"/>
<path d="M170,300 L230,300" stroke="var(--mu)" stroke-width="4"/>
<circle cx="688" cy="300" r="62" stroke="var(--ink)" stroke-width="4"/>
<path d="M650,300 C660,262 720,262 718,300 C716,336 662,336 664,300 C666,276 706,276 704,300 C702,318 676,318 680,298 C690,250 740,280 724,330 C700,360 640,350 646,290" stroke="var(--pen)" stroke-width="4"/>
{pen(200, 400, "ele", 38, "var(--mu)", "middle")}
{pen(688, 400, "você", 38, "var(--pen)", "middle")}
''', "margin-top:auto; margin-bottom:40px"))

B.append(f'''<h2>Porque a lista é a mesma. O que ela toca, não.</h2>
<p style="margin-top:36px">Se liga nessa parte: a sua posição no app não tem força sozinha. Ela {hl("pega força emprestada")} de algo que já estava aí.</p>''' + svg(480, f'''
<path d="M0,120 L888,120" stroke="var(--mu)" stroke-width="3" stroke-dasharray="10 10"/>
<rect x="384" y="70" width="120" height="44" rx="6" stroke="var(--ink)" stroke-width="4"/>
<path d="M398,92 L490,92" stroke="var(--mu)" stroke-width="3"/>
{pen(530, 100, "o que se vê", 34, "var(--ink)")}
<path d="M444,124 C320,150 210,220 200,300 C190,390 320,450 444,452 C590,454 700,400 690,300 C680,210 560,150 444,124" stroke="var(--pen)" stroke-width="5"/>
<path d="M290,260 C330,250 380,280 420,270 M330,340 C390,330 450,360 520,340 M480,230 C520,222 560,240 600,232" stroke="var(--pen)" stroke-width="3" opacity=".6"/>
{pen(444, 312, "o que já estava aí", 40, "var(--pen)", "middle", -2)}
{pen(0, 60, "posição no app", 32, "var(--mu)")}
''', "margin-top:auto"))

B.append(parece("Você reagiu ao que aconteceu.") + acontece(f'O fato acertou um alvo que já existia: lembranças e emoções juntas em volta de {hl("um tema seu")}.') + svg(420, f'''
<circle cx="560" cy="226" r="182" stroke="var(--mu)" stroke-width="3"/>
<circle cx="560" cy="220" r="125" stroke="var(--ink)" stroke-width="3"/>
<circle cx="560" cy="220" r="58" stroke="var(--pen)" stroke-width="4"/>
{pen(560, 22, "lembranças", 32, "var(--mu)", "middle")}
{pen(560, 120, "emoções", 32, "var(--ink)", "middle")}
{pen(560, 302, "um tema seu", 32, "var(--pen)", "middle")}
<path d="M30,120 L548,216" stroke="var(--ink)" stroke-width="4"/>
<path d="M30,120 L10,96 M30,120 L4,128" stroke="var(--ink)" stroke-width="3"/>
<path d="M530,200 L552,218 L524,222" stroke="var(--ink)" stroke-width="4"/>
{pen(0, 200, "o ranking", 34, "var(--ink)", rot=6)}
''', "margin-top:auto"))

B.append(parece("Você pensou e depois reagiu.") + acontece(f'Repara: a reação sai na frente. Quando o raciocínio chega, {hl("ela já está decidindo")} o seu ritmo.') + svg(430, f'''
<path d="M40,10 L40,360 L870,360" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,350 C80,348 100,90 170,70 C260,46 500,60 860,70" stroke="var(--pen)" stroke-width="5"/>
{pen(220, 44, "a reação", 40, "var(--pen)")}
<path d="M40,352 C300,350 420,330 520,250 C620,170 720,150 860,146" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 12"/>
{pen(600, 216, "o raciocínio", 38, "var(--ink)")}
<path d="M170,110 L170,340 M470,110 L470,300" stroke="var(--mu)" stroke-width="2"/>
<path d="M180,120 L460,120 M444,108 L462,120 L444,132 M196,108 L178,120 L196,132" stroke="var(--mu)" stroke-width="2"/>
{pen(320, 170, "você já estava", 32, "var(--mu)", "middle")}
{pen(320, 206, "dentro dela", 32, "var(--mu)", "middle")}
<text x="740" y="400" font-family="Inter" font-size="22" fill="var(--mu)">tempo →</text>
''', "margin-top:auto"))

def cloud(cx, cy, s=1.0):
    d = "M-70,10 C-90,-30 -40,-60 -10,-40 C10,-75 70,-60 66,-20 C100,-10 96,40 60,44 C40,74 -20,70 -30,46 C-70,56 -96,30 -70,10 Z"
    return (f'<g transform="translate({cx},{cy}) scale({s})"><path d="{d}" stroke="var(--pen)" stroke-width="{4/s:.1f}"/>'
            f'<path d="M-30,0 C-20,-20 20,-20 30,0 C20,20 -10,16 -5,0" stroke="var(--pen)" stroke-width="{3/s:.1f}"/></g>')

B.append(parece("Entender o motivo faz ele sumir.") + acontece(f'Pois é, ele não some. Mas, quando você reconhece e dá nome ao tema, ele {hl("decide menos")} por você.') + svg(420, f'''
{cloud(110, 170, 0.9)}
<path d="M176,190 C230,230 250,240 296,250" stroke="var(--ink)" stroke-width="3"/>
{runner(320, 330, 28)}
<path d="M240,340 L380,340" stroke="var(--mu)" stroke-width="2"/>
{pen(200, 410, "sem nome: ele puxa", 34, "var(--mu)", "middle")}
<path d="M444,20 L444,400" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 12"/>
{runner(600, 330, 0)}
<path d="M626,262 C680,300 700,300 730,270" stroke="var(--ink)" stroke-width="3"/>
{cloud(760, 240, 0.7)}
<rect x="730" y="300" width="80" height="34" rx="6" stroke="var(--ink)" stroke-width="3"/>
<path d="M742,320 L798,320" stroke="var(--pen)" stroke-width="3"/>
<path d="M520,340 L860,340" stroke="var(--mu)" stroke-width="2"/>
{pen(680, 410, "com nome: ele vai junto", 34, "var(--pen)", "middle")}
''', "margin-top:auto"))

B.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">O ranking diz onde você chegou.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A sua reação diz onde você foi tocado.</h1>''')

def form_row(y):
    return (f'<path d="M20,{y} L270,{y} M310,{y} L540,{y} M580,{y} L868,{y}" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>')

B.append('''<h2>Preenche aí, de cabeça.</h2>
<p style="margin-top:30px">Quais foram as três últimas vezes? O que você viu? Onde estava? No ônibus, na cama, no aquecimento?</p>''' + svg(470, f'''
<rect x="4" y="10" width="880" height="400" rx="12" stroke="var(--ink)" stroke-width="4" transform="rotate(-1 444 210)"/>
<g transform="rotate(-1 444 210)">
<text x="30" y="70" font-family="Inter" font-weight="800" font-size="22" fill="var(--ink)">O QUE VOCÊ VIU</text>
<text x="310" y="70" font-family="Inter" font-weight="800" font-size="22" fill="var(--ink)">ATÉ QUANDO DUROU</text>
<text x="580" y="70" font-family="Inter" font-weight="800" font-size="22" fill="var(--pen)">O QUE ELE TOCOU</text>
<path d="M4,96 L884,96" stroke="var(--ink)" stroke-width="3"/>
{form_row(180)}{form_row(270)}{form_row(360)}
{pen(30, 166, "1.", 34, "var(--mu)")}{pen(70, 166, "a foto no grupo", 32, "var(--mu)")}{pen(320, 166, "até o almoço", 32, "var(--mu)")}{pen(590, 166, "?", 36, "var(--pen)")}{pen(30, 256, "2.", 34, "var(--mu)")}{pen(30, 346, "3.", 34, "var(--mu)")}
</g>
{pen(444, 460, "se a última coluna se repete, você achou o tema.", 36, "var(--pen)", "middle", -2)}
''', "margin-top:auto"))

B.append(paraquem("Pra quem é isso, e pra quem não é.",
    "a posição, o tempo ou a foto de alguém tira você do seu treino, e você quer entender por quê.",
    "esse incômodo aparece em tudo, atrapalha o sono ou o trabalho, ou se as lembranças que surgem são pesadas demais. Aí procure um psicólogo."))

B.append('''<div style="margin-top:60px"></div>
<h1 style="font-size:78px">Não foi a lista que mexeu com você.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Foi o que ela encontrou.</h1>
<p class="mu" style="margin-top:44px">Manda pra aquele corredor do seu grupo que abre o ranking antes de olhar o próprio treino.</p>''' + svg(250, f'''
<path d="M560,120 L860,20 L760,220 L700,150 Z M700,150 L860,20 M700,150 L690,200 L730,176" stroke="var(--pen)" stroke-width="4" style="fill:var(--hl)"/>
<path d="M40,220 C160,230 300,200 420,170 C480,156 520,140 548,126" stroke="var(--pen)" stroke-width="3" stroke-dasharray="4 12"/>
{pen(0, 60, "para: quem confere", 38, "var(--pen)", rot=-2)}
{pen(0, 104, "a posição dos outros primeiro", 38, "var(--pen)", rot=-2)}
''', "margin-top:30px"))

# =============================================================== VERSÃO C — capa clara — "A ou B?"
C = []
C.append('''<div style="margin-top:40px"></div>
<h1>Qual tira você do treino mais rápido: A&nbsp;ou&nbsp;B?</h1>''' + svg(470, f'''
<rect x="20" y="40" width="380" height="290" rx="8" stroke="var(--ink)" stroke-width="4" transform="rotate(-3 210 185)"/>
<g transform="rotate(-3 210 185)">
<path d="M50,240 L370,240" stroke="var(--pen)" stroke-width="3" stroke-dasharray="8 8"/>
<g transform="translate(210,300) scale(1.1)"><circle cx="0" cy="-160" r="18" stroke="var(--ink)" stroke-width="4"/>
<path d="M0,-140 L0,-70 M0,-70 L-26,0 M0,-70 L26,0 M0,-124 L-40,-170 M0,-124 L40,-170" stroke="var(--ink)" stroke-width="4"/></g>
</g>
<text x="40" y="34" font-family="Pen" font-size="64" fill="var(--pen)">A</text>
{pen(210, 400, "a foto de chegada", 32, "var(--ink)", "middle")}
{pen(210, 438, "de alguém do grupo", 32, "var(--ink)", "middle")}
<rect x="540" y="30" width="210" height="320" rx="24" stroke="var(--ink)" stroke-width="4" transform="rotate(3 645 190)"/>
<g transform="rotate(3 645 190)">
<rect x="560" y="90" width="170" height="100" rx="10" stroke="var(--pen)" stroke-width="3"/>
<text x="645" y="130" text-anchor="middle" font-family="Inter" font-weight="800" font-size="18" fill="var(--pen)">NOVO RECORDE</text>
<text x="645" y="158" text-anchor="middle" font-family="Inter" font-weight="800" font-size="18" fill="var(--pen)">PESSOAL</text>
<path d="M580,230 L710,230 M580,260 L690,260" stroke="var(--mu)" stroke-width="3"/>
</g>
<text x="770" y="40" font-family="Pen" font-size="64" fill="var(--pen)">B</text>
{pen(660, 400, "o aviso do recorde", 32, "var(--ink)", "middle")}
{pen(660, 438, "de um amigo", 32, "var(--ink)", "middle")}
''', "margin-top:auto; margin-bottom:30px"))

C.append(f'''<h2>Se você ficou em dúvida, já respondeu.</h2>
<p style="margin-top:36px">Já parou pra pensar nisso? Se as duas mexem do mesmo jeito, o problema não está na foto nem no aviso. Está no que {hl("as duas tocam")} em você.</p>''' + svg(430, f'''
<circle cx="120" cy="90" r="40" stroke="var(--ink)" stroke-width="4"/>
<path d="M160,90 L330,90 M300,90 L300,116 M276,90 L276,108" stroke="var(--ink)" stroke-width="4"/>
{pen(108, 104, "A", 40, "var(--pen)")}
<rect x="80" y="270" width="80" height="80" rx="4" stroke="var(--ink)" stroke-width="4" transform="rotate(45 120 310)"/>
<path d="M176,310 L330,310 M290,310 L290,336 M310,310 L310,330 M266,310 L266,326" stroke="var(--ink)" stroke-width="4"/>
{pen(108, 324, "B", 40, "var(--pen)")}
<path d="M350,100 C440,120 500,170 560,200 M542,184 L564,202 L536,206" stroke="var(--mu)" stroke-width="3"/>
<path d="M350,300 C440,280 500,240 560,226 M534,214 L564,224 L540,244" stroke="var(--mu)" stroke-width="3"/>
<path d="M640,180 L640,140 C640,90 760,90 760,140 L760,180" stroke="var(--pen)" stroke-width="5"/>
<rect x="610" y="180" width="180" height="150" rx="14" stroke="var(--pen)" stroke-width="5"/>
<circle cx="700" cy="240" r="14" stroke="var(--pen)" stroke-width="4"/>
<path d="M700,254 L700,290" stroke="var(--pen)" stroke-width="5"/>
{pen(700, 390, "a mesma fechadura", 36, "var(--pen)", "middle", -2)}
''', "margin-top:auto"))

def quiz(n, q):
    return f'<div class="lab or">Pergunta {n}</div><h2>{q}</h2>'

C.append(quiz(1, "Por que uma foto pesa tanto? Qualquer foto?") + f'''
<p style="margin-top:30px">Não. Só a que cai num copo que já estava cheio: lembranças e emoções juntas em volta de {hl("um tema seu")}.</p>''' + svg(470, f'''
<path d="M300,120 L330,440 L560,440 L590,120" stroke="var(--ink)" stroke-width="5"/>
<path d="M304,150 C380,140 500,160 586,148" stroke="var(--pen)" stroke-width="4"/>
<path d="M312,250 C400,240 480,262 576,250" stroke="var(--mu)" stroke-width="3"/>
<path d="M320,350 C400,340 480,360 568,350" stroke="var(--mu)" stroke-width="3"/>
{pen(445, 214, "lembranças", 32, "var(--ink)", "middle")}
{pen(445, 314, "emoções", 32, "var(--ink)", "middle")}
{pen(445, 408, "um tema seu", 32, "var(--pen)", "middle")}
<path d="M445,20 C430,46 430,60 445,64 C460,60 460,46 445,20 Z" stroke="var(--pen)" stroke-width="4"/>
{pen(470, 56, "a foto", 34, "var(--pen)")}
<path d="M590,124 C620,140 640,180 650,240 M300,124 C270,140 250,180 240,240" stroke="var(--pen)" stroke-width="4"/>
{pen(670, 290, "a reação", 36, "var(--pen)")}
''', "margin-top:auto"))

def spike(x, h=210, base=360):
    return f'<path d="M{x-50},{base} C{x-30},{base} {x-16},{base-h} {x},{base-h} C{x+20},{base-h} {x+40},{base-20} {x+90},{base-6}" stroke="var(--pen)" stroke-width="5"/>'

C.append(quiz(2, "Por que volta? Com a foto, o aviso, o ranking?") + f'''
<p style="margin-top:30px">Porque o tema é o mesmo. Muda a cena, e a reação {hl("acorda igual")}.</p>''' + svg(470, f'''
<path d="M30,10 L30,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M30,366 L870,366" stroke="var(--mu)" stroke-width="2" stroke-dasharray="3 12"/>
{spike(170)}{spike(440)}{spike(710)}
<path d="M80,150 L840,150" stroke="var(--ink)" stroke-width="2" stroke-dasharray="10 10"/>
{pen(860, 136, "a mesma altura", 32, "var(--ink)", "end")}
{pen(170, 430, "a foto", 34, "var(--ink)", "middle")}
{pen(440, 430, "o aviso", 34, "var(--ink)", "middle")}
{pen(710, 430, "o ranking", 34, "var(--ink)", "middle")}
<text x="740" y="466" font-family="Inter" font-size="22" fill="var(--mu)">semanas →</text>
''', "margin-top:auto"))

C.append(quiz(3, "Dá pra desligar? De vez?") + f'''
<p style="margin-top:30px">Não. Mas reconhecer e dar nome ao tema {hl("diminui o quanto")} ele decide por você.</p>''' + svg(450, f'''
<circle cx="444" cy="250" r="130" stroke="var(--ink)" stroke-width="5"/>
<circle cx="444" cy="250" r="14" style="fill:var(--ink); stroke:none"/>
<path d="M260,350 C210,250 250,150 330,100" stroke="var(--mu)" stroke-width="3"/>
<path d="M558,100 C640,150 680,250 628,350" stroke="var(--mu)" stroke-width="3"/>
<path d="M444,250 L560,330" stroke="var(--mu)" stroke-width="4" stroke-dasharray="4 10"/>
{pen(640, 396, "sem nome", 34, "var(--mu)")}
<path d="M444,250 L444,130" stroke="var(--pen)" stroke-width="7"/>
{pen(444, 90, "com nome", 38, "var(--pen)", "middle")}
<path d="M300,370 L340,330 M300,330 L340,370" stroke="var(--ink)" stroke-width="4"/>
{pen(150, 420, "o zero não existe", 34, "var(--ink)", rot=-2)}
''', "margin-top:auto"))

C.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A foto era de outra pessoa.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">O incômodo tinha o seu endereço.</h1>''')

def check(y, t, marked=False):
    mk = f'<path d="M8,{y-10} L24,{y+8} L56,{y-34}" stroke="var(--pen)" stroke-width="5"/>' if marked else ""
    return (f'<rect x="4" y="{y-30}" width="44" height="44" rx="6" stroke="var(--ink)" stroke-width="4"/>{mk}'
            f'<text x="80" y="{y}" font-family="Inter" font-size="33" fill="var(--ink)">{t}</text>')

C.append('''<h2>Marca aí o que já aconteceu com você.</h2><p class="mu" style="margin-top:20px">Quando foi a última? Onde você estava? No ônibus, na cama, no aquecimento?</p>''' + svg(560, f'''
{check(70, "Fechei o app e levei o incômodo pro treino.", True)}
{check(170, "Uma foto e um aviso me pegaram igual.")}
{check(270, "Reagi antes de entender por quê.")}
{check(370, "Lembro onde eu estava quando bateu.")}
{check(470, "Sei dizer numa palavra o que foi tocado.")}
''', "margin-top:30px") + '<div class="note" style="margin-top:auto; transform:rotate(-2deg)">cada marca aponta<br>para o mesmo lugar.</div>')

C.append(paraquem("Pra quem é isso, e pra quem não é.",
    "a conquista de alguém do seu grupo tira você do seu treino, e você quer entender o que ela está tocando.",
    "esse peso aparece fora da corrida também, no sono, no trabalho, nas relações, ou se o que vem à tona é difícil demais de olhar sozinho. Aí o caminho é um psicólogo."))

C.append('''<div style="margin-top:60px"></div>
<h1 style="font-size:78px">Não é a foto.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">É onde ela encosta em você.</h1>
<p class="mu" style="margin-top:44px">Comenta aí: A ou B? E manda pra quem marcaria a outra.</p>''' + svg(280, f'''
<rect x="40" y="70" width="620" height="110" rx="55" stroke="var(--ink)" stroke-width="4"/>
<text x="100" y="146" font-family="Pen" font-size="60" fill="var(--pen)">A</text>
<path d="M150,100 L150,154" stroke="var(--ink)" stroke-width="3"/>
{pen(190, 138, "ou B?", 40, "var(--mu)")}
<rect x="680" y="85" width="170" height="80" rx="40" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
<text x="765" y="138" text-anchor="middle" font-family="Inter" font-weight="800" font-size="28" fill="var(--ink)">publicar</text>
{pen(60, 240, "e marca quem escolheria a outra.", 34, "var(--pen)", rot=-1)}
''', "margin-top:40px"))

VERSOES = {"A": build("light", A), "B": build("dark", B), "C": build("light", C)}

LEGENDAS = {"A": """Sabe aquele longão em que você sai de casa já com o tempo de alguém na cabeça? Você nem decidiu pensar nisso. Simplesmente estava lá.

Tem um jeito simples de usar isso a seu favor no próximo treino. Quando perceber que a cabeça voltou pro número de outra pessoa, marca mentalmente o ponto: qual trecho, qual subida, qual semáforo.

Depois do treino, escreve só duas coisas: onde começou e onde parou. Não precisa explicar nem resolver. O tamanho desse trecho diz mais sobre você do que o tempo do outro.

Faz isso por três ou quatro treinos. O gatilho muda, mas repara se o lugar onde ele encosta é o mesmo. Dar nome a esse lugar já tira um pouco da força dele.

Salva pra fazer esse registro no próximo longão, antes de abrir o app.

Quer ir além? O diagnóstico gratuito, inteiro, te espera no link do perfil.""",

"B": """Repara numa coisa no seu grupo de corrida. A mesma notícia chega pra todo mundo: um pódio, um recorde, uma posição no app. Tem gente que comenta e segue o dia. Tem gente que fica com aquilo grudado até a noite.

A diferença não está na notícia. Está no que cada um carrega antes dela chegar.

Um teste pra próxima vez: quando bater o incômodo, troca a pergunta. Em vez de "por que ele foi melhor?", pergunta "o que isso encostou em mim?". A primeira olha pra fora e não tem fim. A segunda olha pra dentro e costuma caber em uma ou duas palavras.

Essa resposta não faz o incômodo sumir. Mas, com nome, ele decide menos o seu treino do dia seguinte.

Manda pra quem do seu grupo responde toda conquista alheia com um "boa!" e depois passa o dia remoendo.

Diagnóstico completo, sem pagar nada, no endereço da bio.""",

"C": """Já reparou em que hora você abre o app de corrida? Ao acordar, no intervalo do trabalho, antes de dormir. A hora conta, porque é ali que a foto ou o aviso de alguém te encontra desprevenido.

Uma ideia pro próximo treino: deixa o app fechado até terminar. Não é proibição, é observação. Repara como o treino corre sem o resultado de outra pessoa entrando no meio.

E no dia em que abrir e bater, anota três coisas: o que você viu, onde estava e quanto tempo levou pra voltar ao seu ritmo. Três linhas no bloco de notas bastam. Com o tempo, essas linhas começam a apontar sempre pro mesmo lugar.

Comenta aqui embaixo: A ou B? Qual das duas te pegou mais na última vez?

Pra enxergar o quadro inteiro: diagnóstico de graça, link na bio.""",
}
