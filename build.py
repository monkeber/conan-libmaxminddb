from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "gcc --version && g++ --version"
    builder = ConanMultiPackager()
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86_64',
        'build_type': 'Release', 'compiler': 'gcc'})
    builder.run()