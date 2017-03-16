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

    arqMemory = open("Memory.txt", "r")
    memory = arqMemory.read().split("\n")

    while run_bit:
        print("AC =", AC)
        instr = programa[PC]
        PC = PC + 1
        if len(instr)==0: break

        instr_type = get_instr_type(instr)
        data = find_data(instr,memory)
        AC = execute(instr_type,data,AC)
        print("AC: ", AC)


def get_instr_type(instr):
    instr_type = instr[0:4]
    return instr_type

def find_data(instr,memory):
    data_loc = int(instr[4:8],2)
    data = int(memory[data_loc])
    return data

def execute(type, data, AC):
    if type == "0000":
        AC = AC + data
        print("+",data)
    elif type == "0001":
        AC = AC - data
        print("-",data)
    elif type == "0010":
        AC = AC / data
        print("/",data)
    elif type == "0011":
        AC = AC * data
        print("*",data)
    elif type == "1000":
        #Save
        AC1 = str(AC)
        arq = open("registrador.txt","a")
        arq.write(AC1)
        print("Saved")
    return AC


if __name__ == '__main__':
    interpreter()
