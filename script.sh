export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
mkdir nst
cd nst
mkdir res
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/features.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/cost.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/dependencies.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/load.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/main.py
wget https://raw.githubusercontent.com/Greyless/Neural-Style-Transfer/main/src/style_transfer.py
wget https://github.com/Greyless/Neural-Style-Transfer/raw/main/src/style.jpg
wget https://github.com/Greyless/Neural-Style-Transfer/raw/main/src/content.jpg
