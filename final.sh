#!/bin/bash

# Ensure the target directory exists
mkdir -p /home/doc-bd-a1/service-result/

# Move the result files instead of copying them
mv /home/doc-bd-a1/eda-in-1.txt /home/doc-bd-a1/service-result/
mv /home/doc-bd-a1/eda-in-2.txt /home/doc-bd-a1/service-result/
mv /home/doc-bd-a1/eda-in-3.txt /home/doc-bd-a1/service-result/
mv /home/doc-bd-a1/vis.png /home/doc-bd-a1/service-result/
mv /home/doc-bd-a1/k.txt /home/doc-bd-a1/service-result/
mv /home/doc-bd-a1/res_dpre.csv /home/doc-bd-a1/service-result/

# Stop the container
echo "Stopping container..."
exit
