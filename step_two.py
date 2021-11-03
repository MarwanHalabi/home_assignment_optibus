from parse_model import start_end_time_stop_name
import json


def step_two(data_j):
    times = start_end_time_stop_name(data_j)
    times.insert(0, ["Duty id", "Start time", "End time", "Start stop description", "End stop description"])

    dash = '-' * 85

    for i in range(len(times)):
        if i == 0:
            print(dash)
            print('{:<8s}{:<12s}{:<12s}{:<30s}{:<30s}'.format(times[i][0], times[i][1], times[i][2], times[i][3],
                                                              times[i][4]))
            print(dash)
        else:
            print('{:<8s}{:<12}{:<12s}{:<30s}{:<30s}'.format(times[i][0], times[i][1][2:], times[i][2][2:], times[i][3],
                                                             times[i][4]))


if __name__ == "__main__":
    with open("mini_json_dataset.json") as f:
        data = json.load(f)

    step_two(data)
