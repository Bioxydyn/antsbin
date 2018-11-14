import os
import sys

name = "antsbin"


def ants_apply_transforms():
    d = os.path.dirname(sys.modules['antsbin'].__file__)
    return os.path.join(d, 'antsApplyTransforms')


def ants_registration():
    d = os.path.dirname(sys.modules['antsbin'].__file__)
    return os.path.join(d, 'antsRegistration')
