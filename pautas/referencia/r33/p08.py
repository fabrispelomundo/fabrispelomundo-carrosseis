# -*- coding: utf-8 -*-
# Pauta p08 — "Se o pace cair, eu sou fraco" (a frase automática que chega junto com o número)
from base import *

L, D = "light", "dark"

def pa(parece, acontece):
    return (f'<div style="margin-top:30px"><div class="lab" style="color:var(--mu); margin-bottom:6px">Parece</div>'
            f'<p style="font-size:33px">{parece}</p>'
            f'<div class="lab or" style="margin:20px 0 6px">Acontece</div><p style="font-size:33px">{acontece}</p></div>')

def quiz(n, pergunta, resposta):
    return (f'<div class="lab or">Pergunta {n}</div><h2>{pergunta}</h2>'
            f'<div class="lab" style="color:var(--mu); margin:30px 0 8px">Resposta</div><p>{resposta}</p>')

# =============================================================== VERSÃO A · capa clara · "pergunta para você"
A = []
A.append((L, '''<div style="margin-top:30px"></div>
<h1>O pace caiu. Em qual km? Na subida? E que frase veio junto?</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:30px">
<path d="M40,150 L48,108 L86,108 L94,150 M40,262 L48,304 L86,304 L94,262" stroke="var(--ink)" stroke-width="4"/>
<rect x="22" y="150" width="90" height="112" rx="24" stroke="var(--ink)" stroke-width="4"/>
<path d="M67,176 L67,230 M52,214 L67,232 L82,214" stroke="var(--pen)" stroke-width="5"/>
<text x="67" y="352" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">bip</text>
<path d="M134,206 C160,186 190,186 214,204 M198,190 L216,206 L196,214" stroke="var(--mu)" stroke-width="3"/>
<text x="250" y="190" font-family="Pen" font-size="110" fill="var(--ink)">eu sou</text>
<path d="M250,300 L870,296" stroke="var(--pen)" stroke-width="5" stroke-dasharray="2 16"/>
<text x="560" y="380" text-anchor="middle" font-family="Pen" font-size="42" fill="var(--pen)" transform="rotate(-2 560 380)">você completou, né?</text>
</svg>''', True))

def keyboard():
    k = ''
    for row, (n, x0) in enumerate([(10, 44), (9, 84), (7, 164)]):
        for i in range(n):
            k += f'<rect x="{x0 + i*80}" y="{250 + row*62}" width="68" height="48" rx="8" stroke="var(--mu)" stroke-width="2"/>'
    return k

A.append((D, f'''<h2>Repara: ela chega pronta, antes do próximo passo.</h2>
<p style="margin-top:34px">Sem esforço, sem você pedir, já com cara de verdade. É como se a cabeça tivesse um {hl("autocompletar")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<rect x="40" y="10" width="808" height="90" rx="45" stroke="var(--mu)" stroke-width="3"/>
<text x="84" y="68" font-family="Inter" font-size="34" fill="var(--ink)">se o pace cair, eu</text>
<path d="M392,34 L392,78" stroke="var(--pen)" stroke-width="3"/>
<rect x="40" y="128" width="808" height="84" rx="12" stroke="var(--mu)" stroke-width="2"/>
<path d="M309,140 L309,200 M578,140 L578,200" stroke="var(--mu)" stroke-width="2"/>
<rect x="46" y="134" width="258" height="72" rx="10" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="3"/>
<text x="175" y="181" text-anchor="middle" font-family="Inter" font-weight="700" font-size="30" fill="var(--ink)">sou fraco</text>
<text x="444" y="181" text-anchor="middle" font-family="Inter" font-size="30" fill="var(--mu)">não sirvo</text>
<text x="713" y="181" text-anchor="middle" font-family="Inter" font-size="30" fill="var(--mu)">sempre quebro</text>
{keyboard()}
</svg>
<div class="note" style="margin-top:10px; transform:rotate(-2deg)">você não digitou. já tava sugerido.</div>''', False))

A.append((L, f'''<h2>O relógio te dá um número. A frase é outra coisa.</h2>
<p style="margin-top:34px">Ela é a sua leitura do número. Olha a ordem: o dado chega, a frase interpreta, e o {hl("km seguinte obedece à frase")}.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:50px">
<rect x="0" y="40" width="250" height="170" rx="18" stroke="var(--ink)" stroke-width="4"/>
<text x="125" y="96" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--mu)">DADO</text>
<text x="125" y="160" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--ink)">o pace caiu</text>
<path d="M262,125 L306,125 M292,112 L308,125 L292,138" stroke="var(--ink)" stroke-width="4"/>
<rect x="319" y="40" width="250" height="170" rx="18" stroke="var(--pen)" stroke-width="5"/>
<text x="444" y="96" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--pen)">LEITURA</text>
<text x="444" y="160" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)">“sou fraco”</text>
<path d="M581,125 L625,125 M611,112 L627,125 L611,138" stroke="var(--ink)" stroke-width="4"/>
<rect x="638" y="40" width="250" height="170" rx="18" stroke="var(--ink)" stroke-width="4"/>
<text x="763" y="96" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--mu)">RESPOSTA</text>
<text x="763" y="160" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--ink)">o km seguinte</text>
<path d="M10,240 C10,262 30,262 60,262 L100,262 C115,262 125,272 125,284 C125,272 135,262 150,262 L190,262 C220,262 240,262 240,240" stroke="var(--mu)" stroke-width="3"/>
<text x="125" y="330" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">o relógio só vê isto</text>
<text x="444" y="390" text-anchor="middle" font-family="Pen" font-size="38" fill="var(--pen)" transform="rotate(-2 444 390)">quem decide é a do meio</text>
</svg>''', False))

A.append((D, f'''<h2>A prova muda. A frase, não.</h2>
<p style="margin-top:34px">Já parou pra pensar? Calor, subida, sono, percurso: cada prova é um dia diferente. Se a frase vem igual em todas, ela {hl("não está lendo a prova do dia")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:46px">
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,250 C110,120 170,110 230,220 C290,330 350,340 420,180 C480,60 540,80 600,260 C650,360 720,330 780,170 C810,100 840,110 860,150" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
<text x="150" y="80" font-family="Pen" font-size="36" fill="var(--ink)">o dia de cada prova</text>
<path d="M40,300 L860,300" stroke="var(--pen)" stroke-width="5"/>
<circle cx="230" cy="300" r="9" style="fill:var(--pen); stroke:none"/>
<circle cx="420" cy="300" r="9" style="fill:var(--pen); stroke:none"/>
<circle cx="600" cy="300" r="9" style="fill:var(--pen); stroke:none"/>
<circle cx="780" cy="300" r="9" style="fill:var(--pen); stroke:none"/>
<text x="470" y="352" font-family="Pen" font-size="38" fill="var(--pen)">a frase: igualzinha</text>
<text x="660" y="424" font-family="Inter" font-size="22" fill="var(--mu)">prova após prova →</text>
</svg>''', False))

A.append((L, f'''<h2>Acabou o treino? Escreve a frase exata.</h2>
<p style="margin-top:34px">Palavra por palavra, do jeito que veio. No papel, ela perde o tom de verdade e vira só uma frase que {hl("você pode examinar")}.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<rect x="90" y="10" width="708" height="330" rx="6" stroke="var(--ink)" stroke-width="5"/>
<rect x="112" y="32" width="664" height="286" rx="4" stroke="var(--mu)" stroke-width="2"/>
<path d="M210,120 L690,112 L700,206 L218,214 Z" stroke="var(--ink)" stroke-width="3" style="fill:var(--bg)"/>
<text x="455" y="182" text-anchor="middle" font-family="Pen" font-size="58" fill="var(--ink)" transform="rotate(-1 455 170)">“eu sou fraco”</text>
<line x1="226" y1="122" x2="226" y2="80" stroke="var(--pen)" stroke-width="4"/>
<circle cx="226" cy="74" r="9" style="fill:var(--pen); stroke:none"/>
<line x1="684" y1="114" x2="684" y2="72" stroke="var(--pen)" stroke-width="4"/>
<circle cx="684" cy="66" r="9" style="fill:var(--pen); stroke:none"/>
<rect x="250" y="244" width="388" height="52" rx="4" stroke="var(--mu)" stroke-width="2"/>
<text x="444" y="279" text-anchor="middle" font-family="Inter" font-weight="700" font-size="20" fill="var(--mu)">FRASE AUTOMÁTICA · KM DA SUBIDA</text>
<text x="444" y="410" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)" transform="rotate(-2 444 410)">presa no papel, ela para de correr com você</text>
</svg>''', False))

A.append((D, '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">O relógio te dá um número.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">A frase te dá um veredito. E quem corre o km seguinte é ela.</h1>''', False))

A.append((L, qs("Pega o último treino em que o pace caiu.", [
    ("Qual foi a frase? A exata? Com que palavras?", "“Sou fraco”, “não sirvo”, “de novo isso”. Do jeito que veio, sem arrumar."),
    ("Ela já veio antes? Em qual prova? Em que trecho?", "Na subida, no retorno, no vento contra, no último km. Se veio igual, não estava lendo aquele dia."),
    ("E se fosse verdade? Diria o quê sobre você?", "Que você não é corredor? Que só vale se bater o tempo? Ali está a crença que puxa a frase.")]), False))

A.append((D, paraquem("Pra quem é isso, e pra quem não é.",
    "o pace cai no meio da prova e, junto com o número, chega uma frase sobre você que parece verdade.",
    "essa voz te acompanha fora do esporte e pesa no trabalho, em casa, no sono. Aí o caminho é um psicólogo. Se o pace cai por dor, procure um médico."), False))

A.append((L, '''<div style="margin-top:60px"></div>
<h1 style="font-size:76px">O relógio só sabe que o pace caiu.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">O resto da frase foi você que escreveu.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Salva pra reler no fim do próximo treino em que o pace cair. E anota a frase antes de esquecer.</p>
''' + cta_box("o que o relógio", "registrou de fato", "“eu sou fraco”", "o pace caiu. só."), True))

# =============================================================== VERSÃO B · capa escura · "pergunta-enigma"
B = []
B.append((D, '''<div style="margin-top:30px"></div>
<h1>Plana ou trail, frio ou calor. Por que a frase do pior km é sempre igual?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:30px">
<path d="M10,200 L60,196 L120,198 L180,194 L240,197 L300,195 L380,196" stroke="var(--ink)" stroke-width="4"/>
<text x="195" y="250" text-anchor="middle" font-family="Inter" font-weight="700" font-size="22" fill="var(--mu)">PLANA, FRIO, CEDO</text>
<path d="M500,200 L540,170 L580,90 L610,120 L650,40 L700,150 L740,110 L790,190 L878,196" stroke="var(--ink)" stroke-width="4"/>
<text x="690" y="250" text-anchor="middle" font-family="Inter" font-weight="700" font-size="22" fill="var(--mu)">TRAIL, SUBIDA, CALOR</text>
<text x="444" y="140" text-anchor="middle" font-family="Pen" font-size="60" fill="var(--mu)">≠</text>
<text x="195" y="330" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)" transform="rotate(-2 195 330)">“eu nunca aguento”</text>
<text x="690" y="330" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)" transform="rotate(-2 690 330)">“eu nunca aguento”</text>
<text x="444" y="336" text-anchor="middle" font-family="Pen" font-size="60" fill="var(--pen)">=</text>
</svg>''', True))

B.append((L, f'''<h2>Porque ela não tá lendo a prova.</h2>
<p style="margin-top:34px">Ela foi com você para a largada. Pronta, gravada, esperando o primeiro número ruim no relógio pra {hl("tocar sozinha")}.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:44px">
<rect x="94" y="20" width="700" height="360" rx="30" stroke="var(--ink)" stroke-width="5"/>
<rect x="150" y="60" width="588" height="110" rx="10" stroke="var(--ink)" stroke-width="3"/>
<text x="180" y="104" font-family="Pen" font-size="34" fill="var(--mu)">pior km · lado A</text>
<text x="180" y="150" font-family="Pen" font-size="40" fill="var(--pen)">faixa 1: “eu nunca aguento”</text>
<rect x="230" y="200" width="428" height="110" rx="55" stroke="var(--ink)" stroke-width="3"/>
<circle cx="300" cy="255" r="38" stroke="var(--ink)" stroke-width="4"/>
<circle cx="588" cy="255" r="38" stroke="var(--ink)" stroke-width="4"/>
<circle cx="300" cy="255" r="12" stroke="var(--ink)" stroke-width="3"/>
<circle cx="588" cy="255" r="12" stroke="var(--ink)" stroke-width="3"/>
<path d="M338,255 L550,255" stroke="var(--mu)" stroke-width="2"/>
<path d="M250,380 L280,340 L608,340 L638,380" stroke="var(--ink)" stroke-width="3"/>
</svg>
<div class="note" style="margin-top:20px; transform:rotate(-2deg)">então vem de onde?</div>''', False))

B.append((D, '''<h2>Se liga: ela não brota na prova. Tem raiz.</h2>''' + pa(
    "a frase fala do km em que você está.",
    "ela nasce de uma crença sobre você, que quase nunca aparece. O que aparece é só a frase.") + '''
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:30px">
<path d="M0,170 L888,170" stroke="var(--mu)" stroke-width="3" stroke-dasharray="10 10"/>
<path d="M444,170 C440,130 446,100 444,60" stroke="var(--ink)" stroke-width="4"/>
<path d="M444,100 C410,70 370,70 340,90 C370,110 410,112 444,100 Z" stroke="var(--ink)" stroke-width="3"/>
<path d="M444,80 C480,46 520,48 548,66 C520,90 480,92 444,80 Z" stroke="var(--ink)" stroke-width="3"/>
<text x="580" y="70" font-family="Pen" font-size="38" fill="var(--ink)">“eu nunca aguento”</text>
<path d="M444,170 C440,220 420,250 380,280 M444,170 C450,230 480,260 520,290 M444,190 C444,250 446,300 440,340 M410,250 C380,260 340,250 310,270 M480,250 C520,250 560,240 590,256" stroke="var(--pen)" stroke-width="4"/>
<text x="444" y="390" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--pen)">“meu valor está no resultado”</text>
<text x="20" y="130" font-family="Pen" font-size="32" fill="var(--mu)">corta a folha,</text>
<text x="20" y="160" font-family="Pen" font-size="32" fill="var(--mu)">ela volta igual</text>
</svg>''', False))

B.append((L, '''<h2>O pace caiu. Mas não foi o número que derrubou o resto.</h2>''' + pa(
    "o pace caiu e o resto da prova foi junto.",
    "o número caiu, aí veio a frase. E foi ela que decidiu o km seguinte.") + '''
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:30px">
<path d="M40,10 L40,310 L870,310" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,80 L260,84 C290,86 300,118 330,120 L420,122" stroke="var(--ink)" stroke-width="5"/>
<path d="M420,122 C520,124 560,126 860,130" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
<text x="610" y="110" font-family="Pen" font-size="32" fill="var(--ink)">só com o dado</text>
<path d="M420,122 C520,160 640,240 860,276" stroke="var(--pen)" stroke-width="5"/>
<text x="560" y="300" font-family="Pen" font-size="34" fill="var(--pen)">com a frase junto</text>
<path d="M300,160 L300,200" stroke="var(--mu)" stroke-width="2"/>
<text x="250" y="232" font-family="Pen" font-size="30" fill="var(--mu)">o número</text>
<circle cx="420" cy="122" r="10" style="fill:var(--pen); stroke:none"/>
<text x="400" y="66" font-family="Pen" font-size="32" fill="var(--pen)">a frase</text>
<text x="700" y="350" font-family="Inter" font-size="22" fill="var(--mu)">quilômetros →</text>
</svg>''', False))

B.append((D, '''<h2>Ela passa direto pela conferência.</h2>''' + pa(
    "se veio tão forte, deve ser verdade.",
    "veio forte porque veio rápido, sem esforço. E o que chega assim você nem pensa em conferir.") + '''
<svg class="draw" width="888" height="300" viewBox="0 0 888 300" style="margin-top:20px">
<path d="M0,250 L888,250 M0,270 L888,270" stroke="var(--mu)" stroke-width="3"/>
<circle cx="60" cy="282" r="10" stroke="var(--mu)" stroke-width="2"/><circle cx="440" cy="282" r="10" stroke="var(--mu)" stroke-width="2"/><circle cx="820" cy="282" r="10" stroke="var(--mu)" stroke-width="2"/>
<rect x="20" y="190" width="130" height="60" rx="8" stroke="var(--ink)" stroke-width="3"/>
<text x="85" y="230" text-anchor="middle" font-family="Pen" font-size="30" fill="var(--ink)">o pace</text>
<rect x="170" y="190" width="130" height="60" rx="8" stroke="var(--ink)" stroke-width="3"/>
<text x="235" y="230" text-anchor="middle" font-family="Pen" font-size="30" fill="var(--ink)">a subida</text>
<path d="M360,250 L360,120 L560,120 L560,250" stroke="var(--ink)" stroke-width="5"/>
<text x="460" y="176" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--ink)">CONFERIR</text>
<path d="M240,150 C320,10 620,0 690,160" stroke="var(--pen)" stroke-width="4" stroke-dasharray="4 12"/>
<path d="M670,150 L692,166 L700,140" stroke="var(--pen)" stroke-width="4"/>
<rect x="610" y="176" width="270" height="70" rx="8" stroke="var(--pen)" stroke-width="4" transform="rotate(-4 745 211)"/>
<text x="745" y="222" text-anchor="middle" font-family="Pen" font-size="32" fill="var(--pen)" transform="rotate(-4 745 211)">“eu nunca aguento”</text>
<text x="300" y="34" font-family="Pen" font-size="32" fill="var(--pen)">passou direto</text>
</svg>
<p style="margin-top:20px">Confere com uma pergunta: %s</p>''' % hl("“se isso fosse verdade, o que diria sobre mim?”"), False))

B.append((L, '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">A frase parece falar da prova.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Ela fala de você. E chegou antes da largada.</h1>''', False))

def blank(label):
    return (f'<p style="font-size:33px; margin-top:34px">{label}</p>'
            f'<div style="height:64px; border-bottom:3px dashed var(--mu); opacity:.7"></div>')

B.append((D, '<h2>Pensa na sua última prova ruim.</h2>'
    + blank("1. O pace caiu em que trecho? Na subida? No retorno? E a frase, qual foi?")
    + blank("2. Você já tinha ouvido essa? Em qual prova? No mesmo trecho?")
    + blank("3. Se fosse verdade, diria o quê sobre você?")
    + '<p class="mu" style="margin-top:40px">Se a 1 aparece na 2, a frase não estava lendo aquele dia. A 3 mostra de onde ela vem.</p>', False))

B.append((L, paraquem("Pra quem é, e pra quem não é.",
    "você reconhece a mesma frase em provas diferentes e quer entender de onde ela vem.",
    "a frase sobre você aparece todo dia, não só correndo, e anda pesada de carregar. Aí é com um psicólogo. Pace caindo com dor ou tontura: médico."), False))

B.append((D, '''<div style="margin-top:60px"></div>
<h1 style="font-size:76px">A prova muda toda vez.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">Se a frase não muda, ela não é sobre a prova.</h1>
<p class="mu" style="margin-top:44px; max-width:860px">Manda pra aquele amigo que termina toda prova repetindo a mesma frase sobre o km que deu errado.</p>
''' + cta_box("manda pra quem", "repete a frase", "“eu nunca aguento”", "a prova era outra"), True))

# =============================================================== VERSÃO C · capa escura · "A ou B?"
C = []
C.append((D, '''<div style="margin-top:20px"></div>
<h1 style="font-size:80px">Fim do treino. O pace caiu lá no meio. No caderno, vai o quê: A ou B?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:30px">
<rect x="10" y="40" width="410" height="300" rx="16" stroke="var(--ink)" stroke-width="4" transform="rotate(-2 215 190)"/>
<circle cx="60" cy="90" r="32" stroke="var(--pen)" stroke-width="4"/>
<text x="60" y="104" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)">A</text>
<text x="110" y="104" font-family="Inter" font-weight="700" font-size="28" fill="var(--ink)">o pace</text>
<path d="M50,170 L380,170 M50,290 L380,290" stroke="var(--line)" stroke-width="2"/>
<path d="M50,190 L150,194 L210,200 C240,210 260,250 290,262 L380,272" stroke="var(--ink)" stroke-width="4"/>
<text x="230" y="320" font-family="Pen" font-size="30" fill="var(--mu)">caiu aqui ↑</text>
<rect x="468" y="40" width="410" height="300" rx="16" stroke="var(--ink)" stroke-width="4" transform="rotate(2 673 190)"/>
<circle cx="520" cy="94" r="32" stroke="var(--pen)" stroke-width="4"/>
<text x="520" y="108" text-anchor="middle" font-family="Pen" font-size="44" fill="var(--pen)">B</text>
<text x="570" y="108" font-family="Inter" font-weight="700" font-size="28" fill="var(--ink)">a frase</text>
<text x="500" y="200" font-family="Pen" font-size="40" fill="var(--ink)">“não sou corredor</text>
<text x="500" y="250" font-family="Pen" font-size="40" fill="var(--ink)">de verdade”</text>
</svg>''', True))

C.append((L, f'''<h2>Se você anotou só a A, ficou faltando metade.</h2>
<p style="margin-top:34px">Repara: o relógio já guardou o pace inteiro. {hl("A frase que veio junto, não.")}</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:40px">
<rect x="244" y="10" width="400" height="400" rx="10" stroke="var(--ink)" stroke-width="5"/>
<rect x="270" y="40" width="348" height="150" rx="6" stroke="var(--ink)" stroke-width="3"/>
<path d="M290,60 L300,20 M330,56 L336,8 M370,58 L384,14 M420,56 L420,4 M460,58 L476,12 M510,56 L518,10 M560,58 L566,18 M590,60 L604,26" stroke="var(--mu)" stroke-width="3"/>
<rect x="404" y="108" width="80" height="16" rx="8" stroke="var(--ink)" stroke-width="3"/>
<text x="444" y="168" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--ink)">PACE</text>
<path d="M270,230 L618,230 L618,380 L270,380 Z" stroke="var(--pen)" stroke-width="3"/>
<path d="M252,214 L636,214 L640,250 L248,250 Z" stroke="var(--pen)" stroke-width="4"/>
<text x="444" y="290" text-anchor="middle" font-family="Inter" font-weight="800" font-size="24" fill="var(--pen)">FRASES</text>
<path d="M290,300 L340,330 M290,330 L340,300" stroke="var(--mu)" stroke-width="2" opacity=".6"/>
<text x="444" y="350" text-anchor="middle" font-family="Pen" font-size="40" fill="var(--mu)">vazia</text>
<text x="20" y="110" font-family="Pen" font-size="34" fill="var(--mu)">lotada</text>
<path d="M120,100 L236,104" stroke="var(--mu)" stroke-width="2"/>
</svg>
<div class="note" style="margin-top:6px; transform:rotate(-2deg)">e é a frase que corre o km seguinte.</div>''', False))

C.append((D, quiz(1, "Quando a frase chegou? Depois de você pensar? Ou antes?",
    "Antes. Rápida, sem esforço, já com cara de verdade. Por isso passa sem você questionar.") + '''
<svg class="draw" width="888" height="300" viewBox="0 0 888 300" style="margin-top:40px">
<path d="M20,140 L868,140" stroke="var(--mu)" stroke-width="3"/>
<path d="M854,128 L870,140 L854,152" stroke="var(--mu)" stroke-width="3"/>
<circle cx="60" cy="140" r="12" style="fill:var(--ink); stroke:none"/>
<text x="40" y="100" font-family="Pen" font-size="34" fill="var(--ink)">bip: o pace caiu</text>
<circle cx="110" cy="140" r="14" style="fill:var(--pen); stroke:none"/>
<path d="M110,160 L110,200" stroke="var(--pen)" stroke-width="3"/>
<text x="70" y="240" font-family="Pen" font-size="38" fill="var(--pen)">a frase, já</text>
<circle cx="780" cy="140" r="12" stroke="var(--ink)" stroke-width="4"/>
<text x="780" y="100" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--ink)">você pensa</text>
<path d="M130,180 C300,200 600,200 770,180" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 10"/>
<text x="420" y="280" text-anchor="middle" font-family="Pen" font-size="34" fill="var(--mu)">aqui, o próximo passo já foi com ela</text>
</svg>''', False))

C.append((L, quiz(2, "Dá pra saber de onde ela vem? Com uma pergunta só?",
    "Dá. Pergunta assim: %s Cada resposta desce um degrau." % hl("“se isso fosse verdade, o que diria sobre mim?”")) + '''
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:30px">
<path d="M30,10 L30,320" stroke="var(--mu)" stroke-width="3"/>
<path d="M18,300 L30,320 L42,300" stroke="var(--mu)" stroke-width="3"/>
<path d="M60,70 L290,70 L290,170 L560,170 L560,270 L870,270" stroke="var(--ink)" stroke-width="5"/>
<text x="70" y="56" font-family="Pen" font-size="34" fill="var(--mu)">o pace caiu</text>
<text x="300" y="156" font-family="Pen" font-size="34" fill="var(--ink)">“não sou corredor de verdade”</text>
<text x="570" y="256" font-family="Pen" font-size="34" fill="var(--pen)">“meu valor é o resultado”</text>
<path d="M220,90 C250,120 260,130 280,140 M268,128 L282,142 L264,146" stroke="var(--pen)" stroke-width="3"/>
<path d="M490,190 C520,220 530,230 550,240 M538,228 L552,242 L534,246" stroke="var(--pen)" stroke-width="3"/>
<text x="50" y="250" font-family="Inter" font-size="22" fill="var(--mu)">mais fundo</text>
</svg>''', False))

C.append((D, quiz(3, "E escrever? Não deixa a frase mais forte?",
    "Pois é, acontece o contrário. No papel, ela perde o tom de verdade e vira um texto que você pode revisar.") + '''
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:40px">
<rect x="0" y="20" width="888" height="290" rx="8" stroke="var(--mu)" stroke-width="2"/>
<text x="40" y="170" font-family="Pen" font-size="54" fill="var(--ink)">não sou corredor de verdade</text>
<ellipse cx="492" cy="150" rx="84" ry="44" stroke="var(--pen)" stroke-width="4" transform="rotate(-3 492 150)"/>
<path d="M530,108 C560,84 590,76 620,74" stroke="var(--pen)" stroke-width="3"/>
<text x="630" y="80" font-family="Pen" font-size="34" fill="var(--pen)">segundo quem?</text>
<path d="M150,190 C150,230 170,240 200,248" stroke="var(--pen)" stroke-width="3"/>
<text x="210" y="262" font-family="Pen" font-size="34" fill="var(--pen)">em todo treino? ou só nesse km?</text>
</svg>''', False))

C.append((L, '''<div style="margin-top:110px"></div>
<h1 style="font-size:76px">Anotar o pace mostra o que aconteceu.</h1>
<h1 class="or" style="font-size:76px; margin-top:22px">Anotar a frase mostra quem estava correndo.</h1>''', False))

def check(t):
    return ('<div style="display:flex; gap:26px; align-items:flex-start; margin-top:30px">'
            '<svg class="draw" width="44" height="44" viewBox="0 0 44 44" style="flex:none; margin-top:4px">'
            '<rect x="3" y="3" width="38" height="38" rx="6" stroke="var(--pen)" stroke-width="3"/></svg>'
            f'<p style="font-size:34px">{t}</p></div>')

C.append((D, '<h2 style="margin-bottom:16px">Marca o que já aconteceu com você.</h2>'
    + check("O pace caiu e veio uma frase sobre você. Na subida? No retorno? No fim?")
    + check("Era a mesma frase de outra prova. Lembra qual?")
    + check("Você acreditou nela sem perguntar nada.")
    + check("O km seguinte foi pior que o anterior.")
    + check("Você anotou o pace, mas não a frase.")
    + '<p class="mu" style="margin-top:44px">Cada marca é um km em que a frase correu sem ser conferida.</p>', False))

C.append((L, paraquem("Pra quem é, e pra quem não é.",
    "você registra tudo do treino, menos o que passou pela cabeça no km em que o pace caiu.",
    "o que você pensa sobre si mesmo pesa fora da corrida também, a ponto de atrapalhar a rotina. Aí procure um psicólogo. Pace caindo com dor: médico ou fisioterapeuta."), False))

C.append((D, '''<div style="margin-top:50px"></div>
<h1 style="font-size:76px">O seu relógio já fez a parte dele.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">A frase é a parte que falta no caderno.</h1>
<p class="mu" style="margin-top:40px; max-width:860px">Comenta aqui: A ou B, o que você anotou no último treino? E manda pra aquele amigo que anota tudo, menos a frase.</p>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:30px">
<rect x="20" y="40" width="54" height="54" rx="8" stroke="var(--mu)" stroke-width="3"/>
<path d="M30,66 L44,82 L68,48" stroke="var(--mu)" stroke-width="5"/>
<text x="96" y="80" font-family="Pen" font-size="38" fill="var(--mu)">A · o pace</text>
<text x="96" y="122" font-family="Pen" font-size="28" fill="var(--mu)">(o relógio já fez)</text>
<rect x="470" y="40" width="54" height="54" rx="8" stroke="var(--pen)" stroke-width="4" style="fill:var(--hl)"/>
<text x="546" y="80" font-family="Pen" font-size="42" fill="var(--pen)">B · a frase</text>
<path d="M800,150 C760,170 640,170 560,120 M574,116 L558,118 L566,134" stroke="var(--pen)" stroke-width="3"/>
<text x="600" y="190" font-family="Pen" font-size="32" fill="var(--pen)">falta esta</text>
</svg>''', True))

VERSOES = {"A": A, "B": B, "C": C}

LEGENDAS = {"A": """Sabe aquela frase que aparece no meio do treino, quando o relógio vibra e o número não é o que você queria? Ela vem tão rápido que você nem percebe que ela chegou. Só sente o peso.

Repara numa coisa: ela não precisa de esforço nenhum pra aparecer. Você não escolhe pensar nela. E justamente por vir assim, sem pedir licença, ela parece verdade.

Um exercício pequeno pro próximo treino. Quando acabar, antes do banho, abre a nota do celular e faz duas linhas. Na primeira: o que o relógio mostrou. Na segunda: o que você disse pra você naquele trecho, com as palavras exatas.

Não precisa responder nada à frase. Nem discutir com ela. Só deixa as duas linhas uma embaixo da outra e lê de novo.

A primeira linha é um dado. A segunda é uma interpretação. Quando elas ficam lado a lado, fica mais fácil ver qual das duas decidiu o km seguinte.

Salva pra fazer isso no próximo treino em que o pace cair.

Quer olhar isso com calma, junto comigo? Tem uma avaliação sem custo esperando no perfil.""",
"B": """Já parou pra pensar que a voz que fala com você no pior trecho da prova quase nunca é nova?

Ela não comenta o vento, a subida ou a noite mal dormida. Ela comenta você. E usa as mesmas palavras de sempre, como se tivesse decorado.

Isso acontece porque essas frases não nascem na hora. Elas vêm de algo que você acredita sobre si mesmo e que quase nunca aparece inteiro. O que aparece é só a ponta: uma frase curta, rápida, que soa como fato.

Da próxima vez que ela vier, tenta só reconhecer: "olha ela aí de novo". Não precisa calar nem rebater. Reconhecer que é a mesma frase de outras provas já tira um pouco da cara de notícia que ela tem.

Depois, em casa, com calma, faz a pergunta que desce um nível: se isso fosse verdade, o que diria sobre mim? Repara se a resposta fala de um km ruim ou de você inteiro.

Manda pra quem sempre sai da prova contando a mesma história sobre o trecho em que tudo desandou.

No perfil tem um link: lá você faz, de graça, uma análise inteira de como a cabeça corre junto com você.""",
"C": """Olha o seu caderno de treino, ou o app onde você registra tudo. Tem distância, pace, frequência cardíaca, sensação de esforço, talvez até o tênis que usou.

Agora procura ali o que passou pela sua cabeça no trecho em que o ritmo caiu. Pois é. Provavelmente não tem nada.

O relógio cuida do número sozinho. Mas a frase que veio junto com ele, aquela que decidiu como foi o resto do treino, só fica registrada se você escrever.

Uma ideia simples: cria uma coluna nova na sua planilha. Pode chamar de "frase". Depois de cada treino em que o ritmo despencou, coloca nela as palavras exatas que vieram, sem arrumar.

Depois de algumas semanas, lê só essa coluna, de cima pra baixo. Se as frases se repetem em dias completamente diferentes, você já descobriu algo que nenhum gráfico ia mostrar.

Comenta aqui embaixo: A ou B? O que foi pro seu caderno no último treino?

E pra ir além da planilha, existe um diagnóstico completo te aguardando na bio, sem pagar nada."""}
