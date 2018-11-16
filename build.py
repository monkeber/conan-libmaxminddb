from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    command = "gcc --version && g++ --version"
    builder = ConanMultiPackager(docker_entry_script=command)
    builder.add(settings={'compiler.libcxx': 'libstdc++11', 'arch': 'x86_64',
        'build_type': 'Release', 'compiler': 'gcc'})
    builder.run()