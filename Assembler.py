#iteration 2
#iteration 1
lines=["adii r1 ,r1 ,5"]
program_counter=0
instru_lines=[]
regs={
    'zero':0,'ra':1,'sp':2,'gp':3,'tp':4,
    't0':5,'t1':6,'t2':7,
    's0':8,'fp':8,'s1':9,
    'a0':10,'a1':11,'a2':12,'a3':13,'a4':14,'a5':15,'a6':16,'a7':17,
    's2':18,'s3':19,'s4':20,'s5':21,'s6':22,'s7':23,'s8':24,'s9':25,'s10':26,'s11':27,
    't3':28,'t4':29,'t5':30,'t6':31,
}



###########          INPUT TAKER          ###########
inpt_dict={}
pure_lines=[]
label_dict={}
instr_to_line=[]

for line_num,line in enumerate(lines,1):#chopping off all the lables ,regs and removing trash like comma and all
    temp=line.split()
    temp=[i.replace(',','') for i in temp]
    if len(temp)==1 and temp[0].endswith(':'):
        label_dict[temp[0].replace(':','')]=len(pure_lines)
    else:
        if temp[0].endswith(':'):
            label_dict[temp[0].replace(':','')]=len(pure_lines)
            temp=temp[1:]
        pure_lines.append(temp)
        instr_to_line.append(line_num)
#####################################################


#making main structure of code:

def error(msg):
    return f"{msg} error at line no:{program_counter}"

#encoding block will return all the encoded instruction directly
def encoding_r(opcode, f3, f7, rd, rs1, rs2):
    return f"{f7}{rs2}{rs1}{f3}{rd}{opcode}"
    
def encoding_i(opcode, f3, rd, rs1, imm):
    return f"{imm}{rs1}{f3}{rd}{opcode}"

def encoding_s(opcode, f3, rs1, rs2, imm):
    return f"{imm[:7]}{rs2}{rs1}{f3}{imm[7:]}{opcode}"

def encoding_b(opcode, f3, rs1, rs2, imm):
    return f"{imm[0]}{imm[2:8]}{rs2}{rs1}{f3}{imm[8:12]}{imm[1]}{opcode}"

def encoding_u(opcode, rd, imm):
    return f"{imm[:20]}{rd}{opcode}"

def encoding_j(opcode, rd, imm):
    return f"{imm[0]}{imm[10:20]}{imm[9]}{imm[1:9]}{rd}{opcode}"


def runner(n):#all the instruction are seperated by their type or by diff opcode note:- i have used opcode copied from web
    global pure_lines,program_counter
    temp=pure_lines[n]
    valid_ops=['add','sub','sll','slt','sltu','xor','srl','or','and','mul',
        'addi','sltiu','jalr','lw','sw',
        'beq','bne','blt','bge','bltu','bgeu',
        'lui','auipc','jal','rvrs','rst','halt']
    if temp[0] not in valid_ops:
        error("instruction used is not defined")
        return
        
    f7s = {
        'add':'0000000','sub':'0100000','sll':'0000000','slt':'0000000','sltu':'0000000',
        'xor':'0000000','srl':'0000000','or':'0000000','and':'0000000','mul':'0000001'}
    
    f3s = {
        'add':'000','sub':'000','sll':'001','slt':'010','sltu':'011',
        'xor':'100','srl':'101','or':'110','and':'111','mul':'000'}
    
    #r type instru
    if temp[0] in ("add","sub","sll","slt","sltu","xor","srl","or","and","mul"):
        encoding_r()
    
    #i type instru
    if temp[0]=="addi":
        encoding_i()
    if temp[0]=="lw":
        encoding_i()
    if temp[0]=="sltiu":
        encoding_i()
    if temp[0]=="jalr":
        encoding_i()

    #s type instru 
    if temp[0]=="sw":
        encoding_s()
    
    #b type instru 
    b3={'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
    if temp[0] in b3:
        encoding_b()
    
    #u type instru
    if temp[0]=='lui':
        encoding_u()
    if temp[0]=='auipc':
        encoding_u()

    #j type instru
    if temp[0]=='jal':
        encoding_j()

while program_counter<len(pure_lines):
    instru_lines.append(runner(program_counter))
    program_counter+=1

for line in instru_lines:
    print(line)
#~piyush
