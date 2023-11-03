# Funções de Otimização

- **SGD (Stochastic Gradient Descent):** Este é o otimizador mais simples e tem um único parâmetro de taxa de aprendizado. Ele pode ser mais estável do que Adam em alguns casos, mas geralmente requer mais tempo e cuidado para sintonizar a taxa de aprendizado e pode precisar de um scheduler de taxa de aprendizado para convergir de forma eficaz.

- **RMSprop:** Semelhante ao Adam, o RMSprop também ajusta a taxa de aprendizado para cada parâmetro, mas não tem o viés de correção que o Adam tem. Pode ser uma boa escolha se o Adam estiver causando instabilidade no treinamento.

- **Adagrad:** Este otimizador ajusta a taxa de aprendizado com base na frequência com que um parâmetro é atualizado, o que pode ser útil para dados esparsos. No entanto, ele pode ser menos eficaz para treinamento de redes profundas, pois a taxa de aprendizado pode diminuir muito rapidamente.

- **Adadelta:** Uma extensão do Adagrad que busca reduzir seu agressivo, monótono decréscimo da taxa de aprendizado. É mais robusto e não requer uma taxa de aprendizado a ser definida.

- **Nadam:** Combina o Adam com o Nesterov momentum, o que pode ajudar a acelerar o treinamento em algumas situações.

- **L-BFGS:** Um otimizador baseado em quase-Newton métodos, mais adequado para problemas de pequena e média escala devido ao seu alto custo computacional e requisitos de memória.