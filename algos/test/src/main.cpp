#include <vector>
#include <chrono>
#include <iostream>
#include <fstream>
#include <string>
#include <random>
#include "board.h"

int count = 0;
std::vector<std::vector<int>> solutions;

void write_file(int n) {
	std::cout << "writing to file" << std::endl;
	std::ofstream fs("solutions" + std::to_string(n) + ".bin", std::ios::binary);
	for (const auto& solution : solutions) {
		int size = solution.size();
		fs.write(reinterpret_cast<const char*>(&size), sizeof(int));
		fs.write(reinterpret_cast<const char*>(solution.data()), size * sizeof(int));
	}
	fs.close();
}

void print_solution(nqueens::board& solution) {
	//int size = solution.size();
	srand(time(0));
	if (solution.size() <= 1) return;
	std::random_device rd;
	std::mt19937 gen(rd());
	std::uniform_int_distribution<> distr(0, solution.size() - 1);

	std::cout << "Random solution from n = " << solution[0].size() << std::endl;
	const auto& final_solution = solution[distr(gen)];
	for (int i = 0; i < final_solution.size(); i++) {
		for (int j = 0; j < final_solution.size(); j++) {
			std::string letter = " O ";
			if (final_solution[i] == j) {
				letter = " \x1B[31mQ\033[0m ";
			}
			std::cout << letter;
		}
		std::cout << std::endl;
	}
}

int main() {
	for (int n = 0; n <= 16; n++) {
		std::vector<int> solution;
		count = 0;
		auto start = std::chrono::high_resolution_clock::now();
		const int SIZE = n;
		nqueens::board _board = std::vector<std::vector<int>>();
		for (int i = 0; i < SIZE; i++) {
			std::vector<int> temp;
			for (int j = 0; j < SIZE; j++) {
				temp.push_back(0);
			}
			_board.push_back(temp);
		}

		nqueens::recursionThing(_board, 0, solution, count, solutions);
		print_solution(solutions);
		auto end = std::chrono::high_resolution_clock::now();
		write_file(n);
		std::cout << "final count for n = " << SIZE << ": " << count << " total solutions" << std::endl;
		std::chrono::duration<double> duration = end - start;
		auto count = duration.count();
		int minutes = count / 60;
		auto seconds = count - minutes * 60;
		std::cout << "Execution time: " << minutes << " minutes, " << seconds << " seconds" << "\n" << std::endl;
		solution.clear();
		solutions.clear();
	}
	return 0;
}