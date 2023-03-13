#landmark DevOps
#Eddie
#JohnPaul
#femi
def userMgt(name str, age int) -->str:
    pass
    return {}.{}.format(name, age)

Forloop assingment

#!Write a shell script to print numbers from 100-90
#using for-loop [100, 99, 98, ---, 90]

#!/bin/sh
#b = 100
#b = 100 -1 = 99
#b = 99 -1 = 98
#b = 98 -1 = 97
#loop will break
#70 = 71 -1 = 70

#forloop.sh
#=========
for (( b=100;b>69;b-- ))
do
echo $b
done
echo "forloops ends"
