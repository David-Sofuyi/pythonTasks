# code prints 10 rows
# each rows has 10 characters
# odd rowc <
# even rows >




for row in range(10):
    for column in range(10):
        print('<' if row % 2 == 1 else '>', end='')
    print()
