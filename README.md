# conan-system-libs
Conan recipes to link to system libraries instead of self-built. They have only been tested with Conan v1.

## Known to work configurations

- Apple platforms (tested macOS/iOS): all recipes
- Android: zlib

## Zlib usage example

First, add recipe to your Conan cache:

    conan create PATH_TO_THIS_REPO/zlib some_user/some_channel

`PATH_TO_THIS_REPO`, `some_user` and `some_channel` are placeholders. 

To consume it, use one of the following possibilities:

- add `self.requires("zlib/1.2.12@some_user/some_channel", override=True)` to `def requirements(self)` method of your `conanfile.py`
- add `zlib/1.2.12@some_user/some_channel` to `[requires]` section of your `conanfile.txt`
- pass `--require-override zlib/1.2.12@some_user/some_channel` on the command line
