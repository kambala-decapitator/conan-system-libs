from conan import ConanFile

class ZlibConan(ConanFile):
    name = "zlib"
    version = "1.2.12"
    options = {
        "shared": [True, False],
    }
    default_options = {
        "shared": True,
    }

    def package_info(self):
        self.cpp_info.includedirs = []

        libName = "z"
        self.cpp_info.system_libs = [libName]
        self.cpp_info.sharedlinkflags = [f"-l{libName}"]
        self.cpp_info.exelinkflags = [f"-l{libName}"]

        # copied from CCI zlib package
        # uppercase name is required e.g. for libpng
        self.cpp_info.set_property("cmake_file_name", "ZLIB")
        self.cpp_info.set_property("cmake_target_name", "ZLIB::ZLIB")
        self.cpp_info.set_property("pkg_config_name", "zlib")

        self.cpp_info.names["cmake_find_package"] = "ZLIB"
        self.cpp_info.names["cmake_find_package_multi"] = "ZLIB"
