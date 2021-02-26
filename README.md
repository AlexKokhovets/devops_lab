#DevOps Lab 2021 winter/spring
## Homework 3 by Aliaksei Kakhavets

### Package information
This package can be used to create snapshots of the state of the system. It snapshot such information as cpu, memory, virtual memory, io, network.

### How to install
1. go to the package folder

2. pip install . 

### How to use
snapshot -s 10 -t json

snapshot -s 5 -t txt

snapshot -s {interval between snapshots in sec} -t {type of output file(txt or json }

### How to uninstall
pip uninstall snapshot
