
Language Design: 

    Assembly extension: .vasm 
    Compiled bin extension: .vbin 

Syntax Design:

& -> register directions
# -> number literals 

What istructions are available?:
    For now, the instruction set we are going to use
    is a reduced RISC-V set, it supports all of the 
    arithmetic operations except division and all of
    the logic operations


Assembly Example:

    # This is a comment
    NOP 
    ADD &save &num1 &num2
    SUB &save &num1 &num2
    ADDI &save &num1 #imm 
    IF cond DOIF ... ENDIF (Not implemented yet)