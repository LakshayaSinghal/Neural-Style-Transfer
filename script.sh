export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/
mkdir -p $CONDA_PREFIX/etc/conda/activate.d
echo 'export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$CONDA_PREFIX/lib/' > $CONDA_PREFIX/etc/conda/activate.d/env_vars.sh
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
