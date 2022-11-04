# Bubble Sort

def solution(array, commands):
    answer=[]
    for command in commands:
        goalidx = command[2]-1
        arr = array[command[0]-1:command[1]]
        
        step = len(arr) - 1
        for j in range(step):
            for i in range(len(arr)):
                if i + 1 == len(arr):
                    break
                if arr[i] > arr[i + 1]:
                    tmp = arr[i + 1]
                    arr[i + 1] = arr[i]
                    arr[i] = tmp
        answer.append(arr[goalidx])
    return answer
