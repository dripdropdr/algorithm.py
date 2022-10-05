N = int(input())
if N<100:
    result_list = [*list(range(1,N+1))]
else:
    result_list = [*list(range(1,100))]

    #자리수 3
    for n in range(100,N+1):
        if int(str(n)[0]) - int(str(n)[1]) == int(str(n)[1]) - int(str(n)[2]):
            result_list.append(n)

print(len(result_list))
print(*result_list, end = ' ')