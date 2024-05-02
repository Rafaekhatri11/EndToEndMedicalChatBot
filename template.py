# import os
# from pathlib import Path
# import logging

# logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
# list_of_files = [
#     "src/__init__.py",
#     "src/helper.py",
#     "src/prompt.py",
#     ".env",
#     "setup.py",
#     "research/trials.ipynb",
#     "app.py",
#     "store_index.py",
#     "static",
#     "templates/chat.html"
# ]

# for filepath in list_of_files:
#     filepath = Path(filepath)
#     filedir, filename = os.path.split(filepath)

#     if filedir !="":
#         os.makedirs(filedir,exist_ok=True)
#         logging.info(f"Creating directory; {filedir} for the file {filename}")

#     if (not os.path.exists(filepath)) or (os.path.getsize(filename) == 0):
#         with open(filedir, 'w') as f:
#             logging.info(f"Creating empty file: {filepath}")
#     else:
#         logging.info(f"{filename} is already created")
            

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "research/trials.ipynb",
    "app.py",
    "store_index.py",
    "static/.gitkeep",
    "templates/chat.html"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    # print(f"+++++++++++++++++++++++++++ filedir {filedir} filename {filename}")

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file {filename}")

    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:  # Fix: Use `filepath` instead of `filename`
        with open(filepath, 'w'):  # Fix: Use `filepath` instead of `filedir`
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")
