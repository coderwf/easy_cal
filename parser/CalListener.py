# Generated from Cal.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .CalParser import CalParser
else:
    from CalParser import CalParser

# This class defines a complete listener for a parse tree produced by CalParser.
class CalListener(ParseTreeListener):

    # Enter a parse tree produced by CalParser#integerLiteral.
    def enterIntegerLiteral(self, ctx:CalParser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by CalParser#integerLiteral.
    def exitIntegerLiteral(self, ctx:CalParser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by CalParser#floatLiteral.
    def enterFloatLiteral(self, ctx:CalParser.FloatLiteralContext):
        pass

    # Exit a parse tree produced by CalParser#floatLiteral.
    def exitFloatLiteral(self, ctx:CalParser.FloatLiteralContext):
        pass


    # Enter a parse tree produced by CalParser#decimalLiteral.
    def enterDecimalLiteral(self, ctx:CalParser.DecimalLiteralContext):
        pass

    # Exit a parse tree produced by CalParser#decimalLiteral.
    def exitDecimalLiteral(self, ctx:CalParser.DecimalLiteralContext):
        pass


    # Enter a parse tree produced by CalParser#calculator.
    def enterCalculator(self, ctx:CalParser.CalculatorContext):
        pass

    # Exit a parse tree produced by CalParser#calculator.
    def exitCalculator(self, ctx:CalParser.CalculatorContext):
        pass


    # Enter a parse tree produced by CalParser#expressionStatement.
    def enterExpressionStatement(self, ctx:CalParser.ExpressionStatementContext):
        pass

    # Exit a parse tree produced by CalParser#expressionStatement.
    def exitExpressionStatement(self, ctx:CalParser.ExpressionStatementContext):
        pass


    # Enter a parse tree produced by CalParser#signedExpression.
    def enterSignedExpression(self, ctx:CalParser.SignedExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#signedExpression.
    def exitSignedExpression(self, ctx:CalParser.SignedExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#fpMathOperatorExpression.
    def enterFpMathOperatorExpression(self, ctx:CalParser.FpMathOperatorExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#fpMathOperatorExpression.
    def exitFpMathOperatorExpression(self, ctx:CalParser.FpMathOperatorExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#assignExpression.
    def enterAssignExpression(self, ctx:CalParser.AssignExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#assignExpression.
    def exitAssignExpression(self, ctx:CalParser.AssignExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:CalParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:CalParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:CalParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:CalParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#literalExpression.
    def enterLiteralExpression(self, ctx:CalParser.LiteralExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#literalExpression.
    def exitLiteralExpression(self, ctx:CalParser.LiteralExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#spMathOperatorExpression.
    def enterSpMathOperatorExpression(self, ctx:CalParser.SpMathOperatorExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#spMathOperatorExpression.
    def exitSpMathOperatorExpression(self, ctx:CalParser.SpMathOperatorExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#parentExpression.
    def enterParentExpression(self, ctx:CalParser.ParentExpressionContext):
        pass

    # Exit a parse tree produced by CalParser#parentExpression.
    def exitParentExpression(self, ctx:CalParser.ParentExpressionContext):
        pass


    # Enter a parse tree produced by CalParser#firstPrecedenceMathOperator.
    def enterFirstPrecedenceMathOperator(self, ctx:CalParser.FirstPrecedenceMathOperatorContext):
        pass

    # Exit a parse tree produced by CalParser#firstPrecedenceMathOperator.
    def exitFirstPrecedenceMathOperator(self, ctx:CalParser.FirstPrecedenceMathOperatorContext):
        pass


    # Enter a parse tree produced by CalParser#secondPrecedenceMathOperator.
    def enterSecondPrecedenceMathOperator(self, ctx:CalParser.SecondPrecedenceMathOperatorContext):
        pass

    # Exit a parse tree produced by CalParser#secondPrecedenceMathOperator.
    def exitSecondPrecedenceMathOperator(self, ctx:CalParser.SecondPrecedenceMathOperatorContext):
        pass


    # Enter a parse tree produced by CalParser#funcCall.
    def enterFuncCall(self, ctx:CalParser.FuncCallContext):
        pass

    # Exit a parse tree produced by CalParser#funcCall.
    def exitFuncCall(self, ctx:CalParser.FuncCallContext):
        pass


    # Enter a parse tree produced by CalParser#functionArgs.
    def enterFunctionArgs(self, ctx:CalParser.FunctionArgsContext):
        pass

    # Exit a parse tree produced by CalParser#functionArgs.
    def exitFunctionArgs(self, ctx:CalParser.FunctionArgsContext):
        pass


    # Enter a parse tree produced by CalParser#identifier.
    def enterIdentifier(self, ctx:CalParser.IdentifierContext):
        pass

    # Exit a parse tree produced by CalParser#identifier.
    def exitIdentifier(self, ctx:CalParser.IdentifierContext):
        pass


    # Enter a parse tree produced by CalParser#sign.
    def enterSign(self, ctx:CalParser.SignContext):
        pass

    # Exit a parse tree produced by CalParser#sign.
    def exitSign(self, ctx:CalParser.SignContext):
        pass


    # Enter a parse tree produced by CalParser#firstMathOperator.
    def enterFirstMathOperator(self, ctx:CalParser.FirstMathOperatorContext):
        pass

    # Exit a parse tree produced by CalParser#firstMathOperator.
    def exitFirstMathOperator(self, ctx:CalParser.FirstMathOperatorContext):
        pass


    # Enter a parse tree produced by CalParser#secondMathOperator.
    def enterSecondMathOperator(self, ctx:CalParser.SecondMathOperatorContext):
        pass

    # Exit a parse tree produced by CalParser#secondMathOperator.
    def exitSecondMathOperator(self, ctx:CalParser.SecondMathOperatorContext):
        pass


    # Enter a parse tree produced by CalParser#assign.
    def enterAssign(self, ctx:CalParser.AssignContext):
        pass

    # Exit a parse tree produced by CalParser#assign.
    def exitAssign(self, ctx:CalParser.AssignContext):
        pass


