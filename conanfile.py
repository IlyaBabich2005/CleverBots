from conan import ConanFile

class CleverBotsRecipe(ConanFile):
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"

    def requirements(self):
        self.requires("boost/1.88.0")
        self.requires("gtest/1.16.0")

    def build_requirements(self):
        self.tool_requires("cmake/4.0.3")
