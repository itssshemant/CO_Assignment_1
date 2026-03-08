#iteration 7 #last iteration #added complete error handling and compatablity with code in assigment folder
#iteration 6
#iteration 5
#iteration 4 
#iteration 3
#iteration 2
#iteration 1
import sys
if len(sys.argv)<3:
    print('usage: Assembler.py <in> <out> [readable]'); sys.exit(1)
with open(sys.argv[1],'r') as f:
    lines=[l.rstrip('\n').rstrip('\r') for l in f.readlines()]

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
    stripped=line.strip()
    if not stripped: 
        continue
    string=stripped.split()
    temp=[]
    for i in string:
        parts=[p.strip() for p in i.split(',') if p.strip()]
        temp.extend(parts)
    if len(temp)==1 and temp[0].endswith(':'):
        if temp[0].replace(':','') in label_dict:
            print(f"duplicate label '{temp[0].replace(':','')}'")
            sys.exit(1)
        label_dict[temp[0].replace(':','')]=len(pure_lines)
    else:
        if temp[0].endswith(':'):
            if temp[0].replace(':','') in label_dict:
                print(f"duplicate label '{temp[0].replace(':','')}'")
                sys.exit(1)
            label_dict[temp[0].replace(':','')]=len(pure_lines)
            temp=temp[1:]
        pure_lines.append(temp)
        instr_to_line.append(line_num)
#####################################################


def get_register(mnemonic):
    global regs
    if mnemonic not in regs:
        print(f"unknown register '{mnemonic}'")
        sys.exit(1)
    bit=regs[mnemonic]
    return f"{bit:0{5}b}"


def paranthesis_tackle(s):#takeling the paranthesis in some operations for ex:- lw r1 ,-->10(a0)<--here
    global regs
    offset,mnemonic=s.replace(')','').split('(')
    offset=int(offset)
    num=regs[mnemonic]
    
    imm12=to_signed_bits(offset,12)
    rd=f"{num:05b}"
    
    return rd,imm12


def to_signed_bits(val,nbits):#this function convert an immediate value into fixed width 2's complement bits
    if val<0:
        val=val+(1<<nbits)
    return format(val&((1<<nbits)-1),f'0{nbits}b')


def lable_offset_b(lable):
    global label_dict,program_counter
    try:
        offset=int(lable)
    except:
        if lable not in label_dict:
            error(f"undefined label '{lable}'")
        offset=(label_dict[lable]-program_counter)*4
    return to_signed_bits(offset,13)


def lable_offset_j(lable):
    global label_dict,program_counter
    try:
        offset=int(lable)
    except:
        if lable not in label_dict:
            error(f"undefined label '{lable}'")
        offset=(label_dict[lable]-program_counter)*4
    return to_signed_bits(offset,21)

def error(msg):
    print(f"syntax error at line {instr_to_line[program_counter]} : {msg}")
    sys.exit(1)

#encoding block will return all the encoded instruction directly
def encoding_r(opcode, f3, f7, rd, rs1, rs2):
    global instru_lines
    instru_str=f"{f7}{rs2}{rs1}{f3}{rd}{opcode}"
    instru_lines.append(instru_str)
    
def encoding_i(opcode, f3, rd, rs1, imm):
    global instru_lines
    instru_str=f"{imm}{rs1}{f3}{rd}{opcode}"
    instru_lines.append(instru_str)

def encoding_s(opcode, f3, rs1, rs2, imm):
    global instru_lines
    instru_str=f"{imm[:7]}{rs2}{rs1}{f3}{imm[7:]}{opcode}"
    instru_lines.append(instru_str)

def encoding_b(opcode, f3, rs1, rs2, imm):
    global instru_lines
    instru_str=f"{imm[0]}{imm[2:8]}{rs2}{rs1}{f3}{imm[8:12]}{imm[1]}{opcode}"
    instru_lines.append(instru_str)

def encoding_u(opcode, rd, imm):
    global instru_lines
    instru_str=f"{imm[:20]}{rd}{opcode}"
    instru_lines.append(instru_str)

def encoding_j(opcode, rd, imm):
    global instru_lines
    # imm is 21 bits: imm[20|10:1|11|19:12]
    # imm[0]=bit20, imm[1:9]=bit19:12, imm[9]=bit11, imm[10:20]=bit10:1
    instru_str=f"{imm[0]}{imm[10:20]}{imm[9]}{imm[1:9]}{rd}{opcode}"
    instru_lines.append(instru_str)


def runner(n):#all the instruction are seperated by their type or by diff opcode [note:- i have used opcode copied from web]
    global pure_lines,program_counter
    temp=pure_lines[n]
    valid_ops=['add','sub','sll','slt','sltu','xor','srl','or','and','mul',
        'addi','sltiu','jalr','lw','sw',
        'beq','bne','blt','bge','bltu','bgeu',
        'lui','auipc','jal','rvrs','rst','halt']
    if temp[0] not in valid_ops:
        error(f"instruction used is not defined")
        return
        
    f7s = {
        'add':'0000000','sub':'0100000','sll':'0000000','slt':'0000000','sltu':'0000000',
        'xor':'0000000','srl':'0000000','or':'0000000','and':'0000000','mul':'0000001'}
    
    f3s = {
        'add':'000','sub':'000','sll':'001','slt':'010','sltu':'011',
        'xor':'100','srl':'101','or':'110','and':'111','mul':'000'}
    
    #r type instru
    if temp[0] in ("add","sub","sll","slt","sltu","xor","srl","or","and","mul"):
        try:
            encoding_r("0110011",f3s[temp[0]],f7s[temp[0]],get_register(temp[1]),get_register(temp[2]),get_register(temp[3]))
        except:
            error(f"problem in encoding_r")
    if temp[0]=="rvrs":
        try:
            r5,imm12=paranthesis_tackle(temp[2])
            encoding_i("0001011","000","0000000",r5,imm12)
        except:
            error(f"problem in encoding_r")
    
    #i type instru
    if temp[0]=="addi":
        try:
            encoding_i("0010011","000",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))
        except:
            error(f"problem in encoding_i")
    if temp[0]=="lw":
        try:
            r5,imm12=paranthesis_tackle(temp[2])
            encoding_i("0000011","010",get_register(temp[1]),r5,imm12)
        except:
            error(f"problem in encoding_i")
    if temp[0]=="sltiu":
        try:
            encoding_i("0010011","011",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))
        except:
            error(f"problem in encoding_i")
    if temp[0]=="jalr":
        try:
            encoding_i("1100111","000",get_register(temp[1]),get_register(temp[2]),to_signed_bits(int(temp[3]),12))
        except:
            error(f"problem in encoding_i")
    if temp[0]=="rst":
        try:
            encoding_i("1110011","000","00000","00000","000000000001") 
        except:
            error(f"problem in encoding_i")
    if temp[0]=="halt":
        try:
            encoding_i("1110011","000","00000","00000","000000000000")
        except:
            error(f"problem in encoding_i")
    
    #s type instru 0100011
    if temp[0]=="sw":
        try:
            r5,imm12=paranthesis_tackle(temp[2])
            encoding_s("0100011","010",r5,get_register(temp[1]),imm12)
        except:
            error(f"problem in encoding_s")
    
    #b type instru 1100011
    b3={'beq':'000','bne':'001','blt':'100','bge':'101','bltu':'110','bgeu':'111'}
    if temp[0] in b3:
        try:
            encoding_b("1100011",b3[temp[0]],get_register(temp[1]),get_register(temp[2]),lable_offset_b(temp[3]))
        except:
            error(f"problem in encoding_b")
    
    #u type instru
    if temp[0]=='lui':
        try:
            encoding_u("0110111",get_register(temp[1]),format(int(temp[2])&0xFFFFF,"020b"))
        except:
            error(f"problem in encoding_u")
    if temp[0]=='auipc':
        try:
            encoding_u("0010111",get_register(temp[1]),format(int(temp[2])&0xFFFFF,"020b"))
        except:
            error(f"problem in encoding_u")

    #j type instru
    if temp[0]=='jal':
        try:
            encoding_j("1101111",get_register(temp[1]),lable_offset_j(temp[2]))
        except:
            error(f"problem in encoding_j")
    

while program_counter<len(pure_lines):
    runner(program_counter)
    program_counter+=1

with open(sys.argv[2],'w') as f:
    f.write('\n'.join(instru_lines)+'\n')
if len(sys.argv)>3:
    with open(sys.argv[3],'w') as f:
        f.write('\n'.join(instru_lines)+'\n')
#~dev chaudhary
