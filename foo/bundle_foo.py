#!/bin/env -S pyboots --http http://automationmd/virtualenv/neo/requirements.txt  --require 3.12 --rebuild-on-changes

import os
import zipapp
from shutil import rmtree
from pathlib import Path
from zip_app.foo import __version__ 
from zip_app.foo import __appname__ 


def clean_crap(path:Path):
    for glob in '**/__pycache__', '**/.sesskey':
        for crap in path.rglob(glob):
            rmtree(crap)

def main():

    ME = Path(__file__).name
    WORK_DIR = Path(__file__).resolve().parent

    assert (WORK_DIR / 'zip_app').is_dir(), f"{ME} needs to be relative to zip_app dir for deploy"
    
    clean_crap(WORK_DIR)
    os.chdir(WORK_DIR)

    # create the app dir for ziping
    Path('dist').mkdir(exist_ok=True)
    zipapp.create_archive(
        source='zip_app',
        target=f'dist/{__appname__}-{__version__}', 
        interpreter=f'/bin/env -S pyboots --http http://automationmd.s/virtualenv/neo/requirements.txt  --require 3.12'  
    )
    return  str(Path(f'./dist/{__appname__}-{__version__}').resolve())

script = main()
print(script) 
# alias foo='$($HOME/exp/foo/bundle_foo.py)'