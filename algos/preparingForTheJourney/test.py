listy = { 1 : 1, 2 : 2, 3 : 3 }

print(f"before function: {listy}")

def func(list: list):
    list[2], list[1] = list[1], list[2]
    print(f"inside function: {listy}")

func(listy)

print(f"after function: {listy}")
