#  mock data set for testing only

data = {"vehicles": [
    {
        "vehicle_id": "1",
        "vehicle_events": [
            {
                "vehicle_event_sequence": "0",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.03:15",
                "end_time": "0.03:35",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "1",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.03:35",
                "end_time": "0.04:10",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "CiGL",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "2",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301431",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "3",
                "vehicle_event_type": "deadhead",
                "start_time": "0.05:22",
                "end_time": "0.05:24",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "4",
                "vehicle_event_type": "deadhead",
                "start_time": "0.05:43",
                "end_time": "0.05:45",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "5",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301533",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "6",
                "vehicle_event_type": "deadhead",
                "start_time": "0.07:04",
                "end_time": "0.07:09",
                "origin_stop_id": "CiGL",
                "destination_stop_id": "GrPR",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "7",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302243",
                "sub_trip_index": "1",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "8",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302243",
                "sub_trip_index": "2",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "9",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.08:55",
                "end_time": "0.09:50",
                "origin_stop_id": "9thHo",
                "destination_stop_id": "Pomona",
                "duty_id": "110"
            },
            {
                "vehicle_event_sequence": "10",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.12:00",
                "end_time": "0.12:20",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "11",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.12:20",
                "end_time": "0.12:30",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "PTC",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "12",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301891",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "13",
                "vehicle_event_type": "deadhead",
                "start_time": "0.13:41",
                "end_time": "0.13:45",
                "origin_stop_id": "PHM",
                "destination_stop_id": "PHMLO",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "14",
                "vehicle_event_type": "deadhead",
                "start_time": "0.14:14",
                "end_time": "0.14:15",
                "origin_stop_id": "PHMLO",
                "destination_stop_id": "PHM",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "15",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301813",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "16",
                "vehicle_event_type": "deadhead",
                "start_time": "0.15:26",
                "end_time": "0.15:37",
                "origin_stop_id": "PTC",
                "destination_stop_id": "VaLO",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "17",
                "vehicle_event_type": "deadhead",
                "start_time": "0.16:23",
                "end_time": "0.16:25",
                "origin_stop_id": "VaLO",
                "destination_stop_id": "TeSC",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "18",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302034",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "19",
                "vehicle_event_type": "deadhead",
                "start_time": "0.17:15",
                "end_time": "0.17:19",
                "origin_stop_id": "PHM",
                "destination_stop_id": "PHMLO",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "20",
                "vehicle_event_type": "deadhead",
                "start_time": "0.17:24",
                "end_time": "0.17:25",
                "origin_stop_id": "PHMLO",
                "destination_stop_id": "PHM",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "21",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301826",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "22",
                "vehicle_event_type": "deadhead",
                "start_time": "0.18:13",
                "end_time": "0.18:17",
                "origin_stop_id": "TeSC",
                "destination_stop_id": "VaLO",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "23",
                "vehicle_event_type": "deadhead",
                "start_time": "0.18:33",
                "end_time": "0.18:35",
                "origin_stop_id": "VaLO",
                "destination_stop_id": "TeSC",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "24",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302043",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "25",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:38",
                "end_time": "0.19:40",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "26",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:48",
                "end_time": "0.19:50",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "27",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301614",
                "duty_id": "144"
            },
            {
                "vehicle_event_sequence": "28",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.20:49",
                "end_time": "0.21:04",
                "origin_stop_id": "TeSC",
                "destination_stop_id": "Pomona",
                "duty_id": "144"
            }
        ]
    },
    {
        "vehicle_id": "2",
        "vehicle_events": [
            {
                "vehicle_event_sequence": "0",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.03:25",
                "end_time": "0.03:45",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "1",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.03:45",
                "end_time": "0.04:00",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "MTC",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "2",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301688",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "3",
                "vehicle_event_type": "deadhead",
                "start_time": "0.05:12",
                "end_time": "0.05:47",
                "origin_stop_id": "9thHo",
                "destination_stop_id": "EMSLO",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "4",
                "vehicle_event_type": "deadhead",
                "start_time": "0.05:58",
                "end_time": "0.06:00",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "5",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301535",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "6",
                "vehicle_event_type": "deadhead",
                "start_time": "0.07:37",
                "end_time": "0.07:39",
                "origin_stop_id": "MTC",
                "destination_stop_id": "MTCLO",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "7",
                "vehicle_event_type": "deadhead",
                "start_time": "0.07:58",
                "end_time": "0.08:00",
                "origin_stop_id": "MTCLO",
                "destination_stop_id": "MTC",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "8",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301731",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "9",
                "vehicle_event_type": "deadhead",
                "start_time": "0.08:50",
                "end_time": "0.08:52",
                "origin_stop_id": "PTC",
                "destination_stop_id": "PTCLO",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "10",
                "vehicle_event_type": "deadhead",
                "start_time": "0.09:28",
                "end_time": "0.09:30",
                "origin_stop_id": "PTCLO",
                "destination_stop_id": "PTC",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "11",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302166",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "12",
                "vehicle_event_type": "service_trip",
                "trip_id": "5306894",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "13",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.11:29",
                "end_time": "0.11:39",
                "origin_stop_id": "PTC",
                "destination_stop_id": "Pomona",
                "duty_id": "1"
            },
            {
                "vehicle_event_sequence": "14",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.12:35",
                "end_time": "0.12:55",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "15",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.12:55",
                "end_time": "0.14:05",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Fi9t",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "16",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301626",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "17",
                "vehicle_event_type": "deadhead",
                "start_time": "0.15:29",
                "end_time": "0.15:46",
                "origin_stop_id": "MTC",
                "destination_stop_id": "PTCLO",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "18",
                "vehicle_event_type": "deadhead",
                "start_time": "0.15:58",
                "end_time": "0.16:00",
                "origin_stop_id": "PTCLO",
                "destination_stop_id": "PTC",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "19",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301916",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "20",
                "vehicle_event_type": "deadhead",
                "start_time": "0.16:55",
                "end_time": "0.16:57",
                "origin_stop_id": "MTC",
                "destination_stop_id": "MTCLO",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "21",
                "vehicle_event_type": "deadhead",
                "start_time": "0.17:33",
                "end_time": "0.17:35",
                "origin_stop_id": "MTCLO",
                "destination_stop_id": "MTC",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "22",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301766",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "23",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:18",
                "end_time": "0.19:20",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "24",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:28",
                "end_time": "0.19:30",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "25",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301612",
                "duty_id": "106"
            },
            {
                "vehicle_event_sequence": "26",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.21:06",
                "end_time": "0.21:21",
                "origin_stop_id": "MTC",
                "destination_stop_id": "Pomona",
                "duty_id": "106"
            }
        ]
    },
    {
        "vehicle_id": "59",
        "vehicle_events": [
            {
                "vehicle_event_sequence": "0",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.05:22",
                "end_time": "0.05:42",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "1",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.05:42",
                "end_time": "0.05:57",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "TeSC",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "2",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301988",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "3",
                "vehicle_event_type": "deadhead",
                "start_time": "0.06:57",
                "end_time": "0.06:59",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "4",
                "vehicle_event_type": "deadhead",
                "start_time": "0.07:10",
                "end_time": "0.07:12",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "5",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301547",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "6",
                "vehicle_event_type": "deadhead",
                "start_time": "0.08:16",
                "end_time": "0.08:20",
                "origin_stop_id": "TeSC",
                "destination_stop_id": "VaLO",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "7",
                "vehicle_event_type": "deadhead",
                "start_time": "0.08:31",
                "end_time": "0.08:33",
                "origin_stop_id": "VaLO",
                "destination_stop_id": "TeSC",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "8",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302003",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "9",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.09:37",
                "end_time": "0.10:17",
                "origin_stop_id": "EMS",
                "destination_stop_id": "Pomona",
                "duty_id": "137"
            },
            {
                "vehicle_event_sequence": "10",
                "vehicle_event_type": "pre_trip",
                "start_time": "0.13:00",
                "end_time": "0.13:20",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "Pomona",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "11",
                "vehicle_event_type": "depot_pull_out",
                "start_time": "0.13:20",
                "end_time": "0.13:30",
                "origin_stop_id": "Pomona",
                "destination_stop_id": "PTC",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "12",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301897",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "13",
                "vehicle_event_type": "deadhead",
                "start_time": "0.14:25",
                "end_time": "0.14:27",
                "origin_stop_id": "MTC",
                "destination_stop_id": "MTCLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "14",
                "vehicle_event_type": "deadhead",
                "start_time": "0.14:33",
                "end_time": "0.14:35",
                "origin_stop_id": "MTCLO",
                "destination_stop_id": "MTC",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "15",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301755",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "16",
                "vehicle_event_type": "deadhead",
                "start_time": "0.16:13",
                "end_time": "0.16:15",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "17",
                "vehicle_event_type": "deadhead",
                "start_time": "0.16:28",
                "end_time": "0.16:30",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "18",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301590",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "19",
                "vehicle_event_type": "deadhead",
                "start_time": "0.18:20",
                "end_time": "0.18:22",
                "origin_stop_id": "MTC",
                "destination_stop_id": "MTCLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "20",
                "vehicle_event_type": "deadhead",
                "start_time": "0.18:58",
                "end_time": "0.19:00",
                "origin_stop_id": "MTCLO",
                "destination_stop_id": "MTC",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "21",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301770",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "22",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:50",
                "end_time": "0.19:52",
                "origin_stop_id": "PTC",
                "destination_stop_id": "PTCLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "23",
                "vehicle_event_type": "deadhead",
                "start_time": "0.19:58",
                "end_time": "0.20:00",
                "origin_stop_id": "PTCLO",
                "destination_stop_id": "PTC",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "24",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301936",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "25",
                "vehicle_event_type": "deadhead",
                "start_time": "0.21:04",
                "end_time": "0.21:08",
                "origin_stop_id": "PHM",
                "destination_stop_id": "PHMLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "26",
                "vehicle_event_type": "deadhead",
                "start_time": "0.21:19",
                "end_time": "0.21:20",
                "origin_stop_id": "PHMLO",
                "destination_stop_id": "PHM",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "27",
                "vehicle_event_type": "service_trip",
                "trip_id": "5302147",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "28",
                "vehicle_event_type": "deadhead",
                "start_time": "0.21:58",
                "end_time": "0.22:00",
                "origin_stop_id": "EMS",
                "destination_stop_id": "EMSLO",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "29",
                "vehicle_event_type": "deadhead",
                "start_time": "0.22:08",
                "end_time": "0.22:10",
                "origin_stop_id": "EMSLO",
                "destination_stop_id": "EMS",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "30",
                "vehicle_event_type": "service_trip",
                "trip_id": "5301625",
                "duty_id": "2"
            },
            {
                "vehicle_event_sequence": "31",
                "vehicle_event_type": "depot_pull_in",
                "start_time": "0.23:06",
                "end_time": "0.23:21",
                "origin_stop_id": "TeSC",
                "destination_stop_id": "Pomona",
                "duty_id": "2"
            }
        ]
    }
]
    , "duties": [
        {
            "duty_id": "1",
            "duty_events": [
                {
                    "duty_event_sequence": "0",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 0,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "1",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 1,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "2",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 2,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "3",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 3,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "4",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 4,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "5",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 5,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "6",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 6,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "7",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 7,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "8",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 8,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "9",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 9,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "10",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 10,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "11",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 11,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "12",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 12,
                    "vehicle_id": "2"
                },
                {
                    "duty_event_sequence": "13",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 13,
                    "vehicle_id": "2"
                },
            ]
        },

        {
            "duty_id": "2",
            "duty_events": [
                {
                    "duty_event_sequence": "0",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 10,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "1",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 11,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "2",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 12,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "3",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 13,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "4",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 14,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "5",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 15,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "6",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 16,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "7",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 17,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "8",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 18,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "9",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 19,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "10",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 20,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "11",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 21,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "12",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 22,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "13",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 23,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "14",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 24,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "15",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 25,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "16",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 26,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "17",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 27,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "18",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 28,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "19",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 29,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "20",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 30,
                    "vehicle_id": "59"
                },
                {
                    "duty_event_sequence": "21",
                    "duty_event_type": "vehicle_event",
                    "vehicle_event_sequence": 31,
                    "vehicle_id": "59"
                }],
        },
        {
            "duty_id": "3",
            "duty_events": [
                {
                    "duty_event_sequence": "-1",  # TEST ONLY
                    "duty_event_type": "taxi",
                    "start_time": "0.15:06",
                    "end_time": "0.15:16",
                    "origin_stop_id": "Pomona",
                    "destination_stop_id": "PTCLO"
                }],

        }
    ],
    "trips": [
        {
            "trip_id": "5301688",
            "route_number": "699",
            "origin_stop_id": "MTC",
            "destination_stop_id": "9thHo",
            "departure_time": "0.04:00",
            "arrival_time": "0.05:12"
        },
        {
            "trip_id": "5301431",
            "route_number": "492",
            "origin_stop_id": "EMS",
            "destination_stop_id": "MTC",
            "departure_time": "0.07:45",
            "arrival_time": "0.09:10"
        },
        {
            "trip_id": "5301533",
            "route_number": "197",
            "origin_stop_id": "PTC",
            "destination_stop_id": "MTC",
            "departure_time": "0.08:03",
            "arrival_time": "0.08:56"
        },
        {
            "trip_id": "5302243",
            "route_number": "197",
            "origin_stop_id": "PTC",
            "destination_stop_id": "MTC",
            "departure_time": "0.07:03",
            "arrival_time": "0.07:54"
        },
        {
            "trip_id": "5306797",
            "route_number": "492",
            "origin_stop_id": "EMS",
            "destination_stop_id": "MTC",
            "departure_time": "0.06:45",
            "arrival_time": "0.08:08"
        },
        {
            "trip_id": "5306803",
            "route_number": "492",
            "origin_stop_id": "EMS",
            "destination_stop_id": "MTC",
            "departure_time": "0.07:15",
            "arrival_time": "0.08:40"
        },
        {
            "trip_id": "5306841",
            "route_number": "195",
            "origin_stop_id": "RiVa",
            "destination_stop_id": "PTC",
            "departure_time": "0.07:14",
            "arrival_time": "0.07:50"
        },
        {
            "trip_id": "5306908",
            "route_number": "486",
            "origin_stop_id": "TeSC",
            "destination_stop_id": "EMS",
            "departure_time": "0.06:00",
            "arrival_time": "0.06:53"
        },
        {
            "trip_id": "5306821",
            "route_number": "197",
            "origin_stop_id": "PTC",
            "destination_stop_id": "MTC",
            "departure_time": "0.11:03",
            "arrival_time": "0.12:00"
        },
        {
            "trip_id": "5306847",
            "route_number": "195",
            "origin_stop_id": "RiVa",
            "destination_stop_id": "PTC",
            "departure_time": "0.06:14",
            "arrival_time": "0.06:50"
        },
        {
            "trip_id": "5306842",
            "route_number": "195",
            "origin_stop_id": "RiVa",
            "destination_stop_id": "PTC",
            "departure_time": "0.08:14",
            "arrival_time": "0.08:52"
        },
        {
            "trip_id": "5306855",
            "route_number": "197",
            "origin_stop_id": "PTC",
            "destination_stop_id": "MTC",
            "departure_time": "0.13:03",
            "arrival_time": "0.13:57"
        },
        {
            "trip_id": "5306794",
            "route_number": "492",
            "origin_stop_id": "MTC",
            "destination_stop_id": "EMS",
            "departure_time": "0.07:35",
            "arrival_time": "0.08:57"
        },
        {
            "trip_id": "5306894",
            "route_number": "486",
            "origin_stop_id": "TeSC",
            "destination_stop_id": "EMS",
            "departure_time": "0.16:30",
            "arrival_time": "0.17:28"
        },
        {
            "trip_id": "5301625",
            "route_number": "486",
            "origin_stop_id": "TeSC",
            "destination_stop_id": "EMS",
            "departure_time": "0.16:30",
            "arrival_time": "0.17:28"
        }
    ],
    "stops": [
        {
            "stop_id": "1sSp",
            "stop_name": "1st and Spring",
            "latitude": 34.053788,
            "longitude": -118.243691,
            "is_depot": False
        },
        {
            "stop_id": "9thHo",
            "stop_name": "Hope and 9th",
            "latitude": 34.045356,
            "longitude": -118.260212,
            "is_depot": False
        },
        {
            "stop_id": "ArAz",
            "stop_name": "Azusa and Arrow",
            "latitude": 34.106779,
            "longitude": -117.907678,
            "is_depot": False
        },
        {
            "stop_id": "ArGr",
            "stop_name": "Arrow Hwy and Grand Ave",
            "latitude": 34.106058,
            "longitude": -117.872705,
            "is_depot": False
        },
        {
            "stop_id": "ArIr",
            "stop_name": "Arrow Hwy and Irwindale Ave",
            "latitude": 34.106926,
            "longitude": -117.934151,
            "is_depot": False
        },
        {
            "stop_id": "ArTo",
            "stop_name": "Arrow Hwy and Towne Ave",
            "latitude": 34.09006,
            "longitude": -117.736813,
            "is_depot": False
        },
        {
            "stop_id": "AzAm",
            "stop_name": "Azusa and Amar",
            "latitude": 34.031248,
            "longitude": -117.914755,
            "is_depot": False
        },
        {
            "stop_id": "BaInH",
            "stop_name": "Baseline Rd and Indian Hill Blvd",
            "latitude": 34.121384,
            "longitude": -117.720373,
            "is_depot": False
        },
        {
            "stop_id": "BeLH",
            "stop_name": "Beach and La Habra",
            "latitude": 33.932593,
            "longitude": -117.967716,
            "is_depot": False
        },
        {
            "stop_id": "BMTC",
            "stop_name": "Brea Mall Transit Center",
            "latitude": 33.915642,
            "longitude": -117.883578,
            "is_depot": False
        },
        {
            "stop_id": "BoGa",
            "stop_name": "Garey and Bonita",
            "latitude": 34.096309,
            "longitude": -117.748688,
            "is_depot": False
        },
        {
            "stop_id": "BoSD",
            "stop_name": "San Dimas and Bonita",
            "latitude": 34.106625,
            "longitude": -117.807118,
            "is_depot": False
        },
        {
            "stop_id": "CiCLO",
            "stop_name": "CiCo Layover",
            "latitude": 34.125899,
            "longitude": -117.872452,
            "is_depot": False
        },
        {
            "stop_id": "CiGL",
            "stop_name": "Citrus Gold Line Station",
            "latitude": 34.135898,
            "longitude": -117.88926,
            "is_depot": False
        },
        {
            "stop_id": "CoNo",
            "stop_name": "Colima and Nogales",
            "latitude": 33.987416,
            "longitude": -117.889175,
            "is_depot": False
        },
        {
            "stop_id": "CoTC",
            "stop_name": "Covina Transit Center",
            "latitude": 34.100118,
            "longitude": -117.890203,
            "is_depot": False
        },
        {
            "stop_id": "CSLA",
            "stop_name": "Cal State LA",
            "latitude": 34.062495,
            "longitude": -118.167996,
            "is_depot": False
        },
        {
            "stop_id": "CTC",
            "stop_name": "Claremont Transit Center",
            "latitude": 34.094642,
            "longitude": -117.711141,
            "is_depot": False
        },
        {
            "stop_id": "DBBC",
            "stop_name": "Diamond Bar and Brea Canyon",
            "latitude": 33.967992,
            "longitude": -117.847468,
            "is_depot": False
        },
        {
            "stop_id": "DBCH",
            "stop_name": "Diamond Bar City Hall",
            "latitude": 33.998385,
            "longitude": -117.833935,
            "is_depot": False
        },
        {
            "stop_id": "DBGr",
            "stop_name": "Diamond Bar and Grand",
            "latitude": 33.9992,
            "longitude": -117.812278,
            "is_depot": False
        },
        {
            "stop_id": "DBTe",
            "stop_name": "Diamond Bar and Temple",
            "latitude": 34.040346,
            "longitude": -117.798543,
            "is_depot": False
        },
        {
            "stop_id": "DuDs",
            "stop_name": "Durward and D St",
            "latitude": 34.111055,
            "longitude": -117.764052,
            "is_depot": False
        },
        {
            "stop_id": "EMS",
            "stop_name": "El Monte Station",
            "latitude": 34.072106,
            "longitude": -118.044699,
            "is_depot": False
        },
        {
            "stop_id": "EMSLO",
            "stop_name": "EMS Layover",
            "latitude": 34.07104,
            "longitude": -118.04341,
            "is_depot": False
        },
        {
            "stop_id": "ETC",
            "stop_name": "Eastland Center",
            "latitude": 34.075298,
            "longitude": -117.886681,
            "is_depot": False
        },
        {
            "stop_id": "FaOG",
            "stop_name": "Fairplex and Orage Grove",
            "latitude": 34.062863,
            "longitude": -117.786629,
            "is_depot": False
        },
        {
            "stop_id": "Fi9t",
            "stop_name": "Figueroa and 9th",
            "latitude": 34.046546,
            "longitude": -118.262397,
            "is_depot": False
        },
        {
            "stop_id": "FoTo",
            "stop_name": "Towne and Foothill",
            "latitude": 34.106989,
            "longitude": -117.73673,
            "is_depot": False
        },
        {
            "stop_id": "FPR",
            "stop_name": "Fairplex Park and Ride",
            "latitude": 34.073271,
            "longitude": -117.785889,
            "is_depot": False
        },
        {
            "stop_id": "FTDt1",
            "stop_name": "Foothill Transit Downtown",
            "latitude": 34.03447,
            "longitude": -118.265964,
            "is_depot": False
        },
        {
            "stop_id": "GaHa",
            "stop_name": "Gale and Hacienda",
            "latitude": 34.010919,
            "longitude": -117.963006,
            "is_depot": False
        },
        {
            "stop_id": "GaPh",
            "stop_name": "Garey Ave and Philadelphia St",
            "latitude": 34.033285,
            "longitude": -117.749197,
            "is_depot": False
        },
        {
            "stop_id": "GaRR",
            "stop_name": "Garey Ave and Rio Rancho Rd",
            "latitude": 34.033233,
            "longitude": -117.749343,
            "is_depot": False
        },
        {
            "stop_id": "GaVa",
            "stop_name": "Garvey and Valley",
            "latitude": 34.062784,
            "longitude": -118.01902,
            "is_depot": False
        },
        {
            "stop_id": "GrAr",
            "stop_name": "Grand and Arrow",
            "latitude": 34.106099,
            "longitude": -117.872487,
            "is_depot": False
        },
        {
            "stop_id": "GrPR",
            "stop_name": "Grand Ave Park and Ride",
            "latitude": 34.121428,
            "longitude": -117.874155,
            "is_depot": False
        },
        {
            "stop_id": "GrTe",
            "stop_name": "Grand and Temple",
            "latitude": 34.042984,
            "longitude": -117.847658,
            "is_depot": False
        },
        {
            "stop_id": "GSDB",
            "stop_name": "Golden Springs and Diamond Bar",
            "latitude": 34.01908,
            "longitude": -117.808428,
            "is_depot": False
        },
        {
            "stop_id": "HaAm",
            "stop_name": "Hacienda and Amar",
            "latitude": 34.037055,
            "longitude": -117.949842,
            "is_depot": False
        },
        {
            "stop_id": "HaCo",
            "stop_name": "Hacienda and Colima",
            "latitude": 33.981306,
            "longitude": -117.973113,
            "is_depot": False
        },
        {
            "stop_id": "HoTo",
            "stop_name": "Holt and Towne",
            "latitude": 34.062624,
            "longitude": -117.741598,
            "is_depot": False
        },
        {
            "stop_id": "IHFo",
            "stop_name": "Foothill and Indian Hill",
            "latitude": 34.106988,
            "longitude": -117.720365,
            "is_depot": False
        },
        {
            "stop_id": "IMPR",
            "stop_name": "Industry Park & Ride",
            "latitude": 34.009596,
            "longitude": -117.846115,
            "is_depot": False
        },
        {
            "stop_id": "MiRe",
            "stop_name": "Mission Blvd and Resevoir St",
            "latitude": 34.05548,
            "longitude": -117.732571,
            "is_depot": False
        },
        {
            "stop_id": "MiTe",
            "stop_name": "Mission Blvd and Temple Ave",
            "latitude": 34.040324,
            "longitude": -117.79853,
            "is_depot": False
        },
        {
            "stop_id": "MoHa",
            "stop_name": "Mountain and Harrison",
            "latitude": 34.099504,
            "longitude": -117.729087,
            "is_depot": False
        },
        {
            "stop_id": "MTC",
            "stop_name": "Montclair Transit Center",
            "latitude": 34.094181,
            "longitude": -117.695705,
            "is_depot": False
        },
        {
            "stop_id": "MTCLO",
            "stop_name": "MTC Layover",
            "latitude": 34.095742,
            "longitude": -117.694219,
            "is_depot": False
        },
        {
            "stop_id": "NoLP",
            "stop_name": "La Puente and Nogales",
            "latitude": 34.010174,
            "longitude": -117.886832,
            "is_depot": False
        },
        {
            "stop_id": "PeLO",
            "stop_name": "Peck and Live Oak",
            "latitude": 34.111063,
            "longitude": -118.00427,
            "is_depot": False
        },
        {
            "stop_id": "PHM",
            "stop_name": "Puente Hills Mall",
            "latitude": 33.994326,
            "longitude": -117.929064,
            "is_depot": False
        },
        {
            "stop_id": "PHMLO",
            "stop_name": "Puente Hills Mall Layover",
            "latitude": 33.992866,
            "longitude": -117.928945,
            "is_depot": False
        },
        {
            "stop_id": "Pomona",
            "stop_name": "Pomona Yard",
            "latitude": 34.057907,
            "longitude": -117.723094,
            "is_depot": True
        },
        {
            "stop_id": "PTC",
            "stop_name": "Pomona Transit Center",
            "latitude": 34.059384,
            "longitude": -117.752374,
            "is_depot": False
        },
        {
            "stop_id": "PTCLO",
            "stop_name": "PTC Layover",
            "latitude": 34.059615,
            "longitude": -117.753187,
            "is_depot": False
        },
        {
            "stop_id": "PuAm",
            "stop_name": "Puente and Amar",
            "latitude": 34.05451,
            "longitude": -117.978213,
            "is_depot": False
        },
        {
            "stop_id": "RaCo",
            "stop_name": "Ramona Ave and Cogswell Rd",
            "latitude": 34.075274,
            "longitude": -118.012749,
            "is_depot": False
        },
        {
            "stop_id": "RiVa",
            "stop_name": "Ridgeway and Valley",
            "latitude": 34.061208,
            "longitude": -117.795564,
            "is_depot": False
        },
        {
            "stop_id": "RoAz",
            "stop_name": "Azusa and Rowland",
            "latitude": 34.07907,
            "longitude": -117.907652,
            "is_depot": False
        },
        {
            "stop_id": "SALO",
            "stop_name": "Live Oak and Santa Anita",
            "latitude": 34.107338,
            "longitude": -118.030391,
            "is_depot": False
        },
        {
            "stop_id": "SASB",
            "stop_name": "San Antonio and San Bernardino",
            "latitude": 34.076276,
            "longitude": -117.736728,
            "is_depot": False
        },
        {
            "stop_id": "SDPR",
            "stop_name": "San Dimas Park and Ride",
            "latitude": 34.105278,
            "longitude": -117.808617,
            "is_depot": False
        },
        {
            "stop_id": "Sp1s",
            "stop_name": "Spring and 1st",
            "latitude": 34.054905,
            "longitude": -118.242648,
            "is_depot": False
        },
        {
            "stop_id": "TeSC",
            "stop_name": "Temple Ave and S. Campus Dr",
            "latitude": 34.050237,
            "longitude": -117.816445,
            "is_depot": False
        },
        {
            "stop_id": "ToMa",
            "stop_name": "Towne and Marketplace",
            "latitude": 34.023181,
            "longitude": -117.740301,
            "is_depot": False
        },
        {
            "stop_id": "UnSt",
            "stop_name": "Union Station",
            "latitude": 34.054302,
            "longitude": -118.236615,
            "is_depot": False
        },
        {
            "stop_id": "USC",
            "stop_name": "USC Medical Center",
            "latitude": 34.055392,
            "longitude": -118.210398,
            "is_depot": False
        },
        {
            "stop_id": "VaHw",
            "stop_name": "Valley Blvd and Humane Way",
            "latitude": 34.061277,
            "longitude": -117.792507,
            "is_depot": False
        },
        {
            "stop_id": "VaLO",
            "stop_name": "Valley and Temple Layover",
            "latitude": 34.048625,
            "longitude": -117.812335,
            "is_depot": False
        },
        {
            "stop_id": "VaPu",
            "stop_name": "Valley and Puente",
            "latitude": 34.044451,
            "longitude": -117.988571,
            "is_depot": False
        },
        {
            "stop_id": "ViGl",
            "stop_name": "Vincent and Glendora",
            "latitude": 34.065693,
            "longitude": -117.927607,
            "is_depot": False
        },
        {
            "stop_id": "VVPR",
            "stop_name": "Via Verde Park and Ride",
            "latitude": 34.070034,
            "longitude": -117.836808,
            "is_depot": False
        },
        {
            "stop_id": "WhCo",
            "stop_name": "Whittier and Colima",
            "latitude": 33.948832,
            "longitude": -118.006415,
            "is_depot": False
        },
        {
            "stop_id": "WhMcK",
            "stop_name": "White Ave and McKinley Ave",
            "latitude": 34.078531,
            "longitude": -117.759791,
            "is_depot": False
        },
        {
            "stop_id": "WhOG",
            "stop_name": "White Ave and Orange Grove",
            "latitude": 34.06966,
            "longitude": -117.759351,
            "is_depot": False
        }
    ]
}
