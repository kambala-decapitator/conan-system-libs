# conan-system-libs
[Conan](https://conan.io/) recipes to link to system libraries instead of self-built.

These recipes are compatible with Conan v2. For v1 see [previous revision](https://github.com/kambala-decapitator/conan-system-libs/tree/4dadde6f565a3cf099165e622402b535d571f2b8).

## Known to work configurations

- Apple platforms (tested macOS/iOS): all recipes
- Android: zlib

## Zlib usage example

First, add recipe to your Conan cache:

    conan create PATH_TO_THIS_REPO/zlib --user some_user --channel some_channel

`PATH_TO_THIS_REPO`, `some_user` and `some_channel` are placeholders. User and channel are optional, one recommendation would be using `--user system`.

To consume it, use one of the following possibilities:

- **the most recommended way**: add to your profile
```
[replace_requires]
zlib/*: zlib/[*]@some_user/some_channel
```

- add `self.requires("zlib/1.2.12@some_user/some_channel", override=True)` to the `def requirements(self)` method of your `conanfile.py`
- add `zlib/1.2.12@some_user/some_channel` to the `[requires]` section of your `conanfile.txt`
