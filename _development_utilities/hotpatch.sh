#!/usr/bin/bash

#This script creates a hotfix from a specified commit to the current HEAD while preserving directory
#structure so end users can drag/drop it.

#Needs to be executed from the top level because I'm too lazy to handle the indirection.

mkdir -p hotfix
echo $1
#We do all this indirection because git diff does *not* support regular shell processing
git diff --exit-code --name-only $1 HEAD > tmp_file
#Remove these git diff --exit-code artifacts
sed -i -b '/^diff/d' tmp_file
sed -i -b '/^new/d' tmp_file
sed -i -b '/^index/d' tmp_file
sed -i -b '/deleted file mode 100644/{N;d}' tmp_file #In case of file delete
sed -i -b '/Binary files /d' tmp_file #Binary file changes
#Load the data back into file
file_list=($(cat tmp_file))
#Garbage collect
rm tmp_file

tar cf - ${file_list[*]} | (cd hotfix; tar xf -)
