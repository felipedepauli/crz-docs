# Funções de Perda


- Mean Squeared Error
- Categorical Cross-Entropy
- Dice Loss
- IoU (Intersection over Union) / Jaccard Loss
- Focal Loss
- Losses Combination


### Entropia Cruzada (Cross-Entropy Loss)

- **Descrição:** Mede o desempenho de um modelo de classificação cuja saída é uma probabilidade entre 0 e 1. A perda aumenta à medida que a previsão probabilística diverge do rótulo verdadeiro.
- **Tipo de ML:** Classificação supervisionada.
- **Exemplo de Aplicação:** Usada em classificação de múltiplas classes, como identificar a raça de um cão em uma foto.

### Erro Quadrático Médio (Mean Squared Erros - MSE)

- **Descrição:** Calcula a média dos quadrados das diferenças entre os valores previstos e os valores reais.
- **Tipo de ML:** Regressão supervisionada.
- **Exemplo de Aplicação:** Previsão do preço de casas com base em características como tamanho e localização.

### Erro Absoluto Médio (Mean Absolute Error - MAE)

- **Descrição:** Semelhante ao MSE, mas usa o valor absoluto da diferença entre previsões e valores reais, o que o torna menos sensível a outliers do que o MSE.
- **Tipo de ML:** Regressão supervisionada.
- **Exemplo de Aplicação:** Previsão de vendas onde as discrepâncias ocasionais não devem influenciar fortemente a perda geral.

### Hinge Loss

- **Descrição:** Usada principalmente para "Support Vector Machines" (SVMs) e alguns tipos de classificação "one-vs-all". É útil quando se tem rótulos de classes que são +1 e -1.
- **Tipo de ML:** Classificação supervisionada.
- **Exemplo de Aplicação:** Classificação de sentimentos onde as entradas são classificadas como positivas ou negativas.

### Log Loss

- **Descrição:** Uma variação da entropia cruzada para classificação binária.
- **Tipo de ML:** Classificação binária supervisionada.
- **Exemplo de Aplicação:** Previsão de se um e-mail é spam ou não.

## Dice Loss

- **Descrição:** Uma função de perda baseada na métrica Dice Coefficient, usada para quantificar a similaridade entre previsões e rótulos verdadeiros, especialmente útil para dados desbalanceados.
- **Tipo de ML:** Segmentação de imagens supervisionada.
- **Exemplo de Aplicação:** Segmentação de tumores em imagens médicas.

## Contrastive Loss / Triplet Loss

- **Descrição:** Usada para aprender embeddings, onde o objetivo é garantir que exemplos semelhantes estejam próximos uns dos outros no espaço de embedding, enquanto exemplos diferentes estão distantes.
- **Tipo de ML:** Aprendizado de máquina supervisionado e semi-supervisionado para tarefas de aprendizado de métrica.
- **Exemplo de Aplicação:** Reconhecimento facial, onde queremos que as imagens da mesma pessoa tenham embeddings semelhantes.