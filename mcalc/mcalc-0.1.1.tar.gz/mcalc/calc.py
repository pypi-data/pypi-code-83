class Calculator:
    def __init__(self, num: float) -> None:
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

    def n_root(self, n: int) -> int:
        if self.memory < 0:
            print("Roots of negative numbers not supported")
            return self.memory
        self.memory = self.memory ** (1 / n)
        return self.memory

    def reset(self) -> float:
        self.memory = 0
        return self.memory
