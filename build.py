from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager()
    builder.add_common_builds()
    builder.add(settings={"compiler.libcxx": "libstdc++11",'compiler.version': '4.9',
        'arch': 'x86', 'build_type': 'Release', 'compiler': 'gcc'})
    builder.run()