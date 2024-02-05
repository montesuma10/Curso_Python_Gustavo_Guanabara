import math
ang = float(input('Digite o valor do ângulo: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'O ângulo de {ang}º tem SENO de {sen:.2f}')
print(f'O ângulo de {ang}º tem COSSENO de {cos:.2f}')
print(f'O ângulo de {ang}º tem TANGENTE de {tang:.2f}')