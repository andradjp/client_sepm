from json import loads

def verify():

    f = open('servers','r').readlines()
    z = open('list_computers.json','r').read().upper()
    lista_sep = loads(z)

    for x in f:
        if x.upper().strip() in lista_sep:
            continue
        else:
            print(x.strip())

verify()