# To create a virtual environment : create a folder where we wanna create environment
#                                   Open the forlder in terminal
#                                   write command : python -m venv "myenv"(DirName)
#                                   Activate the env : myenv(DirName)\Scripts\activate
#                                   (myenv)Activated now 
# 
# A Virtual environment is a tool used to isolate specific python environments on a single machine,
# allowing you to work on multiple projects with different dependencies and packages without conflicts
# This can be especially useful when working on projects that have conflicting package versions or
# or packages that are not compatible with each other.

# once the virtual env is activated,any packages that you install using pip will be installed in the virtual environment,rather than in the global python environment.
# This allows you to have separate set of packages for each project,without affecting the packages installed in the global environment .

# we can deactivate the virtual env by using command "deactivate"