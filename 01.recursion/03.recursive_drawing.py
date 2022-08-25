#3.	Recursive Drawing
def rec_draw(num):
    if num <= 0:
        return

    print('*' * num)
    rec_draw(num - 1)
    print('#' * num)


rec_draw(int(input()))
