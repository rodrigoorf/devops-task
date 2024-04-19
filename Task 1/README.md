## Python and Docker Automation Task


### 1) The Script

We need to generate some documents, but this should be done automatically. The files that need to be filled is  ```template.docx``` file. . All information needed to generate this documents are in ```config.yaml```.

You should create a Python Script that looks for the information inside ```config.yaml``` file and fill ```template.docx```.with the correct information. The script should be parametrized, so we will be able to change the output directory and the configuration file. A ```debug``` optional flag should also be available, so is possible to show more information on script log. The script must be called as described below:

```bash
$> python main.py -c [CONFIG-FILE] -o [OUTPUT-DIR] --debug
```
or

```bash
$> python main.py --config [CONFIG-FILE] --output [OUTPUT-DIR] --debug
```


The output must be a folder with N documents filled with the information within ```config.yaml```. The output file name must be  ```[BAND_NAME].docx```. Look at ```output_example.docx``` file to know how the outputted document should look like

### 2) Docker Image

This script should run inside a Docker Image based on [Alpine Image](https://hub.docker.com/_/alpine/) developed by you with all the dependencies needed. 


### Deliverables
  * A Python scipt that reads a yaml file and fill a document based in a template with the information.
  * A Docker Image deployed on docker hub containing the script and libraries used (so we don't have to worry about setting up an environment to run the automation).
  * The Dockerfile done by yourself to generate the deployed Docker Image.
  * All documents generated by you script.

#### Hint:

Look for Microsoft Word Merge Fields.