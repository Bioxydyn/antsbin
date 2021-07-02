Getting Started
===============

_antsbin_ is a python-3 package that provides access to **statically linked** binaries for _antsApplyTransforms_ and _antsRegistration_ for Linux and macOS platforms. It is lightweight and ideal for dockerized applications - and allows easy calling of the ANTs binaries from python. _antsbin_ doesn't provide a pythonic wrapper around the applications. This is a design compromise because the ANTs command lines are mature and complex.  A lot of existing code and most of the examples of ANTs use the command lines.

You can install it using pip:

     pip install https://github.com/Bioxydyn/antsbin/releases/download/v0.1.1/antsbin-0.1.1-cp37-cp37m-linux_x86_64.whl
     
or if you have a Mac

     pip install https://github.com/Bioxydyn/antsbin/releases/download/v0.0.2/antsbin-0.0.2-cp37-cp37m-macosx_10_13_x86_64.whl

Then you can use it e.g. like this from python (it's crude and simple):

    from antsbin import ants_apply_transforms, ants_registration

    result = subprocess.run(ants_apply_transforms, capture_output=True,
                        check=False)

Unfortunately there isn't a Windows build.
