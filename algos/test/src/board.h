#include <vector>
#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>

namespace nqueens {

    using board = std::vector<std::vector<int>>;

    static inline void shift(int& board_pos, bool& left) {
        board_pos += left ? 1 : -1;
    }
    
    static inline void removeQueen(board& _board, int x, int y, std::vector<int>& solution) {
        int size = _board.size();
        bool right = false;
        shift(_board[y][x], right);
        solution.pop_back();
        for (int i = 1; i < size - y; i++) {
            std::vector<int>& board_y_plus_i = _board[y + i];
            if (y + i >= size) {
                continue;
            }
    
            shift(board_y_plus_i[x], right);
    
            if (x + i < size) {
                shift(board_y_plus_i[x + i], right);
            }
    
            if (x - i >= 0) {
                shift(board_y_plus_i[x - i], right);
            }
        }
    }
    
    static inline void placeQueen(board& _board, int x, int y, std::vector<int>& solution) {
        int size = _board.size();
        bool left = true;
        shift(_board[y][x], left);
        solution.emplace_back(x);
        for (int i = 1; i < size - y; i++) {
            std::vector<int>& board_y_plus_i = _board[y + i];
            if (y + i >= size) {
                continue;
            }
    
            shift(board_y_plus_i[x], left);
    
            if (x + i < size) {
                shift(board_y_plus_i[x + i], left);
            }
    
            if (x - i >= 0) {
                shift(board_y_plus_i[x - i], left);
            }
        }
    }
    
    static inline void recursionThing(board& _board, int y, std::vector<int>& solution, int& count, std::vector<std::vector<int>>& solutions) {
        int SIZE = _board.size();
    
        for (int i = 0; i < SIZE; i++) {
            if (_board[y][i] != 0) {
                continue;
            }
            if (y == SIZE - 1) {
                count++;
                placeQueen(_board, i, y, solution);
                solutions.emplace_back(solution);
                removeQueen(_board, i, y, solution);
                return;
            }
            placeQueen(_board, i, y, solution);
            recursionThing(_board, y + 1, solution, count, solutions);
            removeQueen(_board, i, y, solution);
        }
    }
    
}
