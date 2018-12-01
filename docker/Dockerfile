FROM alpine:3.8 AS builder

# Become root.
USER root

# Install some base packages, mainly for building certain pip modules
RUN apk add --update \
  gcc \
  g++ \
  make \
  cmake \
  bash \
  zlib \
  zlib-dev \
  git

# # Build and install cmake (for building pyxel which is done in the docker builder)
# RUN mkdir -p /tmp/build/cmake && cd /tmp/build/cmake && \
#   wget -nv https://cmake.org/files/v3.11/cmake-3.11.2.tar.gz && \
#   tar xf cmake-3.11.2.tar.gz --strip 1 && \
#   ./configure --prefix=/usr/local && \
#   make -j4 && \
#   make install && \
#   rm -rf /tmp/build 


# Clone the relevant repositories, yes it is fucking meta
RUN git clone --recursive https://github.com/Bioxydyn/antsbin.git && \
    cd antsbin && \
    git checkout a42b5c3 && \
    /bin/bash make_bins.sh


# Now the wheel files can be extracted by the makefile
