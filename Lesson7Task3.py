import os
import shutil

ROOT = os.path.join(os.path.dirname(__file__), 'my_project2')
DIRS = os.path.join(os.path.dirname(__file__), 'my_project2', 'templates')

if not os.path.exists(DIRS):
    os.makedirs(DIRS)
for root, dirs, files in os.walk(ROOT):
    if root.count('templates'):
        for _dirs in dirs:
            if not os.path.exists(os.path.join(DIRS, _dirs)):
                os.makedirs(os.path.join(DIRS, _dirs))
            for file in files:
                src_file = os.path.join(root, file)
                dsc_file = os.path.join(DIRS, os.path.basename(root))
                if not os.path.dirname(src_file) == dsc_file:
                    shutil.copy(src_file, dsc_file)
