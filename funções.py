def sum(x, y): #definimos a função que recebe dois parametros
    return x + y #e aqui definimos o que a função retornará

def multiply(x, y, z): #a função pode ter quantos parametros forem necessarios
    return x * y * z


print(sum(10, 20)) #quando chamamos a função precisamos somente colocar o nome e os numeros que vão dentro dos parametros
print(sum(-20, 100))
print(sum(20*32, sum(3, 4)))
print(multiply(sum(20, 40), sum(65, 3), multiply(2, 3, 4))) #podemos adicionar varias funções umas dentro das outras para calculos mais complexos

def name_of_your_team(): #temos tbm funções que não recebem parametros mas retornam valores
    return 'SPFC'




