#! /bin/bash
set -eux


# Clean every time
yes | rm -rf temp/


# Make a working folder
mkdir temp && cd temp

# Get the source
git clone --recursive https://github.com/mj-heaton/ANTs.git
cd ANTs
git checkout 444b85c42fab18f9bf202d69deb7ab46bff40b33
cd ../


# Run CMake
mkdir build && cd build


cmake \
    -DCMAKE_EXE_LINKER_FLAGS="-static" \
    -DBUILD_SHARED_LIBS=OFF \
    -DUSE_VTK=OFF \
    -DSuperBuild_ANTS_USE_GIT_PROTOCOL=OFF \
    -DBUILD_TESTING=OFF \
    -DRUN_LONG_TESTS=OFF \
    -DRUN_SHORT_TESTS=OFF \
    ../ANTs

# Ants has a superbuild, so this should pull down dependencies
make -j8
