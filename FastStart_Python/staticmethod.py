class MyMath:
    ARG = 2

    @staticmethod
    def super_sum(a, b):
        return (a + b + MyMath.ARG) * MyMath.ARG * (a + b + MyMath.ARG)

test_a = MyMath.super_sum(1, 2)

print(test_a)
