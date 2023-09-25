# Exercício 10 - Crie um regex em Python para extrair a palavra que aparece depois das palavras
# Data e Science na frase: 'A Data Science Academy oferce os melhores cursos de análise de dados do Brasil.'
import re
texto = 'A Data Science Academy oferece os melhores cursos de análise de dados do Brasil.'

#Solution
result = re.findall(r'Data Science (\w+)', texto)
print(result[0])