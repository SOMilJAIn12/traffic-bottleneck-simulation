import random
from config import TIME_STEPS, ARRIVAL_PROB, PASS_PROB

def simulate(strategy):
    left_lane = []
    right_lane = []

    waiting_time = 0
    passed_cars = 0

    for t in range(TIME_STEPS):

        if random.random() < ARRIVAL_PROB:
            left_lane.append(t)

        if random.random() < ARRIVAL_PROB:
            right_lane.append(t)

        if strategy == "chaos":
            if left_lane and right_lane:
                lane = random.choice(["L", "R"])
            elif left_lane:
                lane = "L"
            elif right_lane:
                lane = "R"
            else:
                lane = None

        elif strategy == "zipper":
            if t % 2 == 0 and left_lane:
                lane = "L"
            elif right_lane:
                lane = "R"
            else:
                lane = "L" if left_lane else None

        elif strategy == "signal":
            if (t // 5) % 2 == 0:
                lane = "L" if left_lane else None
            else:
                lane = "R" if right_lane else None

        elif strategy == "smart":
            if len(left_lane) > len(right_lane) + 2:
                lane = "L"
            elif len(right_lane) > len(left_lane) + 2:
                lane = "R"
            else:
                lane = random.choice(["L", "R"])
        else:
            lane = None

        if random.random() < PASS_PROB:

            if lane == "L" and left_lane:
                arrival_time = left_lane.pop(0)
                waiting_time += (t - arrival_time)
                passed_cars += 1

            elif lane == "R" and right_lane:
                arrival_time = right_lane.pop(0)
                waiting_time += (t - arrival_time)
                passed_cars += 1

    avg_wait = waiting_time / passed_cars if passed_cars > 0 else 0
    return avg_wait, passed_cars