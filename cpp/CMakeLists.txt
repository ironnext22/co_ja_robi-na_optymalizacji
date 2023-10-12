cmake_minimum_required(VERSION 3.26)
project(cpp)

set(CMAKE_CXX_STANDARD 17)

add_executable(cpp main.cpp src/matrix.cpp src/matrix.h src/ode_solver.cpp src/ode_solver.h src/opt_alg.h src/opt_alg.cpp src/solution.h src/solution.cpp src/user_funs.cpp src/user_funs.h)
