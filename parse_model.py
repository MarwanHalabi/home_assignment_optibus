
def find_vehicle_events(vehicles, vehicle_id):  # given vehicle id returns that vehicle events
    for vehicle in vehicles:
        if int(vehicle["vehicle_id"]) == vehicle_id:
            return vehicle["vehicle_events"]


def find_time(event, vehicles, s_or_e: str):  # given event, returns start or end time
    # s_or_e = "start_time" or "end_time"
    my_time = -1
    if event["duty_event_type"] != "vehicle_event":  # if time found in the event
        my_time = event[s_or_e]
    else:
        vehicle_event_sequence = event["vehicle_event_sequence"]
        vehicle_id = int(event["vehicle_id"])
        vehicle_events = find_vehicle_events(vehicles, vehicle_id)

        for vehicle_event in vehicle_events:
            if int(vehicle_event["vehicle_event_sequence"]) == vehicle_event_sequence:
                my_time = vehicle_event[s_or_e]  # if time found in the vehicle event
                break
    return my_time


def duty_duration(data_j, duty_id):  # given duty id, return the start and finish time of this duty
    start_event = data_j["duties"][duty_id - 1]["duty_events"][0]
    end_event = data_j["duties"][duty_id - 1]["duty_events"][-1]

    start_time = find_time(start_event, data_j["vehicles"], "start_time")
    end_time = find_time(end_event, data_j["vehicles"], "end_time")

    return start_time, end_time


# step one main function, return start and end time
def start_end_time(data_j):  # iterate over all duties and get start and finish time
    table = list()
    for duty in data_j["duties"]:
        start, end = duty_duration(data_j, int(duty["duty_id"]))
        table.append([duty["duty_id"], start, end])

    return table


##########################################################################################


def find_trip_stop_id(trips, trip_id, start: bool):  # given trip id, returns stop id
    for trip in trips:
        if int(trip["trip_id"]) == int(trip_id):
            if start:
                return trip["origin_stop_id"]
            else:
                return trip["destination_stop_id"]


def find_stop_name(stops, stop_id):  # given stop id, returns stop name
    for stop in stops:
        if stop["stop_id"] == stop_id:
            return stop["stop_name"]


def service_stops_names(data_j, duty_id):  # given duty id, returns the first and last trip name
    start_service_name = -1
    end_service_name = -1

    duty_events = data_j["duties"][duty_id - 1]["duty_events"]
    duty_len = len(duty_events)
    for i in range(2, duty_len):  # skip first two , pre trip , pullout
        flag = False

        vehicle_id = int(duty_events[i]["vehicle_id"])
        vehicle_event_sequence = duty_events[i]["vehicle_event_sequence"]

        vehicle_events = find_vehicle_events(data_j["vehicles"], vehicle_id)

        for vehicle_event in vehicle_events:
            if int(vehicle_event["vehicle_event_sequence"]) == vehicle_event_sequence:
                if vehicle_event["vehicle_event_type"] == "service_trip":
                    trip_id = vehicle_event["trip_id"]
                    start_service_id = find_trip_stop_id(data_j["trips"], trip_id, True)
                    start_service_name = find_stop_name(data_j["stops"], start_service_id)
                    flag = True

                    break
        if flag:
            break

    for i in reversed(range(2, duty_len - 1)):  # skip last one, (pull in or taxi + more)
        flag = False
        vehicle_id = int(duty_events[i]["vehicle_id"])
        vehicle_event_sequence = duty_events[i]["vehicle_event_sequence"]
        vehicle_events = find_vehicle_events(data_j["vehicles"], vehicle_id)

        for vehicle_event in vehicle_events:
            if int(vehicle_event["vehicle_event_sequence"]) == vehicle_event_sequence:
                if vehicle_event["vehicle_event_type"] == "service_trip":
                    trip_id = vehicle_event["trip_id"]
                    end_service_id = find_trip_stop_id(data_j["trips"], trip_id, False)
                    end_service_name = find_stop_name(data_j["stops"], end_service_id)
                    flag = True
                    break
        if flag:
            break

    return start_service_name, end_service_name


# step two main function, time and stops name
def start_end_time_stop_name(data_j):  # iterate over all duties, get start and finish time and first and last trip name
    table = start_end_time(data_j)

    for idx, duty in enumerate(data_j["duties"]):
        start_stop_name, end_stop_name = service_stops_names(data_j, int(duty["duty_id"]))

        table[idx].extend([start_stop_name, end_stop_name])

    return table


##########################################################################################


def find_trip_time(trips, trip_id):  # given trip id, return times and destination stop id
    for trip in trips:
        if int(trip["trip_id"]) == int(trip_id):
            return [trip["departure_time"], trip["arrival_time"], trip["destination_stop_id"]]


def get_event_start_end(event, data_j):  # given event, return times, destination stop id and vehicle event type
    if event["duty_event_type"] != "vehicle_event":
        return event["start_time"], event["end_time"], event["destination_stop_id"], event["duty_event_type"]
    else:
        vehicle_event_sequence = event["vehicle_event_sequence"]
        vehicle_id = int(event["vehicle_id"])
        vehicle_events = find_vehicle_events(data_j["vehicles"], vehicle_id)

        for vehicle_event in vehicle_events:
            if int(vehicle_event["vehicle_event_sequence"]) == vehicle_event_sequence:
                if vehicle_event["vehicle_event_type"] == "service_trip":
                    trip_id = vehicle_event["trip_id"]
                    l = find_trip_time(data_j["trips"], trip_id)
                    l.append(vehicle_event["vehicle_event_type"])
                    return tuple(l)
                else:
                    return vehicle_event["start_time"], vehicle_event["end_time"], vehicle_event["destination_stop_id"], \
                           vehicle_event["vehicle_event_type"]


def find_events_time(duty, data_j):  # given duty, return all events times
    events_time = list()
    for event in duty["duty_events"]:
        events_time.append(get_event_start_end(event, data_j))
    return events_time


def time_to_mins(time: str):  # helper function, covet time to minutes
    l = [int(i) for i in time.replace(":", ".").split(".")]
    return l[2] + l[1] * 60 + l[0] * 24 * 60


def find_breaks(duty, data_j):  # given duty, return all breaks on duty (skip splits)
    events_time = find_events_time(duty, data_j)

    breaks = list()

    for idx in range(len(events_time) - 1):
        if events_time[idx][1] != events_time[idx + 1][0]:
            durtion = time_to_mins(events_time[idx + 1][0]) - time_to_mins(events_time[idx][1])
            if durtion >= 15 and events_time[idx][3] != "taxi" and events_time[idx][3] != "depot_pull_in":
                # check for split, to skip
                breaks.append([events_time[idx][1][2:], durtion, find_stop_name(data_j["stops"], events_time[idx][2])])

    return breaks


# step three main function, return list of all breaks
def find_all_breaks(data_j):  # iterate over all duties, return list of all breaks (skip splits)
    times = start_end_time_stop_name(data_j)
    all_breaks = list()
    # times.pop(0)
    for duty_id, duty in enumerate(data_j["duties"]):
        duty_times = times[duty_id]
        breaks = find_breaks(duty, data_j)
        for br in breaks:
            all_breaks.append(duty_times + br)

    return all_breaks
