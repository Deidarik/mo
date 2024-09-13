from typing import Callable
from gold_sec import gold_sec
from bisec import bisect
from tests import test_f
from fib import fibbonachi

if __name__== "__main__":
    print(bisect(test_f,-2.0, 2.0))
    print(gold_sec(test_f,-2.0,2.0))
    print(fibbonachi(test_f,-2.0,2.0))
