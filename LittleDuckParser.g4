parser grammar LittleDuckParser;

options { tokenVocab=LittleDuckLexer; }

programa : PROGRAM ID SEMICOLON vars bloque END;

vars : VAR var_decl+ | ;

var_decl : ID (COMMA ID)* COLON tipo SEMICOLON;

tipo : INT | FLOAT;

bloque : LBRACE estatuto* RBRACE;

estatuto : asignacion
         | condicion
         | ciclo
         | escritura
         ;

asignacion : ID EQUAL expresion SEMICOLON;

condicion : IF LPAREN expresion RPAREN bloque (ELSE bloque)?;

ciclo : WHILE LPAREN expresion RPAREN bloque;

escritura : PRINT LPAREN (expresion (COMMA expresion)*)? RPAREN SEMICOLON;

expresion : exp ( (LT | GT | EQUAL | NEQ) exp )?;

exp : termino ( (PLUS | MINUS) termino )*;

termino : factor ( (MULT | DIV) factor )*;

factor : LPAREN expresion RPAREN
       | PLUS factor
       | MINUS factor
       | var_cte;

var_cte : ID | CTE_INT | CTE_FLOAT | CTE_STRING;