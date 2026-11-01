# -*- coding: utf-8 -*-
# p07 — "A prova não termina na chegada": a explicação que você repete na semana volta na próxima largada.
# A = pergunta para você (capa escura) · B = pergunta-enigma (capa escura) · C = A ou B? (capa clara)
import math
from base import *


def pen(x, y, s, size=38, color="var(--pen)", anchor="start", rot=0, extra=""):
    tr = ' transform="rotate(%s %d %d)"' % (rot, x, y) if rot else ""
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Pen" font-size="%d" fill="%s"%s%s>%s</text>' % (
        x, y, anchor, size, color, tr, extra, s)


def sans(x, y, s, size=24, color="var(--mu)", anchor="start", weight=700):
    return '<text x="%d" y="%d" text-anchor="%s" font-family="Inter" font-weight="%d" font-size="%d" fill="%s">%s</text>' % (
        x, y, anchor, weight, size, color, s)


def loops(x0, y0, x1, r=34, k=14, n=None):
    """linha que anda girando em laços (remoer)"""
    pts = []
    t = 0.0
    while True:
        x = x0 + k * t - r * math.sin(t)
        y = y0 - r * (1 - math.cos(t)) * 0.9
        if x > x1:
            break
        pts.append("%.1f,%.1f" % (x, y))
        t += 0.12
    return "M" + " L".join(pts)


def lab2(label, color, text, mt=34):
    return ('<div class="lab" style="color:%s; margin-top:%dpx; margin-bottom:6px">%s</div><p style="font-size:33px">%s</p>'
            % (color, mt, label, text))


# ====================================================================== VERSÃO A · capa escura
A = []

A.append(("dark", '''<div style="margin-top:20px"></div>
<h1>Segunda-feira, alguém pergunta: “e aí, a prova?”</h1>
<h1 class="or" style="margin-top:18px; font-size:60px; line-height:1.08">O que sai primeiro? O tempo? A desculpa? Qual frase, exatamente?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:60px">
<path d="M190,400 L190,40 C190,18 206,4 228,4 L660,4 C682,4 698,18 698,40 L698,400" stroke="var(--ink)" stroke-width="4"/>
<path d="M400,24 L488,24" stroke="var(--mu)" stroke-width="4"/>
<rect x="218" y="60" width="452" height="110" rx="18" stroke="var(--mu)" stroke-width="3"/>
%s
%s
<rect x="218" y="250" width="452" height="76" rx="38" stroke="var(--pen)" stroke-width="4"/>
<path d="M248,268 L248,308" stroke="var(--pen)" stroke-width="4"/>
<path d="M620,288 L650,288 M638,276 L652,288 L638,300" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M150,330 C120,310 110,290 130,274 M118,290 L130,272 L146,284" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % (sans(244, 100, "GRUPO DA CORRIDA", 20),
              pen(244, 148, "e aí, como foi domingo?", 36, "var(--ink)"),
              pen(20, 380, "você, aqui.", 38, "var(--pen)", rot=-4)), True))

A.append(("light", '''<h2>Essa frase não é um resumo. É o rascunho da próxima largada.</h2>
<p style="margin-top:34px">Repara nisso aqui: você vai repetir no trabalho, no grupo, em casa. E, mais do que tudo, %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
%s%s%s%s
<path d="M300,48 C360,30 420,62 480,44 C540,28 600,58 660,42 C720,30 780,52 840,40" stroke="var(--ink)" stroke-width="2"/>
<path d="M300,138 C360,120 420,152 480,134 C540,118 600,148 660,132 C720,120 780,142 840,130" stroke="var(--ink)" stroke-width="4"/>
<path d="M300,228 C360,210 420,242 480,224 C540,208 600,238 660,222 C720,210 780,232 840,220" stroke="var(--ink)" stroke-width="8"/>
<path d="M300,318 C360,300 420,332 480,314 C540,298 600,328 660,312 C720,300 780,322 840,310" stroke="var(--pen)" stroke-width="15"/>
%s
</svg>''' % (hl("sozinho, na sua cabeça"),
             sans(0, 52, "NO TRABALHO", 22), sans(0, 142, "NO GRUPO", 22), sans(0, 232, "EM CASA", 22),
             sans(0, 322, "NA SUA CABEÇA", 22, "var(--pen)"),
             pen(888, 400, "a mesma frase. cada vez mais funda.", 38, "var(--pen)", "end", -2)), False))

A.append(("dark", '''<h2>Agora escuta a causa que a frase dá.</h2>
<p style="margin-top:30px">“Sou ruim de prova” põe a causa em algo fixo, que mora em você. “Larguei forte demais” põe a causa numa escolha daquele dia, que tá na sua mão.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:10px">
<rect x="0" y="30" width="270" height="110" rx="14" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M284,85 L350,85 M336,72 L352,85 L336,98" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M580,85 L630,85 M616,72 L632,85 L616,98" stroke="var(--mu)" stroke-width="3"/>
%s%s
<rect x="0" y="230" width="270" height="110" rx="14" stroke="var(--pen)" stroke-width="4"/>
%s
<path d="M284,285 L350,285 M336,272 L352,285 L336,298" stroke="var(--pen)" stroke-width="3"/>
%s
<path d="M580,285 L630,285 M616,272 L632,285 L616,298" stroke="var(--pen)" stroke-width="3"/>
%s%s
%s
</svg>''' % (pen(135, 98, "“eu sou...”", 40, "var(--mu)", "middle"),
             sans(362, 94, "CAUSA FIXA", 24),
             pen(646, 80, "próxima prova:", 30, "var(--mu)"), pen(646, 118, "vai ser igual", 30, "var(--mu)"),
             pen(135, 298, "“eu fiz...”", 40, "var(--pen)", "middle"),
             sans(362, 294, "CAUSA QUE MUDA", 22, "var(--pen)"),
             pen(646, 280, "próxima prova:", 30), pen(646, 318, "depende do ajuste", 30),
             pen(0, 396, "a causa decide o que você espera da próxima.", 36, "var(--ink)", rot=-1)), False))

A.append(("light", '''<h2>Remoer gira. Refletir chega.</h2>
<p style="margin-top:30px">Sabe aquela cena que você passa e repassa sem tirar nada dela? Isso é remoer, e só estica o mal-estar. Refletir faz uma pergunta e %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M30,26 L40,10 L50,26 M854,370 L870,380 L854,390" stroke="var(--mu)" stroke-width="3"/>
<path d="%s" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M40,350 C200,346 300,170 470,120 C560,94 600,92 620,92" stroke="var(--pen)" stroke-width="5"/>
<circle cx="626" cy="92" r="10" style="fill:var(--pen); stroke:none"/>
%s
%s
%s
</svg>''' % (hl("para quando encontra a resposta"),
             loops(60, 352, 860, 30, 13),
             pen(640, 290, "remoer", 38, "var(--mu)"),
             pen(650, 104, "refletir: fecha", 38),
             '<text x="58" y="34" font-family="Inter" font-weight="700" font-size="20" fill="var(--mu)">O QUE DÁ PRA LEVAR PRO TREINO</text>',
             sans(870, 420, "DIAS DEPOIS DA PROVA →", 20, "var(--mu)", "end")), False))

A.append(("dark", '''<h2>Cada vez que você relembra a prova, ela é salva de novo.</h2>
<p style="margin-top:30px">Olha isso: em humanos ainda está em estudo, mas a ideia é que uma lembrança que volta fica instável e é guardada outra vez. Quem reconta %s.</p>
<svg class="draw" width="888" height="360" viewBox="0 0 888 360" style="margin-top:auto; margin-bottom:10px">
<rect x="94" y="10" width="700" height="300" rx="16" stroke="var(--ink)" stroke-width="4"/>
<path d="M94,66 L794,66" stroke="var(--ink)" stroke-width="3"/>
<circle cx="126" cy="38" r="8" stroke="var(--mu)" stroke-width="3"/><circle cx="154" cy="38" r="8" stroke="var(--mu)" stroke-width="3"/>
%s
%s%s
<rect x="400" y="210" width="190" height="64" rx="12" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
%s
<rect x="606" y="210" width="160" height="64" rx="12" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M520,256 L520,318 L534,304 L546,330 L556,326 L544,300 L562,300 Z" style="fill:var(--ink)" stroke="var(--bg)" stroke-width="3"/>
</svg>''' % ("participa do que fica",
             sans(444, 46, "a prova de domingo", 22, "var(--mu)", "middle"),
             sans(130, 124, "Esse arquivo já existe.", 28, "var(--ink)"),
             sans(130, 168, "Substituir pela versão que você contou agora?", 26, "var(--ink)", weight=400),
             sans(495, 252, "Substituir", 26, "var(--ink)", "middle"),
             sans(686, 252, "Cancelar", 26, "var(--mu)", "middle", 400)), False))

A.append(("light", '''<div style="margin-top:150px"></div>
<h1 style="font-size:78px">A prova acabou na linha de chegada.</h1>
<h1 class="or" style="font-size:78px; margin-top:26px">A frase que você repete corre a próxima junto com você.</h1>''', False))

A.append(("dark", qs("Faz agora, com a sua última prova.", [
    ("Qual frase você mais repetiu? Pra quem? Onde?", "No carro, no grupo do WhatsApp, no café de segunda, no banho. Escreve do jeito que saiu."),
    ("Ela fala de quem você é? Ou do que você fez? Em que trecho?", "“Sou ruim de prova” ou “acelerei na primeira subida”, “pulei o gel”, “larguei colado no pelotão rápido”."),
    ("Ela termina em algo pro próximo treino? Qual treino? O que muda nele?", "Se não termina em nada, ela ainda está girando.")]), False))

A.append(("light", paraquem("Pra quem é isso, e pra quem não é.",
    "você termina uma prova ruim e passa a semana repetindo a mesma frase sobre ela, sem tirar nada de útil.",
    "o mal-estar não passa com as semanas, tira o seu sono ou aparece fora do esporte: procure um psicólogo. Se o que deu errado foi dor ou lesão, um médico ou fisioterapeuta."), False))

A.append(("dark", '''<div style="margin-top:40px"></div>
<h1 style="font-size:78px">A prova já terminou.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">A frase sobre ela, você ainda está escrevendo.</h1>
<p class="mu" style="margin-top:40px">Salva pra abrir na segunda depois da próxima prova, antes de responder “e aí, como foi?”.</p>
<svg class="draw" width="888" height="210" viewBox="0 0 888 210" style="margin-top:auto; margin-bottom:60px">
<rect x="40" y="70" width="640" height="84" rx="42" stroke="var(--pen)" stroke-width="4"/>
%s
<circle cx="740" cy="112" r="40" style="fill:var(--pen); stroke:none"/>
<path d="M722,112 L758,112 M744,98 L760,112 L744,126" stroke="#140C06" stroke-width="5"/>
%s
<path d="M620,40 C660,30 700,40 720,62 M704,58 L722,66 L724,46" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % (pen(76, 124, "larguei forte demais. dá pra ajustar.", 36, "var(--ink)"),
             pen(380, 40, "salva pra essa hora", 36, "var(--pen)", rot=-2)), True))


# ====================================================================== VERSÃO B · capa escura
B = []

B.append(("dark", '''<div style="margin-top:20px"></div>
<h1>Já parou pra pensar por que uma prova de uma manhã ocupa a semana inteira?</h1>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:60px">
<path d="M150,300 L888,250 L888,372 L150,316 Z" style="fill:var(--mu); fill-opacity:.28; stroke:none"/>
<path d="M0,316 L888,316" stroke="var(--mu)" stroke-width="3"/>
<path d="M120,316 L120,260" stroke="var(--ink)" stroke-width="4"/>
<rect x="60" y="180" width="120" height="86" rx="6" stroke="var(--ink)" stroke-width="4" transform="rotate(-4 120 223)"/>
<circle cx="76" cy="196" r="4" style="fill:var(--ink); stroke:none"/><circle cx="164" cy="190" r="4" style="fill:var(--ink); stroke:none"/>
%s
%s
%s
<path d="M70,130 C80,110 100,100 118,112 M104,100 L120,114 L100,120" stroke="var(--mu)" stroke-width="3"/>
%s
</svg>''' % (sans(120, 236, "a prova", 22, "var(--ink)", "middle"),
             pen(0, 90, "a prova", 34, "var(--mu)"),
             pen(840, 300, "o que você diz sobre ela", 40, "var(--pen)", "end", -2),
             pen(840, 410, "e ela continua crescendo →", 30, "var(--mu)", "end")), True))

B.append(("light", '''<h2>Porque a prova tem hora pra acabar. A explicação, não.</h2>
<p style="margin-top:30px">Ela vai com você no carro, no almoço, no grupo de corrida. E se liga nessa parte: cada vez que sai, %s.</p>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:auto; margin-bottom:0">
<path d="M60,10 L440,10 L440,440 L420,456 L400,440 L380,456 L360,440 L340,456 L320,440 L300,456 L280,440 L260,456 L240,440 L220,456 L200,440 L180,456 L160,440 L140,456 L120,440 L100,456 L80,440 L60,456 Z" stroke="var(--ink)" stroke-width="3" transform="rotate(-2 250 230)"/>
<g transform="rotate(-2 250 230)" font-family="Inter" font-size="21" fill="var(--ink)">
<text x="250" y="52" text-anchor="middle" font-weight="800">CUPOM</text>
<path d="M84,74 L416,74" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 8"/>
<text x="84" y="112">a prova</text><text x="416" y="112" text-anchor="end">1 manhã</text>
<text x="84" y="158">explicação no carro</text><text x="416" y="158" text-anchor="end">+</text>
<text x="84" y="198">explicação no almoço</text><text x="416" y="198" text-anchor="end">+</text>
<text x="84" y="238">explicação no grupo</text><text x="416" y="238" text-anchor="end">+</text>
<text x="84" y="278">explicação no banho</text><text x="416" y="278" text-anchor="end">+</text>
<text x="84" y="318">explicação de madrugada</text><text x="416" y="318" text-anchor="end">+</text>
<path d="M84,344 L416,344" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 8"/>
<text x="84" y="392" font-weight="800" font-size="26">TOTAL</text><text x="416" y="392" text-anchor="end" font-weight="800" font-size="26" fill="var(--pen)">a semana</text>
</g>
%s%s
<path d="M560,250 C520,280 490,330 470,380 M462,360 L470,384 L490,368" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % (hl("mexe no que você espera da próxima"),
             pen(500, 170, "a conta que", 44, "var(--pen)", rot=-3),
             pen(500, 222, "você não pediu", 44, "var(--pen)", rot=-3)), False))

B.append(("dark", '''<h2>O tempo final não é o que pesa.</h2>
%s%s
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:auto; margin-bottom:10px">
<path d="M60,120 L828,120" stroke="var(--ink)" stroke-width="10"/>
<path d="M60,100 L60,140 M828,100 L828,140" stroke="var(--ink)" stroke-width="4"/>
<rect x="140" y="88" width="44" height="64" rx="10" style="fill:var(--ink)" stroke="var(--ink)" stroke-width="3"/>
%s%s
%s%s%s
%s%s%s
<path d="M162,180 C150,240 180,270 230,286" stroke="var(--pen)" stroke-width="3"/>
%s
</svg>''' % (lab2("parece", "var(--mu)", "Que a frustração vem do número que apareceu no relógio.", 30),
             lab2("acontece", "var(--pen)", "Pesa a causa que você dá pra ele. Causa fixa faz a próxima prova parecer decidida. Causa que muda deixa a próxima em aberto."),
             sans(60, 60, "FIXA", 24), sans(828, 60, "MUDA", 24, "var(--pen)", "end"),
             pen(60, 210, "sempre", 34, "var(--mu)"), pen(60, 250, "nunca", 34, "var(--mu)"), pen(60, 290, "eu sou", 34, "var(--mu)"),
             pen(828, 210, "hoje", 34, "var(--pen)", "end"), pen(828, 250, "dessa vez", 34, "var(--pen)", "end"), pen(828, 290, "eu fiz", 34, "var(--pen)", "end"),
             pen(240, 300, "onde está a sua explicação?", 36, "var(--pen)", rot=-2)), False))

B.append(("light", '''<h2>Voltar à prova a semana toda não é levar a sério.</h2>
%s%s
<svg class="draw" width="888" height="380" viewBox="0 0 888 380" style="margin-top:auto; margin-bottom:0">
<path d="M40,10 L40,320 L870,320" stroke="var(--mu)" stroke-width="3"/>
<path d="M30,26 L40,10 L50,26 M854,310 L870,320 L854,330" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,300 L70,90 L110,120 L150,80 L200,112 L250,78 L300,110 L360,72 L420,104 L480,70 L540,100 L600,66 L660,98 L720,64 L780,96 L850,62" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,300 L80,60 C110,40 130,140 170,220 C220,290 400,296 860,298" stroke="var(--pen)" stroke-width="5"/>
%s%s
<text x="58" y="34" font-family="Inter" font-weight="700" font-size="20" fill="var(--mu)">TEMPO DE CABEÇA NA PROVA</text>
%s
</svg>''' % (lab2("parece", "var(--mu)", "Que ficar remoendo a prova é ser exigente com você.", 26),
             lab2("acontece", "var(--pen)", "Pois é: girar em volta do erro sem chegar a lugar nenhum só estica o mal-estar. Refletir é olhar uma vez, de propósito, e sair com algo.", 20),
             pen(560, 50, "remoer", 36, "var(--mu)"),
             pen(260, 266, "refletir: olha, aprende, solta", 36),
             sans(870, 362, "DIAS DEPOIS DA PROVA →", 20, "var(--mu)", "end")), False))

B.append(("dark", '''<h2>A lembrança da prova não fica quietinha na gaveta.</h2>
%s%s
<svg class="draw" width="888" height="330" viewBox="0 0 888 330" style="margin-top:auto; margin-bottom:10px">
<path d="M120,120 L840,120 L760,300 L40,300 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M80,210 L800,210" stroke="var(--mu)" stroke-width="2" stroke-dasharray="6 10"/>
%s
%s
<path d="M200,184 L460,170" stroke="var(--mu)" stroke-width="3"/>
<path d="M60,120 L60,10" stroke="var(--ink)" stroke-width="4"/>
<rect x="0" y="10" width="300" height="70" rx="6" stroke="var(--pen)" stroke-width="4"/>
%s
</svg>''' % (lab2("parece", "var(--mu)", "Que a memória guarda a prova do jeito que ela foi.", 26),
             lab2("acontece", "var(--pen)", "A ideia, ainda em estudo em humanos: quando volta, a lembrança fica instável e é guardada de novo, com o que você disse junto.", 20),
             pen(190, 182, "larguei forte", 36, "var(--mu)", rot=-3),
             pen(260, 270, "eu nunca aguento", 46, "var(--pen)", rot=-2),
             pen(150, 56, "fresco de novo", 34, "var(--pen)", "middle")), False))

B.append(("light", '''<div style="margin-top:150px"></div>
<h1 style="font-size:78px">A prova acontece uma vez.</h1>
<h1 class="or" style="font-size:78px; margin-top:26px">A explicação, você repete até ela virar expectativa.</h1>''', False))

B.append(("dark", qs("Pega a sua última prova ruim.", [
    ("O que você disse logo depois da chegada? Pra quem?", "No funil da chegada, na foto com o grupo, na mensagem pra casa. A primeira frase."),
    ("E hoje, o que você diria? A mesma frase? Outra?", "Se alguém perguntasse agora, no treino de amanhã, no café."),
    ("Ela foi de “eu fiz” pra “eu sou”? Em que dia virou?", "Se “errei a largada” virou “eu sou assim”, ela endureceu no caminho.")]), False))

B.append(("light", paraquem("Pra quem é isso, e pra quem não é.",
    "depois de uma prova ruim, a cabeça volta para ela muito mais vezes do que a explicação precisa.",
    "a prova deixou dor que não passa: procure um médico ou fisioterapeuta. Se o peso dela se mistura com o resto da vida e não vai embora com as semanas, um psicólogo."), False))

B.append(("dark", '''<div style="margin-top:40px"></div>
<h1 style="font-size:78px">A prova coube numa manhã.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">A explicação não precisa ocupar a próxima largada.</h1>
<p class="mu" style="margin-top:40px">Manda pra aquele parceiro de treino que ainda tá explicando a prova de domingo até pra quem nem perguntou.</p>
<svg class="draw" width="888" height="220" viewBox="0 -10 888 220" style="margin-top:auto; margin-bottom:60px">
<path d="M60,20 L60,120 L80,104 L100,120 L120,104 L140,120 L160,104 L180,120 L200,104 L220,120 L240,104 L260,120 L280,104 L300,120 L320,104 L340,120 L360,104 L380,120 L400,104 L420,120 L440,104 L460,120 L460,20" stroke="var(--ink)" stroke-width="3"/>
%s
<path d="M40,150 L560,150" stroke="var(--pen)" stroke-width="3" stroke-dasharray="10 10"/>
<circle cx="600" cy="136" r="16" stroke="var(--pen)" stroke-width="4"/><circle cx="600" cy="170" r="16" stroke="var(--pen)" stroke-width="4"/>
<path d="M614,128 L680,158 M614,178 L680,146" stroke="var(--pen)" stroke-width="4"/>
%s
</svg>''' % (sans(260, 70, "TOTAL: a semana", 26, "var(--ink)", "middle", 800),
             pen(500, 30, "manda pra quem ainda", 32, "var(--pen)", rot=-2) + pen(500, 64, "está pagando", 32, "var(--pen)", rot=-2) + pen(500, 98, "essa conta", 32, "var(--pen)", rot=-2)), True))


# ====================================================================== VERSÃO C · capa clara
C = []

C.append(("light", '''<div style="margin-top:20px"></div>
<h1>Prova ruim no domingo. Segunda de manhã, você:</h1>
<svg class="draw" width="888" height="560" viewBox="0 0 888 560" style="margin-top:auto; margin-bottom:50px">
%s
<path d="M70,250 L90,470 L250,470 L270,250 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M56,250 L284,250" stroke="var(--ink)" stroke-width="5"/>
<path d="M130,290 L140,440 M170,290 L170,440 M210,290 L200,440" stroke="var(--mu)" stroke-width="2"/>
<path d="M120,236 L104,180 L140,150 L196,166 L224,140 L236,196 L214,236 Z" stroke="var(--ink)" stroke-width="4" style="fill:var(--bg)"/>
<path d="M130,186 L170,200 L208,176 M150,220 L196,206" stroke="var(--mu)" stroke-width="2"/>
%s
%s
<rect x="490" y="160" width="360" height="310" rx="10" stroke="var(--ink)" stroke-width="4"/>
<path d="M520,430 C560,380 600,420 640,360 C680,300 740,340 760,280 C780,220 820,240 830,200" stroke="var(--ink)" stroke-width="16" style="opacity:.85"/>
<path d="M524,436 C566,374 596,428 646,352 C690,296 734,350 764,274 C784,228 816,234 826,196" stroke="var(--pen)" stroke-width="3"/>
<path d="M516,426 C556,388 604,412 636,366 C676,306 746,334 756,286" stroke="var(--pen)" stroke-width="3"/>
%s
%s
</svg>''' % (pen(20, 70, "A", 90, "var(--pen)"),
             pen(170, 530, "esquece e segue", 38, "var(--ink)", "middle"),
             pen(460, 70, "B", 90, "var(--pen)"),
             pen(670, 530, "repassa cada km", 38, "var(--ink)", "middle"),
             pen(380, 340, "A ou B?", 48, "var(--pen)", "middle", -3)), True))

C.append(("dark", '''<h2>Nenhuma das duas. A pergunta certa é outra.</h2>
<p style="margin-top:30px">Repara: A apaga o que dava pra aprender. B, quando vira disco riscado, só estica o mal-estar. O que importa é %s.</p>
<svg class="draw" width="888" height="380" viewBox="0 0 888 380" style="margin-top:auto; margin-bottom:10px">
<rect x="150" y="30" width="520" height="300" rx="10" stroke="var(--ink)" stroke-width="4" transform="rotate(2 410 180)"/>
<g transform="rotate(2 410 180)">
<circle cx="176" cy="56" r="8" stroke="var(--mu)" stroke-width="3"/><circle cx="644" cy="56" r="8" stroke="var(--mu)" stroke-width="3"/>
<circle cx="176" cy="304" r="8" stroke="var(--mu)" stroke-width="3"/><circle cx="644" cy="304" r="8" stroke="var(--mu)" stroke-width="3"/>
%s
%s
<path d="M200,190 L620,190 M200,250 L620,250" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 10"/>
%s
</g>
%s
<path d="M760,240 C740,220 720,210 690,212 M704,200 L688,212 L704,224" stroke="var(--pen)" stroke-width="3"/>
</svg>''' % (hl("qual explicação você leva para a próxima largada"),
             sans(410, 100, "VERSO DO NÚMERO DE PEITO", 20, "var(--mu)", "middle"),
             pen(200, 160, "o que eu levo daqui:", 38, "var(--ink)"),
             pen(200, 240, "uma coisa que dá para mudar", 34, "var(--pen)"),
             pen(888, 300, "o lado que você", 32, "var(--pen)", "end") + pen(888, 336, "nunca usou", 32, "var(--pen)", "end")), False))

C.append(("light", '''<div class="lab or">Pergunta 1</div>
<h2>“Não nasci pra prova longa” ou “larguei rápido demais”. Qual muda a próxima largada?</h2>
<p style="margin-top:28px">A segunda. A primeira é causa fixa: se o motivo é você, a próxima vai ser igual. A segunda é uma escolha daquele dia. %s.</p>
<svg class="draw" width="888" height="300" viewBox="0 0 888 300" style="margin-top:auto; margin-bottom:0">
<path d="M150,110 L150,70 C150,10 270,10 270,70 L270,110" stroke="var(--mu)" stroke-width="8"/>
<rect x="110" y="110" width="200" height="140" rx="14" stroke="var(--mu)" stroke-width="5"/>
%s
<path d="M570,110 L570,70 C570,10 690,10 690,70 L690,110" stroke="var(--pen)" stroke-width="8"/>
<rect x="530" y="110" width="200" height="140" rx="14" stroke="var(--pen)" stroke-width="5"/>
<circle cx="630" cy="170" r="12" stroke="var(--pen)" stroke-width="4"/><path d="M630,182 L630,210" stroke="var(--pen)" stroke-width="4"/>
<circle cx="800" cy="180" r="26" stroke="var(--ink)" stroke-width="4"/><path d="M774,180 L650,180 M690,180 L690,200 M710,180 L710,196" stroke="var(--ink)" stroke-width="4"/>
%s%s
</svg>''' % ("E escolha se ajusta",
             pen(210, 196, "sem fechadura", 28, "var(--mu)", "middle"),
             pen(210, 290, "“não nasci pra isso”", 32, "var(--mu)", "middle"),
             pen(640, 290, "“larguei rápido”", 32, "var(--pen)", "middle")), False))

C.append(("dark", '''<div class="lab or">Pergunta 2</div>
<h2>Pensou na prova a semana toda? Todo dia? Sempre na mesma cena?</h2>
<p style="margin-top:28px">Então olha a direção. Remoer volta às mesmas perguntas e não fecha nenhuma. %s.</p>
<svg class="draw" width="888" height="400" viewBox="0 0 888 400" style="margin-top:auto; margin-bottom:0">
<path d="M40,10 L40,340 L870,340" stroke="var(--mu)" stroke-width="3"/>
<path d="M30,26 L40,10 L50,26 M854,330 L870,340 L854,350" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,80 C120,70 160,96 240,80 C320,64 360,94 440,78 C520,62 560,92 640,76 C720,62 780,86 860,74" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>
<path d="M40,80 L180,80 L180,150 L320,150 L320,220 L460,220 L460,290 L860,290" stroke="var(--pen)" stroke-width="5"/>
<path d="M180,80 L180,150 M320,150 L320,220 M460,220 L460,290" stroke="var(--pen)" stroke-width="5"/>
%s%s%s%s%s
%s
</svg>''' % ("Refletir fecha uma de cada vez",
             pen(640, 56, "remoer", 36, "var(--mu)"),
             pen(196, 136, "✓", 30), pen(336, 206, "✓", 30), pen(476, 276, "✓", 30),
             pen(560, 270, "refletir", 38),
             '<text x="58" y="34" font-family="Inter" font-weight="700" font-size="20" fill="var(--mu)">PERGUNTAS ABERTAS SOBRE A PROVA</text>' +
             sans(870, 384, "DIAS DEPOIS DA PROVA →", 20, "var(--mu)", "end")), False))

C.append(("light", '''<div class="lab or">Pergunta 3</div>
<h2>Na sexta, a prova de domingo ainda é a mesma? Igualzinha? Com as mesmas palavras?</h2>
<p style="margin-top:28px">Talvez não. A ideia, ainda em estudo em humanos, é que cada vez que volta, a lembrança é guardada de novo. %s.</p>
<svg class="draw" width="888" height="340" viewBox="0 0 888 340" style="margin-top:auto; margin-bottom:0">
<rect x="4" y="40" width="270" height="190" rx="6" stroke="var(--ink)" stroke-width="4" transform="rotate(-3 139 135)"/>
<rect x="309" y="50" width="270" height="190" rx="6" stroke="var(--ink)" stroke-width="3" stroke-dasharray="14 6" transform="rotate(2 444 145)"/>
<rect x="612" y="40" width="270" height="190" rx="6" stroke="var(--pen)" stroke-width="4" transform="rotate(-2 747 135)"/>
<g transform="rotate(-3 139 135)">%s%s%s</g>
<g transform="rotate(2 444 145)">%s%s%s</g>
<g transform="rotate(-2 747 135)">%s%s%s</g>
%s%s%s
</svg>''' % ("Quem conta, edita",
             sans(20, 76, "CÓPIA 1", 18), pen(20, 140, "larguei rápido", 34, "var(--ink)"), pen(20, 182, "demais", 34, "var(--ink)"),
             sans(329, 86, "CÓPIA 2", 18), pen(329, 150, "larguei rápido,", 34, "var(--ink)"), pen(329, 192, "como sempre", 34, "var(--ink)"),
             sans(632, 76, "CÓPIA 3", 18, "var(--pen)"), pen(632, 140, "eu sempre", 34), pen(632, 182, "faço isso", 34),
             pen(139, 300, "domingo", 32, "var(--mu)", "middle"), pen(444, 310, "terça", 32, "var(--mu)", "middle"),
             pen(747, 300, "sexta", 32, "var(--pen)", "middle")), False))

C.append(("dark", '''<div style="margin-top:150px"></div>
<h1 style="font-size:74px">Remoer pergunta: “por que eu sou assim?”</h1>
<h1 class="or" style="font-size:74px; margin-top:30px">Refletir pergunta: “o que eu mudo na próxima?”</h1>''', False))

BOX = '<svg width="44" height="44" viewBox="0 0 44 44" style="flex:none; margin-top:4px"><rect x="4" y="4" width="36" height="36" rx="6" fill="none" stroke="%s" stroke-width="3"/></svg>'
def chk(text, color="var(--ink)"):
    return '<div style="display:flex; gap:24px; align-items:flex-start; padding:22px 0; border-top:2px dashed var(--line)">%s<p style="font-size:34px; line-height:1.3">%s</p></div>' % (BOX % color, text)

C.append(("light", '''<h2 style="margin-bottom:30px">Marca o que aconteceu depois da sua última prova ruim.</h2>
%s%s%s
<div class="sep" style="margin:10px 0"></div>
%s
<div class="note" style="margin-top:auto; margin-bottom:10px; transform:rotate(-2deg); font-size:44px">mais marcas em cima do que embaixo?<br>a prova ainda está girando.</div>''' % (
    chk("Expliquei com “sempre”, “nunca” ou “eu sou”, no grupo ou em casa."),
    chk("Contei a mesma cena (a subida, o km que travou) várias vezes, sem tirar nada novo."),
    chk("Ela voltou na hora de dormir, no banho ou no trote seguinte."),
    chk("Anotei uma coisa que dá pra mudar no próximo treino.", "var(--pen)")), False))

C.append(("dark", paraquem("Pra quem é isso, e pra quem não é.",
    "você fecha a prova no relógio, mas não fecha na cabeça, e ela ainda está lá na largada seguinte.",
    "a semana depois da prova vem com dor ou lesão: médico ou fisioterapeuta. Se o mal-estar dura semanas e transborda para o trabalho, o sono ou a casa, procure um psicólogo."), False))

C.append(("light", '''<div style="margin-top:30px"></div>
<h1 style="font-size:78px">Correr de novo aquela prova, você não pode.</h1>
<h1 class="or" style="font-size:78px; margin-top:18px">Escolher o que leva dela, sim.</h1>
<p class="mu" style="margin-top:36px">Comenta aqui embaixo, A ou B: na sua última prova ruim, você esqueceu ou ficou repassando? E manda pra quem marcaria a outra letra.</p>
<svg class="draw" width="888" height="160" viewBox="0 0 888 160" style="margin-top:auto; margin-bottom:60px">
<rect x="0" y="40" width="888" height="90" rx="45" stroke="var(--ink)" stroke-width="3"/>
%s
<rect x="520" y="54" width="100" height="62" rx="31" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
<rect x="640" y="54" width="100" height="62" rx="31" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
%s%s
%s
</svg>''' % (sans(40, 96, "Adicione um comentário…", 26, "var(--mu)", weight=400),
             pen(570, 100, "A", 44, "var(--ink)", "middle"), pen(690, 100, "B", 44, "var(--ink)", "middle"),
             pen(800, 100, "?", 48, "var(--pen)")), True))

VERSOES = {"A": A, "B": B, "C": C}


LEGENDAS = {"A": """Repara quando nasce a primeira explicação da sua prova. Às vezes é no caminho do guarda-volumes, olhando o relógio, antes até de tirar o número de peito.

Ela sai cansada, com fome e com o corpo ainda quente. E é essa versão que você leva pra semana.

Uma coisa pequena pra testar depois da próxima prova: antes de mandar mensagem pra qualquer pessoa, abre o bloco de notas do celular e escreve três linhas.

1. O que aconteceu, sem adjetivo.
2. O que, naquele dia, estava na sua mão.
3. O que você testa no próximo treino.

Depois fecha a nota. Refletir tem hora pra começar e hora pra acabar. Se a cena voltar na quarta-feira, você já sabe onde está a resposta.

Salva pra lembrar disso no domingo da próxima prova, ainda com a medalha no pescoço.

Quer enxergar o seu padrão completo de competição? O diagnóstico gratuito mora no link da bio.""",

"B": """Já reparou no primeiro trote depois de uma prova ruim? Ritmo leve, você sozinho, fone sem música. É o cenário perfeito pra cabeça voltar pro km que deu errado e ficar lá, dando volta.

O corpo está se recuperando. A cabeça, nem sempre.

Testa isso no próximo regenerativo: antes de sair de casa, escolhe uma única pergunta sobre a prova. Uma só. Algo como "o que eu faria diferente na largada?".

Responde até o fim do aquecimento. Achou a resposta? Ótimo, guarda. Não achou? Anota a pergunta e deixa pra depois do banho.

O resto do treino é sobre o treino: respiração, passada, o barulho do tênis no asfalto. Se a prova voltar, você já sabe que ela tem horário marcado e não é agora.

Manda pra aquele parceiro do grupo que, no trote de recuperação, só fala da prova passada.

E se quiser destrinchar o seu caso de ponta a ponta, tem uma avaliação inteira, sem custo, esperando no link da bio.""",

"C": """Uma cena que passa batida: o campo de descrição da atividade no app de corrida, logo depois da prova.

O que você escreve ali vira registro. E é ele que aparece quando você rola o histórico na véspera da próxima largada.

"Dia horrível, corpo não respondeu" é uma descrição. "Larguei no ritmo de prova curta, paguei no fim" é outra. Os dois textos contam a mesma manhã. Só um deles te dá algo pra fazer na próxima.

Exercício pra próxima prova: escreve a descrição como se fosse ler ela de novo três dias antes de largar outra vez. Uma linha sobre o que aconteceu, uma sobre o que você ajusta. Sem "sempre" e sem "nunca".

Se a prova foi boa, faz igual. Registro bom não serve só pra prova ruim.

Comenta aqui embaixo: A ou B? E, se for B, conta qual cena você mais repassou.

Pra ir mais fundo no seu jeito de competir, tem diagnóstico liberado, de graça, no link da bio."""}
