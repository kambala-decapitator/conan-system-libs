from conan import ConanFile

class IconvConan(ConanFile):
    name = "libiconv"
    version = "1.17"

    def package_info(self):
        self.cpp_info.includedirs = []

        libName = "iconv"
        self.cpp_info.system_libs = [libName]
        self.cpp_info.sharedlinkflags = [f"-l{libName}"]
        self.cpp_info.exelinkflags = [f"-l{libName}"]
