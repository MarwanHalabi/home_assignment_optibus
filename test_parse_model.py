import unittest
import parse_model
import mock_data


class TestQues(unittest.TestCase):
    def test_find_vehicle_events(self):
        self.assertEqual(parse_model.find_vehicle_events(mock_data.data["vehicles"], 1),mock_data.data["vehicles"][0]["vehicle_events"])
        self.assertEqual(parse_model.find_vehicle_events(mock_data.data["vehicles"], 2),mock_data.data["vehicles"][1]["vehicle_events"])
        self.assertRaises(IndexError, parse_model.find_vehicle_events(mock_data.data["vehicles"], 3))

    def test_find_time(self):
        self.assertEqual(parse_model.find_time(mock_data.data["duties"][0]["duty_events"][0],mock_data.data["vehicles"], "start_time"), "0.03:25")
        self.assertEqual(parse_model.find_time(mock_data.data["duties"][1]["duty_events"][-1],mock_data.data["vehicles"], "end_time"), "0.23:21")
        self.assertEqual(parse_model.find_time(mock_data.data["duties"][2]["duty_events"][0], mock_data.data["vehicles"],"end_time"), "0.15:16")
        self.assertEqual(parse_model.find_time(mock_data.data["duties"][2]["duty_events"][0], mock_data.data["vehicles"],"start_time"), "0.15:06")

    def test_duty_duration(self):
        self.assertEqual(parse_model.duty_duration(mock_data.data, 1), ("0.03:25", "0.11:39"))

    def test_find_trip_stop_id(self):
        self.assertEqual(parse_model.find_trip_stop_id(mock_data.data["trips"], 5306803, True), "EMS")
        self.assertEqual(parse_model.find_trip_stop_id(mock_data.data["trips"], 5306803, False), "MTC")
        self.assertEqual(parse_model.find_trip_stop_id(mock_data.data["trips"], 5306842, True), "RiVa")
        self.assertEqual(parse_model.find_trip_stop_id(mock_data.data["trips"], 5306842, False), "PTC")

    def test_find_stop_name(self):
        self.assertEqual(parse_model.find_stop_name(mock_data.data["stops"], "9thHo"), "Hope and 9th")
        self.assertEqual(parse_model.find_stop_name(mock_data.data["stops"], "BMTC"), "Brea Mall Transit Center")

    def test_service_stops_names(self):
        self.assertEqual(parse_model.service_stops_names(mock_data.data, 1), ("Montclair Transit Center", "El Monte Station"))

    def test_find_trip_time(self):
        self.assertEqual(parse_model.find_trip_time(mock_data.data["trips"], "5301688"), ["0.04:00","0.05:12","9thHo"])

    def test_get_event_start_end(self):
        self.assertEqual(parse_model.get_event_start_end(mock_data.data["duties"][2]["duty_events"][0],mock_data.data), ("0.15:06","0.15:16","PTCLO","taxi"))
        self.assertEqual(parse_model.get_event_start_end(mock_data.data["duties"][1]["duty_events"][20], mock_data.data),("0.16:30", "0.17:28", "EMS", "service_trip"))
        self.assertEqual(parse_model.get_event_start_end(mock_data.data["duties"][1]["duty_events"][21], mock_data.data),("0.23:06", "0.23:21", "Pomona", "depot_pull_in"))


if __name__ == "__main__":
    unittest.main()
