# -*- coding:utf-8 -*-
import logging
import antlr4
from parser.CalParser import CalParser
from parser.CalVisitor import CalVisitor
from parser.CalLexer import CalLexer


logging.basicConfig(level=logging.DEBUG)


class VarManager:
    def __init__(self):
        self._identifier = dict()

    def set_value(self, identifier, value):
        self._identifier[identifier] = value

    def get_value(self, identifier):
        if identifier not in self._identifier:
            raise Exception("undefined identifier %s" % identifier)
        return self._identifier.get(identifier)


default_funcs = {
    "+": (lambda x, y: x + y),
    "-": (lambda x, y: x - y),
    "*": (lambda x, y: x * y),
    '/': (lambda x, y: x / y),
    "**": (lambda x, y: x ** y),
    "%": (lambda x, y: x % y),
    "ADD": (lambda x, y: x + y),
    "SUM": (lambda *args: sum(*args)),
    "AVG": (lambda *args: sum(*args) / len(*args)),
    "POW": (lambda x, y: x ** y),
    "SUB": (lambda x, y: x - y),
    "DIV": (lambda x, y: x / y),
    "MUL": (lambda x, y: x * y),
    "MODE": (lambda x, y: x % y)
}


class FuncService:
    func_map = dict()
    func_map.update(default_funcs)

    @staticmethod
    def exec(func_name, *args, **kwargs):
        if func_name not in FuncService.func_map:
            raise Exception("func %s not found" % func_name)
        func = FuncService.func_map.get(func_name)
        return func(*args, **kwargs)

    @staticmethod
    def register_func(func_name, func):
        if func_name in FuncService.func_map:
            print("[warning] func %s already exists" % func_name)
            return
        if not callable(func):
            raise Exception("func %s not callable , check it" % func_name)
        FuncService.func_map[func_name] = func


def func_register(func_name):
    def wrapper(func):
        try:
            FuncService.register_func(func_name, func)
        except Exception as e:
            logging.warning("[func_register] error with %s", e)
        return func
    return wrapper


class CalVisitorImpl(CalVisitor):
    def __init__(self):
        self.var_manager = VarManager()

    def visitCalculator(self, ctx: CalParser.CalculatorContext):
        self.var_manager = VarManager()
        expression_statement = ctx.expressionStatement()
        if expression_statement is None:
            return None
        return self.visit(expression_statement)

    def visitExpressionStatement(self, ctx: CalParser.ExpressionStatementContext):
        res = None
        for expression in ctx.expression():
            res = self.visit(expression)
        return res

    def visitLiteralExpression(self, ctx: CalParser.LiteralExpressionContext):
        return self.visit(ctx.decimalLiteral())

    def visitDecimalLiteral(self, ctx: CalParser.DecimalLiteralContext):
        if ctx.integerLiteral() is not None:
            return self.visit(ctx.integerLiteral())
        return self.visit(ctx.floatLiteral())

    def visitIntegerLiteral(self, ctx: CalParser.IntegerLiteralContext):
        return int(ctx.getText())

    def visitFloatLiteral(self, ctx: CalParser.FloatLiteralContext):
        return int(ctx.getText())

    def visitSignedExpression(self, ctx: CalParser.SignedExpressionContext):
        val = self.visit(ctx.expression())
        sign = self.visit(ctx.sign())
        return -val if sign == '-' else val

    def visitSign(self, ctx: CalParser.SignContext):
        return ctx.getText()

    def visitParentExpression(self, ctx: CalParser.ParentExpressionContext):
        return self.visit(ctx.expression())

    def visitAssignExpression(self, ctx: CalParser.AssignExpressionContext):
        identifier = self.visit(ctx.identifier())
        value = self.visit(ctx.expression())
        operator = self.visit(ctx.assign())
        if operator:
            old_value = self.var_manager.get_value(identifier)
            self.var_manager.set_value(identifier, FuncService.exec(operator, old_value, value))
        else:
            self.var_manager.set_value(identifier, value)
        return self.var_manager.get_value(identifier)

    def visitIdentifier(self, ctx: CalParser.IdentifierContext):
        return ctx.getText()

    def visitAssign(self, ctx: CalParser.AssignContext):
        return ctx.getText()[:-1]

    def visitFirstPrecedenceMathOperator(self, ctx: CalParser.FirstPrecedenceMathOperatorContext):
        return ctx.getText()

    def visitSecondPrecedenceMathOperator(self, ctx: CalParser.SecondPrecedenceMathOperatorContext):
        return ctx.getText()

    def visitFpMathOperatorExpression(self, ctx: CalParser.FpMathOperatorExpressionContext):
        left_val = self.visit(ctx.expression(0))
        right_val = self.visit(ctx.expression(1))
        operator = self.visit(ctx.firstPrecedenceMathOperator())
        return FuncService.exec(operator, left_val, right_val)

    def visitSpMathOperatorExpression(self, ctx: CalParser.SpMathOperatorExpressionContext):
        left_val = self.visit(ctx.expression(0))
        right_val = self.visit(ctx.expression(1))
        operator = self.visit(ctx.secondPrecedenceMathOperator())
        return FuncService.exec(operator, left_val, right_val)

    def visitIdentifierExpression(self, ctx: CalParser.IdentifierExpressionContext):
        identifier = ctx.getText()
        return self.var_manager.get_value(identifier)

    def visitFunctionCallExpression(self, ctx: CalParser.FunctionCallExpressionContext):
        func_name = self.visit(ctx.funcCall())
        func_args = ctx.functionArgs()
        if func_args is None:
            return FuncService.exec(func_name)
        return FuncService.exec(func_name, self.visit(func_args))

    def visitFunctionArgs(self, ctx: CalParser.FunctionArgsContext):
        arg_list = []
        for expression in ctx.expression():
            arg_list.append(self.visit(expression))
        return tuple(arg_list)

    def visitFuncCall(self, ctx: CalParser.FuncCallContext):
        return ctx.getText()
