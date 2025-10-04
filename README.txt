
Language Design: 

    Assembly extension: .vasm 
    Compiled bin extension: .vbin 

Syntax Design:

& -> register directions
# -> number literals 

Assembly Example:

    NOP 
    ADD &save &num1 &num2 
    SUB &save &num1 &num2 
    IF cond DOIF ... ENDIF 