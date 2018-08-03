#!/bin/bash
#
# Note: This script uses the tree command. Install it with `sudo apt get install tree`

echo
echo
echo "Putting all found game saves into ~/saves_backup/"

pushd ~pi/ > /dev/null
find ./RetroPie/roms/ -iname "*.srm" -exec rsync -aR {} ~/saves_backup/ \;
popd > /dev/null

tree ~/saves_backup/

echo "Create an archive of all saves using: 'cd ~pi & tar -zcvf saves.tar.gz ./saves_backup/*'"
echo " (sleeping for 5 seconds so you can read that...)"
sleep 5
