import argparse
import statistics
import threading
import time
from urllib.request import urlopen

def init_argparse():
    parser = argparse.ArgumentParser(usage="%(prog)s [OPTION] [URL]", description="Benchmark a URL.")
    parser.add_argument("-q", "--qps", default=1, help="Queries per second")
    parser.add_argument("-t", "--total", default=1, help="Total number of queries")
    parser.add_argument("url", help="URL to benchmark")
    return parser

def evaluate(url, result):
    request = {}
    start = time.time()
    response = urlopen(url)
    end = time.time()
    request['duration'] = float(end - start)
    request['response'] = response.getcode()
    result.append(request)

def main():
    parser = init_argparse()
    args = parser.parse_args()
    qps = int(args.qps)
    total = int(args.total)
    seconds = total//qps
    print(f"Starting benchmark with {total} queries at {qps} QPS over {seconds} seconds")
    print(f"...")
    result = []
    start = time.time()
    thread_batches = [[threading.Thread(target=evaluate, args=(args.url, result)) for _ in range(qps)] for _ in range(seconds)]
    for thread_batch in thread_batches:
        for thread in thread_batch:
            thread.start()
        time.sleep(1)
        for thread in thread_batch:
            thread.join()
    end = time.time()
    print("Done with benchmark")

    duration = float(end - start)
    print(f"Total duration: {duration} seconds")
    print(f"Average duration per query: {duration / total} seconds")

    durations = []
    for request in result:
        durations.append(request['duration'])

    print("\nRequest Duration Statistics")
    print("---------------------------")
    print(f"Count: {total}")
    print(f"Min: {min(durations)} seconds")
    print(f"Max: {max(durations)} seconds")
    print(f"Avg: {statistics.mean(durations)} seconds")
    print(f"Median: {statistics.median(durations)} seconds")

    responses = {}
    for request in result:
        response = request['response']
        if response in responses:
            responses[response] += 1
        else:
            responses[response] = 1
    
    print("\nResponse Status Code Statistics")
    print("---------------------------------")

    for response in responses:
        print(f"Response: {response}. Count: {responses[response]}")
    
    if 200 not in responses:
        print(f"Percent of Status 200 responses: 0%")
    else:
        print(f"Percent of Status 200 responses: {responses[200]/total * 100}%")

if __name__ == "__main__":
    main()