import numpy as np

#utwórz tablicę zawierającą 10 zer,
zero = np.zeros(10)
print(zero)

#utwórz tablicę zawierającą 10 piątek,
five = np.ones(10)*5
print(five)

#utwórz tablicę zawierającą liczby od 10 do 50,
tenFifty = np.arange(10,51,1)
print(tenFifty)

#utwórz macierz (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8,
matrixZeroEight = np.arange(0,9,1).reshape((3, 3))
print(matrixZeroEight)

#utwórz macierz jednostkową o wymiarach 3x3,
matrixThree = np.eye(3)
print(matrixThree)

#utwórz macierz o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),
gaussian = np.random.normal(3, 2.5 , size=(3,3))
print(gaussian)

#utwórz macierz o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01,
matrixTen = np.arange(0.01,1.01,0.01).reshape((10,10))
print(matrixTen)

#utwórz tablicę zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1),
zeroOne = np.linspace(0,1,20)
print(zeroOne)

#utwórz tablicę zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
oneTwentyfive = np.random.randint(1,26,25)
print(oneTwentyfive)
oneTwentyfive = oneTwentyfive.reshape((5,5))
print(oneTwentyfive)

#   oblicz sumę wszystkich liczb w ww. macierzy,
print(oneTwentyfive.sum())

#   oblicz średnią wszystkich liczb w ww. macierzy,
print(oneTwentyfive.mean())

#   oblicz standardową dewiację dla liczb w ww. macierzy,
print(oneTwentyfive.std())

#   oblicz sumę każdej kolumny ww. macierzy i zapisz ją do tablicy.
sumoneTwentyfive = oneTwentyfive.sum(axis=1)
print(sumoneTwentyfive)

#utwórz macierz o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) i:
matrixFive = np.random.randint(100, size=(5,5))
print(matrixFive)

#   oblicz medianę tych liczb,
medianMatrixFive= np.median(matrixFive)
print(medianMatrixFive)

#   znajdź najmniejszą liczbę tej macierzy,
minMatrixFive = np.min(matrixFive)
print(minMatrixFive)

#   znajdź największą liczbę tej macierzy.
maxMatrixFive = np.max(matrixFive)
print(maxMatrixFive)

#utwórz macierz o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
matrixRandom = np.random.randint(100, size=(np.random.randint(18)+2,np.random.randint(18)+2))
print(matrixRandom)
transposeMatrixRandom = np.transpose(matrixRandom)
print(transposeMatrixRandom)

#utwórz dwie macierze o odpowiednich wymiarach (doczytać), większych od 2 i dodaj je do siebie,
matrix1 = np.random.randint(100, size=(4,4))
matrix2 = np.random.randint(100, size=(4,4))
matrixAdd = np.add(matrix1,matrix2)
print(matrixAdd)

#utwórz dwie macierze o odpowiednich wymiarach (doczytać) różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji (np. ‘matmul’ i ‘multiply’),
matrix3 = np.random.randint(100, size=(3,5))
matrix4 = np.random.randint(100, size=(5,3))
matrixMulti1 = np.dot(matrix3,matrix4)
print('Matrix 1', matrixMulti1)
matrixMulti2 = np.matmul(matrix3,matrix4)
print('Matrix 2', matrixMulti2)