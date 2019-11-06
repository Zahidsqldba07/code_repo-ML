matrix = [[['X','.','.','0'],
             ['.','.','.','.'],
              ['.','.','.','.'],
               ['.','.','.','.']],
          [['.','.','.','0'],
            ['.','X','.','.'],
             ['.','.','.','.'],
              ['.','.','.','.']],
          [['.','.','.','0'],
            ['.','.','.','.'],
             ['.','.','X','.'],
              ['.','.','.','.']],
          [['.','.','.','.'],
            ['.','.','.','.'],
             ['.','.','.','.'],
              ['.','.','.','0']]]
row_length= len(matrix[0][0])
for layer in matrix:
    for row in range(len(layer)):
        print(' ' *(row_length-row),end=' ')
        for column in range(len(layer[row])):
            print('{:>4}'.format(layer[row][column]),end='')
        print()
    print()    
        