from utils import simulate

def run_multiple(strategy, runs=5):
    avg_waits = []
    throughputs = []

    for _ in range(runs):
        w, t = simulate(strategy)
        avg_waits.append(w)
        throughputs.append(t)

    return sum(avg_waits)/runs, sum(throughputs)/runs


def compute_results(strategies):
    results = {}
    for s in strategies:
        results[s] = run_multiple(s)
    return results


def compute_improvement(results):
    base = results["chaos"][0]
    improvements = {}

    for s in results:
        improvement = ((base - results[s][0]) / base) * 100
        improvements[s] = improvement

    return improvements