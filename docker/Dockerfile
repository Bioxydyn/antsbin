FROM alpine:3.8 AS builder

# Become root.
USER root

# Install some base packages, mainly for building certain pip modules
RUN apk add --update \
  gcc \
  g++ \
  binutils \
  libgcc \
  musl-dev \
  make \
  cmake \
  bash \
  zlib \
  zlib-dev \
  git

# Clone the relevant repositories, yes it is fucking meta
RUN git clone --recursive https://github.com/Bioxydyn/antsbin.git && \
    cd antsbin && \
    /bin/bash make_wheel.sh

# Now the wheel files can be extracted by the makefile
