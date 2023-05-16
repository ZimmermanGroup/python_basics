#!/bin/bash
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -J test
#SBATCH -p zim2080
#SBATCH -e %3a/error
#SBATCH -o %3a/output
#SBATCH -t 10:00
#SBATCH --array=0-229%10

module load qchem

export x=$(printf "%03d\n" $SLURM_ARRAY_TASK_ID)

cd $x
qchem qchem.in qchem.out
