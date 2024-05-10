# HTTP Benchmarking and Load Testing Library

Reports latencies and error rates for a given url at a given number queries per second for a given total number of requests.

Basic Command:
- python3 benchmark.py url

Help command:
- python3 benchmark.py --help

Optional Arguments:
- --qps or -q: Generate requests at given fixed number of queries per second. Default is 1.
- --total or -q: Total number of queries. Default is 1.

Positional Argument:
- url: Which URL to benchmark


Example:

```
> docker build -t my-python-app .
> docker run --rm my-python-app --qps=10 --total=10 https://www.google.com

Starting benchmark with 10 queries at 10 QPS over 1 seconds
...
Done with benchmark
Total duration: 1.0906398296356201 seconds
Average duration per query: 0.10906398296356201 seconds

Request Duration Statistics
---------------------------
Count: 10
Min: 1.0780112743377686 seconds
Max: 1.0876076221466064 seconds
Avg: 1.0837601184844972 seconds
Median: 1.0834991931915283 seconds

Response Status Code Statistics
---------------------------------
Response: 200. Count: 10
Percent of Status 200 responses: 100.0%
```
