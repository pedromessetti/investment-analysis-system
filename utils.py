# utils.py

import common


def clean_logs_and_cache():
    # Walk the directory tree and remove all log files
    for root, dirs, files in common.os.walk('.'):
        for file in files:
            if file.endswith('.log') or file.endswith('.xlsx'):
                common.os.remove(common.os.path.join(root, file))

    # Remove the __pycache__ folder and its contents
    common.shutil.rmtree('scrapers/__pycache__')
    common.shutil.rmtree('__pycache__')
    print('Logs and cache successfully cleaned!')

