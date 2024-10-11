import os
import random
import re
import sys

DAMPING = 0.85
SAMPLES = 10000


def main():
    if len(sys.argv) != 2:
        sys.exit("Usage: python pagerank.py corpus")
    corpus = crawl(sys.argv[1])
    ranks = sample_pagerank(corpus, DAMPING, SAMPLES)
    print(f"PageRank Results from Sampling (n = {SAMPLES})")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")
    ranks = iterate_pagerank(corpus, DAMPING)
    print(f"PageRank Results from Iteration")
    for page in sorted(ranks):
        print(f"  {page}: {ranks[page]:.4f}")


def crawl(directory):
    """
    Parse a directory of HTML pages and check for links to other pages.
    Return a dictionary where each key is a page, and values are
    a list of all other pages in the corpus that are linked to by the page.
    """
    pages = dict()

    # Extract all links from HTML files
    for filename in os.listdir(directory):
        if not filename.endswith(".html"):
            continue
        with open(os.path.join(directory, filename)) as f:
            contents = f.read()
            links = re.findall(r"<a\s+(?:[^>]*?)href=\"([^\"]*)\"", contents)
            pages[filename] = set(links) - {filename}

    # Only include links to other pages in the corpus
    for filename in pages:
        pages[filename] = set(
            link for link in pages[filename]
            if link in pages
        )

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Return a probability distribution over which page to visit next,
    given a current page.

    With probability `damping_factor`, choose a link at random
    linked to by `page`. With probability `1 - damping_factor`, choose
    a link at random chosen from all pages in the corpus.
    """
    transition_probabilities = {}
    num_pages = len(corpus)
    
    # Calculate probability to choose a link from current page
    if page in corpus:
        num_links = len(corpus[page])
        for link in corpus[page]:
            transition_probabilities[link] = damping_factor / num_links
    
    # Calculate probability to choose a random page
    random_prob = (1 - damping_factor) / num_pages
    for p in corpus:
        transition_probabilities.setdefault(p, 0)
        transition_probabilities[p] += random_prob
    
    return transition_probabilities


def sample_pagerank(corpus, damping_factor, n):
    """
    Return PageRank values for each page by sampling `n` pages
    according to transition model, starting with a page at random.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageranks = {page: 0 for page in corpus}
    current_page = random.choice(list(corpus.keys()))
    
    for _ in range(n):
        pageranks[current_page] += 1
        transition_probs = transition_model(corpus, current_page, damping_factor)
        current_page = random.choices(list(transition_probs.keys()), weights=list(transition_probs.values()))[0]
    
    # Normalize pageranks
    total_samples = sum(pageranks.values())
    pageranks = {page: count / total_samples for page, count in pageranks.items()}
    
    return pageranks


def iterate_pagerank(corpus, damping_factor):
    """
    Return PageRank values for each page by iteratively updating
    PageRank values until convergence.

    Return a dictionary where keys are page names, and values are
    their estimated PageRank value (a value between 0 and 1). All
    PageRank values should sum to 1.
    """
    pageranks = {page: 1 / len(corpus) for page in corpus}
    new_pageranks = pageranks.copy()
    convergence_threshold = 0.001
    
    while True:
        for page in pageranks:
            sum_pr = sum(pageranks[i] / len(corpus[i]) for i in corpus if page in corpus[i])
            new_pageranks[page] = ((1 - damping_factor) / len(corpus)) + (damping_factor * sum_pr)
        
        # Check for convergence
        if all(abs(new_pageranks[page] - pageranks[page]) < convergence_threshold for page in pageranks):
            break
        
        pageranks = new_pageranks.copy()
    
    return pageranks


if __name__ == "__main__":
    main()

