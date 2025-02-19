from __future__ import absolute_import, division, print_function

from setuptools import setup
import os
import sys
import json

sys.path.append('SSINS')


def package_files(package_dir, subdirectory):
    # walk the input package_dir/subdirectory
    # return a package_data list
    paths = []
    directory = os.path.join(package_dir, subdirectory)
    for (path, directories, filenames) in os.walk(directory):
        for filename in filenames:
            path = path.replace(package_dir + '/', '')
            paths.append(os.path.join(path, filename))
    return paths


data_files = package_files('SSINS', 'data')

setup_args = {
    'name': 'SSINS',
    'author': 'M. Wilensky',
    'url': 'https://github.com/mwilensky768/SSINS',
    'license': 'BSD',
    'description': 'Sky-Subtracted Incoherent Noise Spectra',
    'package_dir': {'SSINS': 'SSINS'},
    'packages': ['SSINS'],
    'include_package_data': True,
    'scripts': ['scripts/Run_HERA_SSINS.py', 'scripts/MWA_EoR_High_Flag.py',
                'scripts/MWA_gpubox_to_SSINS_on_Pawsey.sh', 'scripts/MWA_vis_to_SSINS.py',
                'scripts/occ_csv.py'],
    'package_data': {'SSINS': data_files},
    'setup_requires': ['setuptools_scm'],
    'use_scm_version': True,
    'install_requires': ['pyuvdata', 'h5py', 'pyyaml'],
    'zip_safe': False,
}


if __name__ == '__main__':
    setup(**setup_args)
