# Seance 2 - Compléxité des algorithmes

## Exercice 1. Dénombrer le nombre d’instructions d’un programme

### 1. Programme 1 :
```python
test = 0
for i in range(n):
    test = test + 1
for j in range(n):
    test = test - 1
```
#### *Réponse* :
$ 1 + 4n$

Ce qui donne $O(n)$

### 2. Programme 2 :
```python
test = 0
for i in range(n):
    for j in range(n):
        test = test + i * j
```
#### *Réponse* :
$ 1 + 3n^2$

Ce qui donne $O(n^2)$

### 3. Programme 3 :
```python
a=5
b=6
c=10
for i in range(n):
    for j in range(n):
        x = i * i
        y = j * j
        z = i * j
for k in range(n):
    w = a*k + 45
    v = b*b
d = 33
```
#### *Réponse*:

$ 1 + 1 +  1 + 6 n^2 + 5n $

Ce qui donne $ O(n^2) $ 

### 4. Programme 4:
```python
i = n
while i > 0:
    k = 2 + 2
    i = i // 2
```
#### *Réponse*:

$  1 + 4 log(n)$

Ce qui donne $ O(log(n))$ 

### 5. Programme 5:
```python 
sum = 0
for i from 1 to n*n:
    for j from 1 to i:
        for k from 1 to 6:
            sum = sum + 1;
```
#### *Réponse*:

$  1 + 12 n^3$

Ce qui donne $ O(n^3)$

## Exercice 2. Classement par vitesse de croissance asymptotique

#### *Functions to Class*
$
f_1 = 2n\\
f_2 = log(log(n))\\
f_3 = n^3 + log(n)\\
f_4 = log(n)\\
f_5 = n - n^2 + 5n^3\\
f_6 = 2^{n-1}\\
f_7 = n^2\\
f_8 = n^3\\
f_9 = nlog(n)\\
f_{10} = (log(n))^2\\
f_{11} = \sqrt{n}\\
f_{12} =6\\
f_{13} = n!\\
f_{14} = n\\
f_{15} = (3 / 2)^n\\
$

#### *Réponse*:

$f_{12} = O (f_2),\ f_2 = O(f_4),\ f_4 = O (f_{10}),  $    