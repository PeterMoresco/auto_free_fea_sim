#!/usr/bin/env bash

echo
echo "Starting the download and installation"

# Choice of the version to install
 SMECA_VERSION=2019.0.3-1-universal
 # Automatically generate the archive filename and download link 
 SMECA_TGZ=salome_meca-$SMECA_VERSION.tgz 
 SMECA_URL=https://code-aster.org/FICHIERS/$SMECA_TGZ 
 # Download the salome_meca installer archive and inflate the .tgz file 
 INSTDIR=$(mktemp -d -t smeca-install-XXXXXXXXXX) 
 cd $INSTDIR && wget --no-check-certificate $SMECA_URL -O $SMECA_TGZ 
 tar xvf $SMECA_TGZ 
 # Install salome_meca in the default location ($HOME/salome_meca) 
 sh ${SMECA_TGZ/tgz/run} -t $HOME/salome_meca -l English -D –f 
 # Cleanup 
 rm -rf $INSTDIR

 echo "Done installing"

 echo