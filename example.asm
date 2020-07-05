load accum 5 # any comments work 
load a 5 # load register a to 0x05
load b 5 
add_a b
add_a b // Adds a into B
# example of moving a value into register a from register b
load a 0 # loads a to 0
add_b a
# and the value is moved yay

wait # wait for user to press enter

hlt # Halts the Machine