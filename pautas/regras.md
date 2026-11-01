# Regras de produção — carrosséis Fabris Pelo Mundo

Este arquivo reúne todas as regras que valem para escrever, desenhar, renderizar e publicar os carrosséis. Ele junta o antigo documento de pautas do projeto, o padrão visual e o prompt da antiga tarefa de produção diária. Se algo aqui conflitar com um arquivo de `referencia/`, este arquivo vale.

---

## 1. Marca e público

- A marca é sempre **Fabris Pelo Mundo**. Nunca escrever "Coach Fabris" nem usar @coachfabris em nada: slides, legendas, publicação ou análise.
- Publicação no perfil do Instagram Fabris Pelo Mundo. No Windsor.ai é o connector `instagram`, conta `17841400300251197` (fabrispelomundo). A conta coachfabris nunca é usada.
- Fabris é especialista em performance mental para atletas amadores adultos de endurance (corrida de rua, trail e triatlo), de 25 a 35 anos.
- O carrossel mostra como o Fabris pensa: estrutura minimalista e ciência do esporte em linguagem acessível. Ele não explica o método, não nomeia a VYRA e não diz o que o Fabris vende. O leitor deduz o trabalho.

## 2. Ritmo de publicação

- **1 carrossel por dia, às 11h45 (America/Sao_Paulo).** A tarefa "Publicação diária · carrossel Fabris Pelo Mundo" publica a pasta `publicacao/AAAA-MM-DD/` do dia.
- Se não houver pasta para o dia, a tarefa produz o carrossel a partir da primeira pauta "na fila" de `fila-de-pautas.md` que tiver material suficiente, seguindo estas regras.
- Se não houver pasta nem pauta utilizável, nada é publicado e o Fabris recebe um aviso. **Nunca publicar carrossel genérico para preencher.**
- Quando sobrarem menos de 3 dias cobertos (pastas futuras mais pautas completas na fila), o Fabris recebe um aviso.

## 3. Voz

- Segunda pessoa, de igual para igual e calorosa, como o Fabris falando sobre o assunto em diálogo com o leitor ("imagine", "perceba", "repara" e parecidos).
- **Decisão de 30/10/2026:** o texto fica um pouco mais informal, com expressões como "repara nisso aqui", "já parou pra pensar", "olha isso" e "se liga nessa parte". Também entram sequências curtas de perguntas que afunilam e pedem uma resposta específica (por exemplo: qual prova? em que km? o que veio na cabeça?).
- Frases curtas, uma ideia por linha.
- Nada de frase motivacional ("acredite no processo", "mentalidade de campeão"…). Se a frase caberia num pôster de academia, corte.
- Nada de linguagem clínica ("ansiedade de desempenho", "trauma", "regulação emocional"). Descreva o comportamento, não o rótulo.
- Nunca prometer resultado físico (pace, VO2, marca).
- **Jamais citar nomes de autores, estudos ou referências bibliográficas**, nem nos slides nem na legenda. Nada de "fulano mostrou", "segundo o estudo X" ou lista de fontes. A fonte de cada pauta serve só para a pesquisa interna e para garantir que nada é inventado.
- **Nada inventado:** nenhum caso, número, estudo ou observação que não esteja na fonte da pauta. Se não der para confirmar algo, corte.

## 4. Ganchos (slides 1 e 2)

- O slide 1 decide tudo. Aberturas que funcionam: um número concreto e estranho, uma contradição, "se eu começasse do zero", uma conta que o atleta faz de cabeça.
- Desde 30/10/2026 os ganchos vêm em forma de pergunta. Há três tipos em teste:
  - **A · pergunta para você** (uma cena concreta). Corpo clássico de 3 alavancas. CTA: salvar.
  - **B · pergunta-enigma** ("por que…?"). Corpo no formato "parece × acontece". CTA: mandar para outro corredor.
  - **C · escolha A ou B.** Corpo em quiz, com checklist no slide 7. CTA: comentar a letra e mandar.
- O slide 2 continua o gancho do slide 1 (laço aberto), em vez de abrir o enquadramento do zero.
- Categorias de engenharia social testadas desde 25/10/2026, em sequência: resultado / prova social → alerta / erro → curiosidade → praticidade.
  - **Alerta / erro:** "Pare de fazer X se você quer Y" · "O erro bobo que está destruindo o seu [resultado]" · "3 coisas que travam o seu [resultado] e você nem percebe" · "O motivo real está na tela 4".
  - **Curiosidade:** "O que ninguém te conta sobre…" · "Se eu estivesse começando hoje, eu faria exatamente isto:" · "Eu descobri como [resultado] em 3 passos".
  - **Resultado / prova social:** "Como eu saí de X e cheguei a Y" · "O passo a passo para [meta]". **Só com caso e número reais enviados pelo Fabris.** Sem esse material, pule a categoria e use a próxima.
  - **Praticidade:** "Guarde este carrossel se…" · "O checklist essencial para quem…" · "3 atalhos para…".
- Ganchos que pedem dado específico (resultado, caso, número) só são escritos com o material real enviado pelo Fabris.
- Ficam de fora: "segredo que os profissionais não querem que você saiba", "copie e cole minha estratégia", "guia definitivo", "como meu cliente faturou", "ferramenta secreta". Eles prometem resultado ou exigem informação inventada.

## 5. Estrutura dos 9 slides

1. Gancho
2. Continuação do gancho / enquadramento
3. Mecanismo: alavanca 1
4. Mecanismo: alavanca 2
5. Mecanismo: alavanca 3 (ou ponte, se forem só 2 alavancas)
6. Síntese
7. Autodiagnóstico: uma conta ou pergunta que o leitor responde agora, com os próprios dados
8. Para quem é e para quem não é (o que isso não resolve)
9. Frase final com CTA de salvar, mandar para outro corredor ou comentar

## 6. Visual

- Modelo oficial: `pautas/modelo.html`. O CSS fica intacto; só mudam os textos e os desenhos. O código dos 33 carrosséis em `referencia/r33/base.py` é a versão mais recente desse CSS e serve de base.
- Tamanho 1080×1350. Os slides alternam folha clara (#F1ECE3) e folha escura (#111111, com gradiente radial).
- Fontes: Inter (já instalada no sistema) e a manuscrita 'Pen' (`_assets/pen.woff2` e `_assets/pen-ext.woff2`). Laranja como caneta: #F0640F na folha clara, #FF7A1A na escura. Marca-texto laranja (`.hl`), palavra circulada à mão (`.circ`) e anotação manuscrita (`.note`, `.pen`).
- Topo: só a numeração ("03 / 09"). Rodapé: só "arraste →" manuscrito, exceto no slide 9 e onde vai a logo.
- **Sem exceção:** nada de título pequeno (kicker) em laranja no topo e nenhuma referência ou nota em cinza pequeno. O slide abre direto no título grande.
- Logo (o bonequinho cobre/prata correndo): `_assets/logo.png`, no slide 1 e no slide 9, em left:474px; top:1206px; width:138px; height:106px (detalhes em `_assets/README.md`). Não baixar fonte nem logo de outro lugar. Nenhuma assinatura "COACH FABRIS" (essa assinatura do padrão antigo foi abandonada).
- **Capa alternada:** cada carrossel abre com a cor oposta à capa do último carrossel registrado. A cor da próxima capa fica no fim de `fila-de-pautas.md`.

## 7. Desenhos

Não há fotos: tudo é desenhado à caneta. O desenho precisa trabalhar, gerando **surpresa**, **polêmica** ou **engenharia reversa** (o leitor decifra o desenho para entender a ideia).

| Slide | Desenho |
|---|---|
| 1, 2, 5 e 8 | Desenho criativo: surpresa, polêmica ou engenharia reversa |
| 3 | Gráfico, framework, mapa mental ou o que melhor encaixar |
| 4 | Gráfico |
| 6 e 7 | O que melhor encaixar no contexto |
| 9 | Visual provocativo reforçando o CTA |

Recursos que funcionam:

- a resposta desenhada antes da pergunta;
- uma conta ou um gráfico incompleto que o leitor termina de cabeça;
- desproporção proposital (causa minúscula, reação enorme);
- dois desenhos idênticos com legendas diferentes;
- algo familiar riscado, rasgado ou fora do lugar (relógio, troféu, planilha, placa, bilhete).

Limite: o desenho provoca, mas não engana. **Um gráfico sem dado real mostra só a direção do que a fonte diz, sem números nos eixos.**

Desenhos já usados (evite repetir): pavio aceso desde cedo até a bomba do km 7; checklist que esquece "o dia que veio antes"; placa KM 15 pichada "de novo?"; um interruptor acendendo quatro lâmpadas; contagem de cela com 50 riscos; bilhete emitido antes da largada; pórtico "a história começa aqui"; cronômetro da prova parado e o da história rodando; GPS "destino não encontrado"; previsão do tempo "dor, chance alta"; cola escrita no braço; "do nada" riscado para "do dia"; marcadores de combustível; "a prova, versão 7"; urna em que o estômago já votou; cédula marcada antes da pergunta acabar; carimbo "vai dar errado" riscado; retrovisor com placa de km; placa "calma" ao lado de um coração enorme; dois traçados de batimento iguais com nomes diferentes; etiqueta "medo" descolando de "pronto"; número de peito "nervoso" corrigido para "pronto"; arquibancada vazia com uma pessoa sem rosto; balão de fala sem dono; relógio de pulso como juiz; envelope "devolver ao remetente"; megafone sem ninguém segurando; relógio com "FRACO" no visor; "letra miúda" sob a lupa; troféu "1º lugar: mais duro consigo mesmo"; botão minúsculo ligado a uma explosão; relógio com alvo "o pace dele"; placa "proibido ultrapassar" riscada; caderno de treino "quem correu aquele km?"; dois números de peito "EU" e "EU?"; crachá rasgado mostrando o verso; caixa de achados e perdidos; medalha "para: você inteiro"; dois corações com o mesmo batimento e encanamentos diferentes; balança com "provar que eu aguento" pesando no prato da prova; calendário com o longão empurrado e crescendo; ciclo adiar → alívio; tabela "eu achei × aconteceu"; cinco alavancas com a última minúscula; controle remoto com o botão "segurar" gasto; troféu com etiqueta "sorte" descolando; quadro 2×2 "em você / fora × fica / muda"; dois troféus iguais "sorte" × "o que eu fiz"; balões "para um amigo" × "para você"; caderno com a página da prova grampeada; tribunal com a perna pesada no banco dos réus e a cadeira do juiz vazia; "perna pesada = dia perdido" riscado para "= perna pesada". Os 33 carrosséis de `referencia/r33/` também já usaram os desenhos que estão nos scripts.

## 8. Legenda

- Segunda pessoa, na voz do Fabris.
- Traz informação complementar ao carrossel, sem repetir os slides.
- Sem nomes de autores nem referências.
- Até 2.000 caracteres.
- A última linha leva ao diagnóstico completo e gratuito (link na bio), **sempre com palavras diferentes** das legendas anteriores.
- Grave em `legenda.txt`, que é publicada palavra por palavra.

## 9. Render e arquivos

- Monte o HTML com o CSS do modelo (ou com `referencia/r33/base.py`). Renderize cada slide em 1080×1350 com `_assets/render.py` (Playwright) e exporte em JPEG, qualidade 95.
- Grave a pasta `publicacao/AAAA-MM-DD/` com `01.jpg` a `09.jpg` e `legenda.txt`.
- Grave no EXIF DateTimeOriginal uma data de captura sequencial, 1 minuto por slide, a partir das 11h45 do dia da publicação.
- **Confira cada slide visualmente** antes de subir (uma folha de contato serve): texto cortado, sobreposição, logo, numeração e acentos na fonte manuscrita. Corrija e renderize de novo o que estiver errado.
- Antes do push, faça `git fetch origin main` e um rebase. Depois do push, confira com curl que cada URL `https://raw.githubusercontent.com/fabrispelomundo/fabrispelomundo-carrosseis/main/publicacao/AAAA-MM-DD/NN.jpg` responde 200 com image/jpeg.
- Depois de produzir, marque a pauta em `fila-de-pautas.md` como "produzida (DD/MM/AAAA)", acrescente a linha no registro de produção e atualize a "Próxima capa".

## 10. O que nunca fazer

- Usar a marca Coach Fabris ou a conta coachfabris.
- Citar autor, estudo ou referência nos slides ou na legenda.
- Inventar caso, número, estudo, observação ou dado em gráfico.
- Escrever um carrossel genérico para preencher um buraco na fila.
- Usar frase motivacional, linguagem clínica ou promessa de resultado físico.
- Explicar o método, nomear a VYRA ou vender.
- Pôr kicker laranja no topo, nota cinza ou referência pequena no slide.
- Usar foto ou imagem de banco: tudo é desenho à caneta.
- Publicar duas vezes o mesmo carrossel, ou tentar outro caminho de publicação quando o Windsor.ai der erro.
