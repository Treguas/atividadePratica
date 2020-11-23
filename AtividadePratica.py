# variable input
student = int(input('Digite a matrícula do aluno: '))
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))



# functions
def average(n1, n2, n3):
    return ((n1 + n2 + n3) / 3)


def school_achievement(n1, n2, n3):
    return ((n1 + n2 * 2 + n3 * 3 + average(n1, n2, n3)) / 7)


def concept(ma):
    if (ma >= 9):
        return "A"
    elif (ma >= 7.5):
        return "B"
    elif (ma >= 6):
        return "C"
    elif (ma >= 4):
        return "D"
    else:
        return "E"


def message(con):
    if (con == "A" or con == "B" or con == "C"):
        return "APROVADO"
    else:
        return "REPROVADO"

ma = school_achievement(n1, n2, n3)
con = concept(ma)
msg = message(con)

print(f'O Aluno: {student} obteve as seguintes notas:')
print(f'Primeira nota: {n1}')
print(f'Segunda nota: {n2}')
print(f'Terceira nota: {n3}')
print(f'Média:  {average(n1, n2, n3):.2f}')
print(f'Média de Aproveitamento: {school_achievement(n1, n2, n3):.2f}')
print(f'Conceito: {con}')
print(f'Aluno: {msg}')
