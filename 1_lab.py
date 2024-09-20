from one_dimensional.gold_sec import gold_sec
from one_dimensional.bisec import bisect
from one_dimensional.tests import test_f
from one_dimensional.fib import fibbonachi

if __name__ == "__main__":
    print(bisect(test_f,-2.0, 2.0))
    print(gold_sec(test_f, -2.0, 2.0))
    print(fibbonachi(test_f, -2.0, 2.0))