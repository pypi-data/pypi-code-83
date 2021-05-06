from dir2 import file2
from dir3.file3 import double, VALUE_2

def test(arr):
    print("Printing sum form file2:")
    print(file2.print_sum(arr))
    print("Printing constant from file2 (should be 10)")
    print(file2.VALUE)
    print("Printing double function from file3")
    print(double(arr))
    print("Priting VALUE_2 from file3 (should be 5)")
    print(VALUE_2)



