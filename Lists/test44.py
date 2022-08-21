test_list = [(4, 5, 6, 3), (5, 6, 6, 9), (1, 3, 5, 6), (6, 6, 7, 8)]
K=6
res = [idx for idx in test_list if (K, K) not in zip(idx, idx[1:])]

hola=(4, 5, 6, 3)

como=hola[1:]

casa=list(zip(hola,como))

print(casa)