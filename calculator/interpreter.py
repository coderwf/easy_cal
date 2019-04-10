# -*- coding:utf-8 -*-
import antlr4
from calculator.visitor import CalVisitorImpl
from parser.CalLexer import CalLexer
from parser.CalParser import CalParser


class Calculator:
    calculator = CalVisitorImpl()

    @staticmethod
    def calculate(text: str):
        stream = antlr4.InputStream(text)
        cs = CalLexer(stream)
        token_stream = antlr4.CommonTokenStream(cs)
        parser_tree = CalParser(token_stream)
        return Calculator.calculator.visit(parser_tree.calculator())


