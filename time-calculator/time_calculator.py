def add_time(start, duration):

    clock, period = start.split()
    hours, minutes = clock.split(':')
    add_hours, add_minutes = duration.split(':')

    total_min = (int(hours) * 60) + int(minutes) + (int(add_hours) *
                                                    60) + int(add_minutes)

    count_hours = total_min / 60
    count_hours = int(count_hours)
    count_mins = total_min % 60
    no_of_days = -(-int(add_hours) // 24)

    if count_hours > 12 and count_hours <= 24:
        if period == 'AM':
            period = 'PM'
            next_day = ''
        else:
            period = 'AM'
            next_day = ' (next day)'

        new_hours = count_hours - 12

    elif count_hours > 24:
        if no_of_days > 1:
            next_day = ' (' + str(no_of_days) + ' days later)'

        else:
            next_day = ' (next day)'

        new_hours = count_hours - (24 * no_of_days)
        new_hours = abs(new_hours)

    else:
        next_day = ''
        new_hours = count_hours

    if count_mins < 10:
        new_time = str(new_hours) + ':' + '0' + str(
            count_mins) + ' ' + period + next_day

    else:
        new_time = str(new_hours) + ':' + str(
            count_mins) + ' ' + period + next_day

    return new_time
