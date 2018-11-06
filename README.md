### Description

Conan package for [libmaxminddb](https://github.com/maxmind/libmaxminddb).
The libmaxminddb library provides a C library for reading MaxMind DB files, including the GeoIP2 databases from MaxMind.

### Package Status

| Bintray | Linux |
|:-----------:|:-------------------:|
| [ ![Download](https://api.bintray.com/packages/monkeber/monkeber/maxminddb%3Amonkeber/images/download.svg) ](https://bintray.com/monkeber/monkeber/maxminddb%3Amonkeber/_latestVersion) | [![Build Status](https://travis-ci.org/monkeber/conan-libmaxminddb.svg?branch=master)](https://travis-ci.org/monkeber/conan-libmaxminddb)

### Basic setup

```bash
$ conan install maxminddb/1.3.2@monkeber/stable
```

### Project setup

```py
from conans import ConanFile, CMake

class AppConan(ConanFile):
    settings = "os", "compiler", "build_type", "arch"

    requires = "maxminddb/1.3.2@monkeber/stable"

    default_options = "maxminddb:shared=False"

    generators = "cmake"
```

Complete the installation of requirements for your project running:

```bash
conan install .
```

Project setup installs the libraries (with all needed dependencies) and generates
the files *conanbuildinfo.txt* and *conanbuildinfo.cmake*
with all the paths and variables that you need to link with your dependencies.

Follow the Conan getting started: http://docs.conan.io.

## Publish The Package

The example below shows the commands used to publish to conan repository.

### Add Remote

```bash
$ conan remote add monkeber https://api.bintray.com/conan/monkeber/monkeber 
```

### Build

Builds a binary package for recipe (conanfile.py) located in current dir. 
For more info please check [conan create](http://docs.conan.io/en/latest/reference/commands/creator/create.html#conan-create).

```bash
$ conan create . monkeber/stable
```

### Upload

Uploads a recipe and binary packages to a remote. 
For more info please check [conan upload](http://docs.conan.io/en/latest/reference/commands/creator/upload.html#conan-upload).

```bash
$ conan upload maxminddb/1.3.2@monkeber/stable --all -r monkeber
```