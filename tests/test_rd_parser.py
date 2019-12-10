from rd_parser import ExpressionParser


def test_primary_integer_parsing():
    expr = '123'
    parser = ExpressionParser(expr)
    assert parser.primary() == 123


def test_primary_float_parsing():
    expr = '127902.3180128392820226969'
    parser = ExpressionParser(expr)
    assert parser.primary() == 127902.3180128392820226969
