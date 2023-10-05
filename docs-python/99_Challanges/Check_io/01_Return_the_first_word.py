# From a string input, create a function that returns the first word in the string.

# SOLUTION 1
# Esta solução é bem ruim. Dá uma comparada no tempo dele com os outros métodos.
# Ela pega o vetor inteiro, mas inteiro mesmo, e separa todo mundo. Depois disso, retorna apenas o primeiro elemento.
def first_word_1 (str):
    return str.split(" ")[0]

# SOLUTION 2
# Aqui a gente já é mais inteligente. A gente pega somente a primeira palava mesmo. Usamos o find para isso.
def first_word_2 (str):
    index = str.find(" ")
    return str[:index] if index != -1 else str # no caso de haver apenas uma palavra, a gente retorna ela mesmo.

# SOLUTION 3
# Aqui a gente busca o índice que contém o espaço. Como pode ser que a string tenha apenas uma palavra, é necessário
# utilizar o try e except para evitar erros.
def first_word_3 (str):
    try:
        index = str.index(" ")
        return str[:index]
    except ValueError:
        return str

# SOLUTION 4
# Que tal fazer em uma linha?
first_word_4 = lambda str: str.split(" ")[0]


from timeit import timeit as t

# print ("----------------------------------------------------")
# print(t('first_word_1(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~11.7 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~6.1 ms
# print(t('first_word_1(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~90928.2 ms
# print(t('first_word_1(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~5562.9 ms
# print ("----------------------------------------------------")

print ("----------------------------------------------------")
print(t('first_word_2(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~6.3 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~4.7 ms
print(t('first_word_2(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~7.0 ms
print(t('first_word_2(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2108.4 ms
print ("----------------------------------------------------")

print ("----------------------------------------------------")
print(t('first_word_3(x)', setup='x = "asdf we"*10', number=10000, globals=globals()))       #  ~5.8 ms
print(t('first_word_3(x)', setup='x = "asdfawe"*10', number=10000, globals=globals()))       #  ~8.5 ms
print(t('first_word_3(x)', setup='x = "asdf we"*100000', number=10000, globals=globals()))   #  ~5.8 ms
print(t('first_word_3(x)', setup='x = "asdfawe"*100000', number=10000, globals=globals()))   #  ~2005.8 ms
print ("----------------------------------------------------")

# So what conclusions can be made from all of this?

# 1.Since every string is an instance of the string class, it's preferred to use its methods rather than implement
# a new function which seems to be faster. It won't work faster in most of the cases. Compare first_word_2 and
# first_word_4 for example.

# 2.Despite the fact first_word_1 (which uses .split() method) looks nice and concise it works worse with long strings
# than first_word_2 and first_word_3 do(they use .find() and .index() methods respectively). Especially in case there are
# lots of spaces in the text.

# 3.str.index() method works a bit faster than str.find() but only in case there is a space in the text. Otherwise it's
# needed to handle an exception which takes some extra time. 

# Thus, I'd use str.find() method in such kind of tasks.


# Testando a solução 4
assert  first_word_4("asdf we") == "asdf"
assert  first_word_4("asdf we we") == "asdf"
assert  first_word_4("asdf we we we") == "asdf"