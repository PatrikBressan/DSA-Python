# Exercício 2 - Reescreva o código abaixo, usando a função map(). O resultado final deve ser o mesmo!
palavras = 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'.split()
resultado = [[w.upper(), w.lower(), len(w)] for w in palavras]
for i in resultado:
    print (i)


# Solution
resultado2 = map(lambda w: [w.upper(), w.lower(), len(w)], palavras)
for p in resultado2:
    print(p)