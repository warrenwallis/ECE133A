def main():
    m = 4
    n = [100, 5000, 10000, 1000, 10]
    tab = [[0] * m] * m
    
    for l in range(m - 1):
        for i in range(m - l):
            currMin = None

            for k in range(i, i + l - 1):
                curr = tab[i][k] + tab[k + 1][i + l] + (2 * n[i - 1] * n[k] * n[i + l])
                if currMin is None:
                    currMin = curr
                else:
                    currMin = min(currMin, curr)

            tab[i][i + l] = currMin

    print(tab)
            


if __name__ == '__main__':
    main()