# docker-data-sharing-example
Example of getting data into and out of a container from the host without using the network. It also doesn't allow the application process in the container to run as root, which is non-trivial if you're also sharing data. The goal here is to enable execution of (somewhat) untrusted code in a safe and platform-independent way, but you could also just use this as an example of how to easily get data into and out of a docker container.

Assuming you have docker installed, run via:

`$ python driver.py`

Only tested on macOS 10.14.1.
