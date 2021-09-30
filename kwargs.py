"""
kwargs possibilita verificamos os parametros nomeados da funcao
, isto e aqueles parametros que sao passados com um nome!

eles estarao disponiveis como um dicionarios ("chave": "valor")
dentro da funcao. vamos ao exemplo
"""


def to_bring_together(**kwargs):
    result = " "
    for value in kwargs.values():
        result += f'{value}'
    return result


# print(to_bring_together(a='python', b='django', c='drf'))
# print(to_bring_together(a='victor', b='hugo', c='n.oliveira'))


def function(arg_1, arg_2, *args, arg_kw, **kwargs):
    msg1 = f'parametro 1 : {arg_1}'
    msg2 = f'parametro 2 : {arg_2}'
    msg3 = f'*args  : {args}'
    msg4 = f'argumento nomeado 1 : {arg_kw}'
    msg = f'**kwargs 1 : {kwargs}'

    return msg1, msg2, msg3, msg4, msg


print(function(1, 'a', 'arg1', 'arg2', 2, arg_kw='kw', code='B', codes='A'))
