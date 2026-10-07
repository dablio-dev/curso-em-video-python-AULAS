from random import shuffle
n1 = str (input ('Digite o nome de um aluno: '))
n2 = str (input ('Digite o nome de um aluno: '))
n3 = str (input ('Digite o nome de um aluno: '))
n4 = str (input ('Digite o nome de um aluno: '))
grupo= [n1, n2, n3, n4]
shuffle(grupo)
print ('Ésta é a ordem \n{}'.format(grupo))
