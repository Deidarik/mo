from one_dimensional import gold_sec,bisect,test_f,fibbonachi

if __name__ == "__main__":
    print(bisect(test_f,-2.0, 2.0))
    print(gold_sec(test_f, -2.0, 2.0))
    print(fibbonachi(test_f, -2.0, 2.0))