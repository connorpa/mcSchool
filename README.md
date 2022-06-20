# PCD 21 June 2022

Clone locally (preferrably on your private machine).

Then run script `./runNotebook` or `./runLab`: the environment will be ready in the browser under `localhost` address.
The templates for the exercises are in the `temp/template` directory.

## Offline running of the Python programs

Clone the git repository as above and run any command through docker, like:

```
cd exercisePy
./rd python -i exercise-1.py
```
The `-i` is for interactive mode, which can be useful if some plots needs to be shown.

## Offline running of the C++ programs

The C++ programs are longer and need to be compiled but run faster.

Compile in the standard way using make and run afterwards, all in the docker environment `rd`
```
cd exerciseCpp
./rd make
./rd ./example-1
```

For the local running you may need to install docker on your computer (in case of Ubuntu):
```
sudo apt install docker.io
```

## Offline running of the programs without docker on system with access to CVMFS file system

In this case you can use ROOT and LHAPDF libraries installed by CERN on CVMFS.
Just call
```
source setupCVMFS.sh
```
to setup the environment and then simple run Python or C++ programs as above, but without `./rd` in front.

## Offline running without access to CVMFS

Without the Docker image  and access to CVMFS the ROOT and LHAPDF needs to be installed which can take take some time.

Good luck.
