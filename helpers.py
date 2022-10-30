def timerange_to_minutes(t_str):
    """ Returns the amount of minutes for time ranges in the HH:MM format
    :param t_str:
    :return:
    """
    hour = int(t_str.split(":")[0])
    minutes = int(t_str.split(":")[1])
    hour_to_minutes = hour * 60
    
    return hour_to_minutes + minutes

def minutes_to_timerange_str(m):
    """ Return a time range string in the HH:MM format for the given integer
    e.g. m = 115 -> 01:55
    :param m:
    :return:
    """
    hours = m // 60
    hours_str = f"{hours:02d}" # Always print your value with two digits, no matter which format you're using
    minutes = m % 60
    minutes_str = f"{minutes:02d}"
    
    return f"{hours_str}:{minutes_str}"

def prettify_available_minutes(l: list): 
    """ An algorithm that aggreagtes
    the sublists into separate lists
    and turns the elements into the "00:00" format
    """
    grouped_list = [] # A nested list
    list_resettable = [] 
    # Groups the list so that, for example: [[0, 1, 2, 3], [60, 61, 62]]
    for element in l:
        if list_resettable == []:
            list_resettable.append(element)
            continue
        if list_resettable[-1] + 1 == element: # If, for example, 3+1 != 60, then create a sublist
            list_resettable.append(element)
        else: # Else, if, for example, 60+1 not == 61, add 61 into the sublist
            grouped_list.append(list_resettable[:])
            list_resettable.clear()
            list_resettable.append(element)
    
    grouped_list.append(list_resettable)

    time_ranges = []
    for group in grouped_list: # Converting numbers into the HH:MM formatted strings
        start_time = minutes_to_timerange_str(m=group[0])
        end_time = minutes_to_timerange_str(m=group[-1])
        time_range_str = f"{start_time} to {end_time}"
        time_ranges.append(time_range_str)
    
    return time_ranges
