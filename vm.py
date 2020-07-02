#!/usr/bin/python3

import sys
import instruction_set

args = sys.argv

if len(args) == 1:
    print("Usage: python3 " + args[0] + " filename")
    exit(0)

registers = [0, 0, 0, 0]

register_locations = {
    "ACCUMULATOR": 0,
    "REG_A": 1,
    "REG_B": 2
}

accumulator_temp = 0



filename = args[1]

with open(filename, "rb") as file:
    file_contents = list(file.read())


instruction = 0
exit_code = 0
instruction_pointer = 0

def vm_exit():
    print("VM Ended")
    print("Program Finished with Exit Code: " + str(exit_code))
    exit(0)

def load_accumulator_instruction():
    if str(instruction) == instruction_set.instruction_set.get("LOAD_ACCUMULATOR"):
        if hex(file_contents[instruction_pointer + 1]) == instruction_set.instruction_set.get("VALUE"):
            print("LOADING VALUE INTO ACCUMULATOR...")
            accumulator_temp = hex(file_contents[instruction_pointer + 2])
            registers[register_locations.get("ACCUMULATOR")] = accumulator_temp
        else:
            print("Error While Parsing File: NO VALUE FOUND FOR LOAD_ACCUMULATOR")


def load_register_a_instruction():
    if str(instruction) == instruction_set.instruction_set.get("LOAD_A"):
        if hex(file_contents[instruction_pointer + 1]) == instruction_set.instruction_set.get("VALUE"):
            print("LOADING VALUE INTO REGISTER_A...")
            accumulator_temp = hex(file_contents[instruction_pointer + 2])
            registers[register_locations.get("REG_A")] = accumulator_temp
        else:
            print("Error While Parsing File: NO VALUE FOUND FOR LOAD_ACCUMULATOR")

def load_register_b_instruction():
    if str(instruction) == instruction_set.instruction_set.get("LOAD_B"):
        if hex(file_contents[instruction_pointer + 1]) == instruction_set.instruction_set.get("VALUE"):
            print("LOADING VALUE INTO REGISTER_B...")
            accumulator_temp = hex(file_contents[instruction_pointer + 2])
            registers[register_locations.get("REG_B")] = accumulator_temp
        else:
            print("Error While Parsing File: NO VALUE FOUND FOR LOAD_ACCUMULATOR")
def load_add_to_accum_instruction():
    if str(instruction) == instruction_set.instruction_set.get("ADD_ACCUM"):
        print("ADDING VALUE TO ACCUMULATOR")
        accumulator_temp = hex(file_contents[instruction_pointer + 2])
        registers[register_locations.get("ACCUMULATOR")] += accumulator_temp

def load_add_to_register_a_from_b_instruction():
    if str(instruction) == instruction_set.instruction_set.get("ADD_REG_B_TO_A"):
        print("ADDING VALUE from Register_B TO Register_A")
        string = str(registers[register_locations.get("REG_A")])
        string2 = string.replace("0x", '')

        reg_b = str(registers[register_locations.get("REG_B")]).replace("0x", '')

        reg_b = hex(int(reg_b, 16) + int(string2, 16))
        registers[register_locations.get("REG_A")] = str(reg_b)

def load_add_to_register_b_from_a_instruction():
    if str(instruction) == instruction_set.instruction_set.get("ADD_REG_A_TO_B"):
        print("ADDING VALUE from Register_A TO Register_B")
        string = str(registers[register_locations.get("REG_B")])
        string2 = string.replace("0x", '')

        reg_a = str(registers[register_locations.get("REG_A")]).replace("0x", '')

        reg_a = hex(int(reg_a, 16) + int(string2, 16))
        registers[register_locations.get("REG_B")] = str(reg_a)

def load_wait_instruction():
    if str(instruction) == instruction_set.instruction_set.get("WAIT"):
        input("The Program " + filename + " is waiting until you press enter: ")

print("VM Started")
while instruction_pointer < len(file_contents):
    instruction = hex(file_contents[instruction_pointer])
    print("Registers: " + str(registers))
    if str(instruction) == instruction_set.instruction_set.get("HALT"):
        vm_exit()
    load_accumulator_instruction()
    load_register_a_instruction()
    load_register_b_instruction()
    load_add_to_accum_instruction()
    load_add_to_register_a_from_b_instruction()
    load_add_to_register_b_from_a_instruction()
    load_wait_instruction()

    instruction_pointer += 1

vm_exit()