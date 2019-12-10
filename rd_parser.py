class ExpressionParser():
    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.cur = 0

    def advance(self) -> None:
        self.cur += 1

    @property
    def eof(self) -> bool:
        return self.cur >= len(self.expr)

    def primary(self) -> float:
        start_idx = self.cur
        while not self.eof and self.expr[self.cur].isnumeric():
            self.advance()
            if not self.eof and self.expr[self.cur] == '.':
                self.advance()

        return float(self.expr[start_idx:self.cur])

    def unary(self) -> float:
        if not self.eof and self.expr[self.cur] in ['+', '-']:
            operator = self.expr[self.cur]
            self.advance()
            u_expr = self.unary()
            u_expr *= (-1 if operator == '-' else +1)
        elif not self.eof:
            u_expr = self.primary()
        else:
            pass  # Crash, must be handled!

        return u_expr

    def power(self) -> float:
        u_expr = self.unary()
        if not self.eof and self.expr[self.cur] == '^':
            self.advance()
            exponent = self.power()
            u_expr = u_expr ** exponent

        return u_expr

    def multiplication(self) -> float:
        p_expr = self.power()
        if not self.eof and self.expr[self.cur] in ['*', '/']:
            operator = self.expr[self.cur]
            self.advance()
            m_expr = self.multiplication()
            if operator == '*':
                p_expr *= m_expr
            else:
                p_expr /= m_expr

        return p_expr


if __name__ == "__main__":
    while True:
        try:
            expr = input('>>> ')
            parser = ExpressionParser(expr)
            print(parser.multiplication())
        except KeyboardInterrupt:
            print()
            exit()
