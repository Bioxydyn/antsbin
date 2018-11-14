#! /bin/bash
set -eux

# Clean every time
yes | rm -R temp/

mkdir temp
cd temp
git clone --recursive --depth 1 https://github.com/ANTsX/ANTs.git

mkdir build
cd build

cmake ../ANTs

make -j8

