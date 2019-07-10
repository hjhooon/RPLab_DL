input_list_A = ["bcd","bce","cce"]
input_list_B = ["def","deg","dmf","xef","dxg"]

def pair_count(list):
    sum = 0
    i = 0
    l = len(list)
    for i in range(l):
        for j in range(l-1-i):
            if(list[i][:2]==list[i+j+1][:2]):
                sum +=1
            elif(list[i][:2] == list[i+j+1][1:]):
                sum +=1
            elif(list[i][1:]==list[i+j+1][:2]):
                sum +=1
            elif(list[i][1:] == list[i+j+1][1:]):
                sum +=1
            elif(list[i][0]==list[i+j+1][0] and list[i][2] == list[i+j+1][2]):
                sum +=1
            j +=1
        i += 1
    return sum

print(pair_count(input_list_A))
print(pair_count(input_list_B))