def self_num(n):
    result = n
    n_iter = str(n)
    for i in n_iter:
        result += int(i)
    return result

if __name__ == '__main__':
    res = list(range(1, 10001))
    # print(res)
    for i in range(1, 10001):
        try:
            tmp = self_num(i)
            # print(i, tmp)
            res.remove(tmp)
        except ValueError:
            pass
    print(*res, sep='\n')
