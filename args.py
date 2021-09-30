#   *args e **kwargs sao usados, principalmente, em definicoes de funcoes


""" *args e **kwargs permitem que voce passe um numero nao especificado de argumentos para uma funcao.
Dessa forma, ao escrever uma funcaom voce nao precisa definir quantos argumentos serao passados para sua
(funcao)
"""

""" obs Escrever *args e **kwargs e apenas uma convencao: *args vem de "arguments" e **kwargs vem de "Keyword Arguments":
Podemos ate mesmo utilizar por exemplo *codigo, **codigo. """


#   *args e usado para receber uma lista de argumentos de comprimento variavel sem palavra-chave(keyword) na funcao. exemplo

def function_with_variable_arguments(arg, *args):
    print("primeiro argument", arg)

    for argument in args:
        print("Argumento de *args", argument)


# print(function_with_variable_arguments('primeiro_arg', 'arg2', 'arg3', 'arg3'))


# Argumentos nao nomeados ("args) vem sempre primeiro que os argumentos nomeados (**kwargs).

def addition(*args):
    result = 0
    for argumento in args:
        result += argumento
    return result


print(addition(1, 2))
print(addition(1, 2, 4, 5))
print(addition(1, 2, 3, 4, 6, 7))


def show(*letters):
    for l in letters:
        print(f'{l} essa e a letra')


print(show('sdbfsidfsd', 'ashdiuasidhaihsdias'))
