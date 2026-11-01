# -*- coding: utf-8 -*-
# p09 — desafio x ameaça antes da largada. 3 versões (A escura, B clara, C clara).
from base import *

D, L = "dark", "light"

def alt(first):
    o = [first]
    for _ in range(8):
        o.append(L if o[-1] == D else D)
    return o

CHECK = 'M%d,%d l10,12 l22,-26'

# ------------------------------------------------------------------ desenhos
def shoe(x, y, s, loose=False, tag=None):
    """Tênis de corrida de lado. loose=False: cadarço puxado até amassar o cabedal."""
    if not loose:
        upper = ('M30,170 C14,140 22,104 52,96 C70,92 84,84 96,66 C108,48 140,46 156,64 '
                 'C176,86 200,110 236,128 C250,134 262,134 276,128 C300,118 330,118 380,128 '
                 'C450,142 520,150 548,166 C556,172 552,180 540,180')
        laces = ('M196,98 L254,132 M206,126 L250,104 M226,82 L272,126 M224,130 L276,92 '
                 'M246,74 L290,118')
        strain = 'M236,150 L242,140 M262,152 L262,140 M286,150 L280,140 M180,84 L170,76 M300,100 L310,92'
        knot = ('<path d="M262,96 C240,60 214,72 230,90 M262,96 C286,62 312,76 292,92" stroke="var(--pen)" stroke-width="4"/>'
                '<circle cx="262" cy="96" r="7" style="fill:var(--pen); stroke:none"/>')
    else:
        upper = ('M30,170 C14,140 22,104 52,96 C70,92 84,84 96,66 C108,48 140,46 156,64 '
                 'C180,84 210,96 250,100 C300,104 340,112 380,124 '
                 'C450,142 520,150 548,166 C556,172 552,180 540,180')
        laces = 'M196,80 L250,96 M206,100 L246,80 M226,88 C230,40 196,30 186,50 M240,88 C262,46 300,44 306,66 M186,50 C176,70 170,90 160,110 M306,66 C318,90 330,100 344,110'
        strain = ''
        knot = ''
    sole = 'M30,170 L30,194 C200,204 420,204 540,196 L540,180 M30,170 C200,182 420,184 540,180'
    tg = ''
    if tag:
        tg = ('<path d="M268,90 L330,26" stroke="var(--pen)" stroke-width="3"/>'
              '<rect x="326" y="-18" width="250" height="64" rx="10" stroke="var(--pen)" stroke-width="4" transform="rotate(-6 330 26)"/>'
              '<text x="451" y="26" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-6 330 26)">%s</text>') % tag
    return ('<g transform="translate(%d,%d) scale(%s)">'
            '<path d="%s" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="%s" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="%s" stroke="var(--pen)" stroke-width="5"/>'
            '<path d="%s" stroke="var(--pen)" stroke-width="3"/>%s%s</g>') % (x, y, s, upper, sole, laces, strain, knot, tg)

def runner(x, y, s=1.0, col="var(--ink)"):
    """Corredor em posição de largada, de pé, um pé à frente."""
    return ('<g transform="translate(%d,%d) scale(%s)">'
            '<circle cx="60" cy="20" r="20" stroke="%s" stroke-width="4"/>'
            '<path d="M58,42 L48,130 M52,64 L96,96 M52,64 L14,104 M48,130 L86,170 L80,214 M48,130 L22,180 L-4,206" stroke="%s" stroke-width="4"/>'
            '</g>') % (x, y, s, col, col)

def kettle(x, y, s=1.0):
    return ('<g transform="translate(%d,%d) scale(%s)">'
            '<path d="M40,200 L60,80 C64,64 176,64 180,80 L200,200 Z" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M70,74 C70,40 170,40 170,74" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M110,48 L130,48" stroke="var(--ink)" stroke-width="6"/>'
            '<path d="M48,150 L0,110 L-14,78 L4,84" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M-14,62 C-30,40 0,30 -14,6 M-34,52 C-50,30 -20,20 -34,-4" stroke="var(--mu)" stroke-width="3"/>'
            '</g>') % (x, y, s)

def cooker(x, y, s=1.0):
    return ('<g transform="translate(%d,%d) scale(%s)">'
            '<rect x="20" y="96" width="200" height="104" rx="14" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M10,96 C10,64 230,64 230,96 Z" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M230,88 L320,78" stroke="var(--ink)" stroke-width="8"/>'
            '<path d="M112,66 L112,40 L128,40 L128,66" stroke="var(--ink)" stroke-width="4"/>'
            '<path d="M100,24 L88,4 M120,20 L120,-6 M140,24 L152,4" stroke="var(--pen)" stroke-width="4"/>'
            '</g>') % (x, y, s)

def flame(x, y, s=1.0):
    return ('<g transform="translate(%d,%d) scale(%s)">'
            '<path d="M60,0 C90,40 110,70 100,100 C94,124 76,134 60,134 C40,134 22,124 18,100 C12,70 36,56 44,30 C52,50 58,56 60,0 Z" stroke="var(--pen)" stroke-width="4"/>'
            '<path d="M60,74 C72,90 78,104 70,118 C66,126 54,126 50,118 C44,106 52,94 60,74 Z" stroke="var(--pen)" stroke-width="3"/>'
            '<path d="M-10,150 L130,150" stroke="var(--ink)" stroke-width="5"/>'
            '</g>') % (x, y, s)

def box(x, y, checked=False, col="var(--ink)", size=40):
    out = '<rect x="%d" y="%d" width="%d" height="%d" rx="6" stroke="%s" stroke-width="3"/>' % (x, y, size, size, col)
    if checked:
        out += '<path d="M%d,%d l12,14 l26,-34" stroke="var(--pen)" stroke-width="5"/>' % (x + 6, y + 20)
    return out

# ================================================================== VERSÃO A — capa escura — "Pergunta para você" — CTA salvar
A = []
A.append('''<div style="margin-top:20px"></div>
<h1>Na largada, quem você quer convencer? Quem, exatamente?</h1>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:auto; margin-bottom:70px">
<g transform="rotate(-3 444 230)">
<rect x="110" y="20" width="668" height="420" rx="14" stroke="var(--ink)" stroke-width="4"/>
<circle cx="110" cy="96" r="16" style="fill:var(--bg); stroke:none"/><circle cx="778" cy="96" r="16" style="fill:var(--bg); stroke:none"/>
<text x="150" y="74" font-family="Inter" font-weight="800" font-size="26" letter-spacing="4" fill="var(--mu)">GUARDA-VOLUMES</text>
<text x="740" y="74" text-anchor="end" font-family="Inter" font-weight="700" font-size="24" fill="var(--mu)">LARGADA</text>
<path d="M130,96 L758,96" stroke="var(--mu)" stroke-width="3" stroke-dasharray="6 10"/>
<text x="150" y="160" font-family="Pen" font-size="40" fill="var(--ink)">casaco</text>
<text x="740" y="160" text-anchor="end" font-family="Pen" font-size="38" fill="var(--mu)">deixei</text>
<path d="M280,150 L600,150" stroke="var(--mu)" stroke-width="2" stroke-dasharray="2 10"/>
<text x="150" y="222" font-family="Pen" font-size="40" fill="var(--ink)">celular</text>
<text x="740" y="222" text-anchor="end" font-family="Pen" font-size="38" fill="var(--mu)">deixei</text>
<path d="M290,212 L600,212" stroke="var(--mu)" stroke-width="2" stroke-dasharray="2 10"/>
<text x="150" y="284" font-family="Pen" font-size="40" fill="var(--ink)">chave de casa</text>
<text x="740" y="284" text-anchor="end" font-family="Pen" font-size="38" fill="var(--mu)">deixei</text>
<path d="M390,274 L600,274" stroke="var(--mu)" stroke-width="2" stroke-dasharray="2 10"/>
<text x="150" y="358" font-family="Pen" font-size="44" fill="var(--pen)">o que vão pensar de mim</text>
<text x="740" y="412" text-anchor="end" font-family="Pen" font-size="44" fill="var(--pen)">levei comigo</text>
<path d="M560,402 C590,436 690,436 760,418 C780,410 770,380 740,378 C690,374 600,380 570,392" stroke="var(--pen)" stroke-width="3"/>
</g>
</svg>''')

A.append('''<h2>Veio um nome? Pois é, ele largou junto com você.</h2>
<p style="margin-top:36px">E a prova ganhou uma tarefa a mais. Além de chegar, agora ela precisa %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M40,250 C120,170 200,330 290,240 C360,170 430,280 520,220" stroke="var(--ink)" stroke-width="5"/>
<path d="M40,250 L40,150 L90,166 L40,182" stroke="var(--ink)" stroke-width="4"/>
<text x="40" y="300" font-family="Pen" font-size="34" fill="var(--mu)">largada</text>
<path d="M520,220 L520,110 L580,126 L520,142" stroke="var(--ink)" stroke-width="4"/>
<text x="478" y="276" font-family="Pen" font-size="36" fill="var(--ink)">chegada</text>
<path d="M530,214 C620,160 700,250 770,170 C800,136 820,120 846,100" stroke="var(--pen)" stroke-width="4" stroke-dasharray="4 14"/>
<text x="848" y="78" text-anchor="end" font-family="Pen" font-size="60" fill="var(--pen)">?</text>
<text x="860" y="250" text-anchor="end" font-family="Pen" font-size="34" fill="var(--pen)">alguém se convencer</text>
<text x="40" y="380" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-1.5 40 380)">no papel, a mesma distância. na cabeça, não.</text>
</svg>''' % hl("convencer alguém"))

A.append('''<h2>Antes do tiro de largada, a cabeça faz uma %s.</h2>
<p style="margin-top:36px">O que você tem, menos o que a prova pede. Você nem percebe que tá fazendo essa conta. Mas o resultado chega no corpo.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
<text x="120" y="56" font-family="Pen" font-size="46" fill="var(--ink)">o que você tem</text>
<text x="60" y="128" font-family="Pen" font-size="50" fill="var(--ink)">−</text>
<text x="120" y="128" font-family="Pen" font-size="46" fill="var(--ink)">o que a prova pede</text>
<path d="M50,158 L560,150" stroke="var(--ink)" stroke-width="4"/>
<text x="290" y="226" text-anchor="middle" font-family="Pen" font-size="64" fill="var(--pen)">?</text>
<path d="M260,246 L150,312 M138,300 L150,314 L132,320" stroke="var(--mu)" stroke-width="3"/>
<path d="M320,246 L530,312 M512,300 L530,314 L514,326" stroke="var(--mu)" stroke-width="3"/>
<text x="20" y="360" font-family="Inter" font-weight="800" font-size="26" fill="var(--pen)">SOBROU</text>
<text x="20" y="406" font-family="Pen" font-size="44" fill="var(--pen)">→ desafio</text>
<text x="480" y="360" font-family="Inter" font-weight="800" font-size="26" fill="var(--mu)">FALTOU</text>
<text x="480" y="406" font-family="Pen" font-size="44" fill="var(--mu)">→ ameaça</text>
</svg>''' % circ("subtração"))

A.append('''<h2>O coração acelera nas duas respostas.</h2>
<p style="margin-top:36px">Repara nisso aqui: a diferença não tá na pressa da batida. No desafio, os vasos se abrem e cada batida rende mais. Na ameaça, eles resistem e %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M60,10 L60,330 L870,330" stroke="var(--mu)" stroke-width="3"/>
<path d="M50,24 L60,8 L70,24 M856,320 L872,330 L856,340" stroke="var(--mu)" stroke-width="3"/>
<text x="80" y="40" font-family="Inter" font-size="22" fill="var(--mu)">o que cada batida entrega</text>
<text x="870" y="374" text-anchor="end" font-family="Inter" font-size="22" fill="var(--mu)">batimento subindo →</text>
<path d="M60,330 C300,240 520,140 820,70" stroke="var(--pen)" stroke-width="5"/>
<text x="440" y="132" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-14 440 132)">desafio</text>
<path d="M60,330 C320,310 560,290 820,272" stroke="var(--ink)" stroke-width="4"/>
<text x="560" y="262" font-family="Pen" font-size="40" fill="var(--ink)" transform="rotate(-3 560 262)">ameaça</text>
</svg>''' % hl("o coração trabalha mais pra entregar menos"))

A.append('''<h2>Sabe o que a cabeça faz com o extrato? Usa só metade.</h2>
<p style="margin-top:36px">Na fila da largada, ela lembra do treino ruim da semana passada. As semanas de planilha cumpridas %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:0">
<path d="M150,10 L650,10 L650,190 L620,206 L590,186 L560,206 L530,186 L500,206 L470,186 L440,206 L410,186 L380,206 L350,186 L320,206 L290,186 L260,206 L230,186 L200,206 L170,186 L150,200 Z" stroke="var(--ink)" stroke-width="4"/>
<text x="180" y="58" font-family="Inter" font-weight="800" font-size="24" letter-spacing="3" fill="var(--ink)">O QUE EU TENHO</text>
<path d="M180,76 L620,76" stroke="var(--mu)" stroke-width="2" stroke-dasharray="6 8"/>
<text x="180" y="128" font-family="Pen" font-size="38" fill="var(--ink)">o treino ruim de quinta</text>
<text x="180" y="170" font-family="Pen" font-size="38" fill="var(--ink)">a perna pesada de ontem</text>
<g transform="rotate(7 470 330)">
<path d="M220,262 L250,242 L280,262 L310,242 L340,262 L370,242 L400,262 L430,242 L460,262 L490,242 L520,262 L550,242 L580,262 L610,242 L640,262 L670,242 L720,262 L720,420 L220,420 Z" stroke="var(--mu)" stroke-width="3"/>
<text x="250" y="310" font-family="Pen" font-size="36" fill="var(--mu)">os longões cumpridos</text>
<text x="250" y="352" font-family="Pen" font-size="36" fill="var(--mu)">as semanas de planilha</text>
<text x="250" y="394" font-family="Pen" font-size="36" fill="var(--mu)">as provas que você terminou</text>
</g>
<text x="40" y="296" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-6 40 296)">caiu</text>
<text x="20" y="336" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-6 40 336)">da conta</text>
<path d="M120,320 C150,330 180,330 206,316 M192,308 L208,316 L194,328" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % hl("ficam de fora"))

A.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Quem larga pra chegar faz a conta com o treino.</h1>
<h1 class="or" style="font-size:76px; margin-top:26px">Quem larga pra convencer faz a conta com a opinião dos outros.</h1>''')

A.append(qs("Faz essa conta agora, com a sua próxima prova.", [
    ("Qual prova? Que distância? Onde fica a subida?", "Só o que tá no regulamento. Se apareceu o nome de alguém, risque."),
    ("O que você já fez pra ela? Quais longões?", "O de domingo, o da chuva, aquele que você achou que não ia fechar."),
    ("E pra quem você quer provar algo? Quem, exatamente?", "O treinador, o grupo da assessoria, um amigo, você do ano passado?")]))

A.append(paraquem("Para quem é, e quem não é.",
    "você chega na largada com o treino feito, mas com algo a provar pra alguém, e larga travado.",
    "o coração dispara com dor no peito, tontura ou falta de ar: procure um médico. Se a pressão de provar pesa também fora do esporte: um psicólogo."))

A.append('''<div style="margin-top:70px"></div>
<h1 style="font-size:78px">A distância é a mesma para todo mundo.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">O peso extra entra com você.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Salva pra reler na fila do guarda-volumes da próxima prova.</p>
<svg class="draw" width="888" height="250" viewBox="0 0 888 250" style="margin-top:30px">
<text x="0" y="90" font-family="Pen" font-size="38" fill="var(--pen)">deixe aqui,</text>
<text x="0" y="132" font-family="Pen" font-size="38" fill="var(--pen)">antes de largar</text>
<path d="M260,110 L340,120 M322,106 L342,120 L324,134" stroke="var(--pen)" stroke-width="3"/>
<g transform="rotate(-4 600 125)">
<path d="M380,40 L800,40 L800,210 L380,210 L340,125 Z" stroke="var(--ink)" stroke-width="4" style="fill:var(--hl)"/>
<circle cx="378" cy="125" r="12" stroke="var(--ink)" stroke-width="3"/>
<path d="M366,125 C330,110 310,80 300,40" stroke="var(--mu)" stroke-width="3"/>
<text x="420" y="90" font-family="Inter" font-weight="800" font-size="22" letter-spacing="3" fill="var(--ink)">GUARDA-VOLUMES</text>
<text x="420" y="150" font-family="Pen" font-size="40" fill="var(--ink)">o que vão pensar</text>
<text x="420" y="192" font-family="Pen" font-size="40" fill="var(--ink)">de mim</text>
</g>
</svg>''')

# ================================================================== VERSÃO B — capa clara — "Pergunta-enigma" — CTA mandar para alguém
B = []
B.append('''<div style="margin-top:20px"></div>
<h1>Por que quem larga mais determinado às vezes larga mais travado?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:70px">
%s
<text x="444" y="380" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)" transform="rotate(-2 444 380)">amarrado com força demais.</text>
</svg>''' % shoe(150, 110, 1.2, tag="hoje eu provo"))

B.append('''<h2>Porque, de fora, as duas largadas são idênticas.</h2>
<p style="margin-top:36px">Olha só: coração acelerado, olhar fixo, mandíbula dura. A diferença tá por dentro, numa conta que você faz sem perceber. E no que ela faz com os %s.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:10px">
%s%s
<path d="M60,260 L380,260 M508,260 L828,260" stroke="var(--mu)" stroke-width="3"/>
<text x="220" y="320" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">vai correr</text>
<text x="668" y="320" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)">vai provar</text>
<text x="444" y="150" text-anchor="middle" font-family="Pen" font-size="96" fill="var(--mu)">=</text>
</svg>''' % (hl("seus vasos"), runner(160, 40), runner(608, 40)))

def trow(y, lab, a, b, ca="var(--ink)", cb="var(--ink)"):
    return ('<text x="20" y="%d" font-family="Inter" font-weight="700" font-size="26" fill="var(--mu)">%s</text>'
            '<text x="440" y="%d" text-anchor="middle" font-family="Pen" font-size="40" fill="%s">%s</text>'
            '<text x="730" y="%d" text-anchor="middle" font-family="Pen" font-size="40" fill="%s">%s</text>') % (y, lab, y, ca, a, y, cb, b)

B.append('''<h2>Parece: coração disparado na largada é mau sinal.</h2>
<p style="margin-top:36px">Acontece: ele dispara nos dois estados. Se liga nessa parte: o que muda é %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<text x="440" y="50" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" letter-spacing="3" fill="var(--pen)">DESAFIO</text>
<text x="730" y="50" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" letter-spacing="3" fill="var(--ink)">AMEAÇA</text>
<path d="M0,78 L888,78 M0,190 L888,190 M0,296 L888,296 M300,20 L300,390 M590,20 L590,390" stroke="var(--mu)" stroke-width="2"/>
%s%s%s
<path d="M320,104 C300,150 340,176 600,170 C860,170 880,120 840,100 C800,84 600,90 360,96" stroke="var(--pen)" stroke-width="3"/>
<text x="870" y="230" text-anchor="end" font-family="Pen" font-size="32" fill="var(--pen)"></text>
</svg>''' % (hl("o que cada batida entrega"),
             trow(150, "BATIMENTO", "sobe", "sobe"),
             trow(258, "VASOS", "se abrem", "resistem", "var(--pen)"),
             trow(362, "BOMBEAMENTO", "eficiente", "menos eficiente", "var(--pen)")))

B.append('''<h2>Parece: vontade de provar dá mais força.</h2>
<p style="margin-top:36px">Acontece: ela entra na conta do lado do que a prova pede. Quanto mais você precisa provar, %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M60,10 L60,330 L870,330" stroke="var(--mu)" stroke-width="3"/>
<text x="870" y="374" text-anchor="end" font-family="Inter" font-size="22" fill="var(--mu)">quanto você precisa provar a alguém →</text>
<path d="M60,200 L860,200" stroke="var(--ink)" stroke-width="4" stroke-dasharray="4 14"/>
<text x="80" y="186" font-family="Pen" font-size="36" fill="var(--ink)">o que você tem: o seu treino</text>
<path d="M60,300 C300,290 520,190 840,40" stroke="var(--pen)" stroke-width="5"/>
<text x="300" y="70" font-family="Pen" font-size="36" fill="var(--pen)">o tamanho da prova</text><text x="300" y="110" font-family="Pen" font-size="36" fill="var(--pen)">na sua cabeça</text>
<circle cx="545" cy="200" r="26" stroke="var(--pen)" stroke-width="3"/>
<text x="600" y="250" font-family="Pen" font-size="36" fill="var(--pen)">daqui em diante:</text>
<text x="600" y="290" font-family="Pen" font-size="36" fill="var(--pen)">ameaça</text>
</svg>''' % hl("maior a prova fica"))

def cal():
    out = ''
    k = 0
    for r in range(4):
        for c in range(7):
            x, y = 40 + c * 92, 20 + r * 76
            out += '<rect x="%d" y="%d" width="80" height="64" rx="6" stroke="var(--mu)" stroke-width="2"/>' % (x, y)
            if (r, c) == (3, 3):
                out += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="var(--ink)" stroke-width="5"/>' % (x + 22, y + 14, x + 58, y + 50, x + 58, y + 14, x + 22, y + 50)
            elif c not in (0, 4):
                out += '<path d="M%d,%d l12,14 l24,-28" stroke="var(--mu)" stroke-width="3"/>' % (x + 22, y + 34)
            k += 1
    return out

B.append('''<h2>Parece: você lembra de tudo o que treinou.</h2>
<p style="margin-top:36px">Acontece: na hora da conta, a cabeça ilumina só um pedaço da planilha. E pode ser justo %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:0">
%s
<path d="M300,240 L410,326 L728,392 L738,356 Z" style="fill:var(--hl); stroke:none"/>
<path d="M300,240 L738,356 M410,326 L728,392" stroke="var(--pen)" stroke-width="2"/>
<g transform="rotate(22 760 380)"><rect x="730" y="360" width="140" height="44" rx="10" stroke="var(--ink)" stroke-width="4"/><path d="M720,352 L730,360 L730,404 L720,412 Z" stroke="var(--ink)" stroke-width="4"/></g>
<text x="20" y="370" font-family="Pen" font-size="38" fill="var(--pen)">o resto também é seu.</text>
</svg>''' % (hl("o pedaço ruim"), cal()))

B.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">O coração não sabe se você é forte.</h1>
<h1 class="or" style="font-size:78px; margin-top:22px">Ele responde à conta que você fez antes de largar.</h1>''')

B.append('''<h2>Na fila da largada, completa em silêncio:</h2>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:20px">
<text x="0" y="110" font-family="Pen" font-size="62" fill="var(--ink)">Hoje eu corro pra</text>
<path d="M480,116 L880,112" stroke="var(--pen)" stroke-width="4"/>
<text x="700" y="180" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">(a primeira resposta)</text>
</svg>
<p style="margin-top:30px">Pra quê? Pra fechar a prova? Pra alguém ver? Quem?</p>
<p>Se a resposta fala de percurso, ritmo ou chegada, é a prova. Se fala de alguém, %s.</p>''' % hl("é peso a mais na conta"))

B.append(paraquem("Serve para você? Talvez não.",
    "você treina com constância, mas na largada sente que precisa provar algo, e o corpo responde duro.",
    "o coração dispara com dor no peito, tontura ou falta de ar: aí é um médico. Se precisar provar seu valor pesa também no trabalho e em casa: um psicólogo."))

B.append('''<div style="margin-top:70px"></div>
<h1 style="font-size:78px">Largar travado nem sempre é falta de vontade.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Às vezes é vontade demais de provar.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Manda pra aquele amigo que, na fila da largada, sempre solta um “hoje eu provo”.</p>
<svg class="draw" width="888" height="230" viewBox="0 0 888 230" style="margin-top:20px">
<text x="0" y="90" font-family="Pen" font-size="38" fill="var(--pen)">manda pra quem</text>
<text x="0" y="132" font-family="Pen" font-size="38" fill="var(--pen)">amarra assim</text>
<path d="M250,110 L320,120 M302,106 L322,120 L304,134" stroke="var(--pen)" stroke-width="3"/>
%s
</svg>''' % shoe(360, 10, 0.9, tag=None))

# ================================================================== VERSÃO C — capa clara — "A ou B?" — CTA comentar
C = []
C.append('''<div style="margin-top:20px"></div>
<h1>O coração disparou no curral da largada. Sinal de quê?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:60px">
%s%s
<path d="M444,60 L444,340" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 12"/>
<text x="40" y="350" font-family="Inter" font-weight="800" font-size="40" fill="var(--pen)">A</text>
<text x="90" y="350" font-family="Pen" font-size="44" fill="var(--ink)">estou pronto</text>
<text x="484" y="350" font-family="Inter" font-weight="800" font-size="40" fill="var(--pen)">B</text>
<text x="534" y="350" font-family="Pen" font-size="44" fill="var(--ink)">estou nervoso</text>
<text x="444" y="426" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 426)">escolha antes de passar.</text>
</svg>''' % (kettle(140, 70, 1.0), cooker(510, 90, 1.0)))

C.append('''<h2>Se você marcou B, repara: o coração dispara nos dois casos.</h2>
<p style="margin-top:36px">A pergunta certa não é quanto ele bate. É %s.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:10px">
%s%s
<text x="220" y="250" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">pronto</text>
<text x="668" y="250" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--ink)">nervoso</text>
<text x="444" y="336" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 444 336)">o fogo é o mesmo.</text>
</svg>''' % (hl("quanto cada batida consegue entregar"), flame(160, 30), flame(608, 30)))

C.append('''<h2>Pergunta 1: chaleira ou panela? Quem decide? Quando?</h2>
<p style="margin-top:36px">Resposta: uma conta rápida, antes do tiro, que você faz sem perceber. O que a prova pede contra o que você tem.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:0">
<rect x="164" y="10" width="560" height="110" rx="20" stroke="var(--ink)" stroke-width="4"/>
<text x="444" y="56" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">o que eu tenho dá conta</text>
<text x="444" y="98" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--ink)">do que a prova pede?</text>
<path d="M330,124 L210,212 M196,196 L210,214 L188,218" stroke="var(--pen)" stroke-width="4"/>
<path d="M558,124 L678,212 M660,212 L680,214 L676,192" stroke="var(--mu)" stroke-width="4"/>
<text x="236" y="150" text-anchor="end" font-family="Pen" font-size="36" fill="var(--pen)">sim</text>
<text x="652" y="150" font-family="Pen" font-size="36" fill="var(--mu)">não</text>
<rect x="0" y="232" width="420" height="200" rx="18" stroke="var(--pen)" stroke-width="4"/>
<text x="210" y="280" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" letter-spacing="3" fill="var(--pen)">DESAFIO</text>
<text x="210" y="334" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">os vasos se abrem.</text>
<text x="210" y="380" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">o coração bombeia</text>
<text x="210" y="416" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">com mais eficiência.</text>
<rect x="468" y="232" width="420" height="200" rx="18" stroke="var(--mu)" stroke-width="3"/>
<text x="678" y="280" text-anchor="middle" font-family="Inter" font-weight="800" font-size="26" letter-spacing="3" fill="var(--mu)">AMEAÇA</text>
<text x="678" y="334" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">os vasos resistem.</text>
<text x="678" y="380" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">o bombeamento</text>
<text x="678" y="416" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">perde eficiência.</text>
</svg>''')

C.append('''<h2>Pergunta 2: na véspera, você lembra do quê? Do treino? De qual?</h2>
<p style="margin-top:36px">Resposta: na conta da véspera, a prova pode crescer na cabeça. E o treino feito %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M60,10 L60,330 L870,330" stroke="var(--mu)" stroke-width="3"/>
<text x="60" y="374" font-family="Inter" font-size="22" fill="var(--mu)">semana da prova</text>
<text x="870" y="374" text-anchor="end" font-family="Inter" font-size="22" fill="var(--mu)">largada →</text>
<path d="M60,190 C300,186 520,150 840,40" stroke="var(--pen)" stroke-width="5"/>
<text x="90" y="130" font-family="Pen" font-size="36" fill="var(--pen)">o que a prova parece pedir</text>
<path d="M60,170 C300,176 520,220 840,300" stroke="var(--ink)" stroke-width="4"/>
<text x="90" y="236" font-family="Pen" font-size="36" fill="var(--ink)">o treino que você lembra</text>
<path d="M800,60 L800,286" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>
<text x="780" y="180" text-anchor="end" font-family="Pen" font-size="34" fill="var(--mu)">a conta</text>
<text x="780" y="216" text-anchor="end" font-family="Pen" font-size="34" fill="var(--mu)">sai daqui</text>
</svg>''' % hl("some da conta"))

C.append('''<h2>Pergunta 3: quem mais se inscreveu na sua prova? Quem, exatamente?</h2>
<p style="margin-top:36px">Resposta: quem você quer convencer. Não corre um metro, mas entra na conta %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:0">
<g transform="rotate(-2 444 210)">
<rect x="60" y="10" width="768" height="390" rx="16" stroke="var(--ink)" stroke-width="4"/>
<text x="100" y="70" font-family="Inter" font-weight="800" font-size="26" letter-spacing="3" fill="var(--ink)">COMPROVANTE DE INSCRIÇÃO</text>
<path d="M100,96 L788,96" stroke="var(--mu)" stroke-width="2" stroke-dasharray="6 8"/>
<text x="100" y="156" font-family="Inter" font-weight="700" font-size="24" fill="var(--mu)">ATLETA</text>
<text x="300" y="158" font-family="Pen" font-size="42" fill="var(--ink)">você</text>
<text x="100" y="226" font-family="Inter" font-weight="700" font-size="24" fill="var(--mu)">CATEGORIA</text>
<text x="300" y="228" font-family="Pen" font-size="42" fill="var(--ink)">individual</text>
<path d="M290,214 L480,206" stroke="var(--pen)" stroke-width="5"/>
<text x="500" y="230" font-family="Pen" font-size="42" fill="var(--pen)">dupla?</text>
<text x="100" y="296" font-family="Inter" font-weight="700" font-size="24" fill="var(--mu)">+ 1</text>
<text x="300" y="300" font-family="Pen" font-size="42" fill="var(--pen)">quem eu quero convencer</text>
<text x="300" y="360" font-family="Pen" font-size="32" fill="var(--mu)">(não paga, não corre, pesa)</text>
</g>
</svg>''' % hl("do lado do que a prova pede"))

C.append('''<div style="margin-top:110px"></div>
<h1 style="font-size:78px">O fogo é o mesmo nos dois.</h1>
<h1 class="or" style="font-size:78px; margin-top:22px">A conta que você faz decide se ele vira força ou pressão.</h1>''')

def citem(y, txt):
    return ('<rect x="0" y="%d" width="46" height="46" rx="6" stroke="var(--ink)" stroke-width="3"/>'
            '<text x="80" y="%d" font-family="Inter" font-weight="700" font-size="34" fill="var(--ink)">%s</text>') % (y, y + 36, txt)

C.append('''<h2>Marca antes da próxima largada. Com sinceridade.</h2>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:50px">
%s%s%s%s
</svg>
<p style="margin-top:20px">Ficou caixa vazia? Qual? É ali que entra %s.</p>''' % (
    citem(10, "Sei a distância e onde fica a subida."),
    citem(110, "Sei dizer quais longões fiz, e onde."),
    citem(210, "Sei quantas semanas de planilha cumpri."),
    citem(310, "Essa prova vale mesmo sem plateia."),
    hl("peso a mais na conta")))

C.append(paraquem("Isso é para você, ou não?",
    "você sente o coração disparar antes de largar e lê isso como sinal de que algo vai mal.",
    "o coração dispara com dor no peito, tontura ou falta de ar: procure um médico antes de correr. Se a necessidade de provar algo te acompanha no resto da vida: um psicólogo."))

C.append('''<div style="margin-top:70px"></div>
<h1 style="font-size:78px">Coração disparado não responde à pergunta.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">A conta antes da largada responde.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Comenta aqui embaixo: A ou B? O que você marcou lá no começo? E manda pra quem marcaria o contrário.</p>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:30px">
%s<text x="70" y="98" font-family="Inter" font-weight="800" font-size="40" fill="var(--mu)">A</text>
%s<text x="250" y="98" font-family="Inter" font-weight="800" font-size="40" fill="var(--mu)">B</text>
<path d="M0,70 L120,60 M180,70 L300,60" stroke="var(--pen)" stroke-width="4"/>
%s<text x="430" y="100" font-family="Pen" font-size="50" fill="var(--pen)">a conta</text>
<text x="420" y="170" font-family="Pen" font-size="36" fill="var(--pen)" transform="rotate(-2 420 170)">a resposta tá aqui ↑</text>
</svg>''' % (box(10, 60), box(190, 60), box(370, 60, True, "var(--pen)")))

VERSOES = {
    "A": [(t, b, i in (0, 8)) for i, (t, b) in enumerate(zip(alt(D), A))],
    "B": [(t, b, i in (0, 8)) for i, (t, b) in enumerate(zip(alt(L), B))],
    "C": [(t, b, i in (0, 8)) for i, (t, b) in enumerate(zip(alt(L), C))],
}


LEGENDAS = {"A": """Repara numa coisa no seu próximo longão: em que momento você começa a pensar em quem vai ver o resultado? Na saída? No meio? Quando o relógio mostra o pace?

Essa conta entre o que a prova pede e o que você tem não aparece só no dia da prova. Ela aparece no treino também, toda vez que o treino vira vitrine.

Um exercício pequeno pra essa semana: depois do treino, anota duas linhas. Uma com o que o treino pediu. Outra com o que você levou pra ele: as semanas de base, os longões que já estão no corpo.

Com o tempo, essa segunda lista fica mais fácil de lembrar. E é justamente ela que some na fila da largada.

Salva pra reler na véspera da próxima prova, antes de arrumar a mochila.

Pra ir além disso, o diagnóstico completo sai de graça pelo link do perfil.""",
"B": """Já parou pra pensar no que muda quando alguém da assessoria posta a sua inscrição no grupo?

A prova é a mesma. A distância é a mesma. Mas agora tem gente esperando o resultado. E situações em que você vai ser avaliado puxam a cabeça pra leitura de ameaça.

Isso não quer dizer esconder a prova de todo mundo. Quer dizer perceber em que momento a corrida deixou de ser sua e virou uma prestação de contas.

Um teste simples pra próxima vez: na noite anterior, escreve em uma frase por que você vai correr. Se a frase tiver o nome de outra pessoa, repara. Não precisa mudar nada ainda. Só repara.

Manda pra quem posta o print do relógio antes até de tirar o tênis. Ou pra quem sempre fala que dessa vez vai provar.

Seu diagnóstico completo, sem pagar nada, começa no link da bio.""",
"C": """Olha o relógio no curral da largada. O batimento subiu antes do tiro? Pois é. Ele sobe tanto no desafio quanto na ameaça.

Por isso o número sozinho não responde nada. Ele mostra que o corpo tá se preparando. Não mostra pra quê.

O que dá pra observar é outra coisa: o que passou pela sua cabeça logo antes de olhar o pulso. Foi o percurso? O pace? Ou foi alguém?

No próximo treino forte, tenta isso: antes de começar, nota o primeiro pensamento que aparece. Depois, escreve ele num canto da planilha. Em algumas semanas, você tem um registro do que a sua cabeça costuma pôr na conta.

Comenta aqui embaixo: A ou B? E se mudou de ideia no meio do carrossel, conta também.

Quer o mapa inteiro da sua largada? Diagnóstico completo e grátis no link lá em cima.""",
}
