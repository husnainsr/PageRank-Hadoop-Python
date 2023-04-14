#!/usr/bin/sh
i=1
while [ $i != 0 ]:
do
	hadoop jar /usr/local/hadoop/share/hadoop/tools/lib/hadoop-streaming-3.2.4.jar \
	-input /A2/nodes.txt \
	-output /A2/output \
	-mapper "python3 /home/usr/A3/lastTry/mapper.py" \
	-reducer "python3 /home/usr/A3/lastTry/reducer.py"

	hdfs dfs -rm -r /user/hadoopuser/output
	i=`python3 /home/hadoopuser/Desktop/A2/checker.py`
done
cat /dev/null > output.txt