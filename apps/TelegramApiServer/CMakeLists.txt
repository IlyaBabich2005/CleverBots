#find boost 
find_package(Boost 1.88 REQUIRED COMPONENTS system CONFIG)  

# Building Server which talk with Telegram Api 
add_executable(TelegramApiServer  
	src/main.cpp 
)  

set_target_properties(TelegramApiServer 
	PROPERTIES 
		RUNTIME_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR}/TelegramApiServer
)  

target_include_directories(TelegramApiServer 
	PRIVATE
		${Boost_INCLUDE_DIRS}
)  

target_link_libraries(TelegramApiServer
	PRIVATE
		Boost::system
)
