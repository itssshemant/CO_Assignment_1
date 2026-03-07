#initialisation of project creating all the variables and input taker for assembler and eazy testing
lines=["adii r1 ,r1 ,5"]
program_counter=0
instru_lines=[]
regs={#all regs for memonic handling
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

def runner():
    return

while program_counter<len(pure_lines):
    runner(program_counter)
    program_counter+=1

for line in instru_lines:
    print(line)
#~hemant