from conans import ConanFile

class ObserverPtrLiteConan(ConanFile):
    version = "0.2.0"
    name = "observer-ptr-lite"
    description = "An observer_ptr for C++98 and later in a single-file header-only library (Extensions for Library Fundamentals, v2, v3) "
    license = "Boost Software License - Version 1.0. http://www.boost.org/LICENSE_1_0.txt"
    url = "https://github.com/martinmoene/observer-ptr-lite.git"
    exports_sources = "include/nonstd/*", "LICENSE.txt"
    build_policy = "missing"    
    author = "Martin Moene"

    def build(self):
        """Avoid warning on build step"""
        pass

    def package(self):
        """Provide pkg/include/nonstd/*.hpp"""
        self.copy("*.hpp")

    def package_info(self):
        self.info.header_only()
