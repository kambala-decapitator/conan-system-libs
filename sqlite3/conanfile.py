from conan import ConanFile

class Sqlite3Conan(ConanFile):
    name = "sqlite3"
    version = "3.39.2"

    # Qt recipe tries to set options
    options = {
        "shared": [True, False],
        "enable_column_metadata": [True, False],
    }
    default_options = {
        "shared": True,
        "enable_column_metadata": True,
    }

    def package_info(self):
        self.cpp_info.includedirs = []

        libName = "sqlite3"
        self.cpp_info.system_libs = [libName]
        self.cpp_info.sharedlinkflags = [f"-l{libName}"]
        self.cpp_info.exelinkflags = [f"-l{libName}"]
