
# Multiple-Source Personalized PageRank using Hadoop Cluster

## Objective

The objective of this project is to implement multiple-source personalized PageRank algorithm using a Hadoop cluster.

## Tasks

The dataset provided in the last assignment will be used for this project. The task involves implementing multiple-source personalized PageRank algorithm and setting up a multi-node Hadoop cluster (one master and two slaves) to execute the code on.

## Multiple-Source Personalized PageRank

The multiple-source personalized PageRank algorithm involves the following:

-   The notion of source nodes is used to compute the personalization.
-   Instead of a uniform distribution across all nodes, the m source nodes get a mass of 1/m and every other node gets a mass of zero when initializing PageRank.
-   Whenever the model makes a random jump (or jumps out of a dangling node), the random jump is always back to one of the source nodes randomly with 1/m probability to one of the source nodes. This is different from ordinary PageRank, where there is an equal probability of jumping to any node.

The working of multi-source personalized PageRank can be seen in the animation provided in the project description.

## Output

The output of the program should provide personalized PageRank value and node ID for the set of source nodes provided.

## How to Execute

To execute the program, a Hadoop cluster with one master and two slaves must be set up. The code can then be run on the cluste
