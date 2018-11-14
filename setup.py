import setuptools
import os
from shutil import copy


from setuptools import Extension
from setuptools.command.build_ext import build_ext


def get_environment_variable(variable: str, default: str):
    """ Return value of environment variable or the default if not found. """

    value = os.getenv(variable)
    if value is None:
        value = default

    return value


class ANTsExtension(Extension):
    """ Defines a Cmake extension. """

    def __init__(self, name, bin_dir=''):
        Extension.__init__(self, name, sources=[])
        self.bin_dir = os.path.abspath(bin_dir)
        print(self.bin_dir)


class BinCopier(build_ext):
    """ Defines a cmake build. """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def run(self):
        """ Runs the build. """
        for ext in self.extensions:
            self.build_extension(ext)

    def build_extension(self, ext: build_ext):
        """ Builds the requested extension. """
        print('COPYING')
        copy(ext.bin_dir + '/antsRegistration', 'antsbin/')
        copy(ext.bin_dir + '/antsApplyTransforms', 'antsbin/')


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="antsbin",
    version="0.0.2",
    zip_safe=True,
    author="Bioxydyn Ltd",
    author_email="matthew.heaton@bioxydyn.com",
    description="Binaries for ANTs packaged using pip",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/bioxydyn/antsbin",
    ext_modules=[ANTsExtension('ants', 'temp/build/bin')],
    cmdclass=dict(build_ext=BinCopier),
    package_dir={'antsbin': 'antsbin'},
    packages=setuptools.find_packages(),
    platforms='linux',
    include_package_data=True,  # extensions.so (MANIFEST.in)
)
