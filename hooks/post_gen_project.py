#!/usr/bin/env python
import subprocess
import os

project_dir = os.path.realpath(os.path.curdir)
subprocess.run(["git", "init"], cwd=project_dir)
subprocess.run(["git", "add", "."], cwd=project_dir)
subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=project_dir)
