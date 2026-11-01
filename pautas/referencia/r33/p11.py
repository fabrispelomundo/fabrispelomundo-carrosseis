# -*- coding: utf-8 -*-
# p11 — cinco lugares para mexer antes do km pesar (A: cano e fita · B: balão apertado · C: garrafa sacudida)
from base import *


def T(x, y, s, size=36, color="var(--ink)", anchor="start", rot=None, font="Pen", weight=None):
    tr = ' transform="rotate(%s %d %d)"' % (rot, x, y) if rot is not None else ""
    fw = ' font-weight="%s"' % weight if weight else ""
    return '<text x="%d" y="%d" text-anchor="%s" font-family="%s"%s font-size="%d" fill="%s"%s>%s</text>' % (
        x, y, anchor, font, fw, size, color, tr, s)


def svg(h, inner, style="margin-top:auto"):
    return '<svg class="draw" width="888" height="%d" viewBox="0 0 888 %d" style="%s">%s</svg>' % (h, h, style, inner)


def P(d, color="var(--ink)", w=4, extra=""):
    return '<path d="%s" stroke="%s" stroke-width="%s"%s/>' % (d, color, w, extra)


def arrow_head(x, y, dx, dy, color, w=3, s=14):
    # ponta de seta em (x,y) apontando na direção (dx,dy)
    import math
    a = math.atan2(dy, dx)
    p1 = (x - s * math.cos(a - .5), y - s * math.sin(a - .5))
    p2 = (x - s * math.cos(a + .5), y - s * math.sin(a + .5))
    return P("M%d,%d L%d,%d L%d,%d" % (p1[0], p1[1], x, y, p2[0], p2[1]), color, w)


# =================================================================== VERSÃO A · cano e fita · capa escura
def valve(x, y, color="var(--ink)", r=28, w=4):
    # registro: haste saindo do cano + volante
    return (P("M%d,%d L%d,%d" % (x, y, x, y - 44), color, w) +
            '<circle cx="%d" cy="%d" r="%d" stroke="%s" stroke-width="%d"/>' % (x, y - 44 - r, r, color, w) +
            P("M%d,%d L%d,%d M%d,%d L%d,%d" % (x - r, y - 44 - r, x + r, y - 44 - r, x, y - 44 - 2 * r, x, y - 44), color, w - 1))


def drop(x, y, color="var(--pen)", s=1.0):
    return P("M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d Z" % (
        x, y, x - 10 * s, y + 16 * s, x - 10 * s, y + 26 * s, x, y + 26 * s,
        x + 10 * s, y + 26 * s, x + 10 * s, y + 16 * s, x, y), color, 3)


A1_DRAW = svg(470,
    # cano
    P("M20,200 L560,200 M20,250 L560,250 M720,200 L868,200 M720,250 L868,250", "var(--ink)", 5) +
    # inchaço
    P("M560,200 C580,120 700,120 720,200 M560,250 C580,330 700,330 720,250", "var(--ink)", 5) +
    # voltas de fita
    ''.join(P("M%d,%d C%d,%d %d,%d %d,%d" % (x, 150 + abs(x - 640) // 2, x + 12, 200, x + 12, 250, x, 300 - abs(x - 640) // 2),
              "var(--pen)", 16, ' style="stroke-opacity:.55"') for x in (588, 616, 644, 672, 700)) +
    # gotas ainda saindo
    drop(612, 330) + drop(660, 360, s=.8) + drop(636, 400, s=.7) +
    # registro esquecido
    valve(150, 200) +
    T(250, 70, "e isso aqui?", 42, "var(--pen)", rot=-3) +
    P("M244,80 C210,90 196,110 190,124", "var(--pen)", 3) + arrow_head(190, 124, -0.4, 1, "var(--pen)") +
    T(760, 120, "segurar", 38, "var(--ink)", rot=-4) +
    P("M770,128 C750,140 736,150 718,162", "var(--ink)", 3) + arrow_head(718, 162, -1, .6, "var(--ink)") +
    T(444, 456, "a fita segura. o cano continua cheio.", 42, "var(--ink)", "middle", rot=-2),
    "margin-top:auto; margin-bottom:20px")

A1 = ('<div style="margin-top:30px"></div>'
      '<h1>Naquele km que pesa, o que você faz? Além de travar o dente?</h1>' + A1_DRAW)

HEAD = ("M0,0 C-14,-96 60,-150 136,-132 C196,-118 222,-62 216,-14 C214,10 222,22 236,40 L220,52 "
        "C224,74 216,90 200,92 C198,116 182,128 150,124 L146,170 M0,0 C4,60 26,104 56,128 L56,170")


def head(x, y, inside=False):
    g = '<g transform="translate(%d,%d)">%s' % (x, y, P(HEAD, "var(--ink)", 4))
    if inside:
        g += P("M60,-60 C90,-110 150,-90 130,-50 C110,-10 50,-40 80,-80 C110,-120 180,-60 150,-20 "
               "C120,20 40,0 50,-50 C60,-90 120,-70 110,-40 C100,-10 70,-30 90,-60", "var(--pen)", 4)
        g += P("M-6,-20 L230,-20", "var(--mu)", 2, ' stroke-dasharray="6 8"')
    return g + '</g>'


A2 = ('<h2>Travar o dente tem nome: segurar.</h2>'
      '<p style="margin-top:36px">Engolir o palavrão, fechar a cara, não deixar nada escapar. De fora, parece tudo sob controle.</p>'
      '<p>Só que por dentro o peso continua do mesmo tamanho. E manter tudo fechado %s.</p>' % hl("também gasta") +
      svg(390,
          head(120, 170) + head(560, 170, True) +
          T(200, 376, "o que a foto mostra", 36, "var(--mu)", "middle") +
          T(640, 376, "o que você carrega", 36, "var(--pen)", "middle"),
          "margin-top:auto"))


def a3_valve(x, y, n, t1, t2, color="var(--ink)"):
    return (valve(x, y, color, 22, 4) +
            T(x, y + 66, "%s · %s" % (n, t1), 36, color, "middle", font="Inter", weight=800) +
            T(x, y + 108, t2, 30, "var(--mu)", "middle"))


A3 = ('<h2>Repara: a água passa por %s antes da fita.</h2>' % circ("quatro registros") +
      svg(720,
          P("M40,150 L820,150 L820,470 L60,470 L60,640 L330,640", "var(--mu)", 14, ' style="stroke-opacity:.45"') +
          a3_valve(200, 150, "1", "A ESCOLHA", "prova, onda, companhia") +
          a3_valve(620, 150, "2", "A CENA", "o que dá pra mudar ali") +
          a3_valve(620, 470, "3", "O OLHAR", "pra onde a atenção vai") +
          a3_valve(240, 470, "4", "A LEITURA", "que nome você dá ao que sente") +
          # fita no fim
          ''.join(P("M%d,620 L%d,660" % (x, x + 6), "var(--pen)", 14, ' style="stroke-opacity:.6"') for x in (350, 372, 394)) +
          drop(380, 672, s=.7) +
          T(440, 652, "5 · segurar", 42, "var(--pen)"),
          "margin-top:36px"))


def tube(x, level, label, color="var(--ink)", fill="var(--hl)"):
    top, bot = 60, 380
    y = bot - level
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="6" style="fill:%s; stroke:none"/>' % (x + 4, y, 92, level - 4, fill) +
            P("M%d,%d L%d,%d C%d,%d %d,%d %d,%d L%d,%d" % (x, top, x, bot - 20, x, bot, x + 100, bot, x + 100, bot - 20, x + 100, top), color, 4) +
            T(x + 50, bot + 50, label, 32, color, "middle"))


A4 = ('<h2>Olha isso: cada registro adiante pega o cano mais cheio.</h2>'
      '<p style="margin-top:36px">Na escolha, quase nada subiu ainda. Na hora da fita, já subiu tudo o que tinha pra subir. Quanto mais tarde você mexe, %s.</p>' % hl("mais força precisa") +
      svg(450,
          tube(30, 40, "escolha") + tube(205, 90, "cena") + tube(380, 160, "olhar") + tube(555, 230, "leitura") +
          tube(740, 316, "fita", "var(--pen)", "var(--pen)") +
          T(0, 30, "o que já subiu ↑", 26, "var(--mu)", font="Inter") +
          T(888, 30, "tempo →", 26, "var(--mu)", "end", font="Inter"),
          "margin-top:auto"))


def slot(x, y, w, h, label):
    return ('<rect x="%d" y="%d" width="%d" height="%d" rx="14" stroke="var(--mu)" stroke-width="3" stroke-dasharray="8 10"/>' % (x, y, w, h) +
            T(x + w // 2, y + h // 2 + 12, label, 34, "var(--mu)", "middle"))


A5 = ('<h2>Segurar não tá errado.</h2>'
      '<p style="margin-top:36px">Fita salva emergência. O problema é quando ela vira a %s da caixa.</p>' % hl("única ferramenta") +
      '<p>Os outros quatro registros dá pra decidir antes, com calma, longe do km.</p>' +
      svg(440,
          P("M20,120 L868,120 L830,400 L58,400 Z", "var(--ink)", 5) +
          P("M300,120 C300,60 588,60 588,120", "var(--ink)", 5) +
          slot(80, 150, 170, 100, "escolha") + slot(270, 150, 170, 100, "cena") +
          slot(80, 270, 170, 100, "olhar") + slot(270, 270, 170, 100, "leitura") +
          '<circle cx="650" cy="260" r="100" stroke="var(--pen)" stroke-width="5" style="fill:var(--hl)"/>' +
          '<circle cx="650" cy="260" r="42" stroke="var(--pen)" stroke-width="4"/>' +
          P("M748,280 L840,330", "var(--pen)", 14, ' style="stroke-opacity:.6"') +
          T(650, 40, "a caixa veio com cinco. você só tira uma.", 34, "var(--pen)", "middle", rot=-2),
          "margin-top:auto"))

A6 = ('<div style="margin-top:110px"></div>'
      '<h1 style="font-size:78px">A fita esconde o vazamento.</h1>'
      '<h1 class="or" style="font-size:78px; margin-top:22px">O registro decide quanta água chega.</h1>')

A7 = qs("Pega a sua última prova difícil.", [
    ("Onde pesou? Em que km? Na subida?", "Pensa no ponto exato: a placa, a curva, o posto de água, o trecho de vento."),
    ("E o que você fez ali? Só travou o dente?", "Engoliu, fechou a cara, tirou o olho do relógio, puxou conversa. Anota o que foi."),
    ("Dava pra mexer antes? Em qual registro?", "A onda, a hora de chegar, pra onde olhar, o nome que você deu. Escolhe um pra próxima.")])

A8 = paraquem("Para quem é isso, e para quem não é.",
    "você chega bem treinado e, no trecho difícil, a única saída que conhece é fechar a cara e aguentar.",
    "o peso na prova vem com dor no peito, tontura ou falta de ar: isso é com um médico. Se engolir tudo virou o seu jeito de passar também pelo trabalho e pela casa, procure um psicólogo.")

A9 = ('<div style="margin-top:50px"></div>'
      '<h1 style="font-size:76px">Quem só tem fita passa a prova remendando.</h1>'
      '<h1 class="or" style="font-size:76px; margin-top:18px">Os registros ficam antes do km.</h1>'
      '<p class="mu" style="margin-top:40px">Salva esse carrossel. Na véspera da próxima prova, escolhe qual dos quatro registros você vai mexer.</p>' +
      svg(230,
          P("M380,10 L508,10 L508,210 L444,160 L380,210 Z", "var(--pen)", 5, ' style="fill:var(--hl)"') +
          valve(444, 140, "var(--ink)", 22, 4) +
          T(340, 90, "salva aqui", 40, "var(--pen)", "end", rot=-3) +
          P("M346,100 L370,104", "var(--pen)", 3) + arrow_head(372, 104, 1, .1, "var(--pen)") +
          T(560, 150, "abre na véspera", 40, "var(--pen)", rot=-3),
          "margin-top:30px"))

VA = [("dark", A1, True), ("light", A2, False), ("dark", A3, False), ("light", A4, False), ("dark", A5, False),
      ("light", A6, False), ("dark", A7, False), ("light", A8, False), ("dark", A9, True)]


# =================================================================== VERSÃO B · balão apertado · capa clara
def fist(x, y, color="var(--ink)", sc=1.0):
    # mão fechada vista de frente: palma + 4 dedos
    g = '<g transform="translate(%d,%d) scale(%s)">' % (x, y, sc)
    g += P("M0,0 C0,-20 90,-20 90,0 L90,120 C90,140 0,140 0,120 Z", color, 4, ' style="fill:var(--bg)"')
    g += P("M4,30 L86,30 M4,60 L86,60 M4,90 L86,90", color, 3)
    return g + '</g>'


B1 = ('<div style="margin-top:30px"></div>'
      '<h1>Como pode engolir tudo no km difícil e o peso continuar do mesmo tamanho?</h1>' +
      svg(440,
          P("M396,190 C300,70 80,80 70,200 C60,320 300,330 396,230", "var(--ink)", 5) +
          P("M492,190 C588,70 808,80 818,200 C828,320 588,330 492,230", "var(--ink)", 5) +
          P("M818,206 L846,196 L846,218 Z", "var(--ink)", 4) +
          P("M846,206 C870,230 860,260 878,300", "var(--ink)", 3) +
          fist(399, 150, "var(--pen)") +
          T(444, 60, "apertou aqui", 40, "var(--pen)", "middle", rot=-2) +
          T(220, 200, "o ar", 40, "var(--mu)", "middle") + T(220, 244, "foi pra cá", 40, "var(--mu)", "middle") +
          T(690, 200, "e pra cá", 40, "var(--mu)", "middle") +
          T(444, 420, "apertar não tira o ar do balão.", 42, "var(--ink)", "middle", rot=-2),
          "margin-top:auto; margin-bottom:20px"))


def balloon(cx, cy, r, color="var(--ink)", w=4, label=None, lsize=30):
    s = ('<ellipse cx="%d" cy="%d" rx="%d" ry="%d" stroke="%s" stroke-width="%d"/>' % (cx, cy, r, int(r * 1.18), color, w) +
         P("M%d,%d L%d,%d L%d,%d Z" % (cx, cy + int(r * 1.18), cx - 8, cy + int(r * 1.18) + 12, cx + 8, cy + int(r * 1.18) + 12), color, 3) +
         P("M%d,%d C%d,%d %d,%d %d,%d" % (cx, cy + int(r * 1.18) + 12, cx - 14, cy + int(r * 1.18) + 50, cx + 14, cy + int(r * 1.18) + 80, cx, 340), color, 2))
    if label:
        s += T(cx, cy + 10, label, lsize, color, "middle")
    return s


B2 = ('<h2>Pois é: engolir chega quando o balão já encheu.</h2>'
      '<p style="margin-top:36px">Segurar mexe no que os outros veem. O ar continua lá dentro, e a sua mão fica fechada o trecho inteiro.</p>'
      '<p>A pergunta útil é outra: %s?</p>' % hl("onde ele começou a encher") +
      svg(420,
          P("M20,360 L868,360", "var(--mu)", 3) +
          '<ellipse cx="110" cy="290" rx="24" ry="28" stroke="var(--ink)" stroke-width="4"/>' + P("M110,318 L110,360", "var(--ink)", 2) +
          '<ellipse cx="330" cy="230" rx="56" ry="66" stroke="var(--ink)" stroke-width="4"/>' + P("M330,296 L330,360", "var(--ink)", 2) +
          '<ellipse cx="650" cy="150" rx="100" ry="118" stroke="var(--ink)" stroke-width="4"/>' + P("M650,268 L650,280", "var(--ink)", 2) +
          fist(623, 278, "var(--pen)", .6) +
          T(110, 404, "véspera", 30, "var(--mu)", "middle", font="Inter") +
          T(330, 404, "largada", 30, "var(--mu)", "middle", font="Inter") +
          T(650, 404, "o km", 30, "var(--mu)", "middle", font="Inter") +
          T(880, 290, "a mão", 36, "var(--pen)", "end", rot=-4) + T(880, 326, "só chega aqui", 36, "var(--pen)", "end", rot=-4) +
          "margin-top:auto"))


def flag(x, y, n, t1, t2, color, up=True):
    dy = -1 if up else 1
    s = P("M%d,%d L%d,%d" % (x, y, x, y - 70), color, 4)
    s += P("M%d,%d L%d,%d L%d,%d Z" % (x, y - 70, x + 46, y - 58, x, y - 46), color, 3, ' style="fill:%s"' % ("var(--hl)" if color != "var(--mu)" else "none"))
    s += T(x - 14, y - 84, n, 38, color, "middle", font="Inter", weight=800)
    ty = y + 46
    s += T(x, ty, t1, 30, color, "middle") + T(x, ty + 34, t2, 30, "var(--mu)", "middle")
    return s


B3 = ('<h2>Parece que o peso nasce no km.</h2>'
      '<p style="margin-top:36px">Mas ele começa a encher bem antes: na prova que você escolhe, na onda, em quem corre do seu lado, em como você chega no local.</p>' +
      svg(460,
          P("M10,250 L90,230 L270,270 L450,230 L630,280 L810,260 L878,270", "var(--ink)", 4, ' stroke-dasharray="2 14"') +
          flag(90, 230, "1", "na inscrição", "prova e onda", "var(--pen)") +
          flag(270, 270, "2", "no local", "o que mudar", "var(--pen)") +
          flag(450, 230, "3", "no trecho", "o olhar", "var(--ink)") +
          flag(630, 280, "4", "no trecho", "o nome", "var(--ink)") +
          flag(810, 260, "5", "no km", "segurar", "var(--mu)") +
          T(20, 50, "esses dois acontecem antes da largada", 36, "var(--pen)", rot=-2) +
          P("M130,66 C130,80 126,92 118,104", "var(--pen)", 3) + arrow_head(118, 104, -.5, 1, "var(--pen)") +
          P("M310,66 C310,100 304,120 296,138", "var(--pen)", 3) + arrow_head(296, 138, -.4, 1, "var(--pen)") +
          "margin-top:auto"))

B4 = ('<h2>Parece que segurar faz o peso baixar.</h2>'
      '<p style="margin-top:36px">Se liga: baixa uma coisa só, o que aparece por fora. O que você sente fica onde estava. E segurar ainda %s.</p>' % hl("cobra esforço") +
      svg(470,
          P("M40,10 L40,400 L870,400", "var(--mu)", 3) +
          P("M300,30 L300,400", "var(--mu)", 2, ' stroke-dasharray="4 10"') +
          T(310, 440, "começa a segurar", 28, "var(--mu)", font="Inter") +
          P("M40,150 C160,130 240,110 300,110 C400,110 600,112 860,110", "var(--ink)", 4) +
          T(860, 96, "o que você sente", 36, "var(--ink)", "end") +
          P("M40,160 C160,140 240,118 300,118 C380,160 460,320 860,340", "var(--mu)", 4, ' stroke-dasharray="3 12"') +
          T(860, 384, "o que aparece por fora", 36, "var(--mu)", "end") +
          P("M300,380 C420,370 560,270 860,200", "var(--pen)", 5) +
          T(560, 250, "o esforço de segurar", 36, "var(--pen)", rot=-12),
          "margin-top:auto"))

B5 = ('<h2>Parece que no meio do trecho já é tarde.</h2>'
      '<p style="margin-top:36px">Mas ainda dá pra mexer em duas coisas: pra onde o seu olho vai e %s ao que sente.</p>' % hl("que nome você dá") +
      svg(470,
          # dois balões iguais com etiquetas diferentes
          '<ellipse cx="80" cy="100" rx="50" ry="59" stroke="var(--ink)" stroke-width="4"/>' +
          P("M80,159 L80,200", "var(--ink)", 2) +
          '<ellipse cx="80" cy="310" rx="50" ry="59" stroke="var(--ink)" stroke-width="4"/>' +
          P("M80,369 L80,410", "var(--ink)", 2) +
          T(150, 112, "“vou quebrar”", 36, "var(--ink)") +
          T(150, 322, "“é a subida. eu sabia.”", 36, "var(--ink)") +
          P("M530,100 L600,100", "var(--mu)", 3) + arrow_head(602, 100, 1, 0, "var(--mu)") +
          P("M530,310 L600,310", "var(--mu)", 3) + arrow_head(602, 310, 1, 0, "var(--mu)") +
          '<ellipse cx="750" cy="110" rx="110" ry="100" stroke="var(--pen)" stroke-width="5"/>' +
          '<ellipse cx="750" cy="310" rx="50" ry="59" stroke="var(--ink)" stroke-width="4"/>' +
          T(444, 456, "mesmo balão. o nome mudou o tamanho.", 40, "var(--pen)", "middle", rot=-2),
          "margin-top:auto"))

B6 = ('<div style="margin-top:110px"></div>'
      '<h1 style="font-size:78px">Apertar o balão não tira o ar.</h1>'
      '<h1 class="or" style="font-size:78px; margin-top:22px">Mexer antes deixa entrar menos.</h1>')


def blank(y, label):
    return (T(0, y, label, 34, "var(--ink)", font="Inter", weight=700) +
            P("M0,%d L888,%d" % (y + 52, y + 52), "var(--mu)", 2, ' stroke-dasharray="2 10"'))


B7 = ('<h2>Pega a sua última prova e preenche.</h2>'
      '<p style="margin-top:30px">Seja específico: no café, no estacionamento, no curral, na subida. Em branco também vale.</p>' +
      svg(640,
          blank(40, "O que eu escolhi antes? Onda? Companhia?") + blank(150, "O que eu mudei no local? Quando?") +
          blank(260, "Pra onde eu olhei no trecho? Relógio? Chão?") + blank(370, "Que nome eu dei ao peso? Qual frase?") +
          blank(480, "O que eu segurei? Em que ponto?") +
          T(888, 630, "quantas ficaram em branco?", 42, "var(--pen)", "end", rot=-2),
          "margin-top:40px"))

B8 = paraquem("Para quem é isso, e para quem não é.",
    "o seu trecho difícil é sempre igual: você trava a cara, engole e espera passar.",
    "na prova aparecem dor no peito, tontura ou falta de ar: isso é para um médico avaliar. Se segurar tudo também é o seu jeito de atravessar a vida fora da corrida, o caminho é um psicólogo.")


def plane(x, y, color="var(--ink)"):
    return P("M%d,%d L%d,%d L%d,%d L%d,%d Z M%d,%d L%d,%d" % (
        x, y, x + 150, y - 60, x + 100, y + 60, x + 64, y + 18, x + 64, y + 18, x + 150, y - 60), color, 4)


B9 = ('<div style="margin-top:50px"></div>'
      '<h1 style="font-size:76px">Apertar não esvazia balão.</h1>'
      '<h1 class="or" style="font-size:76px; margin-top:18px">Mas dá pra encher menos.</h1>'
      '<p class="mu" style="margin-top:40px">Manda pra aquele corredor que cruza a chegada de cara fechada e jura que tava tudo bem.</p>' +
      svg(250,
          plane(120, 110, "var(--pen)") +
          P("M270,52 C360,40 420,100 520,90", "var(--ink)", 2) +
          '<ellipse cx="590" cy="80" rx="54" ry="64" stroke="var(--ink)" stroke-width="4"/>' +
          P("M532,92 L520,98 L524,84 Z", "var(--ink)", 3) +
          T(444, 220, "para: o “tava de boa”", 44, "var(--pen)", "middle", rot=-3),
          "margin-top:30px"))

VB = [("light", B1, True), ("dark", B2, False), ("light", B3, False), ("dark", B4, False), ("light", B5, False),
      ("dark", B6, False), ("light", B7, False), ("dark", B8, False), ("light", B9, True)]


# =================================================================== VERSÃO C · garrafa sacudida · capa escura
def bottle(x, y, color="var(--ink)", w=4, s=1.0):
    # garrafa em pé, gargalo em (x, y)
    def k(v): return int(v * s)
    return P("M%d,%d L%d,%d C%d,%d %d,%d %d,%d L%d,%d C%d,%d %d,%d %d,%d L%d,%d C%d,%d %d,%d %d,%d L%d,%d Z" % (
        x - k(16), y, x - k(16), y + k(60), x - k(16), y + k(90), x - k(60), y + k(100), x - k(60), y + k(140),
        x - k(60), y + k(290), x - k(60), y + k(300), x + k(60), y + k(300), x + k(60), y + k(290),
        x + k(60), y + k(140), x + k(60), y + k(100), x + k(16), y + k(90), x + k(16), y + k(60), x + k(16), y), color, w)


def cork(x, y, color="var(--ink)", s=1.0):
    return '<rect x="%d" y="%d" width="%d" height="%d" rx="4" stroke="%s" stroke-width="3"/>' % (
        x - int(14 * s), y - int(30 * s), int(28 * s), int(34 * s), color)


def thumb(x, y, color):
    return P("M%d,%d C%d,%d %d,%d %d,%d C%d,%d %d,%d %d,%d" % (
        x - 40, y + 30, x - 40, y - 10, x - 20, y - 20, x + 10, y - 18,
        x + 40, y - 16, x + 50, y + 10, x + 40, y + 50), color, 5)


C1 = ('<div style="margin-top:30px"></div>'
      '<h1>Aquele km que pesa: você segura? Ou deixa sair?</h1>' +
      svg(560,
          bottle(220, 140) + cork(220, 140) + thumb(222, 100, "var(--pen)") +
          T(220, 500, "A", 64, "var(--pen)", "middle", font="Inter", weight=800) +
          T(220, 50, "aperta a rolha", 38, "var(--ink)", "middle", rot=-3) +
          bottle(660, 140) +
          cork(700, 50, "var(--ink)") +
          P("M660,130 C640,90 620,70 590,60 M660,130 C668,80 660,40 650,10 M664,130 C690,100 720,94 760,96", "var(--pen)", 3, ' stroke-dasharray="3 9"') +
          T(660, 500, "B", 64, "var(--pen)", "middle", font="Inter", weight=800) +
          T(820, 70, "solta", 38, "var(--ink)", "middle", rot=4) +
          P("M444,140 L444,460", "var(--mu)", 2, ' stroke-dasharray="4 12"'),
          "margin-top:auto; margin-bottom:10px"))

C2 = ('<h2>Se você ficou entre A e B, repara.</h2>'
      '<p style="margin-top:36px">As duas entram no mesmo ponto: com a garrafa já sacudida. A pergunta que muda a prova é outra.</p>' +
      svg(520,
          '<g transform="rotate(-18 444 260)">' + bottle(444, 110, "var(--ink)") + cork(444, 110) + '</g>' +
          P("M250,160 C230,200 230,260 250,300 M210,140 C186,200 186,270 210,320", "var(--pen)", 4) +
          P("M640,200 C660,240 660,300 640,340 M680,180 C704,240 704,320 680,360", "var(--pen)", 4) +
          T(444, 30, "quem sacudiu essa garrafa?", 44, "var(--pen)", "middle", rot=-2) +
          T(444, 480, "e quando?", 44, "var(--pen)", "middle", rot=-2),
          "margin-top:auto"))


def card(x, y, w, h, n, lines, icon, color="var(--ink)", dashed=False):
    da = ' stroke-dasharray="8 10"' if dashed else ""
    s = '<rect x="%d" y="%d" width="%d" height="%d" rx="18" stroke="%s" stroke-width="3"%s/>' % (x, y, w, h, color, da)
    s += T(x + 24, y + 54, n, 44, "var(--pen)", font="Inter", weight=800)
    s += '<g transform="translate(%d,%d)">%s</g>' % (x + w - 90, y + 20, icon)
    for i, ln in enumerate(lines):
        s += T(x + 24, y + 128 + i * 38, ln, 32, color)
    return s


IC_CAL = (P("M0,10 L64,10 L64,66 L0,66 Z M0,26 L64,26 M16,0 L16,18 M48,0 L48,18", "var(--ink)", 3) +
          P("M18,46 L28,56 L46,36", "var(--pen)", 3))
IC_PIN = P("M32,66 C10,40 4,30 4,22 C4,6 18,0 32,0 C46,0 60,6 60,22 C60,30 54,40 32,66 Z", "var(--ink)", 3) + \
    '<circle cx="32" cy="22" r="8" stroke="var(--pen)" stroke-width="3"/>'
IC_EYE = P("M0,34 C16,8 48,8 64,34 C48,60 16,60 0,34 Z", "var(--ink)", 3) + \
    '<circle cx="32" cy="34" r="10" stroke="var(--pen)" stroke-width="3"/>'
IC_TAG = P("M0,10 L44,10 L64,34 L44,58 L0,58 Z", "var(--ink)", 3) + \
    '<circle cx="46" cy="34" r="5" stroke="var(--pen)" stroke-width="3"/>'
IC_THUMB = P("M14,66 L14,30 M50,66 L50,30 M8,30 L56,30 L56,16 L8,16 Z", "var(--mu)", 3)

C3 = ('<h2>Pergunta 1: dá pra mexer onde? Só no km?</h2>'
      '<p style="margin-top:28px">Resposta: em cinco lugares. E segurar é %s.</p>' % hl("o último da fila") +
      svg(640,
          card(0, 20, 284, 280, "1", ["a prova, a onda,", "com quem, como", "chegar"], IC_CAL) +
          card(302, 20, 284, 280, "2", ["o que dá pra", "mudar no local"], IC_PIN) +
          card(604, 20, 284, 280, "3", ["pra onde vai", "o olho no trecho"], IC_EYE) +
          card(0, 330, 284, 280, "4", ["que nome dar", "ao que você", "sente"], IC_TAG) +
          card(302, 380, 230, 200, "5", ["segurar"], IC_THUMB, "var(--mu)", True) +
          T(570, 470, "← o único que", 38, "var(--pen)", rot=-3) + T(590, 514, "você costuma usar", 38, "var(--pen)", rot=-3),
          "margin-top:auto"))

C4 = ('<h2>Pergunta 2: segurar sai de graça? Mesmo sem ninguém notar?</h2>'
      '<p style="margin-top:36px">Resposta: não. O trecho já cobra a parte dele. Segurar põe %s, e o que você sente por dentro não diminui.</p>' % hl("mais uma conta em cima") +
      svg(470,
          P("M40,10 L40,400 L870,400", "var(--mu)", 3) +
          P("M40,330 C200,320 320,280 420,260 C560,232 700,226 860,222 L860,400 L40,400 Z", "var(--mu)", 3, ' style="fill:var(--line)"') +
          P("M380,268 C500,190 640,140 860,110 L860,222 C700,226 560,232 420,260 Z", "var(--pen)", 4, ' style="fill:var(--hl)"') +
          T(160, 380, "o que o trecho pede", 36, "var(--ink)") +
          T(640, 205, "segurar", 40, "var(--pen)", rot=-6) +
          T(380, 456, "↑ começa a segurar", 26, "var(--mu)", font="Inter") +
          T(0, 0, "", 10),
          "margin-top:auto"))


def menu_row(y, n, txt, color="var(--ink)"):
    return T(40, y, "%s. %s" % (n, txt), 32, color) + P("M40,%d L380,%d" % (y + 14, y + 14), "var(--line)", 2)


C5 = ('<h2>Pergunta 3: então segurar é errado? Tem que parar?</h2>'
      '<p style="margin-top:36px">Resposta: não. Ruim é ele ser o %s em toda prova.</p>' % hl("único prato que você pede") +
      svg(560,
          '<rect x="10" y="20" width="400" height="500" rx="14" stroke="var(--ink)" stroke-width="4"/>' +
          T(210, 80, "CARDÁPIO DO KM", 28, "var(--ink)", "middle", font="Inter", weight=800) +
          menu_row(150, 1, "escolher antes") + menu_row(230, 2, "mudar o local") + menu_row(310, 3, "apontar o olho") +
          menu_row(390, 4, "dar outro nome") + menu_row(470, 5, "segurar", "var(--pen)") +
          '<g transform="rotate(4 680 270)">' +
          '<rect x="520" y="40" width="320" height="460" rx="6" stroke="var(--ink)" stroke-width="3"/>' +
          P("M520,40 L540,24 L560,40 L580,24 L600,40 L620,24 L640,40 L660,24 L680,40 L700,24 L720,40 L740,24 L760,40 L780,24 L800,40 L820,24 L840,40", "var(--ink)", 3) +
          T(680, 100, "comanda", 34, "var(--mu)", "middle") +
          T(560, 170, "prova 1: o 5", 36, "var(--pen)") + T(560, 240, "prova 2: o 5", 36, "var(--pen)") +
          T(560, 310, "prova 3: o 5", 36, "var(--pen)") + T(560, 380, "prova 4: o 5", 36, "var(--pen)") +
          T(560, 450, "a próxima: ?", 36, "var(--ink)") + '</g>',
          "margin-top:auto"))

C6 = ('<div style="margin-top:110px"></div>'
      '<h1 style="font-size:78px">Segurar cuida da rolha.</h1>'
      '<h1 class="or" style="font-size:78px; margin-top:22px">Os outros quatro cuidam da garrafa.</h1>')


def check(y, txt):
    return ('<rect x="0" y="%d" width="52" height="52" rx="8" stroke="var(--ink)" stroke-width="4"/>' % (y - 40) +
            T(84, y, txt, 34, "var(--ink)", font="Inter"))


C7 = ('<h2>Pega a última prova. Marca o que você fez.</h2>' +
      svg(620,
          check(60, "Escolhi onda, companhia ou hora de chegar.") +
          check(160, "Mudei algo no local: lugar, aquecimento.") +
          check(260, "Decidi antes pra onde olhar no trecho.") +
          check(360, "Decidi antes como ler o peso.") +
          check(460, "Segurei. Em que km? Anota do lado.") +
          T(888, 580, "só a última ganhou um x? a sua prova teve um lugar só.", 36, "var(--pen)", "end", rot=-2),
          "margin-top:50px"))

C8 = paraquem("Para quem é isso, e para quem não é.",
    "você treina bem, larga bem e, no km que pesa, a sua única jogada é apertar a rolha até o fim.",
    "o peso vem junto com dor no peito, tontura ou falta de ar: procure um médico. Se segurar tudo também é como você atravessa os dias fora da corrida, procure um psicólogo.")

C9 = ('<div style="margin-top:50px"></div>'
      '<h1 style="font-size:76px">O km só tira a rolha.</h1>'
      '<h1 class="or" style="font-size:76px; margin-top:18px">A garrafa foi sacudida antes.</h1>'
      '<p class="mu" style="margin-top:40px">Comenta A ou B: o que você fazia até hoje no km que pesa. E manda pra quem responderia o contrário.</p>' +
      svg(220,
          '<rect x="20" y="40" width="848" height="110" rx="55" stroke="var(--ink)" stroke-width="4"/>' +
          T(80, 110, "Adicione um comentário...", 34, "var(--mu)", font="Inter") +
          '<g transform="rotate(-6 700 95)"><rect x="620" y="56" width="80" height="80" rx="12" stroke="var(--pen)" stroke-width="4" style="fill:var(--hl)"/>' +
          T(660, 114, "A", 50, "var(--ink)", "middle", font="Inter", weight=800) +
          '<rect x="730" y="56" width="80" height="80" rx="12" stroke="var(--pen)" stroke-width="4" style="fill:var(--hl)"/>' +
          T(770, 114, "B", 50, "var(--ink)", "middle", font="Inter", weight=800) + '</g>' +
          T(715, 205, "qual é a sua?", 38, "var(--pen)", "middle", rot=-3),
          "margin-top:30px"))

VC = [("dark", C1, True), ("light", C2, False), ("dark", C3, False), ("light", C4, False), ("dark", C5, False),
      ("light", C6, False), ("dark", C7, False), ("light", C8, False), ("dark", C9, True)]

VERSOES = {"A": VA, "B": VB, "C": VC}


LEGENDAS = {"A": """Repara no seu próximo longão: em que momento ele começa a ficar pesado? Não no fim. Antes. Na hora em que você acorda, no trânsito até o parque, no grupo que saiu forte demais.

Muito do que pesa lá na frente entrou bem antes, quando ainda era pequeno. Lá atrás, mexer custa pouco. No fim, só sobra apertar.

Um teste pro próximo treino longo: escolhe um registro só. Pode ser com quem você vai correr, a hora de sair de casa ou pra onde vai olhar quando o trecho apertar. Decide isso na véspera, escreve numa linha e confere depois do treino.

Não precisa mexer em tudo. Um registro bem decidido já tira a fita do posto de única ferramenta.

Salva pra rever na véspera do próximo longão e escolher o seu registro.

Quer enxergar o seu padrão inteiro? Diagnóstico grátis no link do perfil.""",
"B": """Sabe a foto oficial da corrida? Aquela em que você aparece inteiro, quase sorrindo, justo no trecho em que por dentro estava tudo gritando?

A foto mostra o que você segurou. Não mostra o que você sentiu, nem quanto custou manter a cara no lugar.

Segurar dá conta do que aparece. O que você sente continua do mesmo tamanho, e ainda pede esforço pra ficar escondido. Num trecho que já pede tudo, isso pesa.

No próximo treino de tiros, faz um teste simples: repara no primeiro sinal de peso. Onde ele apareceu? No aquecimento? No terceiro tiro? Antes de sair de casa? Anota no celular assim que terminar.

Manda pra quem tem a melhor cara de foto da assessoria e chega em casa destruído.

Tem uma avaliação sem custo te esperando na bio, pra mapear de onde vem esse aperto.""",
"C": """Uma pergunta antes da próxima inscrição: você escolhe a prova só pelo percurso e pela data?

A prova, a onda de largada, quem vai com você no carro, a hora de chegar ao local. Tudo isso mexe no quanto a garrafa vai estar sacudida quando o km apertar. E é ali que mexer custa menos.

Quando você chega no trecho difícil, sobra pouca coisa: pra onde olhar, como ler o que tá sentindo e, por último, segurar.

Exercício pra próxima prova: na semana anterior, escreve três escolhas que você ainda pode fazer. Com quem vai? Que horas sai de casa? Em que lugar do curral fica? Só três. Decide com calma, longe do dia.

Comenta aqui embaixo: A ou B? E conta em que km a garrafa costuma estourar.

Pra entender o resto do seu mapa mental, o teste grátis mora no endereço do perfil.""",
}
