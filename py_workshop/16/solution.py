def part_checker(board, i, j):
    test_list=[]
    for j in range(len(board[0])):
        if board[i][j] not in test_list:
            test_list.append(board[i][j])
        else:
            print(f"Row error; Same digit: '{board[i][j]}' (in board[{i}][{j}])")
            return 'Try again!'


def main(board):
    for i in range(len(board)):
        row_test_list=[]
        line_test_list=[]
        square_test_list=[]

        for j in range(len(board[0])):

            digit = board[i][j]
            if digit not in row_test_list:
                row_test_list.append(digit)
            else:
                # print(f"Row error; Same digit: '{digit}' (in board[{i}][{j}])")
                return 'Try again!'

            digit = board[j][i]
            if digit not in line_test_list:
                line_test_list.append(digit)
            else:
                # print(f"Line error; Same digit: '{digit}' (in board[{j}][{i}])")
                return 'Try again!'


            cal_i = j//3 + 3*(i // 3) # y
            cal_j = j%3 + 3*(i % 3) # x
            digit = board[cal_i][cal_j]
            if digit not in square_test_list:
                square_test_list.append(digit)
            else:
                print(f"Square error; Same digit: '{digit}' (in board[{cal_i}][{cal_j}])")
                return 'Try again!'

            print(f"[{cal_i}][{cal_j}]",end=', ')
            # print(board[cal_i][cal_j],end=', ')  # list of each 'square'
        print("")
    return 'Finished!'

# row error -->
# print(main([
#     [1, 1, 2, 5, 7, 9, 4, 6, 8],
#     [4, 9, 8, 2, 6, 1, 3, 7, 5],
#     [7, 5, 6, 3, 8, 4, 2, 1, 9],
#     [6, 4, 3, 1, 5, 8, 7, 9, 2],
#     [5, 2, 1, 7, 9, 3, 8, 4, 6],
#     [9, 8, 7, 4, 2, 6, 5, 3, 1],
#     [2, 1, 4, 9, 3, 5, 6, 8, 7],
#     [3, 6, 5, 8, 1, 7, 9, 2, 4],
#     [8, 7, 9, 6, 4, 2, 1, 5, 3]
#     ]))

# # line error:  ||
# print(main([ # \/
#     [1, 3, 2, 5, 7, 9, 4, 6, 8],
#     [1, 9, 8, 2, 6, 1, 3, 7, 5],
#     [7, 5, 6, 3, 8, 4, 2, 1, 9],
#     [6, 4, 3, 1, 5, 8, 7, 9, 2],
#     [5, 2, 1, 7, 9, 3, 8, 4, 6],
#     [9, 8, 7, 4, 2, 6, 5, 3, 1],
#     [2, 1, 4, 9, 3, 5, 6, 8, 7],
#     [3, 6, 5, 8, 1, 7, 9, 2, 4],
#     [8, 7, 9, 6, 4, 2, 1, 5, 3]
#     ]))

# square error: []
print(main([
    [1, 3, 2, 5, 7, 9, 4, 6, 8],
    [4, 1, 8, 2, 6, 9, 3, 7, 5],
    [7, 5, 6, 3, 8, 4, 2, 1, 9],
    [6, 4, 3, 1, 5, 8, 7, 9, 2],
    [5, 2, 1, 7, 9, 3, 8, 4, 6],
    [9, 8, 7, 4, 2, 6, 5, 3, 1],
    [2, 9, 4, 9, 3, 5, 6, 8, 7],
    [3, 6, 5, 8, 1, 7, 9, 2, 4],
    [8, 7, 9, 6, 4, 2, 1, 5, 3]
    ]))
# (((i*3) + (j-(3*(j//3)))) % 3) + ((i//3)*3)

# correct
# print(main([
#     [1, 3, 2, 5, 7, 9, 4, 6, 8],
#     [4, 9, 8, 2, 6, 1, 3, 7, 5],
#     [7, 5, 6, 3, 8, 4, 2, 1, 9],
#     [6, 4, 3, 1, 5, 8, 7, 9, 2],
#     [5, 2, 1, 7, 9, 3, 8, 4, 6],
#     [9, 8, 7, 4, 2, 6, 5, 3, 1],
#     [2, 1, 4, 9, 3, 5, 6, 8, 7],
#     [3, 6, 5, 8, 1, 7, 9, 2, 4],
#     [8, 7, 9, 6, 4, 2, 1, 5, 3]
#     ]))

1, 3, 2, 4, 9, 8, 7, 5, 6, 
5, 7, 9, 2, 6, 1, 3, 8, 4, 
4, 6, 8, 3, 7, 5, 2, 1, 9, 
6, 4, 3, 5, 2, 1, 9, 8, 7, 
1, 5, 8, 7, 9, 3, 4, 2, 6, 
7, 9, 2, 8, 4, 6, 5, 3, 1, 
2, 1, 4, 3, 6, 5, 8, 7, 9, 
9, 3, 5, 8, 1, 7, 6, 4, 2, 
6, 8, 7, 9, 2, 4, 1, 5, 3,