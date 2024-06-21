#!/bin/bash

singularity build --force --nv --fakeroot eeg_evaluator.sif singularity/singularity.def

# Define the singularity image and script
SIF_IMAGE="eeg_evaluator.sif"

# Iterate over the parameter sets and run the script
singularity exec --nv $SIF_IMAGE python3 main.py network_train
