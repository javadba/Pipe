#!/usr/bin/env python
from distutils.core import setup
setup(
    name = 'pipe',
    py_modules = ['pipe'],
    version = '1.5',
    description = 'Module enablig a sh like infix syntax (using pipes)',
    author='Julien Palard,Stephen Boesch (small enhancements)',
    author_email='javadba@gmail.com',
    url='https://github.com/javadba/Pipe',
    download_url='https://github.com/javadba/Pipe/tarball/pipesteve'
    long_description="""Pipe is a module enablig a sh like infix syntax (using pipes)'.

As an exemple, here is the solution for the 2nd Euler Project exercise :

"Find the sum of all the even-valued terms in Fibonacci
 which do not exceed four million."

Given fib a generator of fibonacci numbers ::

    euler2 = fib() | where(lambda x: x % 2 == 0)
                   | take_while(lambda x: x < 4000000)
                   | add
                   | write('myfile.csv')
                   | tee(20)

""",
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries :: Python Modules"
        ]
)
