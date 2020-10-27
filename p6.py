
def calcular(parentesis:str)->bool:
    if sum([1 if x=='(' else -1 for x in parentesis ])!=0:return False
    else: return True

print(calcular("(()()())()()(())"))
print(calcular("(()("))