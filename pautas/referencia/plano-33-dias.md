# Plano 33 dias — recriação das 11 pautas de baixo alcance (criado em 30/10/2026)

Decisão do Fabris (30/10/2026): manter os 5 posts de maior alcance, arquivar os outros 11 carrosséis e recriar os mesmos temas com ganchos novos (todos em forma de pergunta), palavras e desenhos novos. 3 versões por pauta, 1 carrossel por dia, 33 dias. A cada 11 dias as pautas voltam em outra versão, em outra ordem e com a cor da capa trocada. Legendas escritas (LEGENDAS em cada pNN.py).

Status (30/10/2026): rodada 2 aprovada pelo Fabris (voz levemente mais informal, perguntas que afunilam e pedem resposta específica). Produção final pronta: 33 pastas com 9 JPEGs + legenda.txt entregues em zip em 30/10. Início das publicações: 30/10 à tarde. Ainda não subidos ao GitHub nem agendados.

## Tipos de gancho (teste)
- A · pergunta para você (cena concreta) · corpo clássico 3 alavancas · CTA salvar
- B · pergunta-enigma ("por que…?") · corpo "parece × acontece" · CTA mandar para outro corredor
- C · escolha A ou B · corpo em quiz + checklist no slide 7 · CTA comentar a letra e mandar

## Calendário 30/10 a 01/12/2026 · 1 carrossel por dia

| Dia | Data | Pasta | Pauta | Versão | Capa |
|---|---|---|---|---|---|
| 1 | 30/10 | 2026-10-30_D01_P01A_no-estomago | P01 | A | escura |
| 2 | 31/10 | 2026-10-31_D02_P02A_ultrapassagem | P02 | A | clara |
| 3 | 01/11 | 2026-11-01_D03_P03A_semana-que-vem | P03 | A | escura |
| 4 | 02/11 | 2026-11-02_D04_P04A_trecho-que-pesa | P04 | A | clara |
| 5 | 03/11 | 2026-11-03_D05_P05A_naquele-km | P05 | A | escura |
| 6 | 04/11 | 2026-11-04_D06_P06A_largada-calma | P06 | A | clara |
| 7 | 05/11 | 2026-11-05_D07_P07A_depois-da-chegada | P07 | A | escura |
| 8 | 06/11 | 2026-11-06_D08_P08A_pace-caiu | P08 | A | clara |
| 9 | 07/11 | 2026-11-07_D09_P09A_vou-mostrar | P09 | A | escura |
| 10 | 08/11 | 2026-11-08_D10_P10A_voz-que-cobra | P10 | A | clara |
| 11 | 09/11 | 2026-11-09_D11_P11A_antes-do-km | P11 | A | escura |
| 12 | 10/11 | 2026-11-10_D12_P05B_naquele-km | P05 | B | clara |
| 13 | 11/11 | 2026-11-11_D13_P03B_semana-que-vem | P03 | B | escura |
| 14 | 12/11 | 2026-11-12_D14_P04B_trecho-que-pesa | P04 | B | clara |
| 15 | 13/11 | 2026-11-13_D15_P02B_ultrapassagem | P02 | B | escura |
| 16 | 14/11 | 2026-11-14_D16_P06B_largada-calma | P06 | B | clara |
| 17 | 15/11 | 2026-11-15_D17_P08B_pace-caiu | P08 | B | escura |
| 18 | 16/11 | 2026-11-16_D18_P09B_vou-mostrar | P09 | B | clara |
| 19 | 17/11 | 2026-11-17_D19_P10B_voz-que-cobra | P10 | B | escura |
| 20 | 18/11 | 2026-11-18_D20_P01B_no-estomago | P01 | B | clara |
| 21 | 19/11 | 2026-11-19_D21_P07B_depois-da-chegada | P07 | B | escura |
| 22 | 20/11 | 2026-11-20_D22_P11B_antes-do-km | P11 | B | clara |
| 23 | 21/11 | 2026-11-21_D23_P06C_largada-calma | P06 | C | escura |
| 24 | 22/11 | 2026-11-22_D24_P02C_ultrapassagem | P02 | C | clara |
| 25 | 23/11 | 2026-11-23_D25_P08C_pace-caiu | P08 | C | escura |
| 26 | 24/11 | 2026-11-24_D26_P09C_vou-mostrar | P09 | C | clara |
| 27 | 25/11 | 2026-11-25_D27_P04C_trecho-que-pesa | P04 | C | escura |
| 28 | 26/11 | 2026-11-26_D28_P01C_no-estomago | P01 | C | clara |
| 29 | 27/11 | 2026-11-27_D29_P05C_naquele-km | P05 | C | escura |
| 30 | 28/11 | 2026-11-28_D30_P07C_depois-da-chegada | P07 | C | clara |
| 31 | 29/11 | 2026-11-29_D31_P11C_antes-do-km | P11 | C | escura |
| 32 | 30/11 | 2026-11-30_D32_P03C_semana-que-vem | P03 | C | clara |
| 33 | 01/12 | 2026-12-01_D33_P10C_voz-que-cobra | P10 | C | escura |

## Arquivos
- Código dos slides: `claude/r33/base.py` (CSS + helpers; inclui a regra `.content > .lab:first-child` que transforma rótulo de topo em linha de título) e `claude/r33/pNN.py` (cada um define VERSOES = {"A","B","C"}, 9 tuplas (tema, html, logo)).
- Render: copiar base.py e pNN.py para uma pasta com logo.png, pen.woff2, pen-ext.woff2 e render.py do repositório (_assets/), montar o HTML com `base.build_html(VERSOES[v], caminho)` e rodar `render.py`.
- Fonte de cada pauta: a mesma da fila em claude/pautas-carrossel.md (P04 e P07 vêm de VYRA 2 e VYRA 4: condicionamento/memória emocional/hábito/previsão; atribuição/ruminação/reconsolidação).

## Pendências
- Fabris revisar o PDF; escrever legendas; decidir se a tarefa diária de 20h47 (3 por dia da fila) é pausada ou adaptada para 1 por dia seguindo este calendário.
- Push no GitHub segue bloqueado na tarefa agendada (repositório fora das fontes).
