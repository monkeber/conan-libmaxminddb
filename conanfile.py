from conans import ConanFile, tools, AutoToolsBuildEnvironment
import os


class MaxminddbConan(ConanFile):
    name = "maxminddb"
    version = "1.3.2"
    license = "<Put the package license here>"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "<Description of Maxminddb here>"
    settings = "os", "compiler", "build_type", "arch"

    def source(self):
        tools.download("https://github.com/maxmind/libmaxminddb/releases/download/{0}/" \
            "libmaxminddb-{0}.tar.gz".format(self.version), "libmaxminddb.tar.gz")
        tools.unzip("libmaxminddb.tar.gz")
        os.unlink("libmaxminddb.tar.gz")

    def build(self):
        env_build = AutoToolsBuildEnvironment(self)
        env_build.configure(configure_dir="libmaxminddb-{}".format(self.version))
        self.run("rsync -a libmaxminddb-{}/ .".format(self.version))
        env_build.make()

    def package(self):
        self.copy("*.h", dst="include", src="libmaxminddb")
        self.copy("*maxminddb.lib", dst="lib", keep_path=False)
        self.copy("*.dll", dst="bin", keep_path=False)
        self.copy("*.so", dst="lib", keep_path=False)
        self.copy("*.so.0", dst="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", keep_path=False)
        self.copy("*.a", dst="lib", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["maxminddb"]
