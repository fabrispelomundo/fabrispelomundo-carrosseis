# -*- coding: utf-8 -*-
# p05 — a versão oficial × a parte que vaza no cansaço. 3 versões (A escura, B clara, C escura).
from base import *

def T(x, y, txt, size=38, col="var(--ink)", anchor="start", rot=0, fam="Pen", weight=None):
    a = ' text-anchor="%s"' % anchor if anchor != "start" else ""
    r = ' transform="rotate(%s %d %d)"' % (rot, x, y) if rot else ""
    w = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%d" y="%d"%s font-family="%s"%s font-size="%d" fill="%s"%s>%s</text>' % (x, y, a, fam, w, size, col, r, txt)

def face(cx, cy, r=34, col="var(--ink)", mood="smile", sw=4):
    s = '<circle cx="%d" cy="%d" r="%d" stroke="%s" stroke-width="%d"/>' % (cx, cy, r, col, sw)
    s += '<circle cx="%d" cy="%d" r="3.5" style="fill:%s; stroke:none"/><circle cx="%d" cy="%d" r="3.5" style="fill:%s; stroke:none"/>' % (cx - r * .35, cy - r * .15, col, cx + r * .35, cy - r * .15, col)
    if mood == "smile":
        s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="%d"/>' % (cx - r * .45, cy + r * .25, cx, cy + r * .7, cx + r * .45, cy + r * .25, col, sw - 1)
    else:
        s += '<path d="M%d,%d Q%d,%d %d,%d" stroke="%s" stroke-width="%d"/>' % (cx - r * .4, cy + r * .5, cx, cy + r * .2, cx + r * .4, cy + r * .5, col, sw - 1)
    return s

# ====================================================================== VERSÃO A · escura · "pergunta para você"
A = []

POLA = '''<g transform="rotate(-4 230 190)">
<rect x="60" y="20" width="340" height="360" rx="6" stroke="var(--ink)" stroke-width="4"/>
<rect x="88" y="46" width="284" height="240" stroke="var(--mu)" stroke-width="3"/>
%s
<path d="M230,176 L230,246 M230,196 L190,170 M230,196 L268,160 L262,140 M262,140 L272,142 M230,246 L200,284 M230,246 L262,284" stroke="var(--ink)" stroke-width="4"/>
%s
</g>''' % (face(230, 136, 30), T(230, 340, "a foto da prova", 34, "var(--mu)", "middle"))

A.append(("dark", '''<div style="margin-top:30px"></div>
<h1>O pior km da sua última prova.</h1>
<h1 class="or" style="margin-top:18px; font-size:60px; line-height:1.1">O que passou pela sua cabeça ali? E pra quem você contou?</h1>
<svg class="draw" width="888" height="400" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:30px">
%s
<path d="M410,170 C470,150 500,150 540,160 M522,146 L542,160 L522,174" stroke="var(--pen)" stroke-width="4"/>
%s%s
<path d="M560,206 L870,206 M560,262 L870,262 M560,318 L840,318" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>
%s
</svg>''' % (POLA, T(560, 110, "o que passava", 40, "var(--pen)", rot=-2), T(560, 152, "na sua cabeça:", 40, "var(--pen)", rot=-2), T(880, 396, "a foto não mostra.", 38, "var(--ink)", "end", -2)), True))

A.append(("light", '''<h2>Pois é. Essa frase não combina com a sua bio.</h2>
<p style="margin-top:36px">Você é quem acorda cedo, cumpre a planilha e não reclama. Por isso ela pareceu %s.</p>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:auto; margin-bottom:10px">
<rect x="40" y="10" width="380" height="450" rx="40" stroke="var(--ink)" stroke-width="4"/>
<path d="M190,34 L270,34" stroke="var(--ink)" stroke-width="4"/>
<circle cx="120" cy="120" r="44" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M70,186 L390,186" stroke="var(--mu)" stroke-width="2"/>
%s%s%s
<rect x="70" y="350" width="150" height="54" rx="14" stroke="var(--pen)" stroke-width="3"/>
%s
<path d="M440,250 C520,230 560,260 600,300 M584,300 L602,302 L600,284" stroke="var(--pen)" stroke-width="4"/>
%s%s%s
</svg>''' % (hl("de outra pessoa"), T(186, 112, "você", 40, "var(--ink)"), T(70, 236, "acordo antes do sol", 34), T(70, 280, "planilha em dia", 34), T(70, 324, "sem desculpa", 34), T(145, 386, "seguir", 30, "var(--pen)", "middle"),
     T(470, 360, "e o que pensou", 40, "var(--pen)", rot=-3), T(470, 404, "no km difícil?", 40, "var(--pen)", rot=-3), T(470, 448, "não cabe aqui.", 36, "var(--mu)", rot=-3)), False))

FORA = [(30, 70, "irritação"), (650, 60, "medo"), (20, 400, "vontade de parar"), (640, 400, "inveja")]
fora = "".join(T(x, y, t, 38, "var(--mu)") for x, y, t in FORA)
A.append(("dark", '''<h2>Essa versão de você não é mentira.</h2>
<p style="margin-top:36px">Ela te tirou da cama e te fez cumprir a planilha. Só que, pra ela ficar firme, algumas partes suas %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<rect x="250" y="90" width="388" height="260" rx="8" stroke="var(--ink)" stroke-width="5"/>
<rect x="270" y="110" width="348" height="220" stroke="var(--ink)" stroke-width="2"/>
%s%s%s
%s
%s
<path d="M200,90 L244,120 M720,80 L644,120 M240,380 L270,340 M770,370 L630,340" stroke="var(--mu)" stroke-width="2" stroke-dasharray="3 10"/>
</svg>''' % (hl("ficaram fora da foto"), T(444, 180, "acordar cedo", 38, "var(--pen)", "middle"), T(444, 238, "cumprir tudo", 38, "var(--pen)", "middle"), T(444, 296, "aguentar firme", 38, "var(--pen)", "middle"),
     T(444, 384, "dentro da foto", 26, "var(--ink)", "middle", fam="Inter", weight=800), fora), False))

A.append(("light", '''<h2>No cansaço, o controle cai.</h2>
<p style="margin-top:36px">Repara nisso aqui: quanto mais firme a imagem, menos espaço sobra pro resto. Aí ele aparece de surpresa, e parece %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,70 C260,74 420,110 520,180 C620,250 720,320 860,340" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M40,350 C300,348 440,330 540,250 C640,170 740,100 860,60" stroke="var(--pen)" stroke-width="5"/>
%s
<circle cx="560" cy="228" r="40" stroke="var(--pen)" stroke-width="3" stroke-dasharray="6 8"/>
%s
%s
</svg>''' % (hl("“não era eu”"), T(70, 56, "a força pra manter a imagem", 34, "var(--ink)"), T(740, 66, "o que ficou de fora", 36, "var(--pen)", "end"),
     T(505, 236, "aquele km", 38, "var(--pen)", "end", -3), T(860, 420, "a prova avançando →", 22, "var(--mu)", "end", fam="Inter")), False))

A.append(("dark", '''<h2>Aí o cansaço pesa em dobro.</h2>
<p style="margin-top:36px">Imagina correr segurando a própria foto. Cada passo mais lento deixa de ser só perna. Vira %s.</p>
<svg class="draw" width="888" height="460" viewBox="0 0 888 460" style="margin-top:auto; margin-bottom:0">
<rect x="150" y="10" width="300" height="200" rx="6" stroke="var(--ink)" stroke-width="5" transform="rotate(-3 300 110)"/>
%s
<path d="M286,160 Q300,178 314,160" stroke="var(--ink)" stroke-width="3" transform="rotate(-3 300 110)"/>
%s
<path d="M200,216 L250,290 M400,206 L330,290" stroke="var(--ink)" stroke-width="4"/>
<path d="M290,300 L290,370 M290,370 L240,440 M290,370 L340,420 L330,450" stroke="var(--ink)" stroke-width="4"/>
<path d="M248,282 C230,260 226,252 232,240 M346,286 C362,264 366,256 360,244" stroke="var(--mu)" stroke-width="2"/>
<path d="M480,120 L540,120" stroke="var(--pen)" stroke-width="3"/>
%s%s
<path d="M480,390 L540,390" stroke="var(--pen)" stroke-width="3"/>
%s%s
</svg>''' % (hl("a imagem em risco"), face(300, 100, 46, "var(--ink)", "smile", 4).replace("<path", '<path transform="rotate(-3 300 110)"'),
     face(290, 266, 28, "var(--ink)", "tired", 4), T(560, 110, "peso 1: a foto", 40, "var(--pen)"), T(560, 152, "que precisa ficar bonita", 32, "var(--mu)"),
     T(560, 380, "peso 2: as pernas", 40, "var(--pen)"), T(560, 422, "que já estavam cansadas", 32, "var(--mu)")), False))

A.append(("light", '''<div style="margin-top:120px"></div>
<h1 style="font-size:76px">Você não virou outra pessoa naquele km.</h1>
<h1 class="or" style="font-size:76px; margin-top:26px">Só ficou sem força pra esconder uma parte sua.</h1>''', False))

A.append(("dark", qs("Pega a sua última prova dura.", [
    ("Em que km veio a frase? Na subida? Depois do último posto?", "No meio do pelotão, sozinho, na reta que não acabava."),
    ("O que ela dizia? Com que palavras?", "“Pra que eu inventei isso?”, “nunca mais”, “tomara que ele quebre”. Escreve a sua, sem arrumar."),
    ("E na hora, o que você fez com ela?", "Brigou, aumentou o som, acelerou pra calar. Ou só reparou?")]), False))

A.append(("light", paraquem("Pra quem é isso, e pra quem não é.",
    "você se cobra ser sempre o forte do grupo e, no fim da prova, estranha o que sentiu.",
    "essas reações aparecem também em casa ou no trabalho, ou se o km difícil vem com dor no peito, tontura ou confusão. Aí o caminho é um psicólogo ou um médico."), False))

A.append(("dark", '''<div style="margin-top:20px"></div>
<h1 style="font-size:76px">Da próxima vez, não briga com a frase.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">Anota. Ela também é sua.</h1>
<p class="mu" style="margin-top:36px">Salva pra reler na véspera da próxima prova longa.</p>
<svg class="draw" width="888" height="250" viewBox="0 0 888 250" style="margin-top:auto; margin-bottom:20px">
<path d="M40,20 L130,20 L130,200 L85,160 L40,200 Z" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
<path d="M150,110 C190,100 220,100 250,110 M234,96 L252,110 L234,124" stroke="var(--pen)" stroke-width="4"/>
<g transform="rotate(-3 560 120)">
<rect x="280" y="10" width="560" height="220" rx="6" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M310,130 L810,130 M310,190 L810,190" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 12"/>
</g>
</svg>''' % T(310, 70, "verso da foto · a frase daquele km:", 34, "var(--pen)"), True))

# ====================================================================== VERSÃO B · clara · "pergunta-enigma"
B = []
B.append(("light", '''<div style="margin-top:30px"></div>
<h1>Por que o mais calmo do grupo explode por um copo d'água?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:30px">
<path d="M60,330 L72,400 L108,400 L120,330 Z" stroke="var(--ink)" stroke-width="3"/>
<path d="M64,350 L116,350" stroke="var(--mu)" stroke-width="2"/>
%s
<path d="M140,350 C220,330 260,300 300,260" stroke="var(--mu)" stroke-width="3" stroke-dasharray="4 10"/>
<path d="M330,230 L360,60 L420,180 L480,20 L520,170 L600,40 L620,190 L720,80 L700,220 L860,170 L740,290 L870,360 L700,350 L720,430 L600,360 L520,430 L480,340 L380,410 L400,320 L310,330 Z" stroke="var(--pen)" stroke-width="5"/>
%s
</svg>''' % (T(90, 300, "copo morno", 28, "var(--ink)", "middle"), T(560, 230, "a reação", 44, "var(--ink)", "middle", -4)), True))

B.append(("dark", '''<h2>Não foi o copo.</h2>
<p style="margin-top:36px">E não foi só o cansaço. Se liga nessa parte: o cansaço tirou a força que você usava pra segurar um pedaço seu.</p>
<p>O pedaço que %s.</p>
<svg class="draw" width="888" height="380" viewBox="0 0 888 380" style="margin-top:auto; margin-bottom:10px">
<path d="M250,200 L250,340 C250,360 270,368 290,368 L598,368 C618,368 638,360 638,340 L638,200" stroke="var(--ink)" stroke-width="5"/>
<path d="M230,200 L658,200 M240,200 L250,186 L638,186 L648,200" stroke="var(--ink)" stroke-width="4"/>
<path d="M410,186 C410,160 478,160 478,186" stroke="var(--ink)" stroke-width="4"/>
<path d="M444,166 L444,120 C444,90 470,80 500,80 L560,80" stroke="var(--ink)" stroke-width="5"/>
<path d="M560,64 L610,64 C626,64 626,96 610,96 L560,96 Z" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M236,184 C210,160 230,140 206,116 M660,184 C690,160 668,138 694,112" stroke="var(--pen)" stroke-width="4"/>
<path d="M300,250 C340,230 380,270 420,250 M470,290 C510,270 550,310 590,290" stroke="var(--mu)" stroke-width="2"/>
%s
</svg>''' % (hl("não cabe em “sempre calmo”"), T(640, 92, "“sempre calmo”", 36, "var(--pen)"), T(40, 90, "a mão cansa.", 40, "var(--pen)", rot=-3)), False))

B.append(("light", '''<h2>Parece: a irritação veio de fora.</h2>
<p style="margin-top:36px">Acontece: ela tava com você desde a largada. Só ficava %s, longe da imagem que você mostra.</p>
<svg class="draw" width="888" height="450" viewBox="0 0 888 450" style="margin-top:auto; margin-bottom:10px">
<path d="M20,400 L868,400 M20,400 L20,80 L868,80 L868,400" stroke="var(--ink)" stroke-width="4"/>
<path d="M500,80 L500,400" stroke="var(--ink)" stroke-width="4"/>
<path d="M500,90 C480,140 520,190 490,240 C470,290 510,340 500,390" stroke="var(--pen)" stroke-width="3"/>
%s
<path d="M250,240 L250,320 M250,260 L200,220 M250,260 L300,220 M250,320 L220,390 M250,320 L280,390" stroke="var(--ink)" stroke-width="4"/>
%s%s
%s%s%s%s
%s
</svg>''' % (hl("no bastidor"), face(250, 200, 32), T(40, 60, "PALCO", 24, "var(--ink)", fam="Inter", weight=800), T(530, 60, "BASTIDOR", 24, "var(--mu)", fam="Inter", weight=800),
     T(540, 150, "irritação", 38, "var(--mu)"), T(560, 220, "vontade de parar", 36, "var(--mu)"), T(540, 290, "medo", 38, "var(--mu)"), T(660, 350, "inveja", 38, "var(--mu)"),
     T(60, 440, "mesmo prédio. mesma pessoa.", 40, "var(--pen)", rot=-2)), False))

B.append(("dark", '''<h2>Parece: imagem firme protege.</h2>
<p style="margin-top:36px">Acontece o contrário. Quanto mais rígida a imagem, menos espaço sobra pro resto. E ele volta %s quando o controle cai.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,380 L870,380" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,150 C300,170 560,250 860,330" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
%s
<path d="M40,330 C300,320 560,240 860,40" stroke="var(--pen)" stroke-width="5"/>
%s
%s%s
</svg>''' % (hl("de surpresa"), T(80, 140, "o que a gente espera", 36, "var(--ink)", rot=4), T(470, 140, "o que acontece", 42, "var(--pen)", rot=-12),
     T(860, 420, "imagem mais rígida →", 22, "var(--mu)", "end", fam="Inter"), T(60, 30, "↑ tamanho da surpresa", 22, "var(--mu)", fam="Inter")), False))

B.append(("light", '''<h2>Parece: o jeito é expulsar essa parte.</h2>
<p style="margin-top:36px">Acontece: segurar a porta também cansa. O outro caminho é deixar entrar e só olhar pra ela, %s.</p>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:10px">
<rect x="150" y="60" width="140" height="300" stroke="var(--ink)" stroke-width="4"/>
<path d="M150,360 L60,360" stroke="var(--ink)" stroke-width="4"/>
%s
<path d="M120,240 L120,300 M120,250 L150,220 M120,250 L150,270 M120,300 L80,360 M120,300 L100,360" stroke="var(--ink)" stroke-width="4"/>
%s%s
%s
<rect x="560" y="60" width="140" height="300" stroke="var(--ink)" stroke-width="4"/>
<path d="M560,60 L500,90 L500,384 L560,360" stroke="var(--ink)" stroke-width="3"/>
%s
<path d="M640,250 L640,310 M640,310 L620,360 M640,310 L660,360" stroke="var(--ink)" stroke-width="4"/>
<path d="M730,300 L800,300 M740,300 L740,360 M790,300 L790,360 M790,300 L790,250" stroke="var(--mu)" stroke-width="3"/>
<path d="M745,296 C735,270 750,240 770,240 C792,240 800,270 790,296 Z" style="fill:var(--hl)" stroke="var(--mu)" stroke-width="3"/>
%s
%s
</svg>''' % (hl("sem corrigir nem brigar"), face(120, 210, 28, "var(--ink)", "tired"), T(220, 140, "toc", 32, "var(--mu)", rot=10), T(230, 190, "toc", 32, "var(--mu)", rot=-8),
     T(170, 420, "expulsar", 44, "var(--ink)", "middle", -2), face(640, 220, 28), T(764, 210, "senta aí.", 34, "var(--pen)", "middle", -4), T(660, 420, "reconhecer", 44, "var(--pen)", "middle", -2)), False))

B.append(("dark", '''<div style="margin-top:120px"></div>
<h1 style="font-size:76px">Não foi o copo morno.</h1>
<h1 class="or" style="font-size:76px; margin-top:26px">Foi a parte que você passou a prova inteira segurando.</h1>''', False))

B.append(("light", qs("Lembra a última vez que você perdeu a paciência numa prova?", [
    ("Onde foi? No posto de água? Na largada? Na subida?", "O copo morno, o buraco, quem fechou você na curva."),
    ("Que imagem sua aquela reação contrariou?", "Calmo? Educado? Sempre de boa? Escreve a palavra que você usa pra se descrever."),
    ("E depois, o que você fez?", "Fingiu que não foi nada, contou rindo, pediu desculpa. Ou olhou pra aquilo como parte sua?")]), False))

B.append(("dark", paraquem("Pra quem é isso, e pra quem não é.",
    "você é o calmo do grupo e, no fim das provas longas, não reconhece as próprias reações.",
    "essa irritação aparece também fora da corrida, com frequência, e machuca você ou quem está perto. Aí o caminho é um psicólogo."), False))

B.append(("light", '''<div style="margin-top:20px"></div>
<h1 style="font-size:76px">O copo morno não explica a explosão.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">A imagem apertada explica.</h1>
<p class="mu" style="margin-top:36px">Manda pro amigo mais calmo do seu grupo de corrida. Ele sabe de que copo você tá falando.</p>
<svg class="draw" width="888" height="210" viewBox="0 0 888 210" style="margin-top:auto; margin-bottom:20px">
<path d="M60,40 L80,190 L150,190 L170,40 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M66,80 L164,80" stroke="var(--mu)" stroke-width="2"/>
<path d="M190,120 C280,90 360,90 440,110" stroke="var(--pen)" stroke-width="4" stroke-dasharray="6 12"/>
<path d="M460,110 L620,50 L560,170 L530,128 Z M530,128 L620,50" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
%s%s
</svg>''' % (T(650, 100, "pro mais calmo", 40, "var(--pen)", rot=-3), T(650, 146, "do grupo", 40, "var(--pen)", rot=-3)), True))

# ====================================================================== VERSÃO C · escura · "A ou B?"
C = []
C.append(("dark", '''<div style="margin-top:30px"></div>
<h1>Meio da subida. Vem a vontade de andar. E aí, A ou B?</h1>
<svg class="draw" width="888" height="440" viewBox="0 0 888 440" style="margin-top:auto; margin-bottom:30px">
%s
<path d="M90,110 C60,110 50,150 60,190 C70,240 110,250 150,240 L200,226 C230,218 236,180 220,150 C210,126 186,120 170,124 C160,100 120,96 100,108 Z" stroke="var(--ink)" stroke-width="4"/>
<path d="M150,240 L160,290 L220,280 L210,226" stroke="var(--ink)" stroke-width="4"/>
<path d="M250,160 L290,150 M250,190 L300,196 M246,130 L280,110" stroke="var(--pen)" stroke-width="3"/>
%s%s
<path d="M444,40 L444,400" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 12"/>
%s
<path d="M560,250 C560,140 760,140 760,250" stroke="var(--ink)" stroke-width="5"/>
<rect x="536" y="230" width="48" height="90" rx="20" stroke="var(--ink)" stroke-width="4"/>
<rect x="736" y="230" width="48" height="90" rx="20" stroke="var(--ink)" stroke-width="4"/>
<path d="M600,260 L620,250 M600,290 L624,290 M720,260 L700,250 M720,290 L696,290" stroke="var(--pen)" stroke-width="3"/>
%s%s
</svg>''' % (T(20, 70, "A", 64, "var(--pen)"), T(20, 350, "briga com ela:", 34, "var(--ink)"), T(20, 392, "“eu não sou de andar”", 34, "var(--ink)"),
     T(500, 70, "B", 64, "var(--pen)"), T(490, 370, "aumenta o som e finge", 34, "var(--ink)"), T(490, 412, "que não ouviu", 34, "var(--ink)")), True))

def box(x, y, mark=None, col="var(--ink)"):
    s = '<rect x="%d" y="%d" width="44" height="44" rx="6" stroke="%s" stroke-width="4"/>' % (x, y, col)
    if mark == "x":
        s += '<path d="M%d,%d L%d,%d M%d,%d L%d,%d" stroke="var(--mu)" stroke-width="4"/>' % (x + 8, y + 8, x + 36, y + 36, x + 36, y + 8, x + 8, y + 36)
    if mark == "v":
        s += '<path d="M%d,%d L%d,%d L%d,%d" stroke="var(--pen)" stroke-width="6"/>' % (x + 6, y + 22, x + 20, y + 40, x + 54, y - 10)
    return s

C.append(("light", '''<h2>Se você marcou A ou B, as duas tentam expulsar a mesma coisa.</h2>
<p style="margin-top:36px">Olha isso: tem uma terceira resposta.</p>
<svg class="draw" width="888" height="430" viewBox="0 0 888 430" style="margin-top:auto; margin-bottom:10px">
%s%s%s
<path d="M90,62 L520,58 M90,152 L620,148" stroke="var(--mu)" stroke-width="3"/>
%s%s
<path d="M60,210 C30,240 30,260 46,280" stroke="var(--pen)" stroke-width="3"/>
%s%s%s
</svg>''' % (box(20, 30, "x"), T(90, 66, "A) brigar com a vontade", 38, "var(--mu)"), box(20, 120, "x"), T(90, 156, "B) fingir que não ouviu", 38, "var(--mu)"), "",
     box(20, 290, "v", "var(--pen)"), T(90, 326, "C) reparar nela:", 44, "var(--pen)", rot=-2), T(90, 386, "“olha, a vontade de andar chegou.”", 40, "var(--pen)", rot=-2)), False))

C.append(("dark", '''<h2>1. Querer andar é fraqueza? Ou é outra coisa?</h2>
<p style="margin-top:36px">Não é fraqueza. Essa vontade sempre correu com você. Ela só %s.</p>
<svg class="draw" width="888" height="470" viewBox="0 0 888 470" style="margin-top:auto; margin-bottom:10px">
%s
<path d="M560,70 L860,70" stroke="var(--ink)" stroke-width="4"/>
%s%s
<path d="M600,170 C620,130 640,110 660,84 M650,98 L662,82 L668,100" stroke="var(--pen)" stroke-width="3"/>
<path d="M20,110 L868,110" stroke="var(--mu)" stroke-width="2" stroke-dasharray="4 12"/>
%s%s%s%s
<path d="M100,260 L130,300 M330,290 L350,330 M560,330 L540,370 M760,280 L780,320" stroke="var(--mu)" stroke-width="2"/>
%s
</svg>''' % (hl("não cabe na frase que você usa pra se descrever"), T(20, 70, "eu sou o corredor que", 44, "var(--ink)"),
     T(580, 200, "não falha", 38, "var(--pen)"), T(580, 244, "cumpre tudo", 38, "var(--pen)"),
     T(20, 230, "cansa", 38, "var(--mu)"), T(240, 270, "tem medo", 38, "var(--mu)"), T(420, 400, "quer parar", 38, "var(--mu)"), T(680, 360, "sente inveja", 38, "var(--mu)"),
     T(20, 456, "o que não cabe na frase fica de fora. não some.", 36, "var(--pen)", rot=-1)), False))

C.append(("light", '''<h2>2. “Eu nunca paro” te ajuda a seguir? Até que km?</h2>
<p style="margin-top:36px">Ajuda até o cansaço apertar. Quanto mais rígida a frase, menos espaço sobra. Aí a vontade de parar aparece %s.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
<path d="M40,10 L40,360 L870,360" stroke="var(--mu)" stroke-width="3"/>
<path d="M40,330 C240,300 460,240 860,160" stroke="var(--ink)" stroke-width="3" stroke-dasharray="3 14"/>
%s
<path d="M40,340 L600,336 C620,336 626,330 630,300 L640,40 L860,36" stroke="var(--pen)" stroke-width="5"/>
%s
%s%s
</svg>''' % (hl("de uma vez"), T(80, 250, "frase flexível: chega aos poucos", 32, "var(--ink)"),
     T(620, 30, "frase rígida: chega de uma vez", 34, "var(--pen)", "end"), T(860, 400, "cansaço →", 22, "var(--mu)", "end", fam="Inter"), T(60, 30, "↑ vontade de parar", 22, "var(--mu)", fam="Inter")), False))

C.append(("dark", '''<h2>3. Por que andar um minuto pesa tanto? É só a perna?</h2>
<p style="margin-top:36px">Não. Repara: quem reclama também é o personagem %s. O cansaço vira ameaça e pesa em dobro.</p>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:auto; margin-bottom:10px">
%s%s%s
<path d="M80,236 L700,236" stroke="var(--ink)" stroke-width="5"/>
%s
<path d="M400,280 L400,280" stroke="var(--pen)" stroke-width="4"/>
%s
<ellipse cx="560" cy="320" rx="200" ry="70" stroke="var(--pen)" stroke-width="4" transform="rotate(-3 560 320)"/>
</svg>''' % (hl("que está sendo ameaçado"), T(120, 70, "perna cansada", 46, "var(--ink)"), T(40, 170, "+", 60, "var(--pen)"), T(120, 170, "“eu não sou de andar”", 46, "var(--ink)"),
     T(40, 340, "=", 60, "var(--ink)"), T(560, 336, "cansaço em dobro", 46, "var(--pen)", "middle", -3)), False))

C.append(("light", '''<div style="margin-top:120px"></div>
<h1 style="font-size:76px">A vontade de parar não é o problema.</h1>
<h1 class="or" style="font-size:76px; margin-top:26px">Fingir que ela não é sua é o que pesa.</h1>''', False))

def check_item(y, t):
    return ('<rect x="0" y="%d" width="44" height="44" rx="6" stroke="var(--ink)" stroke-width="4"/>' % y) + T(74, y + 36, t, 32, "var(--ink)", fam="Inter")

C.append(("dark", '''<h2>Marca o que já aconteceu com você.</h2>
<svg class="draw" width="888" height="420" viewBox="0 0 888 420" style="margin-top:50px">
%s%s%s%s
</svg>
<p style="margin-top:20px">Cada marca é uma parte sua que correu junto. %s</p>''' % (
    check_item(10, "Pensou “isso não sou eu”. Em que trecho?"),
    check_item(110, "Se irritou com quem não tinha culpa. Quem?"),
    check_item(210, "Escondeu que quis andar. De quem?"),
    check_item(310, "Brigou com a própria cabeça. Por quantos km?"),
    hl("Sem convite, mas sua.")), False))

C.append(("light", paraquem("Pra quem é isso, e pra quem não é.",
    "você trava uma briga interna toda vez que a vontade de parar aparece numa prova.",
    "essa vontade vem com dor, tontura ou falta de ar (procure um médico), ou se ela pesa em tudo, também fora do esporte (procure um psicólogo)."), False))

C.append(("dark", '''<div style="margin-top:20px"></div>
<h1 style="font-size:76px">Você não precisa gostar dessa parte.</h1>
<h1 class="or" style="font-size:76px; margin-top:18px">Só parar de gastar força escondendo ela.</h1>
<p class="mu" style="margin-top:36px">Comenta aqui: A, B ou C? E manda pra quem marcaria diferente de você.</p>
<svg class="draw" width="888" height="200" viewBox="0 0 888 200" style="margin-top:auto; margin-bottom:20px">
<rect x="40" y="40" width="130" height="130" rx="12" stroke="var(--ink)" stroke-width="4"/>
<rect x="210" y="40" width="130" height="130" rx="12" stroke="var(--ink)" stroke-width="4"/>
<rect x="380" y="40" width="130" height="130" rx="12" style="fill:var(--hl)" stroke="var(--pen)" stroke-width="4"/>
%s%s%s
<path d="M540,110 C580,96 600,96 630,104 M614,92 L632,104 L614,118" stroke="var(--pen)" stroke-width="4"/>
%s%s
</svg>''' % (T(105, 130, "A", 70, "var(--ink)", "middle"), T(275, 130, "B", 70, "var(--ink)", "middle"), T(445, 130, "C", 70, "var(--pen)", "middle"),
     T(650, 96, "qual é a", 40, "var(--pen)", rot=-3), T(650, 140, "sua?", 40, "var(--pen)", rot=-3)), True))

VERSOES = {"A": A, "B": B, "C": C}

LEGENDAS = {"A": """Sabe quando você chega em casa depois da prova, toma banho, e a frase do km difícil volta? Aquela que você não falou no grupo.

Ela não surgiu ali. Já estava com você antes da largada. Só não tinha lugar na versão que acorda cedo e cumpre tudo.

Essa versão não é o problema. Foi ela que te trouxe até aqui. O aperto começa quando ela é a única que pode existir. Aí qualquer cansaço vira ameaça.

Um exercício pro próximo longão: deixa o bloco de notas do celular aberto. Quando vier um pensamento que você não diria em voz alta, escreve três palavras. Só isso. Sem responder, sem corrigir. Depois do treino, lê.

Talvez você note que algumas frases se repetem, no mesmo trecho ou no mesmo tipo de cansaço. Isso já é informação sobre você.

Salva pra fazer esse exercício no próximo treino longo.

Tem uma análise completa, sem custo, esperando por você na bio.""",

"B": """Já parou pra pensar no voluntário do posto de água? Ele levanta de madrugada, fica horas em pé e às vezes recebe a pior versão de quem passa correndo.

Não é que quem passa seja grosso. É que, no cansaço, a energia que segurava a pose acaba. E o que estava guardado sai no primeiro alvo que aparece: o copo, o buraco, o amigo que te passou.

Repara como o alvo pode ser pequeno. O tamanho da reação não fala do copo. Fala de quanto tempo você passou segurando.

Uma coisa pra testar no próximo treino forte: quando sentir a primeira irritação, em vez de engolir ou explodir, diz o nome dela pra você mesmo. "Irritação." E segue correndo. Observa o que muda no quilômetro seguinte.

Manda pra quem é sempre o mais tranquilo do grupo e no fim do longão vira outra pessoa. Ele vai rir, mas vai entender.

Pra ir mais fundo no seu caso, a avaliação inteira é grátis no link do perfil.""",

"C": """Pensa no último treino de subida. Em que repetição veio a vontade de andar? Na terceira? Na última?

Agora lembra o que você disse pra você mesmo nessa hora. Se foi algo como "eu não sou de andar", repara: não é uma frase sobre a subida. É uma frase sobre quem você acha que precisa ser.

E ela tem custo. Toda vez que a vontade aparece, você sobe a ladeira e ainda discute com ela. Dois trabalhos ao mesmo tempo.

Um teste pra próxima sessão: quando a vontade chegar, fala baixinho "chegou". Não decide nada nesse segundo. Só nomeia. Depois vê se ela fica do mesmo tamanho.

Não é sobre andar ou não andar. Às vezes você vai andar, às vezes não. É sobre não gastar perna brigando com uma parte sua.

Comenta aqui embaixo: A ou B? Se você já faz a C, conta em que treino.

Quer mapear onde isso aparece nas suas provas? É gratuito e começa pelo link na bio.""",
}
