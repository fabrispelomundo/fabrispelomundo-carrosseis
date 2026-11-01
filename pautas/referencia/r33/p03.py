# -*- coding: utf-8 -*-
# p03 — o treino sempre adiado. A (capa escura), B (capa escura), C (capa clara)
from base import *

D, L = "dark", "light"

def pen(x, y, txt, size=40, color="var(--pen)", anchor="start", rot=0):
    r = f' transform="rotate({rot} {x} {y})"' if rot else ""
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Pen" font-size="{size}" fill="{color}"{r}>{txt}</text>'

def sans(x, y, txt, size=24, color="var(--mu)", anchor="start", weight=700):
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-family="Inter" font-weight="{weight}" font-size="{size}" fill="{color}">{txt}</text>'

def check(cx, cy, s=1.0, color="var(--ink)", w=5):
    return (f'<path d="M{cx-26*s:.0f},{cy:.0f} L{cx-8*s:.0f},{cy+20*s:.0f} L{cx+28*s:.0f},{cy-24*s:.0f}" '
            f'stroke="{color}" stroke-width="{w}"/>')

def lab(t, color="var(--pen)"):
    return f'<div class="lab" style="color:{color}">{t}</div>'

def paraquem2(title, sim, nao, drawing):
    return (f'<h2 style="margin-bottom:40px">{title}</h2><div class="lab or">É para você se</div><p>{sim}</p>'
            f'<div class="sep" style="margin:32px 0"></div><div class="lab" style="color:var(--mu)">Não é para você se</div><p>{nao}</p>{drawing}')

# =====================================================================================
# VERSÃO A — pergunta para você · planilha / trilha / régua · CTA salvar
# =====================================================================================
def a_grid():
    days = ["SEG", "TER", "QUA", "QUI", "SEX", "SÁB", "DOM"]
    out = ""
    for i, d in enumerate(days):
        x = 4 + i * 126
        out += sans(x + 58, 34, d, 22, anchor="middle")
        if d == "QUI":
            out += f'<rect x="{x}" y="56" width="116" height="170" rx="10" stroke="var(--pen)" stroke-width="4"/>'
            # rasuras: o treino escrito e riscado várias vezes
            for k, yy in enumerate([92, 128, 164, 200]):
                out += pen(x + 14, yy, "tiros", 28, "var(--mu)", rot=-4 + k * 3)
                out += f'<path d="M{x+10},{yy-10} L{x+92},{yy-6}" stroke="var(--mu)" stroke-width="3"/>'
            # o furo no papel
            out += (f'<path d="M{x+30},{118} L{x+44},{104} L{x+52},{120} L{x+70},{102} L{x+80},{122} L{x+94},{116} '
                    f'L{x+86},{140} L{x+98},{156} L{x+76},{160} L{x+70},{178} L{x+54},{164} L{x+36},{176} L{x+38},{152} '
                    f'L{x+22},{142} Z" style="fill:#050505" stroke="var(--pen)" stroke-width="3"/>')
        else:
            out += f'<rect x="{x}" y="56" width="116" height="170" rx="10" stroke="var(--mu)" stroke-width="3"/>'
            out += check(x + 58, 140, 1.1)
    return out

A1 = f'''<div style="margin-top:30px"></div>
<h1>Qual treino da sua planilha nunca ganha o check?</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">O de quinta? O dos tiros?</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:70px">
{a_grid()}
<path d="M440,300 C470,272 476,254 470,238" stroke="var(--pen)" stroke-width="3"/>
<path d="M458,248 L470,234 L482,250" stroke="var(--pen)" stroke-width="3"/>
{pen(444, 340, "de tanto apagar e remarcar,", 42, anchor="middle", rot=-2)}
{pen(444, 392, "o papel furou.", 42, anchor="middle", rot=-2)}
</svg>'''

def a_excuses():
    rows = [("semana 1", "choveu"), ("semana 2", "reunião cedo"), ("semana 3", "dormi mal"), ("semana 4", "depois eu vejo")]
    out = sans(0, 30, "MOTIVO", 22) + sans(888, 30, "TREINO", 22, anchor="end")
    for i, (w, e) in enumerate(rows):
        y = 96 + i * 70
        out += sans(0, y, w.upper(), 20)
        out += pen(150, y + 4, e, 40, "var(--ink)", rot=[-2, 1, -1, 2][i])
        out += f'<path d="M520,{y-8} L660,{y-8}" stroke="var(--mu)" stroke-width="2" stroke-dasharray="3 10"/>'
        out += pen(888, y + 4, "tiros", 42, "var(--pen)", anchor="end")
    out += '<path d="M800,60 L800,330" stroke="var(--pen)" stroke-width="2" stroke-dasharray="2 12"/>'
    return out

A2 = f'''<h2>Repara nisso aqui: o resto da semana está todo marcado.</h2>
<p style="margin-top:36px">Você não foge de treinar. Treina a semana inteira. Foge de uma coisa só. E o que muda toda vez é a %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
{a_excuses()}
{pen(444, 400, "o motivo troca toda semana. o treino, não.", 42, anchor="middle", rot=-2)}
</svg>''' % hl("desculpa")

def feet(x, y, rot):
    return (f'<g transform="translate({x},{y}) rotate({rot})"><ellipse cx="0" cy="0" rx="7" ry="12" style="fill:var(--pen); stroke:none"/>'
            f'<ellipse cx="14" cy="6" rx="7" ry="12" style="fill:var(--pen); stroke:none; opacity:.7"/></g>')

A3 = f'''<h2>Cada pulo deixa o próximo mais %s.</h2>
<p style="margin-top:36px">Sabe aquele alívio na hora em que você decide não ir? Ele é rápido e é de verdade. E é justamente ele que deixa mais provável pular de novo.</p>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:36px">
<circle cx="70" cy="380" r="14" style="fill:var(--ink); stroke:none"/>
{pen(20, 446, "o dia do treino", 34, "var(--ink)")}
<path d="M80,370 C200,320 260,220 380,170 C470,132 520,90 560,40" stroke="var(--mu)" stroke-width="3" stroke-dasharray="6 12"/>
{pen(580, 52, "fazer", 42, "var(--ink)")}
{sans(590, 90, "trilha quase apagada", 20)}
<path d="M80,388 C260,396 420,392 560,372 C680,354 760,330 860,320" stroke="var(--pen)" stroke-width="22" style="opacity:.25"/>
<path d="M80,388 C260,396 420,392 560,372 C680,354 760,330 860,320" stroke="var(--pen)" stroke-width="4"/>
{feet(200, 382, 90)}{feet(300, 386, 92)}{feet(400, 382, 95)}{feet(500, 374, 98)}{feet(600, 360, 100)}{feet(700, 342, 102)}{feet(790, 328, 104)}
{pen(700, 300, "pular", 46, anchor="middle")}
{pen(330, 280, "cada alívio pisa mais um pouco", 34, "var(--pen)", rot=-3)}
</svg>''' % circ("fácil")

A4 = f'''<h2>Sem o treino, a previsão nunca é conferida.</h2>
<p style="margin-top:36px">Imagina: você acha que vai quebrar no meio dos tiros. Como o treino não sai, nada aparece pra mostrar se isso é verdade. A previsão fica de pé, e %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,250 C200,240 320,200 460,150 C600,100 740,62 860,40" stroke="var(--pen)" stroke-width="5"/>
{pen(120, 140, "a certeza de que vai dar errado", 38, rot=-3)}
<path d="M40,362 L860,362" stroke="var(--ink)" stroke-width="5"/>
{pen(470, 342, "vezes que você conferiu", 36, "var(--ink)")}
{sans(870, 412, "semanas sem fazer →", 22, anchor="end", weight=400)}
</svg>''' % hl("pode crescer")

def ruler():
    out = '<rect x="20" y="150" width="848" height="110" rx="8" stroke="var(--ink)" stroke-width="4"/>'
    for i in range(0, 41):
        x = 40 + i * 20
        h = 40 if i % 5 == 0 else 22
        out += f'<path d="M{x},150 L{x},{150+h}" stroke="var(--mu)" stroke-width="2"/>'
    return out

A5 = f'''<h2>O que ensina é o espaço entre duas marcas.</h2>
<p style="margin-top:36px">Se liga nessa parte: antes do treino, marca o que você acha que vai acontecer. Depois, marca o que aconteceu. A cabeça aprende com a %s entre as duas.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
{ruler()}
<path d="M240,120 L240,290" stroke="var(--mu)" stroke-width="5"/>
{pen(240, 100, "o que eu esperava", 36, "var(--mu)", anchor="middle")}
<path d="M640,120 L640,290" stroke="var(--pen)" stroke-width="6"/>
{pen(640, 100, "o que aconteceu", 38, anchor="middle")}
<path d="M250,320 C250,344 440,330 440,356 C440,330 630,344 630,320" stroke="var(--pen)" stroke-width="4"/>
{pen(440, 410, "é aqui que a previsão muda", 40, anchor="middle", rot=-2)}
</svg>''' % hl("distância")

A6 = '''<div style="margin-top:150px"></div>
<h1 style="font-size:84px">Pular te dá alívio.</h1>
<h1 class="or" style="font-size:84px; margin-top:22px">Fazer te dá a resposta.</h1>'''

A7 = qs("Pega a planilha das últimas oito semanas.", [
    ("Qual treino ficou sem check? O de quinta? O dos tiros? O longão?", "Um só. Aquele que você mais empurrou de dia."),
    ("Quando você desistiu dele? Na véspera? No despertador?", "Na cama, no carro, no vestiário, lendo o grupo de corrida."),
    ("E o que acha que acontece se fizer? Quebrar em qual tiro?", "Escreve a frase do jeito que ela vem. Já conferiu alguma vez?")])

A8 = paraquem("Isso é pra você? E quando não é.",
    "você treina a semana toda, e uma linha da planilha vive em branco. Sempre a mesma.",
    "você pula por dor, lesão ou cansaço que não passa, ou se fugir assim já aparece em outras partes da vida. Aí procure um médico, um fisioterapeuta ou um psicólogo.")

A9 = f'''<div style="margin-top:40px"></div>
<h1 style="font-size:74px">Aquele quadrado em branco não é falta de tempo.</h1>
<h1 class="or" style="font-size:74px; margin-top:18px">É uma previsão nunca conferida.</h1>
<p class="mu" style="margin-top:36px">Salva pra abrir na próxima vez que esse treino aparecer na planilha.</p>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto; margin-bottom:60px">
<rect x="40" y="40" width="130" height="140" rx="10" stroke="var(--mu)" stroke-width="3"/>{check(105, 110, 1.0, "var(--mu)", 4)}
<rect x="190" y="40" width="130" height="140" rx="10" stroke="var(--mu)" stroke-width="3"/>{check(255, 110, 1.0, "var(--mu)", 4)}
<rect x="340" y="40" width="130" height="140" rx="10" stroke="var(--pen)" stroke-width="5"/>
<path d="M500,110 C560,110 600,100 640,86" stroke="var(--pen)" stroke-width="3"/>
<path d="M500,110 L516,98 M500,110 L516,122" stroke="var(--pen)" stroke-width="3"/>
{pen(650, 84, "você sabe", 40, rot=-3)}
{pen(650, 130, "qual é.", 40, rot=-3)}
<path d="M820,20 L860,20 L860,110 L840,94 L820,110 Z" style="fill:var(--pen); stroke:none"/>
</svg>'''

# =====================================================================================
# VERSÃO B — pergunta-enigma · estrela / cupom / cadeado · CTA mandar para outro corredor
# =====================================================================================
def star(cx, cy, r, color="var(--pen)", fill=True):
    import math
    pts = []
    for k in range(10):
        rr = r if k % 2 == 0 else r * 0.45
        a = -math.pi / 2 + k * math.pi / 5
        pts.append(f"{cx + rr*math.cos(a):.0f},{cy + rr*math.sin(a):.0f}")
    f = f"fill:{color}; " if fill else ""
    return f'<polygon points="{" ".join(pts)}" style="{f}stroke:{color}; stroke-width:3; stroke-linejoin:round"/>'

def b_notebook():
    rows = [("SEG", "rodagem", True), ("TER", "força", True), ("QUA", "rodagem", True), ("QUI", "tiros: pulei", False), ("SÁB", "longão", True)]
    out = '<rect x="20" y="0" width="600" height="400" rx="12" stroke="var(--ink)" stroke-width="4" transform="rotate(-2 320 200)"/>'
    out += '<g transform="rotate(-2 320 200)">'
    for i, (d, t, ok) in enumerate(rows):
        y = 64 + i * 72
        out += sans(54, y, d, 22)
        out += pen(140, y + 2, t, 40, "var(--ink)" if ok else "var(--pen)")
        if ok:
            out += check(560, y - 12, 0.7, "var(--mu)", 4)
        out += f'<path d="M50,{y+22} L590,{y+22}" stroke="var(--mu)" stroke-width="1" style="opacity:.4"/>'
    out += '</g>'
    out += star(730, 270, 120)
    out += '<path d="M612,270 C580,272 560,280 540,290" stroke="var(--pen)" stroke-width="3"/>'
    for a, b, c, d in [(730, 110, 730, 136), (850, 160, 832, 178), (610, 160, 628, 178), (880, 290, 860, 288)]:
        out += f'<path d="M{a},{b} L{c},{d}" stroke="var(--pen)" stroke-width="3"/>'
    return out

B1 = f'''<div style="margin-top:30px"></div>
<h1>Como pode um alívio tão pequeno mandar no seu treino?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:70px">
{b_notebook()}
</svg>
'''

def receipt():
    out = ('<path d="M220,0 L668,0 L668,420 L646,404 L624,420 L602,404 L580,420 L558,404 L536,420 L514,404 L492,420 '
           'L470,404 L448,420 L426,404 L404,420 L382,404 L360,420 L338,404 L316,420 L294,404 L272,420 L250,404 L228,420 L220,410 Z" '
           'stroke="var(--ink)" stroke-width="4" transform="rotate(2 444 210)"/>')
    out += '<g transform="rotate(2 444 210)">'
    out += sans(444, 52, "CUPOM", 26, "var(--ink)", "middle", 800)
    out += sans(444, 84, "TREINO PULADO", 22, "var(--mu)", "middle")
    out += '<path d="M250,108 L638,108" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 8"/>'
    items = [("alívio", "recebido"), ("dúvida", "continua"), ("previsão", "intacta")]
    for i, (a, b) in enumerate(items):
        y = 160 + i * 56
        out += pen(254, y, a, 36, "var(--ink)")
        out += pen(634, y, b, 36, "var(--ink)", "end")
    out += '<path d="M250,318 L638,318" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 8"/>'
    out += sans(444, 370, "VOLTE SEMPRE", 30, "var(--pen)", "middle", 800)
    out += '</g>'
    return out

B2 = f'''<h2>Pois é: esse alívio não é só um respiro.</h2>
<p style="margin-top:36px">Ele funciona como prêmio. E a cabeça tende a repetir o que foi premiado. Só que dessa vez o prêmio veio por %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
{receipt()}
</svg>''' % hl("fugir")

def parece(t):
    return f'{lab("Parece", "var(--mu)")}<h2>{t}</h2>'

def acontece(t):
    return f'<div class="lab or" style="margin-top:36px">Acontece</div><p>{t}</p>'

B3 = f'''{parece("Pular é só um treino a menos na conta.")}
{acontece("Olha isso: cada pulo seguido de alívio ensina alguma coisa. Ensina que fugir resolve. E deixa mais provável fugir de novo.")}
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
{sans(0, 70, "1 TREINO PULADO", 34, "var(--mu)", weight=800)}
{sans(380, 70, "=", 40, "var(--mu)", weight=800)}
{sans(440, 70, "0", 44, "var(--mu)", weight=800)}
<path d="M-6,40 C200,30 400,64 500,44" stroke="var(--pen)" stroke-width="5"/>
{pen(560, 66, "a conta que parece", 34, "var(--mu)")}
<path d="M0,130 L888,130" stroke="var(--line)" stroke-width="2"/>
{sans(0, 230, "1 TREINO PULADO", 34, "var(--ink)", weight=800)}
{sans(380, 230, "+", 40, "var(--ink)", weight=800)}
{pen(430, 234, "alívio", 52, "var(--ink)")}
{sans(590, 230, "=", 40, "var(--ink)", weight=800)}
<rect x="40" y="290" width="808" height="100" rx="14" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4" transform="rotate(-1.5 444 340)"/>
{pen(444, 356, "+1 aula de como fugir", 52, "var(--ink)", "middle", -1.5)}
</svg>'''

B4 = f'''{parece("Dá um tempo que o medo baixa sozinho.")}
{acontece("Longe do treino, nada aparece pra desmentir o que você imagina. A previsão ruim continua valendo. E %s.")}
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,340 L870,340" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,120 C240,140 420,220 600,270 C700,296 800,306 860,310" stroke="var(--mu)" stroke-width="4" stroke-dasharray="4 14"/>
{pen(90, 300, "o que você espera do tempo", 34, "var(--mu)", rot=-2)}
<path d="M40,120 C240,118 420,112 560,96 C680,82 780,56 860,36" stroke="var(--pen)" stroke-width="5"/>
{pen(160, 86, "o que acontece sem treinar", 38, rot=-2)}
{sans(870, 386, "semanas longe →", 22, anchor="end", weight=400)}
</svg>''' % hl("pode crescer")

B5 = f'''{parece("Primeiro você se sente seguro. Depois vai.")}
{acontece("O que corrige a previsão tá dentro do treino. Só passando por ele você compara o que esperava com o que veio. É dessa %s que a cabeça aprende.")}
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<rect x="160" y="70" width="420" height="300" rx="16" stroke="var(--ink)" stroke-width="5"/>
{sans(370, 120, "O TREINO", 28, "var(--ink)", "middle", 800)}
<circle cx="330" cy="250" r="34" stroke="var(--pen)" stroke-width="5"/>
<path d="M364,250 L480,250 M440,250 L440,284 M466,250 L466,276" stroke="var(--pen)" stroke-width="5"/>
<path d="M580,200 L640,200" stroke="var(--ink)" stroke-width="4"/>
<rect x="640" y="190" width="90" height="80" rx="10" stroke="var(--ink)" stroke-width="5"/>
<path d="M656,190 L656,160 C656,120 714,120 714,160 L714,190" stroke="var(--ink)" stroke-width="5"/>
<circle cx="685" cy="226" r="8" style="fill:var(--ink); stroke:none"/>
{pen(0, 40, "a chave fica do lado de dentro.", 42, rot=-2)}
</svg>''' % hl("diferença")

B6 = '''<div style="margin-top:150px"></div>
<h1 style="font-size:82px">Esperar não desmente a previsão.</h1>
<h1 class="or" style="font-size:82px; margin-top:22px">Só o treino que acontece desmente.</h1>'''

B7 = qs("Faz a conta agora, de cabeça.", [
    ("Qual treino você mais pulou nos últimos dois meses? Os tiros? O ritmo de prova?", "O nome dele. Sem explicação junto."),
    ("Quantas vezes foi? Lembra de cada uma?", "Esse número é quantas vezes a fuga já ganhou prêmio."),
    ("E logo depois de desmarcar, o que veio? Na hora? Antes de largar o celular?", "Um suspiro, os ombros caindo, vontade de voltar pra cama. Se foi alívio, o prêmio chegou.")])

DOORS = f'''<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto">
<rect x="60" y="10" width="130" height="186" rx="6" stroke="var(--pen)" stroke-width="5"/>
<circle cx="168" cy="110" r="7" style="fill:var(--pen); stroke:none"/>
{pen(215, 110, "aqui", 44)}
<rect x="440" y="10" width="130" height="186" rx="6" stroke="var(--mu)" stroke-width="4"/>
<circle cx="548" cy="110" r="7" style="fill:var(--mu); stroke:none"/>
<path d="M505,50 L505,98 M481,74 L529,74" stroke="var(--mu)" stroke-width="5"/>
{pen(595, 96, "médico, fisio", 38, "var(--mu)")}
{pen(595, 142, "ou psicólogo", 38, "var(--mu)")}
</svg>'''

B8 = paraquem2("Quando isso serve. E quando não serve.",
    "você cumpre o resto do plano, e um treino específico vive sendo trocado por outro mais leve.",
    "o motivo é dor, lesão ou cansaço que não passa, ou se esse jeito de fugir aparece também fora do esporte. Aí é com médico, fisioterapeuta ou psicólogo.", DOORS)

B9 = f'''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">Faltar dá um prêmio para a fuga.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">E fuga premiada volta.</h1>
<p class="mu" style="margin-top:36px">Manda pra aquele corredor que faz todas as rodagens e sempre troca o treino de tiros por um leve.</p>
<svg class="draw" width="888" height="210" viewBox="0 0 888 210" style="margin-top:auto; margin-bottom:50px">
<path d="M40,160 C200,190 330,150 420,110" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>
<path d="M440,100 L760,20 L560,190 L530,130 Z M530,130 L760,20" stroke="var(--pen)" stroke-width="5"/>
<path d="M560,190 L590,146" stroke="var(--pen)" stroke-width="4"/>
{pen(60, 70, "pra quem troca", 38, rot=-3)}
{pen(60, 114, "o tiro pelo leve", 38, rot=-3)}
</svg>'''

# =====================================================================================
# VERSÃO C — pergunta de escolha (A ou B) · rostos / chegada / bilhete / dragão · CTA comentar
# =====================================================================================
def face(cx, cy, kind):
    out = f'<circle cx="{cx}" cy="{cy}" r="88" stroke="var(--ink)" stroke-width="5"/>'
    if kind == "culpa":
        out += f'<path d="M{cx-40},{cy-28} L{cx-18},{cy-20} M{cx+40},{cy-28} L{cx+18},{cy-20}" stroke="var(--ink)" stroke-width="5"/>'
        out += f'<circle cx="{cx-28}" cy="{cy-4}" r="6" style="fill:var(--ink); stroke:none"/><circle cx="{cx+28}" cy="{cy-4}" r="6" style="fill:var(--ink); stroke:none"/>'
        out += f'<path d="M{cx-30},{cy+44} C{cx-10},{cy+26} {cx+10},{cy+26} {cx+30},{cy+44}" stroke="var(--ink)" stroke-width="5"/>'
        out += f'<path d="M{cx+70},{cy-60} C{cx+60},{cy-40} {cx+66},{cy-30} {cx+74},{cy-32} C{cx+82},{cy-34} {cx+82},{cy-44} {cx+70},{cy-60} Z" stroke="var(--ink)" stroke-width="3"/>'
    else:
        out += f'<path d="M{cx-42},{cy-6} C{cx-32},{cy+4} {cx-20},{cy+4} {cx-12},{cy-6} M{cx+12},{cy-6} C{cx+20},{cy+4} {cx+32},{cy+4} {cx+42},{cy-6}" stroke="var(--ink)" stroke-width="5"/>'
        out += f'<ellipse cx="{cx}" cy="{cy+42}" rx="12" ry="9" stroke="var(--ink)" stroke-width="4"/>'
        out += f'<path d="M{cx+20},{cy+48} C{cx+60},{cy+60} {cx+90},{cy+50} {cx+120},{cy+62} M{cx+24},{cy+60} C{cx+56},{cy+80} {cx+86},{cy+74} {cx+112},{cy+86}" stroke="var(--mu)" stroke-width="3"/>'
    return out

def optbox(x, letter, word):
    return (f'<rect x="{x}" y="20" width="380" height="330" rx="18" stroke="var(--mu)" stroke-width="3"/>'
            f'<circle cx="{x+40}" cy="60" r="26" style="fill:var(--pen); stroke:none"/>'
            + sans(x + 40, 70, letter, 30, "#fff", "middle", 800)
            + pen(x + 190, 330, word, 48, "var(--ink)", "middle"))

C1 = f'''<div style="margin-top:30px"></div>
<h1 style="font-size:78px">Você desmarcou aquele treino de novo. O que bate primeiro?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:60px">
{optbox(20, "A", "culpa")}{face(210, 170, "culpa")}
{optbox(488, "B", "alívio")}{face(678, 170, "alivio")}
{pen(444, 396, "escolha uma antes de seguir.", 38, anchor="middle", rot=-2)}
</svg>'''

def runner(x, y, color, sw=5):
    return (f'<circle cx="{x}" cy="{y-80}" r="16" stroke="{color}" stroke-width="{sw}"/>'
            f'<path d="M{x},{y-62} L{x-6},{y-14} M{x-4},{y-50} L{x+24},{y-30} L{x+36},{y-46} M{x-4},{y-50} L{x-30},{y-36} '
            f'M{x-6},{y-14} L{x+22},{y+10} L{x+20},{y+36} M{x-6},{y-14} L{x-28},{y+14} L{x-50},{y+12}" stroke="{color}" stroke-width="{sw}"/>')

C2 = f'''<h2>Se você marcou A, repara: quem chega primeiro é o alívio.</h2>
<p style="margin-top:36px">Se a culpa vier, vem depois. O alívio aparece no segundo em que você decide. E o que chega na hora é o que a cabeça %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<path d="M0,330 L888,330" stroke="var(--mu)" stroke-width="3"/>
<path d="M720,80 L720,330" stroke="var(--ink)" stroke-width="4"/>
<path d="M720,150 C700,180 690,220 700,260" stroke="var(--pen)" stroke-width="4"/>
{sans(720, 60, "CHEGADA", 22, "var(--mu)", "middle")}
{runner(770, 290, "var(--pen)", 6)}
{pen(770, 380, "alívio", 44, anchor="middle")}
{runner(130, 290, "var(--mu)", 4)}
{pen(130, 380, "culpa (se vier)", 36, "var(--mu)", "middle")}
<path d="M230,250 L640,250" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 14"/>
</svg>''' % hl("aprende")

def quiz(n, q):
    return f'{lab("Pergunta " + str(n))}<h2>{q}</h2>'

def postit():
    out = '<g transform="rotate(-3 444 200)">'
    out += '<rect x="194" y="20" width="500" height="320" style="fill:var(--hl); stroke:none"/>'
    out += '<path d="M194,20 L694,20 L694,340 L194,340 Z" stroke="var(--pen)" stroke-width="3"/>'
    out += sans(230, 70, "REGRA", 22, "var(--ink)", weight=800)
    out += pen(230, 140, "quando aquele treino", 42, "var(--ink)")
    out += pen(230, 192, "aparecer: desvia.", 42, "var(--ink)")
    ys = [222, 236, 250, 264, 282]
    for i, y in enumerate(ys):
        c = "var(--pen)" if i == len(ys) - 1 else "var(--ink)"
        w = 6 if i == len(ys) - 1 else 3
        out += f'<path d="M226,{y} C340,{y-4} 480,{y+4} 560,{y-2}" stroke="{c}" stroke-width="{w}"/>'
    out += '</g>'
    out += pen(444, 392, "cada alívio passa mais um traço embaixo.", 38, anchor="middle", rot=-2)
    return out

C3 = f'''{quiz(1, "O que esse alívio deixa escrito? E pra qual treino?")}
<p style="margin-top:30px">Uma regra: quando aquele treino aparecer, desvia. Cada vez que você desvia e sente alívio, a regra fica %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
{postit()}
</svg>''' % hl("mais forte")

def bars():
    out = '<path d="M40,10 L40,330 L870,330" stroke="var(--mu)" stroke-width="3"/>'
    hs = [120, 128, 140, 156, 176, 200, 230]
    for i, h in enumerate(hs):
        x = 80 + i * 112
        out += f'<rect x="{x}" y="{330-h}" width="70" height="{h}" rx="4" stroke="var(--pen)" stroke-width="4"/>'
        out += pen(x + 35, 320 - h - 10, "?", 34, "var(--mu)", "middle")
    return out

C4 = f'''{quiz(2, "E se você esperar? O medo passa sozinho? Em quantas semanas?")}
<p style="margin-top:30px">Sem fazer o treino, nada aparece pra mostrar que a previsão tava errada. Ela fica igual. Ou %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
{bars()}
{pen(60, 50, "o tamanho da previsão", 38, rot=-2)}
{pen(60, 100, "nenhuma barra foi conferida", 34, "var(--mu)", rot=-2)}
{sans(870, 376, "semanas sem fazer →", 22, anchor="end", weight=400)}
</svg>''' % hl("cresce")

def dragon(x, y):
    return (f'<g transform="translate({x},{y})">'
            f'<path d="M0,40 C20,0 50,0 60,30 C70,60 100,60 110,30 C120,0 150,0 160,30" stroke="var(--ink)" stroke-width="4"/>'
            f'<path d="M30,10 L36,-6 L44,8 M88,52 L96,66 M128,8 L136,-8 L142,10" stroke="var(--ink)" stroke-width="3"/>'
            f'<circle cx="174" cy="22" r="18" stroke="var(--ink)" stroke-width="4"/>'
            f'<circle cx="180" cy="18" r="4" style="fill:var(--ink); stroke:none"/>'
            f'<path d="M190,30 L214,24 M190,34 L212,40" stroke="var(--ink)" stroke-width="3"/>'
            f'<path d="M0,40 C-14,50 -24,44 -30,56" stroke="var(--ink)" stroke-width="4"/></g>')

C5 = f'''{quiz(3, "Então o que corrige a previsão? Pensar nela? Ler sobre ela?")}
<p style="margin-top:30px">Passar por ela. Fazer o treino e comparar o que você esperava com o que encontrou. É %s que a cabeça aprende.</p>
<svg class="draw" width="888" height="490" viewBox="0 0 888 490" style="margin-top:auto; margin-bottom:0px">
<rect x="10" y="10" width="250" height="140" rx="8" stroke="var(--mu)" stroke-width="3"/>
<rect x="320" y="10" width="250" height="140" rx="8" stroke="var(--mu)" stroke-width="3"/>
<rect x="630" y="10" width="248" height="140" rx="8" stroke="var(--mu)" stroke-width="3"/>
<rect x="10" y="250" width="250" height="110" rx="8" stroke="var(--mu)" stroke-width="3"/>
<rect x="320" y="250" width="250" height="110" rx="8" stroke="var(--mu)" stroke-width="3"/>
<rect x="630" y="250" width="248" height="110" rx="8" stroke="var(--mu)" stroke-width="3"/>
<path d="M0,200 L290,200 L290,384 L600,384 L600,200 L888,200" stroke="var(--ink)" stroke-width="4" stroke-dasharray="6 12"/>
{pen(620, 410, "o desvio de sempre", 34, "var(--ink)")}
<path d="M0,206 L888,206" stroke="var(--pen)" stroke-width="7"/>
{dragon(345, 160)}
<path d="M330,150 L590,236 M330,236 L590,150" stroke="var(--pen)" stroke-width="5"/>
{pen(640, 240, "aqui tinha um dragão", 32, "var(--mu)", rot=-2)}
{pen(20, 470, "só se risca passando pela rua.", 42, rot=-2)}
</svg>''' % hl("dessa diferença")

C6 = f'''<div style="margin-top:120px"></div>
<h1 style="font-size:82px">Desviar mantém o dragão no mapa.</h1>
<h1 class="or" style="font-size:82px; margin-top:22px">Passar pela rua mostra o que tem lá.</h1>'''

def checklist(items):
    out = '<div style="margin-top:20px">'
    for t in items:
        out += ('<div style="display:flex; gap:28px; align-items:flex-start; padding:26px 0; border-top:2px dashed var(--line)">'
                '<svg class="draw" width="54" height="54" viewBox="0 0 54 54" style="flex:none; margin-top:4px">'
                '<rect x="3" y="3" width="48" height="48" rx="8" stroke="var(--pen)" stroke-width="4"/></svg>'
                f'<div style="font-size:38px; font-weight:700; line-height:1.2; letter-spacing:-.01em">{t}</div></div>')
    return out + '</div>'

C7 = f'''<h2>Marca o que vale pra você.</h2>
{checklist(["Já desmarquei o mesmo treino mais de uma vez. E sei qual é.",
            "Na hora de desmarcar, veio alívio: na cama, no carro, no vestiário.",
            "Sei em que parte dele acho que vai dar errado: a série, o km, o fim.",
            "Nunca fui lá conferir se dá errado mesmo."])}
<div class="note" style="margin-top:auto; transform:rotate(-2deg)">cada marca é um pedaço<br>do mapa que você ainda não conferiu.</div>'''

LEGEND = f'''<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:auto">
<rect x="0" y="6" width="888" height="180" rx="10" stroke="var(--mu)" stroke-width="3"/>
{sans(30, 46, "LEGENDA", 20, "var(--mu)", weight=800)}
<circle cx="50" cy="94" r="12" style="fill:var(--pen); stroke:none"/>
{pen(80, 106, "o treino que você desvia: aqui", 34, "var(--ink)")}
<path d="M38,148 L62,148 M50,136 L50,160" stroke="var(--mu)" stroke-width="5"/>
{pen(80, 160, "dor, lesão, fuga em tudo: outro profissional", 34, "var(--mu)")}
</svg>'''

C8 = paraquem2("Pra quem é. E quando é outra rua.",
    "o resto do plano anda, e um treino específico vive sendo desviado.",
    "o desvio é por dor, lesão ou cansaço que não passa, ou se ele já aparece fora do esporte. Aí o caminho é um médico, um fisioterapeuta ou um psicólogo.", LEGEND)

C9 = f'''<div style="margin-top:40px"></div>
<h1 style="font-size:76px">A rua que você não passa vira dragão.</h1>
<h1 class="or" style="font-size:66px; margin-top:18px">Comenta A ou B: o que bateu primeiro da última vez?</h1>
<p class="mu" style="margin-top:30px">E manda pra quem marcaria a outra letra.</p>
<svg class="draw" width="888" height="170" viewBox="0 0 888 170" style="margin-top:auto; margin-bottom:60px">
<rect x="0" y="40" width="888" height="110" rx="55" stroke="var(--ink)" stroke-width="4"/>
{pen(60, 112, "comenta:", 40, "var(--mu)")}
<circle cx="300" cy="95" r="34" stroke="var(--pen)" stroke-width="4"/>{sans(300, 106, "A", 32, "var(--pen)", "middle", 800)}
{pen(370, 108, "ou", 36, "var(--mu)")}
<circle cx="470" cy="95" r="34" stroke="var(--pen)" stroke-width="4"/>{sans(470, 106, "B", 32, "var(--pen)", "middle", 800)}
<path d="M540,95 L740,95" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 10"/>
</svg>'''

VERSOES = {
    "A": [(D, A1, True), (L, A2, False), (D, A3, False), (L, A4, False), (D, A5, False),
          (L, A6, False), (D, A7, False), (L, A8, False), (D, A9, True)],
    "B": [(D, B1, True), (L, B2, False), (D, B3, False), (L, B4, False), (D, B5, False),
          (L, B6, False), (D, B7, False), (L, B8, False), (D, B9, True)],
    "C": [(L, C1, True), (D, C2, False), (L, C3, False), (D, C4, False), (L, C5, False),
          (D, C6, False), (L, C7, False), (D, C8, False), (L, C9, True)],
}

LEGENDAS = {
"A": """Repara em quando a decisão de pular aquele treino acontece. É na hora dele? Ou antes: na noite anterior, quando o despertador toca, no carro a caminho da pista?

Na próxima semana, anota isso. O dia, a hora e onde você estava quando decidiu não ir. Sem se cobrar. Só registrando.

Anota também o que veio logo depois. Se for aquela leveza de "ufa, hoje não", você acabou de ver o mecanismo funcionando ao vivo.

E tem um detalhe aqui: o resto da sua planilha mostra que preguiça não explica. Quem cumpre rodagem, força e longão sabe acordar cedo. O que trava é uma coisa só, e ela tem nome.

Salva pra reler na noite antes do próximo treino que você costuma empurrar.

Quer ir mais fundo? Diagnóstico completo e gratuito no link da bio.""",
"B": """Sabe quando você abre o treino do dia, vê os tiros e pensa "hoje vou de leve, amanhã eu compenso"? Essa troca parece ajuste de planilha. E às vezes é mesmo.

O jeito de saber a diferença é olhar pro padrão, não pro dia. Se a troca cai sempre no mesmo treino, não é ajuste. É o mesmo desvio com roupa nova.

Uma coisa que ajuda: quando bater a vontade de trocar, pergunta pra você mesmo o que exatamente acha que vai acontecer lá. Não "vai ser ruim". Em qual tiro? Sentindo o quê? Quanto mais concreta a frase, mais fácil conferir depois.

E se você for e a coisa não acontecer do jeito que imaginou, presta atenção nesse momento. É ali que a previsão começa a mudar.

Manda pra quem treina com você e sempre aparece de rodagem leve no dia dos tiros.

Pra enxergar o quadro inteiro: tem um diagnóstico completo, de graça, esperando no link do perfil.""",
"C": """Pensa no último treino que você desmarcou. Como foi? Mensagem no grupo, alarme desligado, ou só deixou o horário passar?

Agora tenta lembrar o que você imaginava que ia acontecer nele. Não o treino inteiro: a parte específica. A terceira série? O trecho de subida? O final, quando o ritmo aperta?

Essa parte é a sua rua com dragão. Enquanto você não passa por ela, a imagem que você tem dela é a única informação disponível. E ela não se corrige sozinha.

Pro próximo ciclo: escolhe só esse treino e coloca num dia em que você costuma cumprir o que está na planilha. Depois de fazer, repara: a parte que você temia apareceu do jeito que você imaginava?

Comenta aqui embaixo: A ou B? O que bateu primeiro da última vez que você desmarcou?

Mapear o resto também vale a pena. Diagnóstico completo, sem pagar nada, pelo link lá em cima.""",
}
