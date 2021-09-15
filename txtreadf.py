def read() :
    lista = []
    with open('GEH.txt','r') as f:
        lines = f.read().split('\n')
        for i in lines:
            for j in i.split(' '):
                lista.append(j)
        print(lista)
        f.close()
        return lista
read()