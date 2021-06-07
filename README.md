# Python_Hadoop_MapReduce_MarketBasketAnalysis
Market Basket Analysis using Hadoop MapReduce in Python

This repository contains the [code](https://github.com/BurraAbhishek/Python_Hadoop_MapReduce_MarketBasketAnalysis/tree/main/src) which finds the most frequently occurring item(set)s from a given list of transactions. In addition to that, this repository also contains a [dataset generator](https://github.com/BurraAbhishek/Python_Hadoop_MapReduce_MarketBasketAnalysis/tree/main/dataset_generator) which generates JSON and CSV datasets for [affinity analysis](https://en.wikipedia.org/wiki/Affinity_analysis).

## Acknowledgements
I wish to express my sincere thanks and deep sense of gratitude to my project guide, Dr. Bharadwaja Kumar, Professor, SCSE, for his consistent encouragement and valuable guidance offered to me in a pleasant manner throughout the course of the project work. I are extremely grateful to the Dean of the SCOPE, VIT Chennai, for extending the facilities of the School towards my project and for the unstinting support. 

I also take this opportunity to thank all the faculty of the School for their support and their wisdom imparted to us throughout the course. 

I thank our parents, family, and friends for bearing with us throughout the course of our project and for the opportunity they provided us in undergoing this course in such a prestigious institution. 

I would also like to thank [SSaikia_JtheRocker](https://stackoverflow.com/users/633970/ssaikia_jtherocker) for his [answer](https://stackoverflow.com/a/18562328)
 in Stack Overflow which helped me in executing the code for k-pass algorithm.

## Description:
Frequent itemset mining is generally used in retail stores to determine the likelihood of customers buying a given set of items. Retail store owners can maximize their profits if they have more stocks of frequently bought items and itemsets. It works by determining the frequency of purchasing an item or a set of items across various transactions.

Hadoop MapReduce is designed to process big data by splitting large files into blocks and splitting them across nodes in a cluster. The data is processed through the nodes in parallel. MapReduce algorithms are generally faster than conventional supercomputing models due to the advantage of data locality, where individual nodes process the data stored in them. Conventional supercomputing, in contrast, relies on high-speed networking. In a MapReduce program, the map function converts a given data into a set of <key, value> pairs and the reduce function converts the output of the mapper (the <key, value> pairs) into a collection of values.

Hadoop Streaming is included by default in Hadoop distributions. It allows developers to write MapReduce code in various programming languages without being forced to write only Java code to run MapReduce programs. Hadoop Streaming relies on streaming of big data and processing of data using the traditional command-prompt interface (STDIN and STDOUT).

The Apriori algorithm is a multi-pass algorithm. This poses some challenges to conventional Java-based MapReduce programs and bigger challenges to using the streaming MapReduce programs. In a conventional Java MapReduce program, multi-pass algorithms can be configured in the driver program. In streaming MapReduce programs, there is no concept of driver programs. Therefore, we have to run all the passes manually and sequentially. In addition to that, writing configurations and reading from them doesn’t work using the Hadoop Streaming utility. Therefore, additional scripts that write configuration changes are required in addition to the MapReduce code. On Linux, this can be automated because Linux can natively run shell scripts (.sh files). 


## Setup:
Please refer to this [page](https://github.com/BurraAbhishek/Python_Hadoop_MapReduce_MarketBasketAnalysis/wiki/Hadoop-Development-Onboarding-(Linux,-Single-Cluster)) in the wiki of this repository.

## Running the code:
Please refer to this [page](https://github.com/BurraAbhishek/Python_Hadoop_MapReduce_MarketBasketAnalysis/wiki/Experiments:-Running-the-MapReduce-code-(Linux)) in the wiki of this repository.

## License

The source code is licensed under the terms of the MIT License.

## References
1. Woo, J. (2013). Market basket analysis algorithms with mapreduce. Wiley Interdisciplinary Reviews: Data Mining and Knowledge Discovery, 3(6), 445-452.
