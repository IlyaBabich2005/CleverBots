cmake_minimum_required(VERSION 3.10)
project(TelegramApiServer)

set(CMAKE_CXX_STANDART 17)

#adding path for packages searching as binary to work with conan
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_BINARY_DIR}")

add_subdirectory(apps/TelegramApiServer)
add_subdirectory(libs)
add_subdirectory(tests)
