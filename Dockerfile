# Use Ubuntu as base image
FROM ubuntu:latest

# Set the working directory inside the container
WORKDIR /home/doc-bd-a1/

# Install Python and required system libraries
RUN apt-get update && apt-get install -y \
    python3 \
    python3-pip && \
    pip3 install --break-system-packages pandas numpy seaborn matplotlib scikit-learn scipy

# Copy the dataset to the container
COPY Games.csv /home/doc-bd-a1/Games.csv

# Start a bash shell when the container runs
CMD ["/bin/bash"]
