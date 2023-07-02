# utils.py

import os
import shutil


def clean_logs_and_cache():
    # Walk the directory tree and remove all log files
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.log') or file.endswith('.xlsx'):
                os.remove(os.path.join(root, file))

    # Remove the __pycache__ folder and its contents
    shutil.rmtree('scrapers/__pycache__')
    shutil.rmtree('__pycache__')
    print('Logs and cache successfully cleaned!')
