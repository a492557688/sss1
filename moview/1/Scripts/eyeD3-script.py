#!C:\Users\Administrator\Documents\GitHub\MusicBox\1\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'eyeD3==0.8','console_scripts','eyeD3'
__requires__ = 'eyeD3==0.8'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('eyeD3==0.8', 'console_scripts', 'eyeD3')()
    )
