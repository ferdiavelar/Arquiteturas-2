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
    instr = programa[PC]
    PC = PC + 1
    if len(instr)==0: break
    instr_type = instr[0:2]
    data_loc = int(instr[2:8],2)
    data = int(memory[data_loc])
    if instr_type == "00":
        AC = AC + data
    elif instr_type == "01":
        AC = AC - data
    elif instr_type == "10":
        AC = AC / data
    elif instr_type == "11":
        AC = AC * data

    print("AC: ", AC)
