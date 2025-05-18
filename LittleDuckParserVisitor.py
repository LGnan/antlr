# Generated from LittleDuckParser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LittleDuckParser import LittleDuckParser
else:
    from LittleDuckParser import LittleDuckParser

# This class defines a complete generic visitor for a parse tree produced by LittleDuckParser.

class LittleDuckParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LittleDuckParser#programa.
    def visitPrograma(self, ctx:LittleDuckParser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#vars.
    def visitVars(self, ctx:LittleDuckParser.VarsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#var_decl.
    def visitVar_decl(self, ctx:LittleDuckParser.Var_declContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#tipo.
    def visitTipo(self, ctx:LittleDuckParser.TipoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#bloque.
    def visitBloque(self, ctx:LittleDuckParser.BloqueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#estatuto.
    def visitEstatuto(self, ctx:LittleDuckParser.EstatutoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#asignacion.
    def visitAsignacion(self, ctx:LittleDuckParser.AsignacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#condicion.
    def visitCondicion(self, ctx:LittleDuckParser.CondicionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#ciclo.
    def visitCiclo(self, ctx:LittleDuckParser.CicloContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#escritura.
    def visitEscritura(self, ctx:LittleDuckParser.EscrituraContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#expresion.
    def visitExpresion(self, ctx:LittleDuckParser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#exp.
    def visitExp(self, ctx:LittleDuckParser.ExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#termino.
    def visitTermino(self, ctx:LittleDuckParser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#factor.
    def visitFactor(self, ctx:LittleDuckParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LittleDuckParser#var_cte.
    def visitVar_cte(self, ctx:LittleDuckParser.Var_cteContext):
        return self.visitChildren(ctx)



del LittleDuckParser