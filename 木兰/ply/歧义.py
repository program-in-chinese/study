# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'NUMBER',
    'PLUS','TIMES'
    )

# Tokens

t_PLUS    = r'\+'
t_TIMES   = r'\*'

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# Parsing rules

#precedence = (
#    ('left','PLUS'),
#    ('left','TIMES'),
#    )

# dictionary of names
names = { }

def p_expression_binop(t):
    '''expression : expression PLUS expression
                  | expression TIMES expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]

def p_expression_number(t):
    'expression : NUMBER'
    t[0] = t[1]

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
parser = yacc.yacc(debug=True)

parser.parse('2*3+4')
