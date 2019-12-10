from rd_parser import ExpressionParser


def test_primary_integer_parsing():
    expr = '123'
    parser = ExpressionParser(expr)
    assert parser.primary() == 123


def test_primary_float_parsing():
    expr = '127902.3180128392820226969'
    parser = ExpressionParser(expr)
    assert parser.primary() == 127902.3180128392820226969


def test_unary_negation():
    expr = '-19.60'
    parser = ExpressionParser(expr)
    assert parser.unary() == -19.60


def test_unary_double_negation():
    expr = '--19.60'
    parser = ExpressionParser(expr)
    assert parser.unary() == 19.60


def test_unary_triple_negation():
    expr = '---20'
    parser = ExpressionParser(expr)
    assert parser.unary() == -20


def test_unary_with_plus_sign():
    expr = '+09.23'
    parser = ExpressionParser(expr)
    assert parser.unary() == 9.23


def test_unary_with_multiple_plus_signs():
    expr = '+++++++++++17.31230'
    parser = ExpressionParser(expr)
    assert parser.unary() == 17.3123


def test_unary_with_combined_signs():
    expr = '-+-+-+-+-78.92'
    parser = ExpressionParser(expr)
    assert parser.unary() == -78.92


def test_power_squared():
    expr = '2^2'
    parser = ExpressionParser(expr)
    assert parser.power() == 2**2


def test_power_squared_negative():
    expr = '-2^2'
    parser = ExpressionParser(expr)
    assert parser.power() == (-2)**2


def test_power_power_to_power():
    expr = '3^2^3'
    parser = ExpressionParser(expr)
    assert parser.power() == 3**2**3


def test_power_squared_root():
    expr = '9^0.5'
    parser = ExpressionParser(expr)
    assert parser.power() == 9**0.5


def test_mult():
    expr = '23*-12.29'
    parser = ExpressionParser(expr)
    assert parser.multiplication() == 23 * (-12.29)


def test_mult_div():
    expr = '782/3.312'
    parser = ExpressionParser(expr)
    assert parser.multiplication() == 782 / 3.312


def test_mult_combined_with_div():
    expr = '25*5/5*2.5'
    parser = ExpressionParser(expr)
    assert parser.multiplication() == (25 * 5) / (5 * 2.5)


def test_addition_add_two_numbers():
    expr = '1923.1023+12312.13'
    parser = ExpressionParser(expr)
    assert parser.addition() == 1923.1023 + 12312.13


def test_addition_subtract_two_numbers():
    expr = '45785.0992-598.598'
    parser = ExpressionParser(expr)
    assert parser.addition() == 45785.0992 - 598.598


def test_expression_grouping_around_primary():
    expr = '((((2))))'
    parser = ExpressionParser(expr)
    assert parser.expression() == 2


def test_expression_grouping_with_multiple_op():
    expr = '(2*(2+2)/4)*2'
    parser = ExpressionParser(expr)
    assert parser.expression() == (2 * (2 + 2) / 4) * 2

# TODO Add tests for mixed expressions
