class Calculator:
    """
    Calculator class for simple arithmetic operations.
    """

    def __init__(self, num: float = 0) -> None:
        self.memory = float(num)

    def add(self, num: float) -> float:
        self.memory += num
        return self.memory

    def subtract(self, num: float) -> float:
        self.memory -= num
        return self.memory

    def multiply(self, num: float) -> float:
        self.memory *= num
        return self.memory

    def divide(self, num: float) -> float:
        self.memory /= num
        return self.memory

    def n_root(self, n: int) -> float:
        if self.memory < 0:
            raise NotImplementedError(
                "Can't take root of negative numbers, complex numbers not supported"
            )
        self.memory = self.memory ** (1 / n)
        return self.memory

    def reset(self, num: float = 0.0) -> float:
        self.memory = float(num)
        return self.memory
