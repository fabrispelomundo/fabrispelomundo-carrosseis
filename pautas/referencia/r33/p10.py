# -*- coding: utf-8 -*-
# Pauta 10 — a voz que cobra (repetição e transferência). Versões A (clara), B (escura), C (escura).
from base import *

L, D = "light", "dark"

def alt(first, bodies):
    other = D if first == L else L
    out = []
    for i, b in enumerate(bodies):
        out.append((first if i % 2 == 0 else other, b, i in (0, 8)))
    return out

def paraquem2(title, sim, nao, drawing):
    return ('<h2 style="margin-bottom:40px">%s</h2><div class="lab or">É para você se</div><p>%s</p>'
            '<div class="sep" style="margin:30px 0"></div><div class="lab" style="color:var(--mu)">Não é para você se</div><p>%s</p>%s') % (title, sim, nao, drawing)

def pen(x, y, t, size=40, color="var(--pen)", anchor="start", rot=0):
    tr = ' transform="rotate(%s %d %d)"' % (rot, x, y) if rot else ""
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Pen" font-size="%d" fill="%s"%s>%s</text>' % (x, y, anchor, size, color, tr, t)

def sans(x, y, t, size=24, color="var(--mu)", anchor="start", w=700):
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Inter" font-weight="%d" font-size="%d" fill="%s">%s</text>' % (x, y, anchor, w, size, color, t)

# =================================================================== VERSÃO A (capa clara) — fita / faixa repetida
A1 = f'''<div style="margin-top:30px"></div>
<h1>Quando o pace cai, que frase aparece na sua cabeça?</h1>
<h1 class="or" style="margin-top:18px; font-size:62px; line-height:1.08">Em qual km? Com que palavras, exatamente?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:60px">
<rect x="170" y="20" width="548" height="300" rx="26" stroke="var(--ink)" stroke-width="5"/>
<g transform="rotate(4 500 130)">
<rect x="270" y="80" width="420" height="90" rx="8" style="fill:var(--bg)" stroke="var(--mu)" stroke-width="3"/>
{pen(470, 156, "gravada: bem antes", 34, "var(--mu)", "middle")}
</g>
<rect x="216" y="40" width="456" height="80" rx="8" style="fill:var(--bg)" stroke="var(--ink)" stroke-width="4"/>
{pen(444, 94, "prova de domingo", 44, "var(--ink)", "middle")}
<rect x="300" y="196" width="288" height="70" rx="34" stroke="var(--ink)" stroke-width="3"/>
<circle cx="350" cy="231" r="24" stroke="var(--ink)" stroke-width="4"/>
<circle cx="538" cy="231" r="24" stroke="var(--ink)" stroke-width="4"/>
<path d="M350,213 L350,249 M332,231 L368,231 M538,213 L538,249 M520,231 L556,231" stroke="var(--ink)" stroke-width="3"/>
<path d="M250,320 L280,280 L608,280 L638,320" stroke="var(--ink)" stroke-width="4"/>
<path d="M720,120 C780,110 800,150 790,176" stroke="var(--pen)" stroke-width="3"/>
<path d="M776,166 L790,180 L800,162" stroke="var(--pen)" stroke-width="3"/>
{pen(444, 384, "a etiqueta é nova. a fita, não.", 42, "var(--pen)", "middle", -2)}
</svg>'''

A2 = f'''<h2>Ela fala de pace. Mas repara no jeito.</h2>
<p style="margin-top:36px">As palavras são de corredor: lento, ritmo, de novo. Só que o tom costuma ser bem mais antigo que elas.</p>
<p>Então a pergunta que vale é outra: {hl("de quando é esse jeito de falar?")}</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:90px">
{sans(888, 40, "HOJE", 22, "var(--mu)", "end")}
<path d="M888,56 L888,330" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 8"/>
<path d="M700,100 L880,100 M700,88 L700,112 M880,88 L880,112" stroke="var(--ink)" stroke-width="4"/>
{pen(700, 80, "o seu relógio", 36, "var(--ink)")}
<path d="M430,190 L880,190 M430,178 L430,202 M880,178 L880,202" stroke="var(--ink)" stroke-width="4"/>
{pen(430, 170, "a sua vida de corredor", 36, "var(--ink)")}
<path d="M40,280 L880,280 M880,268 L880,292" stroke="var(--pen)" stroke-width="5"/>
<path d="M0,280 L24,280" stroke="var(--pen)" stroke-width="5" stroke-dasharray="4 8"/>
{pen(300, 262, "esse tom", 40, "var(--pen)")}
{pen(0, 340, "← começa onde?", 40, "var(--pen)", "start", -2)}
</svg>'''

def track(y, label, hi=False):
    c = "var(--pen)" if hi else "var(--ink)"
    return (f'{sans(20, y, label, 26, "var(--mu)")}'
            f'{pen(250, y + 2, "“você sempre afrouxa aqui”", 38, c)}'
            f'<path d="M806,{y - 4} L806,{y - 20} L856,{y - 20} M846,{y - 30} L858,{y - 20} L846,{y - 10} M856,{y - 2} L856,{y + 6} L806,{y + 6} M816,{y - 4} L804,{y + 6} L816,{y + 16}" stroke="{c}" stroke-width="3"/>'
            f'<path d="M0,{y + 30} L888,{y + 30}" stroke="var(--mu)" stroke-width="1.5" stroke-dasharray="3 9"/>')

A3 = f'''<h2>O que fica sem olhar tende a {circ("voltar")}.</h2>
<p style="margin-top:36px">Já parou pra pensar nisso? Ela volta sem avisar que é repetição. Em cada prova, a frase parece nova, como se fosse a primeira vez.</p>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:50px">
{sans(20, 30, "PROVA", 20, "var(--mu)")}{sans(250, 30, "FAIXA QUE TOCOU NO TRECHO DIFÍCIL", 20, "var(--mu)")}
<path d="M0,50 L888,50" stroke="var(--ink)" stroke-width="3"/>
{track(110, "a primeira")}{track(200, "a seguinte")}{track(290, "a de domingo")}{track(380, "a próxima", True)}
{pen(250, 460, "o modo repetir vem ligado de fábrica", 38, "var(--pen)", "start", -2)}
</svg>'''

A4 = f'''<h2>Olha o tamanho da cobrança perto do que o trecho pede.</h2>
<p style="margin-top:36px">Pensa no km da subida. O pace pede um ajuste. A frase cobra como se fosse {hl("um veredito sobre você")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,330 C240,330 340,326 420,300 C470,284 500,284 540,300 C620,326 760,330 860,330" stroke="var(--ink)" stroke-width="4"/>
{pen(600, 362, "o que o trecho pede", 36, "var(--ink)")}
<path d="M40,326 C240,322 330,300 380,200 C410,120 440,40 470,40 C500,40 520,130 560,230 C600,310 740,322 860,324" stroke="var(--pen)" stroke-width="5"/>
{pen(500, 60, "o tamanho da cobrança", 38, "var(--pen)")}
<path d="M470,52 L470,280" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 8"/>
<path d="M454,60 L470,44 L486,60 M454,272 L470,288 L486,272" stroke="var(--mu)" stroke-width="3"/>
{pen(110, 170, "essa sobra", 38, "var(--mu)")}
{pen(110, 212, "não é do pace", 38, "var(--mu)")}
<path d="M290,196 C340,196 400,180 450,170" stroke="var(--mu)" stroke-width="3"/>
{sans(740, 428, "km da prova →", 22, "var(--mu)", "start", 400)}
</svg>'''

A5 = f'''<h2>Discutir com ela no meio da prova só dá mais força a ela.</h2>
<p style="margin-top:36px">Depois da prova, faz outra coisa: escreve a frase exata, palavra por palavra. No papel, ela {hl("vira algo que dá pra examinar")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<rect x="40" y="20" width="808" height="320" rx="10" stroke="var(--ink)" stroke-width="5"/>
<rect x="60" y="40" width="768" height="280" rx="4" stroke="var(--mu)" stroke-width="2"/>
<rect x="130" y="130" width="628" height="90" rx="4" style="fill:var(--bg)" stroke="var(--ink)" stroke-width="3" transform="rotate(-1.5 444 175)"/>
{pen(444, 188, "“de novo? você sempre afrouxa.”", 42, "var(--ink)", "middle", -1.5)}
<line x1="140" y1="150" x2="170" y2="110" stroke="var(--pen)" stroke-width="4"/>
<circle cx="172" cy="106" r="9" style="fill:var(--pen); stroke:none"/>
<line x1="748" y1="150" x2="718" y2="110" stroke="var(--pen)" stroke-width="4"/>
<circle cx="716" cy="106" r="9" style="fill:var(--pen); stroke:none"/>
<rect x="520" y="250" width="270" height="50" rx="4" stroke="var(--mu)" stroke-width="2"/>
{sans(655, 283, "AMOSTRA: KM DIFÍCIL", 18, "var(--mu)", "middle")}
{pen(70, 400, "quem fala assim?", 40, "var(--pen)", "start", -2)}
{pen(520, 400, "desde quando?", 40, "var(--pen)", "start", -2)}
</svg>'''

A6 = '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A frase que você não olha volta em toda prova.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A frase que você escreve pode ser examinada.</h1>'''

A7 = qs("Depois da próxima prova, responde isso aqui.", [
    ("Qual foi a frase? A primeira que veio? Com quais palavras?", "“de novo?”, “afrouxou”, “eu sabia”. Do jeito que ela falou, sem resumir."),
    ("Onde ela apareceu? Na subida? No último km? Em qual trecho?", "No retorno, na ponte, quando alguém te passou, quando o relógio vibrou."),
    ("Quem falava assim com você? Num time? Em casa? Quando?", "Não precisa contar pra ninguém. Só repara de quem é esse jeito de cobrar.")])

A8 = paraquem("Pra quem é isso, e pra quem não é.",
    "a cobrança aparece no trecho difícil da prova, com palavras que você já conhece, e some depois que você cruza a chegada.",
    "essa voz não te larga fora da corrida, pesa no seu dia a dia ou traz lembranças que doem. Aí o caminho é um psicólogo.")

A9 = f'''<div style="margin-top:70px"></div>
<h1 style="font-size:80px">A frase não é nova.</h1>
<h1 class="or" style="font-size:80px; margin-top:18px">Só nunca foi lida inteira.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Salva pra escrever a sua, palavra por palavra, na noite depois da próxima prova.</p>
<svg class="draw" width="888" height="250" viewBox="0 0 888 250" style="margin-top:36px">
<rect x="0" y="10" width="888" height="210" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-1.5 444 115)"/>
<g transform="rotate(-1.5 444 115)">
{pen(40, 70, "a minha frase, exata:", 38, "var(--pen)")}
{pen(40, 150, "“", 70, "var(--ink)")}
<path d="M90,150 L770,150" stroke="var(--ink)" stroke-width="3" stroke-dasharray="2 12"/>
{pen(800, 150, "”", 70, "var(--ink)")}
{pen(40, 200, "de quando é esse tom? ______", 34, "var(--mu)")}
</g>
</svg>'''

# =================================================================== VERSÃO B (capa escura) — o tom é de antes / projetor
B1 = f'''<div style="margin-top:30px"></div>
<h1>Por que a cobrança da prova é mais velha que o seu primeiro tênis?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:60px">
<rect x="40" y="240" width="250" height="110" rx="6" stroke="var(--ink)" stroke-width="4"/>
<path d="M40,240 L70,210 L320,210 L290,240 M320,210 L320,320 L290,350" stroke="var(--ink)" stroke-width="4"/>
{pen(165, 305, "1º tênis", 40, "var(--ink)", "middle")}
<rect x="430" y="80" width="400" height="270" rx="6" stroke="var(--pen)" stroke-width="5"/>
<path d="M430,80 L470,40 L870,40 L830,80 M870,40 L870,310 L830,350" stroke="var(--pen)" stroke-width="5"/>
<path d="M440,120 L480,90 M450,150 L520,96 M470,150 L540,96 M760,330 L820,290 M790,340 L824,316" stroke="var(--mu)" stroke-width="2"/>
<path d="M430,80 L500,150 M430,110 L470,80 M450,130 L480,80 M430,80 C460,110 470,100 482,92" stroke="var(--mu)" stroke-width="1.5"/>
{pen(630, 225, "a cobrança", 50, "var(--pen)", "middle")}
{pen(630, 275, "(pó de muitos anos)", 32, "var(--mu)", "middle")}
<path d="M0,360 L888,360" stroke="var(--mu)" stroke-width="2"/>
{pen(444, 425, "o tênis é recente. a caixa ao lado, não.", 40, "var(--pen)", "middle", -2)}
</svg>'''

B2 = f'''<h2>Pois é: ela aprendeu a falar de corrida.</h2>
<p style="margin-top:36px">Pace, ritmo, km: as palavras são de agora. Já a pressa, o desdém, o jeito de cobrar {hl("costumam ser de antes")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:20px">
{pen(444, 230, "“anda. tá lento de novo.”", 64, "var(--ink)", "middle")}
<path d="M300,250 C330,262 380,262 420,250" stroke="var(--pen)" stroke-width="4"/>
<path d="M360,262 L360,330" stroke="var(--pen)" stroke-width="3"/>
{pen(360, 372, "palavra de corrida", 38, "var(--pen)", "middle")}
<path d="M150,170 C150,120 160,100 190,90" stroke="var(--mu)" stroke-width="3"/>
<path d="M600,170 C610,120 630,100 660,90" stroke="var(--mu)" stroke-width="3"/>
{pen(110, 70, "tom de antes?", 36, "var(--mu)")}
{pen(620, 70, "tom de antes?", 36, "var(--mu)")}
</svg>
<div class="note" style="transform:rotate(-2deg)">a roupa é de corredor.<br>quem veste, nem sempre.</div>'''

B3 = f'''<div class="lab" style="color:var(--mu)">O que parece</div>
<p style="margin-bottom:28px">É o pace de hoje que tá te cobrando.</p>
<div class="lab or">O que acontece</div>
<h2>Um tom antigo, projetado numa coisa de agora.</h2>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto">
<circle cx="80" cy="120" r="56" stroke="var(--ink)" stroke-width="4"/>
<circle cx="190" cy="104" r="44" stroke="var(--ink)" stroke-width="4"/>
<circle cx="80" cy="120" r="10" style="fill:var(--ink); stroke:none"/><circle cx="190" cy="104" r="8" style="fill:var(--ink); stroke:none"/>
<rect x="40" y="180" width="220" height="110" rx="12" stroke="var(--ink)" stroke-width="4"/>
<path d="M260,220 L300,206 L300,262 L260,250" stroke="var(--ink)" stroke-width="4"/>
{pen(150, 344, "rolo antigo", 36, "var(--mu)", "middle")}
<path d="M300,206 L640,40 M300,262 L640,400" stroke="var(--pen)" stroke-width="3" stroke-dasharray="6 10"/>
<rect x="640" y="40" width="240" height="360" rx="6" stroke="var(--ink)" stroke-width="4"/>
{sans(760, 120, "A TELA", 22, "var(--mu)", "middle")}
{pen(760, 190, "o pace", 40, "var(--ink)", "middle")}
{pen(760, 250, "a subida", 40, "var(--ink)", "middle")}
{pen(760, 310, "o relógio", 40, "var(--ink)", "middle")}
{pen(470, 236, "o filme", 38, "var(--pen)", "middle", -10)}
</svg>'''

B4 = f'''<div class="lab" style="color:var(--mu)">O que parece</div>
<p style="margin-bottom:28px">Se você responder à altura, ela cala.</p>
<div class="lab or">O que acontece</div>
<h2>Discutir no meio da prova só dá mais {circ("força")} a ela.</h2>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto">
<path d="M40,10 L40,360 L870,360" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,150 C240,170 420,240 560,280 C680,312 780,320 860,322" stroke="var(--mu)" stroke-width="3" stroke-dasharray="3 14"/>
{pen(600, 262, "o que você espera", 36, "var(--mu)")}
<path d="M40,150 C200,140 320,110 440,80 C580,46 720,34 860,30" stroke="var(--pen)" stroke-width="5"/>
{pen(380, 140, "o volume da voz", 40, "var(--pen)")}
{sans(600, 400, "respostas que você dá →", 22, "var(--mu)", "start", 400)}
</svg>'''

B5 = f'''<div class="lab" style="color:var(--mu)">O que parece</div>
<p style="margin-bottom:28px">A cobrança diz a verdade sobre você.</p>
<div class="lab or">O que acontece</div>
<h2>Escrita palavra por palavra, ela {hl("encolhe")}.</h2>
<p style="margin-top:24px">Depois da prova, do jeito exato que veio. No papel, dá pra perguntar de quem é esse tom.</p>
<svg class="draw" width="888" height="300" viewBox="0 0 888 300" style="margin-top:auto">
{sans(0, 120, "VOCÊ NUNCA", 58, "var(--ink)", "start", 900)}
{sans(0, 190, "AGUENTA!", 58, "var(--ink)", "start", 900)}
<path d="M360,130 L520,130 M500,112 L522,130 L500,148" stroke="var(--pen)" stroke-width="5"/>
<path d="M410,170 L470,110 L482,122 L422,182 Z M410,170 L404,190 L422,182" stroke="var(--pen)" stroke-width="3"/>
<path d="M560,150 L888,150" stroke="var(--mu)" stroke-width="2"/>
{pen(570, 140, "“você nunca aguenta”", 32, "var(--ink)")}
{pen(570, 200, "nunca? quem diz?", 30, "var(--pen)", "start", -2)}
{pen(570, 240, "de quando é isso?", 30, "var(--pen)", "start", -2)}
</svg>'''

B6 = '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Na prova, a cobrança parece falar do seu pace.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">No papel, dá pra ouvir de quando é o tom.</h1>'''

def field(y, n, q, blank):
    return (f'<text x="0" y="{y}" font-family="Pen" font-size="52" fill="var(--pen)">{n}</text>'
            f'{sans(60, y - 6, q, 30, "var(--ink)")}'
            f'{blank}')

def line(y, x0=60, x1=888):
    return f'<path d="M{x0},{y} L{x1},{y}" stroke="var(--mu)" stroke-width="2" stroke-dasharray="2 10"/>'

B7 = f'''<h2>Pensa na última prova. Responde aqui.</h2>
<svg class="draw" width="888" height="760" viewBox="0 0 888 760" style="margin-top:44px">
{field(40, "1", "Qual foi a frase? As palavras exatas?", pen(60, 112, "“", 56, "var(--ink)") + line(112, 92, 840) + pen(850, 112, "”", 56, "var(--ink)"))}
{field(220, "2", "Onde ela apareceu? Na subida? No último km?", line(290) + pen(60, 335, "subida, retorno, ponte, quando alguém te passou", 30, "var(--mu)"))}
{field(400, "3", "Já apareceu em outra prova? Na anterior?", f'<rect x="60" y="440" width="34" height="34" rx="4" stroke="var(--ink)" stroke-width="3"/>{pen(108, 470, "sim", 38, "var(--ink)")}<rect x="220" y="440" width="34" height="34" rx="4" stroke="var(--ink)" stroke-width="3"/>{pen(268, 470, "não", 38, "var(--ink)")}')}
{field(580, "4", "Esse tom lembra quem? De que época?", line(650))}
{pen(888, 740, "a resposta 4 é o seu diagnóstico", 38, "var(--pen)", "end", -2)}
</svg>'''

B8 = paraquem2("Pra quem é isso, e pra quem não é.",
    "na prova, você se cobra com palavras de pace e ritmo, e o tom parece maior do que o momento pede.",
    "essa cobrança te acompanha fora do esporte, tira o seu sono ou mexe com lembranças difíceis. Aí quem pode ajudar é um psicólogo.",
    f'''<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:auto">
<rect x="40" y="20" width="150" height="110" rx="6" stroke="var(--pen)" stroke-width="4"/>
<path d="M115,20 L115,130 M60,50 L100,50 M60,74 L100,74 M130,50 L170,50" stroke="var(--pen)" stroke-width="3"/>
{pen(220, 70, "aqui: uma frase", 36, "var(--pen)")}
{pen(220, 112, "num caderno", 36, "var(--pen)")}
<path d="M520,130 L520,60 L580,60 L580,130 M520,96 L580,96 M700,130 L700,60 L760,60 L760,130 M700,96 L760,96" stroke="var(--mu)" stroke-width="3"/>
{pen(640, 180, "psicólogo: uma conversa", 34, "var(--mu)", "middle")}
</svg>''')

B9 = f'''<div style="margin-top:70px"></div>
<h1 style="font-size:78px">A cobrança não nasceu na prova.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Só aprendeu a falar de pace.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Manda pra aquele amigo do grupo de corrida que se xinga em toda subida.</p>
{cta_box("manda pra quem", "se xinga na subida", "“anda, lerdo”", "de quando é isso?", x0=500, w=380)}'''

# =================================================================== VERSÃO C (capa escura) — A ou B / eco / iceberg
def stick(x, y, color, run=False, s=1.0):
    if run:
        return (f'<circle cx="{x}" cy="{y}" r="{18*s}" stroke="{color}" stroke-width="4"/>'
                f'<path d="M{x-4},{y+18*s} L{x-20},{y+70*s} M{x-12},{y+40*s} L{x+22},{y+52*s} M{x-12},{y+40*s} L{x-44},{y+30*s} '
                f'M{x-20},{y+70*s} L{x+10},{y+100*s} M{x-20},{y+70*s} L{x-52},{y+92*s}" stroke="{color}" stroke-width="4"/>')
    return (f'<circle cx="{x}" cy="{y}" r="{18*s}" stroke="{color}" stroke-width="4"/>'
            f'<path d="M{x},{y+18*s} L{x},{y+70*s} M{x},{y+36*s} L{x+30*s},{y+20*s} M{x},{y+36*s} L{x-26*s},{y+56*s} '
            f'M{x},{y+70*s} L{x-20*s},{y+104*s} M{x},{y+70*s} L{x+20*s},{y+104*s}" stroke="{color}" stroke-width="4"/>')

SCRIB = "M0,0 C20,-30 60,-20 50,10 C40,40 0,30 10,0 C20,-26 70,-24 66,6 C62,36 16,40 4,16 C-6,-6 40,-30 60,-6"

C1 = f'''<div style="margin-top:30px"></div>
<h1>A cobrança apertou no meio da prova. E aí, você faz o quê?</h1>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:auto; margin-bottom:56px">
<rect x="0" y="20" width="420" height="380" rx="18" stroke="var(--ink)" stroke-width="4"/>
<rect x="468" y="20" width="420" height="380" rx="18" stroke="var(--ink)" stroke-width="4"/>
{sans(30, 76, "A", 52, "var(--pen)", "start", 900)}
{sans(498, 76, "B", 52, "var(--pen)", "start", 900)}
{stick(120, 160, "var(--ink)")}
<g transform="translate(270,170) scale(1.4)"><path d="{SCRIB}" stroke="var(--mu)" stroke-width="3"/></g>
<path d="M156,190 L176,176 L190,200 L208,184 L222,206 L240,190" stroke="var(--pen)" stroke-width="3"/>
<path d="M240,240 L222,254 L208,232 L190,248 L176,226 L156,240" stroke="var(--pen)" stroke-width="3"/>
{pen(210, 370, "discute com ela", 40, "var(--ink)", "middle")}
{stick(790, 160, "var(--ink)", True)}
<path d="M690,180 L730,180 M680,210 L724,210 M690,240 L730,240" stroke="var(--mu)" stroke-width="3"/>
<g transform="translate(580,190) scale(1.1)"><path d="{SCRIB}" stroke="var(--mu)" stroke-width="3"/></g>
{pen(678, 370, "acelera pra calar", 40, "var(--ink)", "middle")}
{pen(444, 456, "escolhe antes de arrastar.", 40, "var(--pen)", "middle", -2)}
</svg>'''

C2 = f'''<h2>Se você marcou B, repara: nas duas, quem dá o ritmo é ela.</h2>
<p style="margin-top:36px">Discutindo ou fugindo, você continua respondendo à cobrança. A pergunta que ajuda é outra: {hl("de quando é esse tom?")}</p>
<svg class="draw" width="888" height="410" viewBox="0 0 888 410" style="margin-top:auto; margin-bottom:10px">
<path d="M0,40 L60,40 L90,110 L70,170 L110,240 L90,300 L130,340 L0,340" stroke="var(--ink)" stroke-width="4"/>
{pen(20, 30, "lá atrás", 34, "var(--mu)")}
<path d="M150,160 C170,180 170,220 150,240" stroke="var(--mu)" stroke-width="3"/>
<path d="M230,140 C262,170 262,230 230,260" stroke="var(--mu)" stroke-width="3"/>
<path d="M330,120 C376,160 376,240 330,280" stroke="var(--pen)" stroke-width="3"/>
<path d="M450,100 C514,150 514,250 450,300" stroke="var(--pen)" stroke-width="4"/>
<path d="M580,80 C664,140 664,260 580,320" stroke="var(--pen)" stroke-width="5"/>
{stick(770, 150, "var(--ink)", True)}
{pen(760, 330, "aqui, no km", 34, "var(--ink)", "middle")}
{pen(160, 392, "o eco chega mais alto do que saiu", 36, "var(--pen)")}
</svg>'''

C3 = f'''<h2>Pergunta 1: ela tá falando do pace de hoje? Só dele?</h2>
<p style="margin-top:30px">Só por cima. As palavras são de corrida. Por baixo, ela costuma repetir um tom antigo, {hl("sem você notar que é repetição")}.</p>
<svg class="draw" width="888" height="500" viewBox="0 0 888 500" style="margin-top:auto">
<path d="M0,130 C120,122 220,138 330,128 C480,116 660,138 888,126" stroke="var(--mu)" stroke-width="3"/>
<path d="M330,128 L400,40 L460,70 L520,30 L580,128" stroke="var(--ink)" stroke-width="4"/>
<path d="M330,128 L250,260 L300,400 L450,480 L620,420 L680,270 L580,128" stroke="var(--ink)" stroke-width="3" stroke-dasharray="6 10"/>
{pen(620, 50, "as palavras:", 34, "var(--ink)")}{pen(620, 92, "“lento”, “pace”", 34, "var(--ink)")}
{pen(460, 240, "o tom", 42, "var(--pen)", "middle")}
<path d="M300,300 L620,300" stroke="var(--mu)" stroke-width="1.5" stroke-dasharray="2 8"/>
{pen(460, 390, "de quem? de quando?", 38, "var(--pen)", "middle")}
{pen(700, 300, "o que você", 32, "var(--mu)")}
{pen(700, 336, "não vê no km", 32, "var(--mu)")}
</svg>'''

C4 = f'''<h2>Pergunta 2: se você discute com ela, ela baixa a voz? Baixa mesmo?</h2>
<p style="margin-top:30px">Costuma ser o contrário. Cada resposta no meio da prova dá mais espaço a ela. E sobra {hl("menos atenção pra correr")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto">
<path d="M40,10 L40,370 L870,370" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,60 C220,66 360,120 480,200 C600,280 740,316 860,320" stroke="var(--ink)" stroke-width="4"/>
{pen(100, 46, "atenção na corrida", 36, "var(--ink)")}
<path d="M40,320 C220,316 360,280 480,200 C600,120 740,70 860,60" stroke="var(--pen)" stroke-width="5"/>
{pen(540, 50, "atenção na discussão", 38, "var(--pen)")}
<circle cx="480" cy="200" r="12" style="fill:var(--pen); stroke:none"/>
{pen(110, 205, "o km em que ela assume", 30, "var(--mu)")}<path d="M410,198 L462,200" stroke="var(--mu)" stroke-width="2"/>
{sans(620, 412, "minutos discutindo →", 22, "var(--mu)", "start", 400)}
</svg>'''

C5 = f'''<h2>Pergunta 3: então o que dá pra fazer? Na hora? Depois?</h2>
<p style="margin-top:30px">Depois da prova, escrever a frase exata, palavra por palavra. Escrita, ela {hl("perde o tom de verdade absoluta")} e vira algo que dá pra examinar.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto">
<rect x="20" y="60" width="520" height="110" rx="6" stroke="var(--ink)" stroke-width="4" transform="rotate(-2 280 115)"/>
{pen(280, 128, "“você não nasceu pra isso”", 38, "var(--ink)", "middle", -2)}
<circle cx="520" cy="112" r="8" stroke="var(--ink)" stroke-width="3"/>
<path d="M528,112 C590,120 600,170 640,190" stroke="var(--mu)" stroke-width="3"/>
<path d="M620,190 L840,170 L870,250 L870,370 L640,390 Z" stroke="var(--pen)" stroke-width="4" transform="rotate(4 750 280)"/>
<circle cx="640" cy="200" r="8" stroke="var(--pen)" stroke-width="3"/>
<g transform="rotate(4 750 280)">
{sans(755, 260, "VERDADE", 34, "var(--ink)", "middle", 900)}
<path d="M670,250 L840,240 M672,262 L838,252" stroke="var(--pen)" stroke-width="4"/>
{pen(755, 310, "uma frase", 36, "var(--pen)", "middle")}
{pen(755, 350, "de alguém, de alguma época", 24, "var(--pen)", "middle")}
</g>
</svg>'''

C6 = '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Responder à voz no meio da prova dá palco a ela.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Escrever a voz depois da prova dá distância.</h1>'''

def chk(y, t, t2=""):
    out = f'<rect x="0" y="{y-34}" width="40" height="40" rx="5" stroke="var(--ink)" stroke-width="3"/>{sans(70, y, t, 32, "var(--ink)", "start", 600)}'
    if t2:
        out += sans(70, y + 42, t2, 32, "var(--ink)", "start", 600)
    return out

C7 = f'''<h2>Marca o que já aconteceu com você.</h2>
<svg class="draw" width="888" height="700" viewBox="0 0 888 700" style="margin-top:50px">
{chk(50, "A frase é sempre a mesma, palavra por palavra.")}
{chk(150, "Ela volta no mesmo tipo de trecho:", "subida, retorno, último km.")}
{chk(292, "Você responde, discute, manda ela calar.")}
{chk(392, "O tom lembra alguém. E você sabe quem.")}
{chk(492, "Você nunca escreveu a frase inteira.")}
<path d="M0,560 L888,560" stroke="var(--mu)" stroke-width="2" stroke-dasharray="3 10"/>
{pen(0, 620, "cada marca é um motivo pra escrever", 40, "var(--pen)", "start", -1)}
{pen(0, 670, "a frase depois da próxima prova.", 40, "var(--pen)", "start", -1)}
</svg>'''

C8 = paraquem2("Pra quem é isso, e pra quem não é.",
    "a cobrança aparece no km difícil, você se pega discutindo com ela e quer entender de onde vem esse tom.",
    "essa voz fala com você o dia inteiro, longe da corrida, ou vem junto com lembranças pesadas. Aí a conversa é com um psicólogo.",
    f'''<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto">
<circle cx="444" cy="180" r="10" style="fill:var(--ink); stroke:none"/>
<path d="M444,170 C444,110 360,80 220,60 M232,46 L216,60 L234,74" stroke="var(--pen)" stroke-width="4"/>
<path d="M444,170 C444,110 528,80 668,60 M656,46 L672,60 L654,74" stroke="var(--mu)" stroke-width="3"/>
{pen(0, 50, "só no km difícil:", 32, "var(--pen)")}
{pen(0, 90, "o caderno", 32, "var(--pen)")}
{pen(888, 50, "em todo lugar:", 30, "var(--mu)", "end")}
{pen(888, 90, "o psicólogo", 30, "var(--mu)", "end")}
</svg>''')

C9 = f'''<div style="margin-top:60px"></div>
<h1 style="font-size:78px">Ganhar a discussão nunca foi o ponto.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Saber de quando ela é, sim.</h1>
<p class="mu" style="margin-top:40px; max-width:860px">Comenta aí: A ou B? O que você faz quando a cobrança aperta? E manda pra quem responderia o contrário.</p>
<svg class="draw" width="888" height="190" viewBox="0 0 888 190" style="margin-top:30px">
<rect x="40" y="40" width="110" height="110" rx="12" stroke="var(--ink)" stroke-width="4"/>
{sans(95, 118, "A", 64, "var(--ink)", "middle", 900)}
<rect x="230" y="40" width="110" height="110" rx="12" stroke="var(--ink)" stroke-width="4"/>
{sans(285, 118, "B", 64, "var(--ink)", "middle", 900)}
<rect x="470" y="30" width="400" height="130" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3" transform="rotate(-3 670 95)"/>
{pen(670, 86, "a sua letra aqui", 38, "var(--ink)", "middle", -3)}
{pen(670, 132, "e o km em que ela fala", 34, "var(--pen)", "middle", -3)}
<path d="M360,95 L450,95 M432,80 L452,95 L432,110" stroke="var(--pen)" stroke-width="3"/>
</svg>'''

VERSOES = {
    "A": alt(L, [A1, A2, A3, A4, A5, A6, A7, A8, A9]),
    "B": alt(D, [B1, B2, B3, B4, B5, B6, B7, B8, B9]),
    "C": alt(D, [C1, C2, C3, C4, C5, C6, C7, C8, C9]),
}


LEGENDAS = {"A": """Sabe aquele momento do treino de ritmo em que o relógio vibra e o número não é o que você queria? Repara no que vem logo depois, antes de qualquer ajuste na passada.

Às vezes é uma frase. Às vezes é só um suspiro com cara de bronca. Ela costuma chegar pronta, como se só faltasse a deixa.

Um exercício pro próximo treino forte: não responde. Não rebate, não concorda. Só guarda o km e a primeira palavra que ela usou.

Em casa, escreve a frase inteira. Depois lê em voz alta, devagar, como se fosse de outra pessoa. Repara no tom. Repara de quando ele parece ser.

Salva este post pra fazer isso no próximo treino forte, e de novo depois da próxima prova.

Quer ir mais fundo? Um diagnóstico completo e gratuito aguarda no link da bio.""",
"B": """Já reparou com quem você fica bravo no meio de uma prova difícil? Com o cara que te passou na subida. Com o relógio. Com o amigo que gritou "bora" da beira da pista.

Às vezes a irritação é bem maior do que a cena pede. Pois é: o tom que chega ali pode ser de outra relação, de outro tempo, apontado pra quem estiver mais perto.

Na próxima prova, quando bater essa irritação, faz uma pergunta curta: essa reação tem o tamanho do que aconteceu agora? Se não tiver, a sobra veio de outro lugar.

Não precisa resolver ali, com o percurso pela frente. Só percebe. Anota mentalmente o km e segue.

Manda pra quem sai de toda prova reclamando de alguém que cruzou o caminho dele.

Pra ir além: diagnóstico completo, sem custo, no link da bio.""",
"C": """Tem uma coluna que talvez falte na sua planilha: a frase do dia.

Do lado do pace, da distância e do batimento, anota a frase que apareceu no momento mais duro do treino. Do jeito que veio, com as palavras dela.

Depois de algumas semanas, olha a coluna inteira. Se ela se repete e só muda o lugar onde aparece, você já tem uma pista. O tom costuma ser o mesmo, mesmo quando o treino muda.

Não é pra brigar com o que tá escrito. É pra ler com distância, como quem lê o caderno de outra pessoa.

E no meio da prova, quando ela aperta, você é mais A ou mais B? Comenta aqui embaixo: A ou B? E marca quem marcaria o contrário.

Pra enxergar o quadro completo, de graça, o diagnóstico mora no link da bio.""",
}
