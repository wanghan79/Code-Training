#! bin/bash
echo "success" >>/mnt/h/biodata/PDBfile/test.txt
rsync -rlpt -v -z --delete --port=33444 \rsync.rcsb.org::ftp_data/structures/divided/pdb/ ./PDB
rsync -rlpt -v -z --delete --port=33444 \rsync.rcsb.org::ftp_data/structures/divided/XML/ ./PDBML