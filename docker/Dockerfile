FROM python:3.7-stretch AS builder

# Become root.
USER root
# Install some base packages, mainly for building certain pip modules
RUN echo "deb http://ftp.debian.org/debian sid main" >> /etc/apt/sources.list && \
  apt-get update && \
    apt-get -y install build-essential git && \
    apt-get autoclean -y && apt-get autoremove -y && \
    rm -rf /var/lib/apt

# Build and install cmake (for building pyxel which is done in the docker builder)
RUN mkdir -p /tmp/build/cmake && cd /tmp/build/cmake && \
  wget -nv https://cmake.org/files/v3.11/cmake-3.11.2.tar.gz && \
  tar xf cmake-3.11.2.tar.gz --strip 1 && \
  ./configure --prefix=/usr/local && \
  make -j4 && \
  make install && \
  rm -rf /tmp/build 

ADD scripts /

# Setup credentials to allow access to the Bioxydyn github repos
# TODO: Disable this token and setup environment variables on the dev
# machines
RUN chmod +x /git_askpass.sh
ENV GIT_ASKPASS="/git_askpass.sh"

# Clone the relevant repositories, yes it is fucking meta
RUN git clone --recursive https://github.com/Bioxydyn/antsbin.git && \
    cd antsbin && \
    git checkout a42b5c3 && \
    /bin/bash make_wheel.sh

# Now the wheel files can be extracted by the makefile
