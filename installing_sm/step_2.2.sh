#!/usr/bin/env bash

echo
echo "Starting the patch"

# Choice of the version to patch 
SMECA_VERSION=2019.0.3-1-universal 
# Extra libraries and patched salome launcher download links  
XTLIBS_URL=https://www.code-aster.org/FICHIERS/sm2019VM/sm19_ubuntu18_xtlibs.tgz 
LAUNCHER_URL=https://www.code-aster.org/FICHIERS/sm2019VM/salome
# Patching the salome app directory (the previous launcher is backed up) 
cd $HOME/salome_meca/appli_V${SMECA_VERSION//-1-univ/_univ} 
wget $XTLIBS_URL --no-check-certificate -O xtlibs.tgz 
tar xvf xtlibs.tgz && rm -f xtlibs.tgz
mv salome salome_gpu 
wget $LAUNCHER_URL --no-check-certificate -O salome_mesa && chmod ugo+x salome_mesa 
ln -s salome_mesa salome 

echo "Done pathcing"

echo
