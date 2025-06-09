#include <gtest/gtest.h>
#include "../src/board.h"

TEST(nqueens, testShiftLeft) {
    int position = 5;
    bool shift = true;

    nqueens::shift(position, shift);

    EXPECT_EQ(6, position);
}

TEST(nqueens, testShiftRight) {
    int position = 8;
    bool shift = false;

    nqueens::shift(position, shift);

    EXPECT_EQ(7, position);
}

TEST(nqueens, testPlaceQueen) {
    const int SIZE = 8;
    nqueens::board board(SIZE, std::vector<int>(SIZE, 0));
    std::vector<int> solution;

    nqueens::placeQueen(board, 3, 4, solution);

    std::vector<std::vector<bool>> check(SIZE, std::vector<bool>(SIZE, false));

    for (int i = 4; i <= 7; i++) {
        check[3][i] = true;
    }

    check[2][5] = true;
    check[1][6] = true;
    check[0][7] = true;

    check[4][5] = true;
    check[5][6] = true;
    check[6][7] = true;

    for (int x = 0; x < SIZE; x++) {
        for (int y = 0; y < SIZE; y++) {
            ASSERT_TRUE(board[x][y] == check[y][x]);
        }
    }
}

TEST(nqueens, testRemoveQueen) {
    const int SIZE = 10;
    nqueens::board board(SIZE, std::vector<int>(SIZE, 0));
    std::vector<int> solution;

    nqueens::placeQueen(board, 4, 5, solution);
    nqueens::removeQueen(board, 4, 5, solution);

    for (int x = 0; x < SIZE; x++) {
        for (int y = 0; y < SIZE; y++) {
            ASSERT_FALSE(board[x][y]);
        }
    }
}

TEST(nqueens, testRecursion) {
    const int answers[] = { 1, 0, 0, 2, 10, 4, 40, 92, 352, 724, 2680, 14200, 73712 };

    for (int i = 0; i < std::size(answers); i++) {
        nqueens::board board(i + 1, std::vector<int>(i + 1, 0));
        std::vector<int> solution;
        std::vector<std::vector<int>> solutions;
        int count = 0;

        nqueens::recursionThing(board, 0, solution, count, solutions);

        ASSERT_EQ(count, answers[i]);
    }
}