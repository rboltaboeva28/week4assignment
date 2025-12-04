def get_daily_temp_swing(weather_day_tuple):
    date, max_t, min_t, precip = weather_day_tuple
    return max_t - min_t


def find_day_with_largest_swing(weather_data):
    best_date = ''
    best_swing = -1
    first = True
    for day in weather_data:
        swing = get_daily_temp_swing(day)
        if first:
            best_date = day[0]
            best_swing = swing
            first = False
        elif swing > best_swing:
            best_date = day[0]
            best_swing = swing
        elif swing == best_swing:
            pass
    return best_date


def count_days_above_precip(weather_data, threshold):
    count = 0
    for day in weather_data:
        if day[3] > threshold:
            count += 1
    return count


def get_monthly_summary(weather_data):
    months = {}
    for day in weather_data:
        date = day[0]
        month = date[:7]
        max_t = day[1]
        precip = day[3]
        if month not in months:
            months[month] = [0, 0, 0]  
        months[month][0] += max_t
        months[month][1] += precip
        months[month][2] += 1

    result = []
    for m in months:
        sum_max, total_p, cnt = months[m]
        result.append((m, sum_max / cnt, total_p))
    result.sort()
    return result


def analyze_weather(weather_data):
    largest_swing = find_day_with_largest_swing(weather_data)
    num_heavy_rain_days = count_days_above_precip(weather_data, 10.0)
    monthly_summary = get_monthly_summary(weather_data)
    return (largest_swing, num_heavy_rain_days, monthly_summary)


weather_data = [
    ('2023-10-01', 22, 10, 5.5),
    ('2023-10-02', 25, 11, 0.0),
    ('2023-10-03', 24, 15, 12.0),
    ('2023-11-01', 18, 7, 2.5),
    ('2023-11-02', 15, 6, 15.5),
    ('2023-11-03', 16, 9, 8.0)
]

print(analyze_weather(weather_data))

    