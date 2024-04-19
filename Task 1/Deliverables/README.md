## Python and Docker Automation Task


### 1) Deliverables

Upload you solution here. Also, use this space to document a what you did in this exercise.

I have created a Python script that performs the duty of reading arguments for config file, output directory and debug. I tried to separate them so code is readable and each method performs a single task.
I had to research on how to handle merge fields with Python, also a bit on how to handle received arguments, iterating dictionaries and reading from .yaml files, as I didn't had a lot of professional experience with Python, using it mostly during my undergraduate course and some other pet projects.
Regarding the Docker image, I took a look at the Alpine image documentation to understand how would I be able to run the created application into a Docker image. So far, I had used only the Python base image to run Python applications. 