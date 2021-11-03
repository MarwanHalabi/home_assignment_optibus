from parse_model import find_all_breaks
import json


def step_three(data_j):
    all_breaks = find_all_breaks(data_j)
    all_breaks.insert(0, ["Duty id", "Start time", "End time","Start stop description", "End stop description","Break start time", "Break duration", "Break stop name"])

    dash = '-' * 155

    for i in range(len(all_breaks)):
        if i == 0:
            print(dash)
            print('{:<8s}{:<12s}{:<12s}{:<30s}{:<30s}{:<20s}{:<18s}{:<30s}'.format(all_breaks[i][0], all_breaks[i][1], all_breaks[i][2], all_breaks[i][3],
                                                              all_breaks[i][4], all_breaks[i][5], all_breaks[i][6], all_breaks[i][7]))
            print(dash)
        else:
            print('{:<8s}{:<12}{:<12s}{:<30s}{:<30s}{:<20s}{:<18d}{:<30s}'.format(all_breaks[i][0], all_breaks[i][1][2:], all_breaks[i][2][2:], all_breaks[i][3],
                                                             all_breaks[i][4], all_breaks[i][5], all_breaks[i][6], all_breaks[i][7]))


if __name__ == "__main__":
    with open("mini_json_dataset.json") as f:
        data = json.load(f)

    step_three(data)