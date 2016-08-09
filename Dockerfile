FROM ubuntu:16.04
RUN apt-get update && \
    apt-get install -y python python-numpy
COPY demo.py /bin/demo.py
RUN chmod 755 /bin/demo.py
ENTRYPOINT ["/bin/demo.py"]
