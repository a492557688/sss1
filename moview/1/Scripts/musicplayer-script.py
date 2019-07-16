#!C:\Users\Administrator\Documents\GitHub\MusicBox\1\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'Music-Player==1.0.5.1','console_scripts','musicplayer'
__requires__ = 'Music-Player==1.0.5.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Music-Player==1.0.5.1', 'console_scripts', 'musicplayer')()
    )
