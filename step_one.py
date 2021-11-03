from parse_model import start_end_time
import json


def step_one(data_j):
    times = start_end_time(data_j)
    times.insert(0, ["Duty id", "Start time", "End time"])

    dash = '-' * 32

    for i in range(len(times)):
        if i == 0:
            print(dash)
            print('{:<8s}{:>5s}{:>12s}'.format(times[i][0], times[i][1], times[i][2]))
            print(dash)
        else:
            print('{:<8s}{:>5}{:>12s}'.format(times[i][0], times[i][1][2:], times[i][2][2:]))


if __name__ == "__main__":
    with open("mini_json_dataset.json") as f:
        data = json.load(f)

    step_one(data)


