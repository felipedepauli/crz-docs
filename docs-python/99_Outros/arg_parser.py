import argparse
# Existem dois tipos de argumentos:
#   1. Posicionais (obrigatórios)
#   2. Optativos (ativam códigos caso sejam passadas)

# Antes de qualquer coisa
# Criar o parser!

parser = argparse.ArgumentParser()

# 1. POSICIONAIS
# Os posisionais não possuem -- na frente do nome do argumento. Você pode dar o nome que quiser, já que o primeiro argumento será atribuído ao primeiro add_argument, e segundo argumento ao segundo add_argument, e assim por diante.

parser.add_argument("a_number_1", help="Digite um número qualquer.", type=int)
parser.add_argument("a_number_2", help="Digite um número qualquer.", type=int)

# 2. OPTATIVOS
# Já os optativos precisam iniciar com --. Feito isso, você pode ou não usá-los. Se eles não aparecerem no linha de comando, o interpretador não irá causar um erro.
# Existem duas opções de argumento optativos: com argumento adicional ou sem (somente eles por eles)
parser.add_argument("--idade", help="Digite sua idade")
parser.add_argument("--quem",  help="Testa, doidão!!", action="store_true")
# Se quiser pode usar as short versions:
parser.add_argument("-v", help="Verbose Mode", action="store_true")
# Quando usar shorts, é interessante utilizar o dest para indicar qual será o nome do atributo dentro de args que receberá o valor.
parser.add_argument("-e", dest="evento", help="Quando for um evento.")

#######################################
# Agora tá na hora de parsear

args = parser.parse_args()

print(f'Dae rapeize: {args.a_number_1}')
print(f'Dae rapeize: {args.a_number_2}')

if args.quem:
    print("perguntou?")

if args.idade:
    print("Idade:", args.idade)

if args.v:
    print("Verboso é o caraleo =D")

if args.evento:
    print(f"É um evento cujo nome é {args.evento}")