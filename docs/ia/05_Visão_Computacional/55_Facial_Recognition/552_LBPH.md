# LBPH (Local Binary Patterns Histograms)

# Capítulo: Introdução ao Algoritmo Local Binary Patterns (LBP) Aplicado ao Reconhecimento Facial

O reconhecimento facial é uma das áreas mais populares e desafiadoras da visão computacional. Entre os diversos algoritmos desenvolvidos para essa finalidade, o **Local Binary Patterns (LBP)** se destaca por sua simplicidade e eficácia. Este capítulo abordará os conceitos fundamentais desse algoritmo, exemplificando seu funcionamento e destacando sua robustez com relação a variações de iluminação, uma das maiores dificuldades no reconhecimento de faces.

## O Conceito Básico do LBP

Uma imagem é composta por pixels, que podem ser representados como uma matriz de valores numéricos. Cada pixel contém uma informação que representa sua intensidade luminosa ou cor. No caso de imagens em tons de cinza, que são as mais comumente utilizadas no LBP, cada pixel tem um valor entre 0 (preto) e 255 (branco).

O LBP opera sobre pequenos blocos de pixels em uma imagem, geralmente de tamanho 3x3. O objetivo é gerar um valor que descreva a textura local da imagem em torno de cada pixel. Para entender melhor, considere uma matriz 3x3 como a seguir, onde o número central (8) representa o pixel de interesse.

| 12  | 15  | 18  |  
| --- | --- | --- |  
| 3   | 8   | 5   |  
| 2   | 1   | 9   |  

No LBP, o valor do pixel central é comparado com os valores dos pixels ao seu redor. Se um pixel ao redor for maior ou igual ao pixel central, atribui-se o valor 1; caso contrário, atribui-se o valor 0. Aplicando essa regra, obtemos uma nova matriz de bits:

| 1 | 1 | 1 |  
|---|---|---|  
| 0 | - | 0 |  
| 0 | 0 | 1 |  

Os bits dessa matriz são concatenados para formar um número binário, que posteriormente pode ser convertido para um número decimal. No exemplo dado, o número binário seria `11100010`, que em decimal corresponde ao valor 226. Este valor representa a textura local ao redor do pixel central.

## Vantagem em Ambientes com Diferentes Iluminações

Uma das grandes vantagens do LBP é sua robustez em relação à iluminação. Considere duas imagens da mesma pessoa, uma em um ambiente claro e outra em um ambiente escuro. Embora a intensidade luminosa dos pixels possa variar significativamente, a estrutura de comparação entre os valores dos pixels vizinhos tende a se manter constante. Isso significa que, mesmo que a intensidade global da imagem varie, o LBP ainda será capaz de extrair características consistentes para o reconhecimento.

Por exemplo, se os valores dos pixels em uma imagem mais clara forem 42, 55, 48 (substituindo os valores da matriz anterior), o algoritmo ainda produzirá um padrão binário semelhante. O resultado binário seria o mesmo: `11100010`, correspondendo ao valor decimal 226. Esse comportamento é o que faz do LBP um algoritmo robusto contra variações de iluminação.

## Criação de Histogramas e Extração de Características

Uma imagem facial pode ser dividida em vários blocos menores, onde o LBP é aplicado a cada um deles. Por exemplo, uma imagem 6x6 pode ser subdividida em 36 blocos, com cada bloco contendo um conjunto de pixels. Dentro de cada bloco, o algoritmo gera um valor binário para cada pixel central, conforme explicado anteriormente.

Após aplicar o LBP em todos os blocos da imagem, é possível gerar um histograma para cada um deles. Um **histograma** é uma representação estatística que descreve a distribuição dos valores numéricos (neste caso, os valores gerados pelo LBP) dentro de uma determinada área da imagem. Assim, o histograma de uma região que contém o olho de uma pessoa será diferente do histograma de uma região que contém o fundo da imagem ou o nariz, por exemplo.

Essa técnica de subdivisão permite que o LBP capture as características locais da face, como a textura ao redor dos olhos, nariz e boca. O reconhecimento facial, então, compara os histogramas gerados a partir de diferentes regiões da face da pessoa. Se os histogramas de uma nova imagem forem semelhantes aos histogramas da imagem de referência, o algoritmo poderá concluir que as duas imagens pertencem à mesma pessoa.

## Comparação de Histogramas para Reconhecimento Facial

Uma vez gerados os histogramas para uma imagem facial, o próximo passo é a classificação. Dada uma nova imagem de uma pessoa, os histogramas dessa nova imagem são comparados com os histogramas previamente armazenados no sistema. A similaridade entre os histogramas é avaliada para determinar a probabilidade de que a nova imagem seja da mesma pessoa.

Por exemplo, se o histograma da região do olho da nova imagem for muito semelhante ao histograma da mesma região da imagem de referência, isso aumenta a chance de que ambas as imagens pertençam à mesma pessoa. Esse método de comparação entre histogramas locais torna o algoritmo LBP uma ferramenta poderosa para reconhecimento facial, mesmo em condições desafiadoras.

## Limitações do LBP

Embora o LBP seja robusto em termos de iluminação, ele tem suas limitações. Uma delas é a incapacidade de capturar informações globais da imagem, pois o algoritmo opera localmente em pequenos blocos. Isso pode ser um problema quando as variações faciais ocorrem em grande escala, como mudanças na pose da cabeça ou expressões faciais exageradas.

Além disso, o LBP pode ser sensível a ruídos em uma imagem. Pequenas variações nos valores dos pixels, causadas por ruído ou baixa qualidade da imagem, podem alterar o valor binário gerado e, consequentemente, modificar o histograma da região.

## Conclusão

O **Local Binary Patterns (LBP)** é um algoritmo simples, porém eficaz, para extração de características faciais, especialmente útil em condições de variação de iluminação. Ao comparar histogramas locais gerados a partir de diferentes regiões da face, o LBP pode identificar pessoas com alta precisão, mesmo quando as imagens apresentam mudanças nas condições de luz. Embora tenha limitações, como sensibilidade a ruídos e incapacidade de capturar variações globais da face, ele continua sendo uma escolha popular em sistemas de reconhecimento facial. Em capítulos futuros, serão discutidos algoritmos complementares que podem mitigar algumas dessas limitações e melhorar a precisão do reconhecimento facial.
