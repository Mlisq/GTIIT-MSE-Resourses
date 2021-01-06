def even_values(a = []):
    #val = [i for i in a if i not in val]当然不能这么写
    val = []
    for i in a:
        if(i % 2 == 0 and i not in val):
            val.append(i)
    return len(val)

val = input("Enter your mountain : \n").split(' ')
a = [int(i) for i in val if i != '']
print(even_values(a))