import numpy as np
import datetime


class edge:
    def __init__(self, u, v, w):
        # 边的顶点和权值
        self.u = u
        self.v = v
        self.w = w


def produce():
    edges = []
    for i in range(n - 1):
        for j in range(i + 1, n):
            weight = np.random.rand()
            # print(weight)
            if weight > 0:
                e = edge(i, j, weight)
                edges.append(e)
    return sorted(edges, key=lambda s: s.w)


def tree():
    edges = produce()
    in_tree = []
    out_tree = []
    for i in range(n):
        out_tree.append(i)
    in_tree.append(edges[0].u)
    in_tree.append(edges[0].v)
    out_tree.remove(edges[0].u)
    out_tree.remove(edges[0].v)
    length = edges[0].w
    while len(out_tree) != 0:
        for i in range(len(edges)):
            e = edges[i]
            if (e.u in in_tree) & (e.v in out_tree):
                in_tree.append(e.v)
                out_tree.remove(e.v)
                # print(e.w)
                length += e.w
                break
            if (e.v in in_tree) & (e.u in out_tree):
                in_tree.append(e.u)
                out_tree.remove(e.u)
                # print(e.w)
                length += e.w
                break
    # print(in_tree)
    return length


if __name__ == '__main__':
    m = 10
    N = [16, 32, 64, 128, 256, 512, 1024]
    for n in N:
        E = 0
        start = datetime.datetime.now()
        for M in range(m):
            E += tree()
        end = datetime.datetime.now()
        print("N = " + str(n) + "  E(length) = " + str(E / m) + "   time:" + str(end - start))





