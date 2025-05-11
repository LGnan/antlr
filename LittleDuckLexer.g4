lexer grammar LittleDuckLexer;

// Palabras reservadas
PROGRAM : 'program';
MAIN    : 'main';
END     : 'end';
VAR     : 'var';
INT     : 'int';
FLOAT   : 'float';
VOID    : 'void';
IF      : 'if';
ELSE    : 'else';
WHILE   : 'while';
DO      : 'do';
PRINT   : 'print';

// Identificadores y constantes
ID       : [a-zA-Z_][a-zA-Z0-9_]*;
CTE_INT  : [0-9]+;
CTE_FLOAT: [0-9]+ '.' [0-9]+;
CTE_STRING : '"' ( ~["\\] | '\\' . )* '"' ;

// Operadores y delimitadores
PLUS     : '+';
MINUS    : '-';
MULT     : '*';
DIV      : '/';
EQUAL    : '=';
NEQ      : '!=';
LT       : '<';
GT       : '>';
LPAREN   : '(';
RPAREN   : ')';
LBRACE   : '{';
RBRACE   : '}';
SEMICOLON: ';';
COMMA    : ',';
COLON    : ':';

// Comentarios y espacios (se ignoran)
LINE_COMMENT : '//' ~[\r\n]* -> skip;
WS           : [ \t\r\n]+ -> skip;