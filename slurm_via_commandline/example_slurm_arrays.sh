#!/bin/bash
#SBATCH --time=0-00:01:00
#SBATCH --nodes=1
#SBATCH --partition=all
#SBATCH --job-name DaskDemo

export LD_PRELOAD=""

source /etc/profile.d/modules.sh

/bin/hostname

python3 /home/cpassow/demos/dask_demo/slurm_via_commandline/array_numpy_vs_dask.py

