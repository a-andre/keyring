#!/usr/bin/env python

import os.path
import sys
import subprocess
import pytest

#tests_dir = os.path.dirname(__file__)
#sys.path.insert(0, os.path.dirname(tests_dir))

if __name__ == '__main__':
    mock = None
    if len(sys.argv) > 1 and os.path.isfile(sys.argv[1]):
        mock = subprocess.Popen(
            (
                '/usr/bin/python3',
                sys.argv[1],
            ),
            stdout=subprocess.PIPE,
            universal_newlines=True,
        )
        assert mock.stdout is not None  # for mypy
    result = pytest.main(['-v', 'tests/backends/test_libsecret.py'])
    if mock is not None:
        mock.terminate()
    sys.exit(result)
