# states which still need the station
states_needed = set(["mt", "wa", "or", "id", "nv", "ut", "ca", "az"])

# the list of which station facing which states
stations = {}
stations["kone"] = set(["id", "nv", "ut"])
stations["ktwo"] = set(["wa", "id", "mt"])
stations["kthree"] = set(["or", "nv", "ca"])
stations["kfour"] = set(["nv", "ut"])
stations["kfive"] = set(["ca", "az"])

final_stations = set()


while states_needed:
    best_station = None
    states_covered = set()  #
    for station, states_for_station in stations.items():
        covered = states_needed & states_for_station  # 当前这个站包含的需要被包含的地方
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered

    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
