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
Starting benchmark with 10 queries at 10 QPS over 1 seconds
...
Done with benchmark
Total duration: 1.0195050239562988 seconds
Average duration per query: 0.10195050239562989 seconds

Request Duration Statistics
---------------------------
Count: 10
Min: 0.6287112236022949 seconds
Max: 1.0130870342254639 seconds
Avg: 0.7145693302154541 seconds
Median: 0.6306490898132324 seconds

Response Status Code Statistics
---------------------------------
Response: 200. Count: 10
Percent of Status 200 responses: 100.0%
```
