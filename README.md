# PageRank-Algorithm-Project
## Overview
This project implements the PageRank algorithm, originally developed by Larry Page and Sergey Brin, to rank web pages based on their importance within a corpus of linked documents. The PageRank algorithm has been implemented using two distinct methods: sampling and iteration.

## Project Aims
* Understand the functioning of the PageRank algorithm.
* Explore and compare two methods of implementation: sampling and iteration.
* Evaluate the effectiveness of each method in determining the importance of web pages within a given corpus.

## Definitions
* **Markov Chain**
A Markov chain is a stochastic process where the probability of transitioning to a future state depends only on the current state and not the previous sequence of events. This property is known as the Markov property.
* **PageRank**
PageRank is a ranking algorithm that assigns a numerical value to each web page based on the link structure of the web. Pages that have more inbound links or links from more important pages receive a higher rank.

## Methods
* **Sampling Method**
The sampling method simulates random walks across the web graph to estimate PageRank. Each step in the walk is governed by a transition model, which dictates the probability of following a link or randomly jumping to any other page. The number of samples (random walks) is a key parameter that affects the accuracy of the estimation.
* **Iterative Method**
The iterative method is a deterministic approach that repeatedly refines the PageRank estimates for each page. Starting with equal ranks for all pages, the algorithm updates these ranks based on the contributions from pages linking to them until the ranks converge.

## Algorithm
* **Transition Model**
The transition model determines the probability distribution over which page to visit next. It is influenced by:
* The damping factor (d), representing the probability of following a link from the current page.
* The number of outbound links on the current page.
  
## Iterative Update Equation
* The iterative method updates the PageRank values for each page using the following equation:
_PR(P)(k+1) = (1 - d) / N + d * Σ [ PR(Pi)(k) / L(Pi) ]_
Where:
* PR(P) is the PageRank of page P.
* d is the damping factor (commonly set to 0.85).
* N is the total number of pages.
* Pi are pages linking to page P.
* L(Pi) is the number of outbound links from page Pi.
  
## Files
* pagerank.py: The main Python script that implements both the sampling and iterative methods for PageRank calculation.
* corpus/: A directory containing sample HTML pages that represent the web corpus used for PageRank calculation.
  
## Usage
* To run the program, use the following command:
_python pagerank.py corpus/_
This will calculate the PageRank of all pages in the corpus/ directory using both sampling and iteration, and print the results.

## Requirements
* Python 3.x
* Required Python packages: os, random, re, sys
  
## Output
* The program will output the PageRank values for each page using both sampling (with 10,000 samples by default) and iteration until convergence.
Example output:
  * PageRank Results from Sampling (n = 10000)
    * page1.html: 0.1953
    * page2.html: 0.1487
    * page3.html: 0.2236

  * PageRank Results from Iteration
   * page1.html: 0.1928
   * page2.html: 0.1491
   * page3.html: 0.2241

## Conclusion
This project successfully implements and compares the PageRank algorithm using both sampling and iteration methods. The iterative method converges to an accurate solution, while the sampling method provides a good estimate based on random walks. Both methods capture the relative importance of web pages within the corpus based on their link structure.
