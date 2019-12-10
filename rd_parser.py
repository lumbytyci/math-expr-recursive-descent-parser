class ExpressionParser():
    def __init__(self, expr: str) -> None:
        self.expr = expr
        self.cur = 0

    def advance(self) -> None:
        self.cur += 1

    @property
    def eof(self) -> bool:
        return self.cur >= len(self.expr)


if __name__ == "__main__":
    pass
