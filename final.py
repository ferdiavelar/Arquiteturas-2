def interpreter():
    PC=0
    AC=0
    instr = ""
    instr_type = ""
    data_loc = 0
    data = 0
    run_bit=True

    arqPrograma = open("ProgramaBinario.txt", "r")
    programa = arqPrograma.read().split("\n")

    memory = [None, None, None,None, None, None,None, None, None,None, None, None,None, None, None,None, None, None]
    cacheV = [None,None,None,None]

    registrador = ['vazio','vazio','vazio']

    while run_bit:
        #print("AC =", AC)
        instr = programa[PC]
        PC = PC + 1
        x=0;
        if len(instr)==0: break

        instr_type = get_instr_type(instr)
        if instr_type == "00":
            store(instr,memory)
        elif instr_type == "01":
            load(instr,registrador,memory,x)
        elif instr_type=="10":
            resultado = operacao(instr,registrador);

    registrador = ['vazio','vazio','vazio']
    print("Memoria = ",memory)

def get_instr_type(instr):
    instr_type = instr[0:2]
    #00-Storage normal
    #01-load
    #10-operacao
    #11-store de operacao
    return instr_type

def store(instr,memory):
    localMemoria = int(instr[4:8],2)
    valorMemoria = int(instr[8:16],2)
    memory[localMemoria] = valorMemoria
    print(memory)
    print("Variavel salva com valor ",valorMemoria)

def cacheF(instr,memory,x):
    if x==0:
        if instr[12] == 0:
            cacheV = [memory[0],memory[1],memory[2],memory[3],memory[4],memory[5],memory[6],memory[7],0]
            print(cacheV)
            x=1
        else:
            cacheV = [memory[8],memory[9],memory[10],memory[11],memory[12],memory[13],memory[14],memory[15],1]
            print(cacheV)
            x=1
    elif instr[12] == cacheV[8]:
        print("Cache hit")
        valor = cacheV[int(instr[13:16],2)]
        return valor
    else:
        print("cache miss")
        x=0;
        cacheF(instr,memory,x)


def load(instr,registrador,memory,x):
    valor = cacheF(instr,memory,x)
    for i in range(0,3):
        if registrador[i] == 'vazio':
            registrador[i] = valor
            break

    print("Variavel carregada com valor ",valor)

def operacao(instr,registrador):
    type =  instr[2:4]
    print("Registrador = ",registrador)
    if type == "00":
        resul = int(registrador[0]) + int(registrador[1])
        print("Operacao de +")
    elif type == "01":
        resul = int(registrador[0]) - int(registrador[1])
        print("Operacao de -")
    elif type == "10":
        resul = int(registrador[0]) / int(registrador[1])
        print("Operacao de /")
    elif type == "11":
        resul = int(registrador[0]) * int(registrador[1])
        print("Operacao de *")

    registrador[2] = resul

    print("resultado = ",resul)

    print("Registrador = ",registrador)

    return resul

def storeOperacao(instr,resultado):
    localMemoria = int(instr_type[12:16],2)
    memory[localMemoria] = resultado


def find_data(instr,memory):
    #localização memoria
    local = instr[4:8]
    #Localização valor
    data_loc = int(instr[4:8],2)
    data = int(memory[data_loc])
    return data

if __name__ == '__main__':
    interpreter()
