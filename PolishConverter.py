#*********************************************************************************
#* Copyright (C) 2020 Vitalii Romakh vitalik55575@gmail.com
#* 
#* This file is part of FunctionConverter.
#* 
#* VerilogFromTruthTable can not be copied and/or distributed without the express
#* permission of Vitalii Romakh
#*********************************************************************************

import argparse # To proccess input arguments
import math


def is_digit(n):
    try:
        float(n)
        return True
    except ValueError:
        return  False

def calculate(input_str):
    output_function_str = ""

    splited_input_str = input_str.split(" ")
    splited_input_str.pop() #delete "" from the end of the string
    
    a = ""
    b = ""
    c = ""
    res = 0
    charachter_ind = 0
    changed = False

    while charachter_ind < len(splited_input_str):
              

        if(changed):
            charachter_ind = 0
        
        changed = False
        
        if(charachter_ind < len(splited_input_str) - 2 ):
            a = splited_input_str[charachter_ind]
            b = splited_input_str[charachter_ind + 1]
            c = splited_input_str[charachter_ind + 2]
        else:
            break
            
        a_isdigit = is_digit(a)          #Added this function because str.isdigit() cast negative numbers as not numbers
        b_isdigit = is_digit(b)

        if(func_priority.get(c) != None and a_isdigit and b_isdigit):
            changed = True
            if(c == "+"):
                res = float(a) + float(b)
            elif(c == "-"):
                res = float(a) - float(b)
            elif(c == "*"):
                res = float(a) * float(b)
            elif(c == "/"):
                res = float(a) / float(b)
            elif(c == "^"):
                res = math.pow(float(a),float(b))

            if(changed):
                splited_input_str.pop(charachter_ind)
                splited_input_str.pop(charachter_ind)
                splited_input_str.pop(charachter_ind)
                splited_input_str.insert(charachter_ind,str(res))
            
        
        charachter_ind += 1

    output_function_str = splited_input_str[0]
    return(output_function_str)
  



arg_parser = argparse.ArgumentParser(description="Simple calculator")

arg_parser.add_argument("--f", required=True,help="Function which should be calculated",type=str)


console_arg = arg_parser.parse_args()


func_priority = {"^":4,"*":3,"/":3,"+":2,"-":2,"(":1,")":1}
original_function_str = console_arg.f
output_function_str = ""


operation_stack = [] 
was_space = False

bracket_counter = 0
charachter = ""
operation = ""

stack_appended = False
prev_was_number = False


for charachter in original_function_str:

    if(charachter.isnumeric()):
        
        if(prev_was_number == True):       
            if(len(output_function_str)>0):                                                                         
                output_function_str = output_function_str[:-1] 
        prev_was_number = True  
        output_function_str += charachter
        output_function_str +=" " 

    elif(func_priority.get(charachter) != None):
        prev_was_number = False 
        current_func_prior = func_priority.get(charachter)

        if(charachter == "("):
            operation_stack.append(charachter)
            bracket_counter += 1
            continue
            
        if(charachter == ")"):
            if(bracket_counter > 0):
                bracket_counter -= 1
                operation =  operation_stack.pop()
                
                while(operation != "("): 
                    output_function_str += operation   
                    output_function_str +=" "                                                                    
                    operation =  operation_stack.pop()
                continue    
            else:
                raise Exception("Wrong bracket amount, check bracket parity!")
        
        if(len(operation_stack) == 0):
            operation_stack.append(charachter)
            stack_appended = True
            continue
        
        if(len(operation_stack) > 0):
            while(current_func_prior <= func_priority.get(operation_stack[len(operation_stack)-1])):
                operation = operation_stack.pop()
                output_function_str += operation
                output_function_str +=" "   
                if(len(operation_stack) == 0):
                    break

        operation_stack += charachter
    else:
        raise Exception("Wrong input symbol!")

if(bracket_counter > 0):
    raise Exception("Wrong bracket amount, check bracket parity!")


stack_left = len(operation_stack)
while(stack_left > 0):
    stack_left -= 1
    operation = operation_stack.pop()
    output_function_str += operation
    output_function_str +=" "

print(output_function_str)    
print(calculate(output_function_str))









