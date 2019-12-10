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
    assert parser.power() == 4


def test_power_squared_negative():
    expr = '-2^2'
    parser = ExpressionParser(expr)
    assert parser.power() == 4


def test_power_power_to_power():
    expr = '3^2^3'
    parser = ExpressionParser(expr)
    assert parser.power() == 6561


def test_power_squared_root():
    expr = '9^0.5'
    parser = ExpressionParser(expr)
    assert parser.power() == 3
