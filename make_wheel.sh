#! /bin/bash
set -eux

#./make_bins.sh

pip3 install -r requirements.txt
python3 setup.py bdist_wheel
python3 setup.py bdist_wheel
