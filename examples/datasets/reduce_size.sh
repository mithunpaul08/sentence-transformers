#if you want to test your code in a smaller set
#for each in ./*.gz;
#do
#gunzip $each
#done
for each in *;
do
head -20 $each >temp
mv temp $each
done
