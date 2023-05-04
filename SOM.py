
w = [[0.2, 0.6, 0.5, 0.9],
    [0.8, 0.4, 0.7, 0.3],]
# inputs
ip = [[1, 1, 0, 0],
        [0, 0, 0, 1],
        [1, 0, 0, 0],
        [0, 0, 1, 1]]
eta = 0.6
epoches = 100
for _ in range(epoches):
    for i in range(len(ip)):
# calculate d^2
        d1, d2 = 0, 0
        for k in range(len(ip[i])):
            d1 += (ip[i][k] - w[0][k]) ** 2
            d2 += (ip[i][k] - w[1][k]) ** 2
# print(f"d1={d1} d2={d2}")
# select minimum d^2
        if (d1 < d2):
            sel = 0
        else:
            sel = 1
# update weights
        for k in range(len(w[sel])):
            w[sel][k] = w[sel][k] + eta * (ip[i][k] - w[sel][k])
# print(f"selected node {sel+1} : updated weights {w}")
    eta = 0.5 * eta
print(f"Final weights:\n{w[0]}\n{w[1]}")
clusters = [[], []]
# dividing inputs into clusters
for i in range(len(ip)):
# calculate d^2
    d1, d2 = 0, 0
    for k in range(len(ip[i])):
        d1 += (ip[i][k] - w[0][k]) ** 2
        d2 += (ip[i][k] - w[1][k]) ** 2
        if (d1 < d2):
            clusters[0].append(i)
        else:
            clusters[1].append(i)
print(f"\n\nResulting clusters:\nCluster1:{clusters[0]}\nCluster2:{clusters[1]}")