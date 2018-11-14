#! /bin/bash
set -eux


# Clean every time
yes | rm -R temp/


# Make a working folder
mkdir temp
cd temp


# Get the source
git clone --recursive https://github.com/ANTsX/ANTs.git
cd ANTs
git checkout f23cba1
cd ../


# Run CMake
mkdir build
cd build
cmake ../ANTs


# Ants has a superbuild, so this should pull down dependencies
make -j8
