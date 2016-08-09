*Note: this extended readme is modified on the original version, it can be downloaded 
when you login beta.mindi.io and click `view example` and `download sample data`*

# Ising spin glass example

The included python script simply takes an Ising spin glass Hamiltonian and 
guesses random configurations. The lowest energy guess is printed to the 
screen, preceeded by a 'v'.

    bash:~$ python demo.py example.txt
    v -1 1 1 -1  ...

To use it on Mindi, you will first need to install Docker (see these [excellent instructions](https://docs.docker.com/engine/installation/)).

Next, run the following (be sure to replace the all caps keywords):

    docker login -u DOCKERHUB_USERNAME -p DOCKERHUB_PASSWORD
	<!---
	may need a `sudo` for these, also `docker login` is enough
	-->
    docker build -t DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION .
    docker push DOCKERHUB_USERNAME/SOLVER_NAME:SOLVER_VERSION

Once you have successfull push the `container` to docker, log into Mindi and submit the container 
URL under the bin packing challenge. To submit, enter:
	
	UserNameOfDocker/ContainerName:VersionNo


The solver with the lowest energy configuration wins!


# Docker install and configuration in Ubuntu 16.04

To install docker, follow [these instructions](https://docs.docker.com/engine/installation/linux/ubuntulinux/)
