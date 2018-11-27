FROM python:3.7-stretch AS builder

# Become root.
USER root
# Install some base packages, mainly for building certain pip modules
RUN echo "deb http://ftp.debian.org/debian stretch-backports main" >> /etc/apt/sources.list && \
  apt-get update && \
    apt-get -y install build-essential git && \
  apt-get -y -t stretch-backports install cmake && \
    apt-get autoclean -y && apt-get autoremove -y && \
    rm -rf /var/lib/apt

ADD scripts /

# Setup credentials to allow access to the Bioxydyn github repos
# TODO: Disable this token and setup environment variables on the dev
# machines
RUN chmod +x /git_askpass.sh
ENV GIT_ASKPASS="/git_askpass.sh"

# Clone the relevant repositories, yes it is fucking meta
RUN git clone --recursive https://github.com/Bioxydyn/antsbin.git && \
    cd antsbin && \
    git checkout 3e91490

RUN /bin/bash make_wheel.sh

# Now the wheel files can be extracted by the makefile
