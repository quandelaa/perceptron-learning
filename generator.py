from random import randint
from pandas import DataFrame

rows = []

for _ in range(10000):
    x1 = randint(0, 1)
    x2 = randint(0, 1)

    label = 1 if x1 != x2 else 0

    rows.append([x1, x2, label])

df = DataFrame(rows, columns=["x1", "x2", "label"])
df.to_csv("dataset.csv", index=False)