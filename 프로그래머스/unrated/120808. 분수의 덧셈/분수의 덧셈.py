from fractions import Fraction
def solution(numer1, denom1, numer2, denom2):
    fraction1 = Fraction(numer1, denom1)
    fraction2 = Fraction(numer2, denom2)
    answer = fraction1 + fraction2
    return [answer.numerator, answer.denominator]