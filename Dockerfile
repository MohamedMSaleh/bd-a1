# Use Ubuntu as base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /home/doc-bd-a1/

# Install Python and required libraries
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip \
    python3-pandas \
    python3-numpy \
    python3-seaborn \
    python3-matplotlib \
    python3-sklearn \
    python3-scipy


# Copy the dataset to the container
COPY Games.csv /home/doc-bd-a1/Games.csv

# Start a bash shell when the container runs
CMD ["/bin/bash"]
