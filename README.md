Getting Started
===============

antsbin is a python-3 package that provides access to statically linked binaries for antsApplyTransforms and antsRegistration for Linux and macOS platforms. It is lightweight and ideal for dockerized applications - and allows easy calling of the Ants binaries from python. No more building ANTs! It doesn't provide a pythonic wrapper around the applications. This is a design compromise because the ANTs command lines are mature and complex.  A lot of existing code and most of the examples of ANTs use the command lines.

You can install it by adding e.g. the following to your requirements.txt:

     pip install https://github.com/Bioxydyn/antsbin/releases/download/v0.1.1/antsbin-0.1.1-cp37-cp37m-linux_x86_64.whl
     
or

     pip install https://github.com/Bioxydyn/antsbin/releases/download/v0.0.2/antsbin-0.0.2-cp37-cp37m-macosx_10_13_x86_64.whl

Then you can use it like this:

    from antsbin import ants_apply_transforms, ants_registration

    result = subprocess.run(ants_apply_transforms, capture_output=True,
                        check=False)
