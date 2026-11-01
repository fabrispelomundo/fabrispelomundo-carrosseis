# Publicação — uma pasta por dia

Cada pasta é um carrossel pronto para o Instagram Fabris Pelo Mundo, publicado às 11h45 (America/Sao_Paulo) da data no nome da pasta.

```
publicacao/
  AAAA-MM-DD/
    01.jpg … 09.jpg   slides na ordem de postagem (1080×1350, JPEG qualidade 95)
    legenda.txt       legenda publicada palavra por palavra
```

## Como funciona

- A tarefa "Publicação diária · carrossel Fabris Pelo Mundo" roda todo dia às 11h45. Se existir `publicacao/HOJE/`, ela confere as 9 imagens pelo link raw do GitHub e publica com a legenda de `legenda.txt`.
- Se não existir pasta para o dia, ela produz o carrossel a partir da primeira pauta "na fila" completa de `pautas/fila-de-pautas.md`, seguindo `pautas/regras.md`, grava a pasta aqui e então publica.
- Para trocar o carrossel de um dia, substitua os arquivos da pasta (mesmos nomes) antes das 11h45. Para tirar um dia da agenda, apague a pasta.

## Pedidos em lote

Um pedido como "crie mais 15 carrosséis" ocupa as datas logo depois da última pasta existente, um carrossel por dia, sem pular datas. Cada carrossel novo segue `pautas/regras.md` (capa alternada a partir da "Próxima capa" de `pautas/fila-de-pautas.md`). As pautas usadas são marcadas como "agendado (DD/MM/AAAA)" na fila.

## Agenda atual

01/11/2026 a 03/12/2026: os 33 carrosséis do plano de recriação (detalhes em `pautas/fila-de-pautas.md`).
