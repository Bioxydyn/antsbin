#! /bin/bash
set -eux
./make_bins.sh

python setup.py bdist_wheel
