# Album Summarizer
## Requirements
- Anaconda
- Node.js

## Python Developer Packages
Note: Only Keras 2.3.0+ supports Tensorflow 2.0+. Use Tensorflow 1.15 if an older version of Keras is used.

Note: End Users do not need to install these.
- Pylint
- autopep8

Run the following in a terminal that has access to Anaconda:
```
conda create --name album keras-gpu "tensorflow-gpu<2" autopep8 pylint dill opencv scikit-learn --yes
```

## Running the Program
The current working directory must be `<project-home>/electron`.
```
npm start
```