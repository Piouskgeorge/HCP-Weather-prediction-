from parallel import run_parallel_predictions

if __name__ == "__main__":
    print("Fetching real-time weather and predicting rain probability...")
    results = run_parallel_predictions()
    for r in results:
        print(r)