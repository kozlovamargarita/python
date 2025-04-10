#Лабораторная работа1, вариант 3, Козлова Маргарита 48 гр.
def hamming_distance(s, t):
#s: Первая строка.
#t: Вторая строка.
  if len(s) != len(t):
    print("Строки должны быть одинаковой длины.")
    return -1 #если количество символов строке не совпадает

  distance = 0
  for i in range(len(s)):
    if s[i] != t[i]:
      distance += 1

  return distance #если количество символов в строке совпадает, то ищем количество точечных мутаций
# Пример использования:
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"
distance = hamming_distance(s, t)

if distance != -1:
    print("Расстояние Хэмминга:", distance)



def hamming_distance_fast(s, t):
    if len(s) != len(t):
        print("Строки должны быть одинаковой длины.")
        return -1

    distance = sum(s[i] != t[i] for i in range(len(s)))
    return distance

s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = hamming_distance_fast(s, t)
print(distance)

def hamming_distance_shortest(s, t):
    return -1 if len(s) != len(t) else sum(a != b for a, b in zip(s, t))
s = "GAGCCTACTAACGGGAT"
t = "CATCGTAATGACGGCCT"

distance = hamming_distance_shortest(s, t)
print(distance)
