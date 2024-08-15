cd /home/troy/Desktop
# python
sudo apt install python3-pip
# git
sudo apt install git
# get conda
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm -rf ~/miniconda3/miniconda.sh
~/miniconda3/bin/conda init bash
~/miniconda3/bin/conda init zsh
# get git repo
git clone https://github.com/troyyxk/CacheGen.git
# install conda dependencies
cd CacheGen
conda env create -f env.yaml
conda activate cachegen
pip install -e LMCache
cd LMCache/third_party/torchac_cuda 
python setup.py install