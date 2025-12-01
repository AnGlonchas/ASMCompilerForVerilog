
Language Design: 

    Assembly extension: .vasm 
    Compiled bin extension: .vbin 

Syntax Design:

$ -> register directions
# -> number literals 

What instructions are available?:

    For now, the instruction set we are going to use
    is a reduced MIPS32 set

Assembly Example:

    # This is a comment
    ADD &save &num1 &num2
    SUB &save &num1 &num2
    ADDI &save &num1 imm
