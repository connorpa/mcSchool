# mcSchool

Use
```
git clone git@github.com:zleba/mcSchool.git
```

or download the archive.
```
wget https://github.com/zleba/mcSchool/archive/master.zip
unzip master.zip
```
Requires ROOT and in one case LHAPDF.

Standardly compile using make
```
cd exercise1
make  #Compiles all examples
./example-1 #run example-1
```

In case that ROOT and/or LHAPDF is not in your machine, you can use Docker image which contains everything required:
```
cd exercise1
./runDocker make  #Compiles all examples
./runDocker ./example-1 #run example-1
```
You may need to install docker on your computer (in case of Ubuntu):

```
sudo apt install docker.io
```
