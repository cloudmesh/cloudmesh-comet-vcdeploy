from pyspark import SparkContext

sc = SparkContext()

txt = sc.textFile('hdfs:///shakespeare.txt')
counts = txt.flatMap(lambda line: line.split(" ")) \
            .map(lambda word: (word, 1)) \
            .reduceByKey(lambda a, b: a + b) \
            .sortBy(lambda t: t[1], ascending=False)
counts.saveAsTextFile('hdfs:///shakespeare-wordcount.txt')

