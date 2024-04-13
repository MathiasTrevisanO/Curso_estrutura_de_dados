import re

string = "blablabla 11 blabalbal 7. Meu numero de CEP é 88036-150. O URL é www.google.com"

print(re.findall('\d{1,2}', string))
print(re.findall('\d{5}-\d{3}', string))
print(re.findall('\w+\.\w+\.\w*', string))