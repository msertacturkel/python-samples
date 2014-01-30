#!/bin/bash

i=0
for file in `ls $1`  
do
    #echo $file;
    array[ $i ]="$file"
    (( i++ ))
done

biggest=${array[0]}

for i in ${array[@]}
do
     if [[ $i -gt $biggest ]]
     then
        biggest="$i"
     fi
done
echo "****en guncel olan****: " $biggest

cd $1/$biggest


j=0
for x in `find . -name *-pages-articles.xml.bz2`; 
do 
        files[ $j ]="$x"
	length=${#files[$j]}
	unzip=${files[$j]:2:length-2}
	echo "Arsivden Cikarilan dosya: "$unzip
	bzip2 -d $unzip
	((j++))
done 


