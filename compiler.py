#!/usr/bin/python3

import sys
import instruction_set


args = sys.argv

if len(args) == 1:
    print("Usage: python3 " + args[0] + " filename")
    exit(0)

filename = args[1]

file = open(filename, "r")

line_num = 0

a_line = []

tokens = {
    "load": "LOAD",
    "hlt": "HLT",
    "accum": "ACCUMULATOR",
    "add_a": "ADD_A",
    "add_b": "ADD_B",
    "wait": "WAIT"
}



token_a = ""
token_b = ""

instructions = []

def exit_compiler():
    print("Error: -1")
    exit(-1)

# Parsing
print("Compiling File to TylerX8 Instruction Set...")
data = file.readlines()
for line in range(len(data)):
    split_data = data[line].split(" ")

    for word in split_data:
        if word == "load":
            print("LOAD INSTRUCTION FOUND!")
            instructions.append("LOAD")
        elif word == "accum":
            print("ACCUM Keyword Found!")
            instructions.append("ACCUM")
        elif word == "a":
            print("REG_A Keyword Found!")
            instructions.append("a")
        elif word == "b":
            print("REG_B Keyword Found!")
            instructions.append("b")
        elif word == "hlt":
            print("HALT Instruction Found!")
            instructions.append("HLT")
        elif word == "add_a":
            print("ADD A Instruction Found!")
            instructions.append("ADD_A")
        elif word == "add_b":
            print("ADD B Instruction Found!")
            instructions.append("ADD_B")
        elif word == "wait":
            instructions.append("wait")
        else:
            instructions.append(word.replace("\n", ''))
print("Using Tokens to Make Machine Code Instructions for TylerX8 Instruction Set...")

# Converting to Machine Code for the Instruction Set
machine_code_instructions = []

i = 0
for i in range(len(instructions)):
    if instructions[i] == "LOAD":
        if instructions[i + 1] == "ACCUM":
            machine_code_instructions.append(instruction_set.instruction_set.get("LOAD_ACCUMULATOR"))
            machine_code_instructions.append(instruction_set.instruction_set.get("VALUE"))
        elif instructions[i + 1] == "a":
            machine_code_instructions.append(instruction_set.instruction_set.get("LOAD_A"))
            machine_code_instructions.append(instruction_set.instruction_set.get("VALUE"))
        elif instructions[i + 1] == "b":
            machine_code_instructions.append(instruction_set.instruction_set.get("LOAD_B"))
            machine_code_instructions.append(instruction_set.instruction_set.get("VALUE"))
        machine_code_instructions.append(instructions[i + 2])
    elif instructions[i] == "ADD_A":
        if instructions[i + 1] == "a":
            machine_code_instructions.append(instruction_set.instruction_set.get("ADD_REG_B_TO_A"))
        elif instructions[i + 1] == "b":
            machine_code_instructions.append(instruction_set.instruction_set.get("ADD_REG_A_TO_B"))
    elif instructions[i] == "ADD_B":
        if instructions[i + 1] == "a":
            machine_code_instructions.append(instruction_set.instruction_set.get("ADD_REG_B_TO_A"))
        elif instructions[i + 1] == "b":
            machine_code_instructions.append(instruction_set.instruction_set.get("ADD_REG_A_TO_B"))
    elif instructions[i] == "wait":
        machine_code_instructions.append(instruction_set.instruction_set.get("WAIT"))
        print("Wait Instruction Found!")
    elif instructions[i] == "HLT":
        machine_code_instructions.append(instruction_set.instruction_set.get("HALT"))

print("Machine Code Instructions Compiled!")
print(machine_code_instructions)

print("Converting Data to Hex...")
file_data = []
for machine_code_instruction in machine_code_instructions:
    file_data += machine_code_instructions

data = []
for machine_code_instruction in machine_code_instructions:
    data.append(int(machine_code_instruction, 16))

print("Writing Compiled Instructions to File!")

with open(filename.split(".")[0] + ".bin", "wb") as binary:
    binary.write(bytes(data))
print("Wrote Compiled Instructions to File.")

print("Compilation Successful.")