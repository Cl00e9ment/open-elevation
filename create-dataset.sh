#!/usr/bin/env bash

OUTDIR="/code/data"
if [ ! -e $OUTDIR ] ; then
    echo $OUTDIR does not exist!
fi

CUR_DIR=$(pwd)

set -eu

cd $OUTDIR
../download-srtm-data.sh
echo "creating tiles, this may take a while..."
../create-tiles.sh SRTM_NE_250m.tif 10 10
../create-tiles.sh SRTM_SE_250m.tif 10 10
../create-tiles.sh SRTM_W_250m.tif 10 20
rm -rf SRTM_NE_250m.tif SRTM_SE_250m.tif SRTM_W_250m.tif *.rar srtm_*_250m_tif

cd $CUR_DIR
