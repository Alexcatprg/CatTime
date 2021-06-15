from colorama import init
from colorama import Fore, Back, Style

init()

print( Back.YELLOW )
print( Fore.RED )
time = (input ('Ночь, Утро, День или Вечер? : '))

print( Back.BLUE )
print( Fore.WHITE )

if time == 'Ночь':
  print('ты дурак? Сейчас же ночь!')
elif time == 'Утро':
  print('Ты завтракал хоть?')
elif time == 'День':
  print('Гулять можно, кэп!') 
elif time == 'Вечер':
  print('Гулять можно, кэп!')   

input()	