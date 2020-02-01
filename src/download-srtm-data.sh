#!/usr/bin/env bash

set -eu

wget http://srtm.csi.cgiar.org/wp-content/uploads/files/250m/srtm_ne_250m_tif.rar && \
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/250m/srtm_se_250m_tif.rar && \
wget http://srtm.csi.cgiar.org/wp-content/uploads/files/250m/srtm_w_250m_tif.rar && \
unar -f srtm_ne_250m_tif.rar && \
unar -f srtm_se_250m_tif.rar && \
unar -f srtm_w_250m_tif.rar && \
mv srtm_ne_250m_tif/SRTM_NE_250m.tif . && \
mv srtm_se_250m_tif/SRTM_SE_250m.tif . && \
mv srtm_w_250m_tif/SRTM_W_250m.tif .
