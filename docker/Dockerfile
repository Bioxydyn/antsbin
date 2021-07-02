FROM alpine:3.13 AS builder

# Become root.
USER root

# Install some base packages, mainly for building certain pip modules
RUN apk add --update \
  gcc \
  linux-headers \
  g++ \
  binutils \
  libgcc \
  musl-dev \
  make \
  cmake \
  bash \
  zlib \
  zlib-dev \
  git \
  python3

# Clone the relevant repositories
RUN git clone --recursive https://github.com/Bioxydyn/antsbin.git && \
    cd antsbin && \
    /bin/bash make_wheel.sh

# Now the wheel files can be extracted by the makefile
