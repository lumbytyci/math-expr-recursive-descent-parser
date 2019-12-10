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


if __name__ == "__main__":
    while True:
        try:
            expr = input('>>> ')
            parser = ExpressionParser(expr)
            print(parser.primary())
        except KeyboardInterrupt:
            print()
            exit()
