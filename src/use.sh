#!/bin/bash
conda create --name nst python=3.9
source ~/miniconda3/etc/profile.d/conda.sh
conda deactivate
conda activate nst
conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
conda activate nst
pip install --upgrade pip
pip install tensorflow
pip install -Iv pillow==9.2.0
pip install -Iv numpy==1.23.2
pip install -Iv matplotlib==3.5.3
conda activate nst
mkdir nst
cd nst
mkdir res
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/features.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/cost.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/dependencies.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/load.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/main.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/style_transfer.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/style.jpg
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/Labeeb/src/content.jpg
