#iteration 4 #debugging the errors
#iteration 3
#iteration 2
#iteration 1
lines=[#assembly lines for testing (ai generated)
    "    addi s0, zero, 2047",
    "    addi s1, zero, -2048",
    "    addi s2, zero, 0",
    "    addi s3, zero, 255",
    "    addi s4, zero, 2047",
    "    addi s5, zero, 2047",
    "    addi s6, zero, 1",
    "    addi zero, zero, 100",
    "    addi ra, zero, 101",
    "    addi sp, zero, 102",
    "    addi gp, zero, 103",
    "    addi tp, zero, 104",
    "    addi t0, zero, 105",
    "    addi t1, zero, 106",
    "    addi t2, zero, 107",
    "    addi s0, zero, 108",
    "    addi s1, zero, 109",
    "    addi a0, zero, 110",
    "    addi a1, zero, 111",
    "    addi a2, zero, 112",
    "    addi a3, zero, 113",
    "    addi a4, zero, 114",
    "    addi a5, zero, 115",
    "    addi a6, zero, 116",
    "    addi a7, zero, 117",
    "    addi s2, zero, 118",
    "    addi s3, zero, 119",
    "    addi s4, zero, 120",
    "    addi s5, zero, 121",
    "    addi s6, zero, 122",
    "    addi s7, zero, 123",
    "    addi s8, zero, 124",
    "    addi s9, zero, 125",
    "    addi s10, zero, 126",
    "    addi s11, zero, 127",
    "    addi t3, zero, 128",
    "    addi t4, zero, 129",
    "    addi t5, zero, 130",
    "    addi t6, zero, 131",
    "    add t0, s0, s1",
    "    sub t1, a0, a1",
    "    mul t2, t0, t1",
    "    add a5, a5, a5",
    "    sub a6, a6, a6",
    "    xor t3, s2, s3",
    "    or t4, s4, s5",
    "    and t5, s6, s2",
    "    sll t6, a0, a1",
    "    srl a2, a3, a4",
    "    slt s4, a0, a1",
    "    sltu s5, a2, a3",
    "    lw t0, 0(sp)",
    "    lw t1, 4(sp)",
    "    lw t2, -4(sp)",
    "    lw t3, 2047(sp)",
    "    lw t4, -2048(sp)",
    "    lw a5, 100(a0)",
    "    lw a6, 0(s4)",
    "    sw t0, 0(sp)",
    "    sw t1, 4(sp)",
    "    sw t2, -4(sp)",
    "    sw t3, 2047(sp)",
    "    sw t4, -2048(sp)",
    "    sw a0, 100(s0)",
    "    sw a1, 200(sp)",
    "    addi s0, zero, 10",
    "outer_loop:",
    "    addi s1, zero, 5",
    "inner_loop:",
    "    addi t0, zero, 1",
    "    addi s1, s1, -1",
    "    bne s1, zero, inner_loop",
    "    addi s0, s0, -1",
    "    bne s0, zero, outer_loop",
    "    addi a0, zero, 5",
    "    addi a1, zero, 5",
    "    addi a2, zero, 10",
    "    addi a3, zero, -5",
    "    beq a0, a1, beq_equal",
    "    addi a0, a0, 1",
    "beq_equal:",
    "    addi a0, a0, 100",
    "    bne a0, a2, bne_not_equal",
    "    addi a0, a0, 1",
    "bne_not_equal:",
    "    addi a0, a0, 100",
    "    blt a3, a0, blt_less_than",
    "    addi a0, a0, 1",
    "blt_less_than:",
    "    addi a0, a0, 100",
    "    bge a0, a3, bge_ge",
    "    addi a0, a0, 1",
    "bge_ge:",
    "    addi a0, a0, 100",
    "    bltu a3, a2, bltu_less_unsigned",
    "    addi a0, a0, 1",
    "bltu_less_unsigned:",
    "    addi a0, a0, 100",
    "    bgeu a2, a3, bgeu_ge_unsigned",
    "    addi a0, a0, 1",
    "bgeu_ge_unsigned:",
    "    addi a0, a0, 100",
    "    jal ra, forward_target",
    "    addi a0, a0, 999",
    "forward_target:",
    "    addi a0, a0, 1",
    "    addi a5, zero, 0",
    "    jalr ra, ra, 0",
    "    lui a0, 74565",
    "    lui a1, 1048575",
    "    lui a2, 1",
    "    auipc a3, 65536",
    "    beq zero, zero, skip_section",
    "    addi a0, a0, 888",
    "skip_section:",
    "    addi a0, a0, 777",
    "    addi s4, zero, 3",
    "backward_loop:",
    "    addi s4, s4, -1",
    "    bne s4, zero, backward_loop",
    "    add ra, sp, gp",
    "    sub fp, s1, s2",
    "    mul a0, a1, a2",
    "    addi tp, zero, 999",
    "    slt t6, t5, t4",
    "    addi t0, zero, 2047",
    "    addi t1, zero, -2048",
    "    addi t2, zero, 1",
    "    addi s0, zero, -1",
    "    addi s1, zero, 1024",
    "    addi a4, zero, -1024",
    "    lw a0, 2047(sp)",
    "    lw a1, -2048(sp)",
    "    sw a2, 2047(sp)",
    "    sw a3, -2048(sp)",
    "    beq a0, a1, end_of_branches",
    "    beq a0, a1, end_of_branches",
    "    beq a0, a1, end_of_branches",
    "    beq a0, a1, end_of_branches",
    "end_of_branches:",
    "    addi a0, a0, 1",
    "    addi a0, zero, 3",
    "    addi a1, zero, 7",
    "    addi a2, zero, 5",
    "    addi a3, zero, 10",
    "    add a4, a0, a1",
    "    mul a5, a4, a2",
    "    sub a6, a5, a3",
    "    addi a0, zero, 42",
    "    add a0, a0, zero",
    "    mul a0, a0, zero",
    "    sub zero, a0, a0",
    "    addi a0, zero, 1",
    "    addi a0, a0, 1",
    "    addi a0, a0, 2",
    "    addi a0, a0, 4",
    "    addi a0, a0, 8",
    "    mul a0, a0, a0",
    "    addi a0, zero, 100",
    "    add a1, a0, zero",
    "    add a2, a1, a0",
    "    add a3, a2, a1",
    "    add a4, a3, a2",
    "    add a5, a4, a3",
    "    addi ra, zero, 1",
    "    addi sp, zero, 2",
    "    addi gp, zero, 3",
    "    addi tp, zero, 4",
    "    addi t0, zero, 5",
    "    addi t1, zero, 6",
    "    addi t2, zero, 7",
    "    addi s0, zero, 8",
    "    addi s1, zero, 9",
    "    addi a0, zero, 10",
    "    add s4, ra, sp",
    "    add s5, sp, gp",
    "    add s6, gp, tp",
    "    add s7, tp, t0",
    "    add s8, t0, t1",
    "    add s9, t1, t2",
    "    add s10, t2, s0",
    "    add s11, s0, s1",
    "    add t3, s1, a0",
    "    add t4, a0, ra",
    "    mul t5, s4, ra",
    "    mul t6, s5, sp",
    "    beq zero, zero, 0",
       ]
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
    print(f"syntax error at line {instr_to_line[program_counter]} : {msg}")

def get_register(mnemonic):
    global regs
    
    bit=regs[mnemonic]
    return f"{bit:0{5}b}"

def to_signed_bits(val,nbits):#this function convert an immediate value into fixed width 2's complement bits
    if val<0:
        val=val+(1<<nbits)
    return format(val&((1<<nbits)-1),f'0{nbits}b')

def paranthesis_tackle(s):#takeling the paranthesis in some operations for ex:- lw r1 ,-->10(a0)<--here
    global regs
    offset,mnemonic=s.replace(')','').split('(')
    offset=int(offset)
    num=regs[mnemonic]
    
    imm12=to_signed_bits(offset,12)
    rd=f"{num:05b}"
    
    return rd,imm12

def lable_offset_b(lable):
    global label_dict,program_counter
    try:
        offset=int(lable)
    except ValueError:
        if lable not in label_dict:
            error(f"undefined label '{lable}'")
        offset=(label_dict[lable]-program_counter)*4
    return to_signed_bits(offset,13)

def lable_offset_j(lable):
    global label_dict,program_counter
    try:
        offset=int(lable)
    except ValueError:
        if lable not in label_dict:
            error(f"undefined label '{lable}'")
        offset=(label_dict[lable]-program_counter)*4
    return to_signed_bits(offset,21)

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


def runner(n):#all the instruction are seperated by their type or by diff opcode [note:- i have used opcode copied from web]
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
        return encoding_r("0110011",f3s[temp[0]],f7s[temp[0]],get_register(temp[1]),get_register(temp[2]),get_register(temp[3]))
    
    #i type instru
    if temp[0]=="addi":
         return encoding_i("0010011","000",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))
    if temp[0]=="lw":
        r5,imm12=paranthesis_tackle(temp[2])
        return encoding_i("0000011","010",get_register(temp[1]),r5,imm12)
    if temp[0]=="sltiu":
        return encoding_i("0010011","011",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))
    if temp[0]=="jalr":
        return encoding_i("1100111","000",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))

    #s type instru 0100011
    if temp[0]=="sw":
        r5,imm12=paranthesis_tackle(temp[2])
        return encoding_s("0100011","010",r5,get_register(temp[1]),imm12)
    
    #b type instru 1100011
    b3={'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
    if temp[0] in b3:
        return encoding_b("1100011",b3[temp[0]],get_register(temp[1]),get_register(temp[2]),lable_offset_b(temp[3]))
    #u type instru
    if temp[0]=='lui':
        return encoding_u("0110111",get_register(temp[1]),format(int(temp[2])&0xFFFFF,"020b"))
    if temp[0]=='auipc':
        return encoding_u("0010111",get_register(temp[1]),format(int(temp[2])&0xFFFFF,"020b"))

    #j type instru
    if temp[0]=='jal':
        return encoding_j("1101111",get_register(temp[1]),lable_offset_j(temp[2]))
    
while program_counter<len(pure_lines):
    instru_lines.append(runner(program_counter))
    program_counter+=1

for line in instru_lines:
    print(line)
    
#the code it working now and printing all the line tho but iam not verifying them all 
#~piyush
