# optibus interview
home assignment

## Step 1 – Start and End Time
Every duty has a start time and an end time - the client would like a report that includes the
start time and the end time per Duty ID.
- Your job is to print that report, with the following columns: Duty ID, Start time, and End time.

## Step 2 – Start and End Stop Name
- Extend the previous report and add the following columns: first service trip start stop and the
last service trip end stop.


## Step 3 – Breaks
As we mentioned before, breaks are very important for companies, and clients want to know
all the breaks that are longer than 15 minutes per duty, how long it lasted, when it started, and
at what stop it was.
- Note: a single duty can have more than one break, i.e. duty can have more than 1 line per
duty
- Modify the previous report and add the following columns: Break duration (in minutes), Break
start time, and Break stop name.

# files description
- parse_model: model that includes all the parsing function created and needed
- step_one: using the "parse_model" print step one
- step_two: using the "parse_model" print step two
- step_three: using the "parse_model" print step three
- test_parse_model: testings for parse_model functions
- mock_data: data file for test purposes

## my assumptions:
- data set is valid
- at least two events in each duty before the first service trip (first event type: pre trip , pullout or taxi)
- at least one event in each duty after the last service trip (last event: pull in or taxi + more)
- split starts of: depot_pull_in or taxi

### notes:
- mock data is for testing only
- testing file provided