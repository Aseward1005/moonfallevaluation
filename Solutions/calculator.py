#use a regular expression to solve
import re
validadd = re.compile(r"\s*\d+\s*[+]\s*\d+\s*") # integer of any length -> whitespace -> plus sign -> whitespace -> integer of any length
#this ensures that the input is exactly two numbers and a plus sign in the correct order
#It doesn't handle numbers split by whitespace or commas, as I am unsure if those are considered as valid strings
#those res would be
#whitespace: same, but \d+\s* now becomes \d(\d|\s)* (ensure at least one digit, then allow digits to be gapped)

#commas are a bit more challenging if we want to ensure the commas are correctly placed, (if not it's the same as whitespace)
#they are added from right to left, but our machine reads from left to right
#one way to do this is to count commas as digits ([0-9]|,), then check whether the commas are correctly placed by reversing the string and processing it that way if the string is valid
#the same can be done for whitespace if we want a specific type of spacing

#floats are more challenging than integers
#3 possibilities(4 if countinging integers): digit.digit, .digit, digit.

#the actual calculator will treat commas and whitespace separating the digits as invalid
class Calculator:
    def eval(self, expression):
        #''' Insert your code to process the string input here '''
        result = "invalid entry"

        if (validadd.fullmatch(expression)):           #if we have a valid expression
            numbers = re.split(r"[+]", expression)     #split the expression by the plus sign
            result = int(numbers[0]) + int(numbers[1]) #and add the two portions

        return result

    def run(self):
        # Run until the user cancels, ctl + C
        while True:
            expression = input('Enter an infix addition statement: ')
            result = self.eval(expression)
            print(' = ', result)

if __name__ == "__main__":
    # If this file is run directly from the command line, run the calculator
    c = Calculator()
    c.run()