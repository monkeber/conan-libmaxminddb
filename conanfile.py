from conans import ConanFile, tools, CMake

class MaxminddbConan(ConanFile):
    name = "maxminddb"
    version = "1.3.2"
    url = "https://github.com/monkeber/conan-libmaxminddb"
    description = "The libmaxminddb library provides a C library for reading MaxMind DB " \
        "files, including the GeoIP2 databases from MaxMind"
    settings = "os", "compiler", "build_type", "arch"
    build_policy = "missing"
    options = { "shared": [True, False] }
    default_options = "shared=False"
    pure_c = False

    def source(self):
        git = tools.Git(folder="maxminddb")
        git.clone("https://github.com/monkeber/libmaxminddb.git")
        git.checkout_submodules(submodule="recursive")

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="maxminddb")
        cmake.build()

    def package(self):
        self.copy("*.h*", dst="include", src="maxminddb/include", keep_path=False)
        if self.options.shared:
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so*", dst="lib", src="maxminddb/src/.libs", keep_path=False)
            self.copy("*.dylib", dst="lib", src="maxminddb/src/.libs", keep_path=False)
        else:
            self.copy("*.lib", dst="lib", keep_path=False)
            self.copy("*.a", dst="lib", src="maxminddb/src/.libs", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["maxminddb"]
        self.cpp_info.includedirs = ["include"]
        self.cpp_info.libdirs = ["lib"]
