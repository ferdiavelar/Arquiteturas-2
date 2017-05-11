PC=0
AC=0
instr = ""
instr_type = ""
data_loc = 0
data = 0
run_bit=True

arqPrograma = open("ProgramaEmTexto.txt", "r")
programa = arqPrograma.read().split("\n")

arqMemory = open("Memory.txt", "r")
memory = arqMemory.read().split("\n")

while run_bit:
    instr = programa[PC]
    PC = PC + 1
    if len(instr)==0: break
    partes = instr.split(" ")
    instr_type = partes[0]
    data_loc = int(partes[1])
    data = int(memory[data_loc]
    if instr_type == "add":
        AC = AC + data
    elif instr_type == "mul":
        AC = AC*data
    elif instr_type == "sub":
        AC = AC - data
    elif instr_type == "div":
        AC = AC/data

    print("AC: ", AC)
