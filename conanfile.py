from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


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

    def imports(self):
        self.copy("*.h*", dst="include")

    def source(self):
        tools.download("https://github.com/maxmind/libmaxminddb/releases/download/{0}/" \
            "libmaxminddb-{0}.tar.gz".format(self.version), "libmaxminddb.tar.gz")
        tools.unzip("libmaxminddb.tar.gz")
        os.unlink("libmaxminddb.tar.gz")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)

        config_args = list()
        config_args.append("--disable-tests")
        config_args.append("--disable-shared")

        if self.settings.build_type == "Debug":
            config_args.append("--enable-debug")

        env_build.configure(configure_dir="libmaxminddb-{}".format(self.version),
            args=config_args)
        self.run("cp -r libmaxminddb-{}/* .".format(self.version))
        env_build.make(args=[
            "CPPFLAGS:=$(CPPFLAGS) -std=gnu99",
            "CFLAGS:=$(CFLAGS) -std=c99"])
        env_build.install()

    def package(self):
        self.copy("*.h", src="libmaxminddb-{}/include".format(self.version), dst="include")
        self.copy("*.h", src="libmaxminddb-{}/include".format(self.version), dst="include", keep_path=False)
        self.copy("*maxminddb.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        self.copy("*.la", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so*", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
        self.cpp_info.libdirs = ["lib"]
        self.cpp_info.includedirs = ["include"]
        self.env_info.CMAKE_PREFIX_PATH.append(self.package_folder)
        self.env_info.CONAN_INCLUDE_DIRS.append(os.path.join(self.package_folder, "include"))
