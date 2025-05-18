# Generated from LittleDuckParser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,33,145,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,4,1,40,8,1,11,1,12,
        1,41,1,1,3,1,45,8,1,1,2,1,2,1,2,5,2,50,8,2,10,2,12,2,53,9,2,1,2,
        1,2,1,2,1,2,1,3,1,3,1,4,1,4,5,4,63,8,4,10,4,12,4,66,9,4,1,4,1,4,
        1,5,1,5,1,5,1,5,3,5,74,8,5,1,6,1,6,1,6,1,6,1,6,1,7,1,7,1,7,1,7,1,
        7,1,7,1,7,3,7,88,8,7,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,1,9,
        5,9,101,8,9,10,9,12,9,104,9,9,3,9,106,8,9,1,9,1,9,1,9,1,10,1,10,
        1,10,3,10,114,8,10,1,11,1,11,1,11,5,11,119,8,11,10,11,12,11,122,
        9,11,1,12,1,12,1,12,5,12,127,8,12,10,12,12,12,130,9,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,13,1,13,3,13,141,8,13,1,14,1,14,1,14,
        0,0,15,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,0,5,1,0,5,6,1,0,21,
        24,1,0,17,18,1,0,19,20,1,0,13,16,145,0,30,1,0,0,0,2,44,1,0,0,0,4,
        46,1,0,0,0,6,58,1,0,0,0,8,60,1,0,0,0,10,73,1,0,0,0,12,75,1,0,0,0,
        14,80,1,0,0,0,16,89,1,0,0,0,18,95,1,0,0,0,20,110,1,0,0,0,22,115,
        1,0,0,0,24,123,1,0,0,0,26,140,1,0,0,0,28,142,1,0,0,0,30,31,5,1,0,
        0,31,32,5,13,0,0,32,33,5,29,0,0,33,34,3,2,1,0,34,35,3,8,4,0,35,36,
        5,3,0,0,36,1,1,0,0,0,37,39,5,4,0,0,38,40,3,4,2,0,39,38,1,0,0,0,40,
        41,1,0,0,0,41,39,1,0,0,0,41,42,1,0,0,0,42,45,1,0,0,0,43,45,1,0,0,
        0,44,37,1,0,0,0,44,43,1,0,0,0,45,3,1,0,0,0,46,51,5,13,0,0,47,48,
        5,30,0,0,48,50,5,13,0,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,0,0,
        0,51,52,1,0,0,0,52,54,1,0,0,0,53,51,1,0,0,0,54,55,5,31,0,0,55,56,
        3,6,3,0,56,57,5,29,0,0,57,5,1,0,0,0,58,59,7,0,0,0,59,7,1,0,0,0,60,
        64,5,27,0,0,61,63,3,10,5,0,62,61,1,0,0,0,63,66,1,0,0,0,64,62,1,0,
        0,0,64,65,1,0,0,0,65,67,1,0,0,0,66,64,1,0,0,0,67,68,5,28,0,0,68,
        9,1,0,0,0,69,74,3,12,6,0,70,74,3,14,7,0,71,74,3,16,8,0,72,74,3,18,
        9,0,73,69,1,0,0,0,73,70,1,0,0,0,73,71,1,0,0,0,73,72,1,0,0,0,74,11,
        1,0,0,0,75,76,5,13,0,0,76,77,5,21,0,0,77,78,3,20,10,0,78,79,5,29,
        0,0,79,13,1,0,0,0,80,81,5,8,0,0,81,82,5,25,0,0,82,83,3,20,10,0,83,
        84,5,26,0,0,84,87,3,8,4,0,85,86,5,9,0,0,86,88,3,8,4,0,87,85,1,0,
        0,0,87,88,1,0,0,0,88,15,1,0,0,0,89,90,5,10,0,0,90,91,5,25,0,0,91,
        92,3,20,10,0,92,93,5,26,0,0,93,94,3,8,4,0,94,17,1,0,0,0,95,96,5,
        12,0,0,96,105,5,25,0,0,97,102,3,20,10,0,98,99,5,30,0,0,99,101,3,
        20,10,0,100,98,1,0,0,0,101,104,1,0,0,0,102,100,1,0,0,0,102,103,1,
        0,0,0,103,106,1,0,0,0,104,102,1,0,0,0,105,97,1,0,0,0,105,106,1,0,
        0,0,106,107,1,0,0,0,107,108,5,26,0,0,108,109,5,29,0,0,109,19,1,0,
        0,0,110,113,3,22,11,0,111,112,7,1,0,0,112,114,3,22,11,0,113,111,
        1,0,0,0,113,114,1,0,0,0,114,21,1,0,0,0,115,120,3,24,12,0,116,117,
        7,2,0,0,117,119,3,24,12,0,118,116,1,0,0,0,119,122,1,0,0,0,120,118,
        1,0,0,0,120,121,1,0,0,0,121,23,1,0,0,0,122,120,1,0,0,0,123,128,3,
        26,13,0,124,125,7,3,0,0,125,127,3,26,13,0,126,124,1,0,0,0,127,130,
        1,0,0,0,128,126,1,0,0,0,128,129,1,0,0,0,129,25,1,0,0,0,130,128,1,
        0,0,0,131,132,5,25,0,0,132,133,3,20,10,0,133,134,5,26,0,0,134,141,
        1,0,0,0,135,136,5,17,0,0,136,141,3,26,13,0,137,138,5,18,0,0,138,
        141,3,26,13,0,139,141,3,28,14,0,140,131,1,0,0,0,140,135,1,0,0,0,
        140,137,1,0,0,0,140,139,1,0,0,0,141,27,1,0,0,0,142,143,7,4,0,0,143,
        29,1,0,0,0,12,41,44,51,64,73,87,102,105,113,120,128,140
    ]

class LittleDuckParser ( Parser ):

    grammarFileName = "LittleDuckParser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'program'", "'main'", "'end'", "'var'", 
                     "'int'", "'float'", "'void'", "'if'", "'else'", "'while'", 
                     "'do'", "'print'", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'='", "'!='", 
                     "'<'", "'>'", "'('", "')'", "'{'", "'}'", "';'", "','", 
                     "':'" ]

    symbolicNames = [ "<INVALID>", "PROGRAM", "MAIN", "END", "VAR", "INT", 
                      "FLOAT", "VOID", "IF", "ELSE", "WHILE", "DO", "PRINT", 
                      "ID", "CTE_INT", "CTE_FLOAT", "CTE_STRING", "PLUS", 
                      "MINUS", "MULT", "DIV", "EQUAL", "NEQ", "LT", "GT", 
                      "LPAREN", "RPAREN", "LBRACE", "RBRACE", "SEMICOLON", 
                      "COMMA", "COLON", "LINE_COMMENT", "WS" ]

    RULE_programa = 0
    RULE_vars = 1
    RULE_var_decl = 2
    RULE_tipo = 3
    RULE_bloque = 4
    RULE_estatuto = 5
    RULE_asignacion = 6
    RULE_condicion = 7
    RULE_ciclo = 8
    RULE_escritura = 9
    RULE_expresion = 10
    RULE_exp = 11
    RULE_termino = 12
    RULE_factor = 13
    RULE_var_cte = 14

    ruleNames =  [ "programa", "vars", "var_decl", "tipo", "bloque", "estatuto", 
                   "asignacion", "condicion", "ciclo", "escritura", "expresion", 
                   "exp", "termino", "factor", "var_cte" ]

    EOF = Token.EOF
    PROGRAM=1
    MAIN=2
    END=3
    VAR=4
    INT=5
    FLOAT=6
    VOID=7
    IF=8
    ELSE=9
    WHILE=10
    DO=11
    PRINT=12
    ID=13
    CTE_INT=14
    CTE_FLOAT=15
    CTE_STRING=16
    PLUS=17
    MINUS=18
    MULT=19
    DIV=20
    EQUAL=21
    NEQ=22
    LT=23
    GT=24
    LPAREN=25
    RPAREN=26
    LBRACE=27
    RBRACE=28
    SEMICOLON=29
    COMMA=30
    COLON=31
    LINE_COMMENT=32
    WS=33

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PROGRAM(self):
            return self.getToken(LittleDuckParser.PROGRAM, 0)

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def SEMICOLON(self):
            return self.getToken(LittleDuckParser.SEMICOLON, 0)

        def vars_(self):
            return self.getTypedRuleContext(LittleDuckParser.VarsContext,0)


        def bloque(self):
            return self.getTypedRuleContext(LittleDuckParser.BloqueContext,0)


        def END(self):
            return self.getToken(LittleDuckParser.END, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = LittleDuckParser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self.match(LittleDuckParser.PROGRAM)
            self.state = 31
            self.match(LittleDuckParser.ID)
            self.state = 32
            self.match(LittleDuckParser.SEMICOLON)
            self.state = 33
            self.vars_()
            self.state = 34
            self.bloque()
            self.state = 35
            self.match(LittleDuckParser.END)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class VarsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(LittleDuckParser.VAR, 0)

        def var_decl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.Var_declContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.Var_declContext,i)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_vars

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVars" ):
                listener.enterVars(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVars" ):
                listener.exitVars(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVars" ):
                return visitor.visitVars(self)
            else:
                return visitor.visitChildren(self)




    def vars_(self):

        localctx = LittleDuckParser.VarsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_vars)
        self._la = 0 # Token type
        try:
            self.state = 44
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [4]:
                self.enterOuterAlt(localctx, 1)
                self.state = 37
                self.match(LittleDuckParser.VAR)
                self.state = 39 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while True:
                    self.state = 38
                    self.var_decl()
                    self.state = 41 
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if not (_la==13):
                        break

                pass
            elif token in [27]:
                self.enterOuterAlt(localctx, 2)

                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_declContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.ID)
            else:
                return self.getToken(LittleDuckParser.ID, i)

        def COLON(self):
            return self.getToken(LittleDuckParser.COLON, 0)

        def tipo(self):
            return self.getTypedRuleContext(LittleDuckParser.TipoContext,0)


        def SEMICOLON(self):
            return self.getToken(LittleDuckParser.SEMICOLON, 0)

        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.COMMA)
            else:
                return self.getToken(LittleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_var_decl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_decl" ):
                listener.enterVar_decl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_decl" ):
                listener.exitVar_decl(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_decl" ):
                return visitor.visitVar_decl(self)
            else:
                return visitor.visitChildren(self)




    def var_decl(self):

        localctx = LittleDuckParser.Var_declContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_var_decl)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.match(LittleDuckParser.ID)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==30:
                self.state = 47
                self.match(LittleDuckParser.COMMA)
                self.state = 48
                self.match(LittleDuckParser.ID)
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(LittleDuckParser.COLON)
            self.state = 55
            self.tipo()
            self.state = 56
            self.match(LittleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INT(self):
            return self.getToken(LittleDuckParser.INT, 0)

        def FLOAT(self):
            return self.getToken(LittleDuckParser.FLOAT, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_tipo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipo" ):
                listener.enterTipo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipo" ):
                listener.exitTipo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipo" ):
                return visitor.visitTipo(self)
            else:
                return visitor.visitChildren(self)




    def tipo(self):

        localctx = LittleDuckParser.TipoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_tipo)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            _la = self._input.LA(1)
            if not(_la==5 or _la==6):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACE(self):
            return self.getToken(LittleDuckParser.LBRACE, 0)

        def RBRACE(self):
            return self.getToken(LittleDuckParser.RBRACE, 0)

        def estatuto(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.EstatutoContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.EstatutoContext,i)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = LittleDuckParser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 60
            self.match(LittleDuckParser.LBRACE)
            self.state = 64
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 13568) != 0):
                self.state = 61
                self.estatuto()
                self.state = 66
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 67
            self.match(LittleDuckParser.RBRACE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EstatutoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def asignacion(self):
            return self.getTypedRuleContext(LittleDuckParser.AsignacionContext,0)


        def condicion(self):
            return self.getTypedRuleContext(LittleDuckParser.CondicionContext,0)


        def ciclo(self):
            return self.getTypedRuleContext(LittleDuckParser.CicloContext,0)


        def escritura(self):
            return self.getTypedRuleContext(LittleDuckParser.EscrituraContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_estatuto

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEstatuto" ):
                listener.enterEstatuto(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEstatuto" ):
                listener.exitEstatuto(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEstatuto" ):
                return visitor.visitEstatuto(self)
            else:
                return visitor.visitChildren(self)




    def estatuto(self):

        localctx = LittleDuckParser.EstatutoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_estatuto)
        try:
            self.state = 73
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [13]:
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.asignacion()
                pass
            elif token in [8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.condicion()
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.ciclo()
                pass
            elif token in [12]:
                self.enterOuterAlt(localctx, 4)
                self.state = 72
                self.escritura()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AsignacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def EQUAL(self):
            return self.getToken(LittleDuckParser.EQUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def SEMICOLON(self):
            return self.getToken(LittleDuckParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_asignacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAsignacion" ):
                listener.enterAsignacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAsignacion" ):
                listener.exitAsignacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAsignacion" ):
                return visitor.visitAsignacion(self)
            else:
                return visitor.visitChildren(self)




    def asignacion(self):

        localctx = LittleDuckParser.AsignacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_asignacion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 75
            self.match(LittleDuckParser.ID)
            self.state = 76
            self.match(LittleDuckParser.EQUAL)
            self.state = 77
            self.expresion()
            self.state = 78
            self.match(LittleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CondicionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(LittleDuckParser.IF, 0)

        def LPAREN(self):
            return self.getToken(LittleDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LittleDuckParser.RPAREN, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.BloqueContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.BloqueContext,i)


        def ELSE(self):
            return self.getToken(LittleDuckParser.ELSE, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_condicion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondicion" ):
                listener.enterCondicion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondicion" ):
                listener.exitCondicion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCondicion" ):
                return visitor.visitCondicion(self)
            else:
                return visitor.visitChildren(self)




    def condicion(self):

        localctx = LittleDuckParser.CondicionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_condicion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(LittleDuckParser.IF)
            self.state = 81
            self.match(LittleDuckParser.LPAREN)
            self.state = 82
            self.expresion()
            self.state = 83
            self.match(LittleDuckParser.RPAREN)
            self.state = 84
            self.bloque()
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==9:
                self.state = 85
                self.match(LittleDuckParser.ELSE)
                self.state = 86
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CicloContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LittleDuckParser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(LittleDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LittleDuckParser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(LittleDuckParser.BloqueContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_ciclo

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCiclo" ):
                listener.enterCiclo(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCiclo" ):
                listener.exitCiclo(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCiclo" ):
                return visitor.visitCiclo(self)
            else:
                return visitor.visitChildren(self)




    def ciclo(self):

        localctx = LittleDuckParser.CicloContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_ciclo)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(LittleDuckParser.WHILE)
            self.state = 90
            self.match(LittleDuckParser.LPAREN)
            self.state = 91
            self.expresion()
            self.state = 92
            self.match(LittleDuckParser.RPAREN)
            self.state = 93
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EscrituraContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PRINT(self):
            return self.getToken(LittleDuckParser.PRINT, 0)

        def LPAREN(self):
            return self.getToken(LittleDuckParser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(LittleDuckParser.RPAREN, 0)

        def SEMICOLON(self):
            return self.getToken(LittleDuckParser.SEMICOLON, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.ExpresionContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,i)


        def COMMA(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.COMMA)
            else:
                return self.getToken(LittleDuckParser.COMMA, i)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_escritura

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEscritura" ):
                listener.enterEscritura(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEscritura" ):
                listener.exitEscritura(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEscritura" ):
                return visitor.visitEscritura(self)
            else:
                return visitor.visitChildren(self)




    def escritura(self):

        localctx = LittleDuckParser.EscrituraContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_escritura)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 95
            self.match(LittleDuckParser.PRINT)
            self.state = 96
            self.match(LittleDuckParser.LPAREN)
            self.state = 105
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 34070528) != 0):
                self.state = 97
                self.expresion()
                self.state = 102
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==30:
                    self.state = 98
                    self.match(LittleDuckParser.COMMA)
                    self.state = 99
                    self.expresion()
                    self.state = 104
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 107
            self.match(LittleDuckParser.RPAREN)
            self.state = 108
            self.match(LittleDuckParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def exp(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.ExpContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.ExpContext,i)


        def LT(self):
            return self.getToken(LittleDuckParser.LT, 0)

        def GT(self):
            return self.getToken(LittleDuckParser.GT, 0)

        def EQUAL(self):
            return self.getToken(LittleDuckParser.EQUAL, 0)

        def NEQ(self):
            return self.getToken(LittleDuckParser.NEQ, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = LittleDuckParser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.exp()
            self.state = 113
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0):
                self.state = 111
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 31457280) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 112
                self.exp()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.TerminoContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.TerminoContext,i)


        def PLUS(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.PLUS)
            else:
                return self.getToken(LittleDuckParser.PLUS, i)

        def MINUS(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.MINUS)
            else:
                return self.getToken(LittleDuckParser.MINUS, i)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_exp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExp" ):
                listener.enterExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExp" ):
                listener.exitExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExp" ):
                return visitor.visitExp(self)
            else:
                return visitor.visitChildren(self)




    def exp(self):

        localctx = LittleDuckParser.ExpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_exp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.termino()
            self.state = 120
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==17 or _la==18:
                self.state = 116
                _la = self._input.LA(1)
                if not(_la==17 or _la==18):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 117
                self.termino()
                self.state = 122
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LittleDuckParser.FactorContext)
            else:
                return self.getTypedRuleContext(LittleDuckParser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.MULT)
            else:
                return self.getToken(LittleDuckParser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(LittleDuckParser.DIV)
            else:
                return self.getToken(LittleDuckParser.DIV, i)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = LittleDuckParser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.factor()
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==19 or _la==20:
                self.state = 124
                _la = self._input.LA(1)
                if not(_la==19 or _la==20):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 125
                self.factor()
                self.state = 130
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(LittleDuckParser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(LittleDuckParser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(LittleDuckParser.RPAREN, 0)

        def PLUS(self):
            return self.getToken(LittleDuckParser.PLUS, 0)

        def factor(self):
            return self.getTypedRuleContext(LittleDuckParser.FactorContext,0)


        def MINUS(self):
            return self.getToken(LittleDuckParser.MINUS, 0)

        def var_cte(self):
            return self.getTypedRuleContext(LittleDuckParser.Var_cteContext,0)


        def getRuleIndex(self):
            return LittleDuckParser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = LittleDuckParser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_factor)
        try:
            self.state = 140
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [25]:
                self.enterOuterAlt(localctx, 1)
                self.state = 131
                self.match(LittleDuckParser.LPAREN)
                self.state = 132
                self.expresion()
                self.state = 133
                self.match(LittleDuckParser.RPAREN)
                pass
            elif token in [17]:
                self.enterOuterAlt(localctx, 2)
                self.state = 135
                self.match(LittleDuckParser.PLUS)
                self.state = 136
                self.factor()
                pass
            elif token in [18]:
                self.enterOuterAlt(localctx, 3)
                self.state = 137
                self.match(LittleDuckParser.MINUS)
                self.state = 138
                self.factor()
                pass
            elif token in [13, 14, 15, 16]:
                self.enterOuterAlt(localctx, 4)
                self.state = 139
                self.var_cte()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Var_cteContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(LittleDuckParser.ID, 0)

        def CTE_INT(self):
            return self.getToken(LittleDuckParser.CTE_INT, 0)

        def CTE_FLOAT(self):
            return self.getToken(LittleDuckParser.CTE_FLOAT, 0)

        def CTE_STRING(self):
            return self.getToken(LittleDuckParser.CTE_STRING, 0)

        def getRuleIndex(self):
            return LittleDuckParser.RULE_var_cte

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_cte" ):
                listener.enterVar_cte(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_cte" ):
                listener.exitVar_cte(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVar_cte" ):
                return visitor.visitVar_cte(self)
            else:
                return visitor.visitChildren(self)




    def var_cte(self):

        localctx = LittleDuckParser.Var_cteContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_var_cte)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 142
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 122880) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





