#!/usr/bin/env  python3

import os
import sys
import zipapp
import subprocess
from shutil import rmtree
from pathlib import Path
from zip_app.bar import __version__
from zip_app.bar import __appname__ 


def setup_venv(path):
    """Setup a new virtualenv at the specified path and install requirements.txt"""
    venv_path = Path(path)
    if venv_path.exists():
        return
    
    requirements = Path(__file__).resolve().parent / 'requirements.txt'
    
    # Create virtualenv
    subprocess.run(['python3', '-m', 'venv', str(venv_path)], capture_output=True, check=True)
    
    # Get pip path
    pip = venv_path / 'bin' / 'pip'
    
    # Install requirements if file exists
    if requirements.exists():
        subprocess.run([str(pip), 'install', '-r', str(requirements)], capture_output=True, check=True)
    else:
        print(f"Warning: {requirements} not found", sys.stderr)

def clean_crap(path:Path):
    for glob in '**/__pycache__', '**/.sesskey':
        for crap in path.rglob(glob):
            rmtree(crap)

def main():

    ME = Path(__file__).name
    WORK_DIR = Path(__file__).resolve().parent
    setup_venv('/tmp/.neo')

    assert (WORK_DIR / 'zip_app').is_dir(), f"{ME} needs to be relative to zip_app dir for deploy"
    
    clean_crap(WORK_DIR)
    os.chdir(WORK_DIR)

    # create the app dir for ziping
    Path('dist').mkdir(exist_ok=True)
    zipapp.create_archive(
        source='zip_app',
        target=f'dist/{__appname__}-{__version__}', 
        interpreter=f'/tmp/.neo/bin/python'  
    )
    return  str(Path(f'./dist/{__appname__}-{__version__}').resolve())

script = main()
print(script) 
# alias bar='$($HOME/exp/bar/bundle_bar.py)'