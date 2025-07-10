cmake_minimum_required(VERSION 3.10)
project(TelegramApiServer)

set(CMAKE_CXX_STANDART 17)

#adding path for packages searching as binary to work with conan
list(APPEND CMAKE_PREFIX_PATH "${CMAKE_BINARY_DIR}")

#apps paths
add_subdirectory(apps/TelegramApiServer)


add_subdirectory(libs)

#tests psaths
add_subdirectory(tests/integrational)
add_subdirectory(tests/smoke)
add_subdirectory(tests/unit)
add_subdirectory(tests/regression)
add_subdirectory(tests/e2e)
