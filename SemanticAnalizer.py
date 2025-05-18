# este es el analizador semantico
from LittleDuckParser import LittleDuckParser
from LittleDuckParserVisitor import LittleDuckParserVisitor

class SemanticError(Exception):
    pass

class SemanticAnalyzer(LittleDuckParserVisitor):
    def __init__(self):
        self.function_directory = {}
        self.constants_table = {}
        self.current_function = None

    def visitPrograma(self, ctx: LittleDuckParser.ProgramaContext):
        func_name = ctx.ID().getText()
        self._add_function(func_name, 'void')
        self.current_function = func_name

        if ctx.vars_():
            self.visit(ctx.vars_())
        self.visit(ctx.bloque())
        return

    def visitVars(self, ctx: LittleDuckParser.VarsContext):
        for var_decl in ctx.var_decl():
            self.visit(var_decl)

    def visitVar_decl(self, ctx: LittleDuckParser.Var_declContext):
        var_type = ctx.tipo().getText()
        for id_token in ctx.ID():
            var_name = id_token.getText()
            self._add_variable(self.current_function, var_name, var_type)

    def visitAsignacion(self, ctx: LittleDuckParser.AsignacionContext):
        var_name = ctx.ID().getText()
        if not self._var_declared(self.current_function, var_name):
            raise SemanticError(f"Variable '{var_name}' no declarada antes de usarse.")
        self.visit(ctx.expresion())

    def visitEscritura(self, ctx: LittleDuckParser.EscrituraContext):
        for expr in ctx.expresion():
            self.visit(expr)

    def visitExpresion(self, ctx: LittleDuckParser.ExpresionContext):
        if ctx.exp():
            self.visit(ctx.exp(0))
            if len(ctx.exp()) > 1:
                self.visit(ctx.exp(1))

    def visitExp(self, ctx: LittleDuckParser.ExpContext):
        for t in ctx.termino():
            self.visit(t)

    def visitTermino(self, ctx: LittleDuckParser.TerminoContext):
        for f in ctx.factor():
            self.visit(f)

    def visitFactor(self, ctx: LittleDuckParser.FactorContext):
        if ctx.expresion():
            self.visit(ctx.expresion())
        elif ctx.var_cte():
            self.visit(ctx.var_cte())

    def visitVar_cte(self, ctx: LittleDuckParser.Var_cteContext):
        token = ctx.getText()
        if ctx.ID():
            var_name = token
            if not self._var_declared(self.current_function, var_name):
                raise SemanticError(f"Variable '{var_name}' no declarada.")
        else:
            self._add_constant(token)

    def _add_function(self, name, return_type):
        if name in self.function_directory:
            raise SemanticError(f"Funci\u00f3n '{name}' ya fue declarada.")
        self.function_directory[name] = {
            "type": return_type,
            "params": [],
            "vars": {}
        }

    def _add_variable(self, func, name, var_type):
        if name in self.function_directory[func]["vars"]:
            raise SemanticError(f"Variable '{name}' ya declarada en funcion '{func}'.")
        self.function_directory[func]["vars"][name] = {"type": var_type}

    def _var_declared(self, func, name):
        return name in self.function_directory[func]["vars"]

    def _add_constant(self, value):
        if value not in self.constants_table:
            if value.isdigit():
                self.constants_table[value] = {"type": "int"}
            elif self._is_float(value):
                self.constants_table[value] = {"type": "float"}
            elif value.startswith('"') and value.endswith('"'):
                self.constants_table[value] = {"type": "string"}

    def _is_float(self, val):
        try:
            float(val)
            return '.' in val
        except:
            return False
    def _is_int(self, val):
        try:
            int(val)
            return '.' not in val
        except:
            return False
    def _is_string(self, val):
        return val.startswith('"') and val.endswith('"')
    def _is_bool(self, val):
        return val in ['true', 'false']