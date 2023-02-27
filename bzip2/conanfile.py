from conan import ConanFile

class Bzip2Conan(ConanFile):
    name = "bzip2"
    version = "1.0.8"

    def package_info(self):
        self.cpp_info.includedirs = []

        libName = "bz2"
        self.cpp_info.system_libs = [libName]
        self.cpp_info.sharedlinkflags = [f"-l{libName}"]
        self.cpp_info.exelinkflags = [f"-l{libName}"]

        # copied from CCI bzip2 package
        self.cpp_info.set_property("cmake_find_mode", "both")
        self.cpp_info.set_property("cmake_file_name", "BZip2")
        self.cpp_info.set_property("cmake_target_name", "BZip2::BZip2")

        self.cpp_info.names["cmake_find_package"] = "BZip2"
        self.cpp_info.names["cmake_find_package_multi"] = "BZip2"
