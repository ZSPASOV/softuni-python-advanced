a = (i for i in range(5))
print(type(a))
# <class 'generator'> - vrushta generator, koito moje da bude obhoden
for item in a:
    print(item)
#0
# 1
# 2
# 3
# 4



for item in a:
    print(item)
# ne printira nishto
# generatorite kato budat obhodeni 1 put ostavat prazni

# da vidq za eager evaluated i lazy evaluated
# lists sa eagerly evaluated, generators sa lazy evaluated

# vsqka funkciq stava lazy/generator ako izpolzvame vmesto return kliu4ovata duma yield