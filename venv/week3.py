graph = [
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 1, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 2, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 3, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 4, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 5, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 6, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 7, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 8, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],     # X Axis 9, in list are the y axis up
   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     # X Axis 10, in list are the y axis up
]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
aircraft_carrier = 5
battleship = 4
submarine = 3
cruiser = 3
destroyer = 2
i = 0

for number_row in range(1, 11):
   print('~~', number_row, '~~', sep='', end='')
print()
print()
for x in graph:
   print(letters[i], end='')
   i += 1
   for y in x:
        if y is True:
            print('~X~~~', end='')
        else:
            print('~O~~~', end='')
   print()
   print()