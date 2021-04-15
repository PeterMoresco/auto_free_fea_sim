#!/usr/bin/env bash
echo
echo "Updating"
sudo -E apt update && sudo -E apt install -y --no-install-recommends \
                wget net-tools python python3 libbsd0 libbz2-1.0 libc6 libdbus-1-3 \
                libexpat1 libffi6 libfontconfig1 libfreeimage3 libfreetype6 \
                libgcc1 libgfortran3 libglib2.0-0 libglu1-mesa libgomp1 libharfbuzz0b \
                libice6 libicu60 libilmbase12 libjbig0 libjpeg62 liblcms2-2 liblzma5 \
                libmng2 libmuparser2v5 libnlopt0 libnss-sss libopenblas-base \
                libopenexr22 libpcre3 libpng16-16 libquadmath0 libraw16 libreadline7 \
                libsm6 libssl1.0.0 libstdc++6 libtbb2 libtiff5 libtinfo5 libuuid1 \
                libx11-6 libx11-xcb1 libxau6 libxcb-glx0 libxcb1 libxcursor1 \
                libxdmcp6 libxext6 libxfixes3 libxi6 libxml2 libxmu6 libxrender1 \
                libxss1 libxt6 xterm x11-xkb-utils xkb-data zlib1g

echo "Done updating"
echo