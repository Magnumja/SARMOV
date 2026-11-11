# Fase 2 · Calibração e coleta

| Estado | Bimestres sugeridos | Atividades do cronograma | Depende de |
|---|---|---|---|
| Planejada | B2–B3 | 3. Coleta de dados; 4. Calibração de câmera | Fases 0 e 1 |

## Objetivo

Obter os parâmetros geométricos da câmera e as imagens brutas dos dois ambientes, com a distância real de cada imagem controlada registrada.

## Entregas

### Calibração

- [ ] Modo de captura fixado e documentado: resolução, estabilização desligada, foco travado ([Q5](../04-questoes-em-aberto.md#q5--modo-de-captura-e-validade-da-calibração))
- [ ] Padrão xadrez 8×6 com quadrados de 2 cm, impresso e colado em superfície rígida
- [ ] No mínimo 15 imagens do padrão: frontal e laterais de ±30°, de 15 cm a 1,5 m
- [ ] Matriz intrínseca `K` e coeficientes de distorção `(k1, k2, p1, p2)` salvos em arquivo versionado
- [ ] Erro de reprojeção RMS registrado

### Coleta controlada

- [ ] Suporte rígido montado; altura `h` e inclinação `α` medidas em três repetições, com média e desvio padrão
- [ ] Objetos posicionados a 1, 2, 3, 5, 7, 10, 12 e 15 m, aferidos com trena
- [ ] Variações por distância: quatro condições de iluminação, ângulo nominal e ±5°, posição horizontal central e ±15 cm
- [ ] Procedimento para Buraco e Irregularidade definido ([Q6](../04-questoes-em-aberto.md#q6--posicionamento-de-buracos-em-ambiente-controlado))
- [ ] Planilha de sessão: uma linha por imagem, com distância real, `h`, `α`, iluminação e arquivo de calibração usado
- [ ] No mínimo 500 imagens

### Coleta urbana

- [ ] Vídeos na Av. Afonso Pena e na Rua Aracy, às 7h, 12h, 17h e 20h, a 30 fps e no mínimo 1280×720
- [ ] Extração de quadros, evitando quadros consecutivos quase idênticos
- [ ] No mínimo 200 imagens

## Planejamento da coleta controlada

Dez imagens por distância somam 80 imagens; a meta é 500. A combinação completa das variações do plano resolve a diferença:

| Fator | Níveis |
|---|---|
| Distância | 8 |
| Iluminação | 4 |
| Ângulo | 3 |
| Posição horizontal | 3 |

São 288 combinações por objeto. Dois objetos de classes diferentes já ultrapassam a meta.

Esta tabela é uma leitura do plano, a confirmar com o orientador. O plano fala em variar o "ângulo (±5 em relação ao nominal)" e a posição horizontal em ±15 cm, sem dizer quantos níveis nem se o ângulo é a inclinação da câmera; aqui se supõem três níveis de cada. Se o ângulo variado for a inclinação, cada captura precisa ter seu `α` medido e registrado.

## Critérios de aceite

- Erro de reprojeção RMS inferior a 0,5 px, obtido no mesmo modo de captura usado na coleta.
- Toda imagem controlada tem distância real, `h`, `α` e arquivo de calibração associados.
- Volumes mínimos atingidos: 500 controladas e 200 urbanas.

## Riscos

| Risco | Mitigação |
|---|---|
| Calibração feita em modo diferente do usado na coleta | Fixar o modo antes de tudo; ponto de controle PC1 |
| Suporte se move entre capturas e invalida `h` e `α` | Medir no início e no fim de cada sessão; descartar a sessão se houver diferença |
| Coleta noturna com pouca qualidade | Registrar como condição de falha a ser analisada, sem descartar |
| Rostos e placas nas imagens urbanas | Dados brutos fora do repositório; anonimizar antes de publicar ([Q9](../04-questoes-em-aberto.md#q9--privacidade-das-imagens-urbanas)) |

## Contribuição para o artigo

Seção de materiais e métodos: protocolo de coleta, tabela de parâmetros de calibração e erro de reprojeção. A planilha de sessão é a referência de verdade para todas as métricas de distância.

## Relatório de encerramento

_A preencher ao concluir a fase._
