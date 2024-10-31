if __name__ == '__main__':

    nm = list()
    sc = list()
    rec = list()

    n = int(input())

    for _ in range(n):
        name = input()
        score = float(input())
        nm.append(name)
        sc.append(score)
        rec.append((score, name))

    fnm = sorted(list(set(nm)))
    #print(fnm)
    fsc = sorted(list(set(sc)))
    #print(fsc)
    frec = sorted(list(set(rec)))
    #print(frec)

    for a in range(n):
        if frec[a][0] == fsc[1]:
            print(frec[a][1])
