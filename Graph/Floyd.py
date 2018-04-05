INF = 65535
D = [[0, 1, 5, INF, INF, INF, INF, INF, INF],
     [1, 0, 3, 7, 5, INF, INF, INF, INF],
     [5, 3, 0, INF, 1, 7, INF, INF, INF],
     [INF, 7, INF, 0, 2, INF, 3, INF, INF],
     [INF, 5, 1, 2, 0, 3, 6, 9, INF],
     [INF, INF, 7, INF, 3, 0, INF, 5, INF],
     [INF, INF, INF, 3, 6, INF, 0, 2, 7],
     [INF, INF, INF, INF, 9, 5, 2, 0, 4],
     [INF, INF, INF, INF, INF, INF, 7, 4, 0]]
P = []
lengthD = len(D)


#邻接矩阵大小
for i in range(lengthD):
    P.append(list(range(lengthD)))


for k in range(lengthD):
    for v in range(lengthD):
        for w in range(lengthD):
            if D[v][w] > D[v][k] + D[k][w]:
                D[v][w] = D[v][k] + D[k][w]
                P[v][w] = P[v][k]

for v in range(lengthD):
    w = v + 1
    while(w < lengthD):
        print("V%d->V%d weight: %d"%(v, w, D[v][w]))
        k = P[v][w]
        print("path:", v)
        while(k!=w):
            print(" -> %d"%k)
            k = P[k][w]
        print(" -> %d"%w)
        w += 1
    print("\n")
# print(D)
# print(P)
