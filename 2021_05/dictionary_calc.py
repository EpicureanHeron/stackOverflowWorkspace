class Calculator:
    def __init__(self,number1,number2):
        self.number1 = number1
        self.number2 = number2
    def divide(self,number1,number2):
        quotient=0
        dividend=0
        divisor=0
        remainder=0
        quotient=int(number1/number2)
        dividend=number1
        divisor=number2
        remainder=number1%number2
        return {
            'Dividend': dividend,
            'Divisor': divisor,
            'Quotient': quotient,
            'Remainder': remainder
        }