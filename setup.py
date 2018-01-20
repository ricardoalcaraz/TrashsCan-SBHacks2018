from distutils.core import setup, Extension
extension_mod = Extension("_display_python", ["_display_module.cc", "Display/Display.cpp"])
setup(name = "swigdemo", ext_modules=[extension_mod])
