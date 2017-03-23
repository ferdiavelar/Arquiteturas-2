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

    #arqMemory = open("Memory.txt", "r")
    #memory = arqMemory.read().split("\n")
    memory = [None, None, None,None, None, None]

    registrador = ['vazio','vazio','vazio']

    while run_bit:
        #print("AC =", AC)
        instr = programa[PC]
        PC = PC + 1
        if len(instr)==0: break

        instr_type = get_instr_type(instr)
        if instr_type == "00":
            store(instr,memory)
        elif instr_type == "01":
            load(instr,registrador,memory)
        elif instr_type=="10":
            resultado = operacao(instr,registrador);

        #data = find_data(instr,memory)
        #AC = execute(instr_type,data,AC)

    print("Memoria = ",memory)
    print("Registrador = ",registrador)
    registrador = ['vazio','vazio','vazio']


def get_instr_type(instr):
    instr_type = instr[0:2]
    #00-Storage normal
    #01-load
    #10-operacao
    #11-11
    return instr_type

def store(instr,memory):
    localMemoria = int(instr[4:8],2)
    valorMemoria = int(instr[8:16],2)
    memory[localMemoria] = valorMemoria
    print("Variavel salva com valor ",valorMemoria)

def load(instr,registrador,memory):
    localMemoria = int(instr[12:16],2)
    valor = memory[localMemoria]
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


    print("resultado = ",resul)

    return registrador[0]

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
