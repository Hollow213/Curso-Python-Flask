def nome(nome, cpf, idade=0, maiusculo=False, *args, **kwargs):

    print(args)
    print(kwargs)

    if maiusculo:
        msg = f"Olá {nome}".upper()
    else:
        msg = f"Olá {nome}, com o cpf:{cpf}, na ,idade: {idade}"

    print(msg)
            
pessoa = {
    "nome": "josé",
    "cpf": "41218584-54",
    "idade": 56

}

nome(**pessoa)
