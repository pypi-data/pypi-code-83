import pytest
import finesse


@pytest.fixture
def solution():
    base = finesse.Model()
    base.parse(
        """
        l L0 P=1

        s s0 L0.p1 m1.p1

        m m1 R=0 T=1

        ad a00 m1.p2.o 0 n=0 m=0
        ad a10 m1.p2.o 0 n=1 m=0
        ad a01 m1.p2.o 0 n=0 m=1
        pd P m1.p2.o

        gauss g1 L0.p1.o w0=1m z=0

        modes(maxtem=1)
        """
    )

    base.L0.tem(0, 0, 1, 0)
    base.L0.tem(1, 0, 2, 0)
    base.L0.tem(0, 1, 4, 0)

    return base.run()


def test_power_conserved(solution):
    sol = solution
    assert abs(sol["P"] - 1) <= 1e-15


def test_hom_relative_power(solution):
    sol = solution
    assert abs(2 * abs(sol["a00"]) ** 2 - abs(sol["a10"]) ** 2) <= 1e-15
    assert abs(4 * abs(sol["a00"]) ** 2 - abs(sol["a01"]) ** 2) <= 1e-15
