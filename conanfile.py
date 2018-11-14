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

    def source(self):
        tools.download("https://github.com/maxmind/libmaxminddb/releases/download/{0}/" \
            "libmaxminddb-{0}.tar.gz".format(self.version), "libmaxminddb.tar.gz")
        tools.unzip("libmaxminddb.tar.gz")
        os.unlink("libmaxminddb.tar.gz")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        args = list()
        if self.settings.build_type == "Debug":
            args.append("--enable-debug")
        env_build.configure(configure_dir="libmaxminddb-{}".format(self.version),
            args=args)
        self.run("cp -r libmaxminddb-{}/* .".format(self.version))
        env_build.make()

    def package(self):
        self.copy("*.h*", dst="include", keep_path=False)
        self.copy("*maxminddb.lib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)
        if self.options.shared:
            self.copy("*.dll", dst="bin", keep_path=False)
            self.copy("*.so", dst="lib", keep_path=False)
            self.copy("*.so.0", dst="lib", keep_path=False)
            self.copy("*.dylib", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["maxminddb"]
