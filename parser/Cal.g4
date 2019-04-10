// Cal.g4

grammar Cal;

DIGIT : [0-9];
NON_DIGIT : [a-zA-Z_];

VAR_CHAR : [0-9a-zA-Z_];

MOD : 'MOD';
ADD : 'ADD';
SUB : 'SUB';
MUL : 'MUL';
DIV : 'DIV';
POW : 'POW';

integerLiteral
    : DIGIT+ ;


floatLiteral
    : DIGIT '.' DIGIT
    ;

decimalLiteral
    : integerLiteral
    | floatLiteral
    ;

calculator
    : expressionStatement? EOF
    ;

expressionStatement
    : expression (';' expression)* ';'?
    ;

expression
    : sign expression       # signedExpression
    | '(' expression ')'    # parentExpression
    | expression firstPrecedenceMathOperator expression # fpMathOperatorExpression
    | expression secondPrecedenceMathOperator expression # spMathOperatorExpression
    | identifier assign expression  # assignExpression
    | funcCall '('functionArgs?')'       # functionCallExpression
    | decimalLiteral        # literalExpression
    | identifier            # identifierExpression
    ;

firstPrecedenceMathOperator
    : '*' | '/' | '**' | '%' | POW | MUL | DIV | MOD
    ;

secondPrecedenceMathOperator
    : '+' | '-' | ADD | SUB
    ;

funcCall
    : NON_DIGIT (DIGIT | NON_DIGIT)*
    ;

functionArgs
    : expression (',' expression)* ','?
    ;


identifier
    : NON_DIGIT (DIGIT | NON_DIGIT)*
    ;

sign : '+' | '-'
     ;

firstMathOperator
    : '*' | MUL | '/' | 'DIV' | '%' | 'MOD'
    ;


secondMathOperator
    : '+' | 'ADD' | '-' | 'SUB'
    ;

assign
    : VAR_ASSIGN
    | MUL_ASSIGN
    | DIV_ASSIGN
    | ADD_ASSIGN
    | SUB_ASSIGN
    | MOD_ASSIGN
    | POW_ASSIGN
    ;

VAR_ASSIGN   :   '=';
MUL_ASSIGN   :   '*=';
DIV_ASSIGN   :   '/=';
ADD_ASSIGN   :   '+=';
SUB_ASSIGN   :   '-=';
MOD_ASSIGN   :   '%=';
POW_ASSIGN   :   '**=';



WS : [ \r\t\n] ->skip;