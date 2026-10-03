# desafio 01 
print("-"*50)
notas = (f"digite as notas do aluno : ") 
print("-"*50)

notas1 = float(input("digite a primeira nota: "))
notas2 = float(input("digite a segunda nota: "))
notas3 = float(input("digite a terceira nota: "))
notas4 = float(input("digite a quarta nota: "))

print("-"*50)
notas = [notas1, notas2, notas3, notas4]



print("Notas inseridas:", notas)
print("-"*50)

print("-"*50)
print(sum(notas))
print(max(notas))
print(min(notas))
print("-"*50)


print(f" a sua primeira nota e {notas1}, sua segunda nota e a {notas2}, sua terceira nota e {notas3}, sua quarta e ultima nota e {notas4}")

print("-"*50)

media = sum(notas)/len(notas)
print(media)

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Recuperação!")
else:
    print("Reprovado!")


