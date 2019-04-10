# Generated from Cal.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalParser import CalParser
else:
    from CalParser import CalParser

# This class defines a complete generic visitor for a parse tree produced by CalParser.

class CalVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by CalParser#integerLiteral.
    def visitIntegerLiteral(self, ctx:CalParser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#floatLiteral.
    def visitFloatLiteral(self, ctx:CalParser.FloatLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#decimalLiteral.
    def visitDecimalLiteral(self, ctx:CalParser.DecimalLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#calculator.
    def visitCalculator(self, ctx:CalParser.CalculatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#expressionStatement.
    def visitExpressionStatement(self, ctx:CalParser.ExpressionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#signedExpression.
    def visitSignedExpression(self, ctx:CalParser.SignedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#fpMathOperatorExpression.
    def visitFpMathOperatorExpression(self, ctx:CalParser.FpMathOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#assignExpression.
    def visitAssignExpression(self, ctx:CalParser.AssignExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:CalParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:CalParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#literalExpression.
    def visitLiteralExpression(self, ctx:CalParser.LiteralExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#spMathOperatorExpression.
    def visitSpMathOperatorExpression(self, ctx:CalParser.SpMathOperatorExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#parentExpression.
    def visitParentExpression(self, ctx:CalParser.ParentExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#firstPrecedenceMathOperator.
    def visitFirstPrecedenceMathOperator(self, ctx:CalParser.FirstPrecedenceMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#secondPrecedenceMathOperator.
    def visitSecondPrecedenceMathOperator(self, ctx:CalParser.SecondPrecedenceMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#funcCall.
    def visitFuncCall(self, ctx:CalParser.FuncCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#functionArgs.
    def visitFunctionArgs(self, ctx:CalParser.FunctionArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#identifier.
    def visitIdentifier(self, ctx:CalParser.IdentifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#sign.
    def visitSign(self, ctx:CalParser.SignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#firstMathOperator.
    def visitFirstMathOperator(self, ctx:CalParser.FirstMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#secondMathOperator.
    def visitSecondMathOperator(self, ctx:CalParser.SecondMathOperatorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by CalParser#assign.
    def visitAssign(self, ctx:CalParser.AssignContext):
        return self.visitChildren(ctx)



del CalParser