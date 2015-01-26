import os
from distutils.core import setup
from Cython.Build import cythonize

setup(name='parabam',
	  description='Parallel BAM File Analysis',
      version='0.1.3dev',
      author="JHR Farmery",
      license='BSD',
      author_email = 'jhrf2@cam.ac.uk',
      package_dir = {'parabam': '','parabam.interface': 'interface'},
      packages = ['parabam','parabam.command'],
      requires = ['cython','numpy','argparse','pysam'],
      scripts = ['bin/parabam'],
      ext_modules=cythonize(("chaser.pyx","support.pyx","core.pyx","command/subset.pyx","command/stat.pyx"))#""
      )
