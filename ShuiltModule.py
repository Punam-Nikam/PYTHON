#shutil module provides a way to perform high-level file operations like copying and removing files and directories.
# Here are some common functions provided by the shutil module:
# copy(): Copies the contents of a file to another file.
# copy2(): Similar to copy() but also preserves metadata.
# copytree(): Recursively copies an entire directory tree rooted at source to the destination directory.
# rmtree(): Recursively deletes a directory tree.
import shutil
import os
# Example usage of shutil module functions
shutil.copytree('.tutorial', '.tutorial_backup')  # Copy entire directory")

