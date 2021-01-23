# Importy
```python
import numpy as np
```

# utworzenie tablicy zawierającą 10 zer,
```python
zero = np.zeros(10)
print(zero)
```

# utworzenie tablicy zawierającą 10 piątek,
```python
five = np.ones(10)*5
print(five)
```

# utworzenie tablicy zawierającą liczby od 10 do 50,
```python
tenFifty = np.arange(10,51,1)
print(tenFifty)
```

# utworzenie macierzy (tablica wielowymiarowa) o wymiarach 3x3 zawierającą liczby od 0 do 8,
```python
matrixZeroEight = np.arange(0,9,1).reshape((3, 3))
print(matrixZeroEight)
```

# utworzenie macierzy jednostkowej o wymiarach 3x3,
```python
matrixThree = np.eye(3)
print(matrixThree)
```

# utworzenie macierzy o wymiarach 5x5 zawierającą liczby z dystrybucji normalnej (Gaussa),
```python
gaussian = np.random.normal(3, 2.5 , size=(3,3))
print(gaussian)
```

# utworzenie macierzy o wymiarach 10x10 zawierającą liczby od 0,01 do 1 z krokiem 0,01,
```python
matrixTen = np.arange(0.01,1.01,0.01).reshape((10,10))
print(matrixTen)
```

# utworzenie tablicy zawierającą 20 liniowo rozłożonych liczb między 0 a 1 (włącznie z 0 i 1),
```python
zeroOne = np.linspace(0,1,20)
print(zeroOne)
```

# utworzenie tablicy zawierającą losowe liczby z przedziału (1, 25), następnie zamień ją na macierz o wymiarach 5 x 5 z tymi samymi liczbami:
```python
oneTwentyfive = np.random.randint(1,26,25)
print(oneTwentyfive)
oneTwentyfive = oneTwentyfive.reshape((5,5))
print(oneTwentyfive)
```

#   obliczanie sumy wszystkich liczb w ww. macierzy,
```python
print(oneTwentyfive.sum())
```

#   obliczanie średniej wszystkich liczb w ww. macierzy,
```python
print(oneTwentyfive.mean())
```

#   obliczanie standardowej dewiacji dla liczb w ww. macierzy,
```python
print(oneTwentyfive.std())
```

#   obliczanie sumy każdej kolumny ww. macierzy i zapisz ją do tablicy.
```python
sumoneTwentyfive = oneTwentyfive.sum(axis=1)
print(sumoneTwentyfive)
```

# utworzenie macierzy o wymiarach 5x5 zawierającą losowe liczby z przedziału (0, 100) i:
```python
matrixFive = np.random.randint(100, size=(5,5))
print(matrixFive)
```

#   obliczanie mediany tych liczb,
```python
medianMatrixFive= np.median(matrixFive)
print(medianMatrixFive)
```

#   znajdowanie najmniejszej liczby tej macierzy,
```python
minMatrixFive = np.min(matrixFive)
print(minMatrixFive)
```

#   znajdowanie największej liczby tej macierzy.
```python
maxMatrixFive = np.max(matrixFive)
print(maxMatrixFive)
```

# utworzenie macierzy o wymiarach różnych od siebie i większych od 1, zawierającą losowe liczby z przedziału (0, 100) i dokonaj jej transpozycji,
```python
matrixRandom = np.random.randint(100, size=(np.random.randint(18)+2,np.random.randint(18)+2))

print(matrixRandom)
transposeMatrixRandom = np.transpose(matrixRandom)
print(transposeMatrixRandom)
```

# utworzenie dwióch macierzy o odpowiednich wymiarach (doczytać), większych od 2 i dodaj je do siebie,
```python
matrix1 = np.random.randint(100, size=(4,4))
matrix2 = np.random.randint(100, size=(4,4))
matrixAdd = np.add(matrix1,matrix2)
print(matrixAdd)
```

# utworzenie dwóch macierzy o odpowiednich wymiarach (doczytać) różnych od siebie i większych od 2, a następnie pomnóż je przez siebie za pomocą dwóch różnych funkcji (np. ‘matmul’ i ‘multiply’),
```python
matrix3 = np.random.randint(100, size=(3,5))
matrix4 = np.random.randint(100, size=(5,3))
matrixMulti1 = np.dot(matrix3,matrix4)
print('Matrix 1', matrixMulti1)
matrixMulti2 = np.matmul(matrix3,matrix4)
print('Matrix 2', matrixMulti2)
```
