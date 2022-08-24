arrival_times = [float(x) for x in input().split()]
departure_times = [float(x) for x in input().split()]


def min_platforms(arrival, departure):

    schedule = []
    for i in range(len(arrival)):
        schedule.append([departure[i], 'd'])
        if ([arrival[i], 'd'] not in schedule):
            schedule.append([arrival[i], 'a'])

    schedule = sorted(schedule, key= lambda x: x[1])
    schedule = sorted(schedule, key=lambda x: x[0])

    platforms, result = 0, 0


    for i in range(len(schedule)):
        if schedule[i][1] == 'a':
            platforms += 1
            result = max(platforms, result)
        else:
            platforms -= 1

    return result

print(min_platforms(arrival_times, departure_times))
