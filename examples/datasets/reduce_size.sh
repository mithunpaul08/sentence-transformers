#if you want to test your code in a smaller set
for each in AllNLI/*.gz;
do
gunzip $each
done
for each in AllNLI/*;
do
head -20 $each >temp
mv temp $each
done
for each in AllNLI/*;
do
gzip $each
done

