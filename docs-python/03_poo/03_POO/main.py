from person import Test, Character

p1 = Test()
p2 = Test()

# Você pode modificar um objeto, mesmo após ter sido instanciado.
p1.text = "Hey... Where am I?"

print(p1.text)

p1 = Character("Jake"        , "Jake"        , "none"        , "dog"     , 28    , "male")
p2 = Character("Finn"        , "Finn"        , "Mertens"     , "human"   , 12    , "male")
p3 = Character("Ice King"    , "Simon"       , "Petrikov"    , "human"   , 1043  , "male")
p4 = Character("Marceline"   , "Marceline"   , "Abadeer"     , "vampire" , 1000  , "female")

p4.when_i_was_created()

Character.random_speaking()
Character.random_speaking()
Character.speaking()
