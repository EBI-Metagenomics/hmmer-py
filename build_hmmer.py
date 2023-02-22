#!/usr/bin/env python

import subprocess
import os
from pathlib import Path

dir_path = Path(os.path.dirname(os.path.realpath(__file__)))
subprocess.check_call([dir_path / "build_hmmer.sh"], shell=True)
