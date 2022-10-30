import helpers as h
from time_range import TimeRange
from friend import Friend
from custom_list import CustomList


def main():
    """ Friends and their actual time ranges can be added here """
    available_minutes = CustomList(range(1440))
    f1 = Friend("Walter")
    f1.add_busy_range(TimeRange(start_time="09:00", end_time="11:30"))
    f2 = Friend("Victor")
    f2.add_busy_range(TimeRange(start_time="10:00", end_time="12:00"))
    f3 = Friend("Max")
    f3.add_busy_range(TimeRange(start_time="18:00", end_time="19:25"))
    for m in available_minutes[:]: # adding [:] copies a list, which helps conduct a safer removal of elements from a list in a for loop
        for r in Friend.all_busy_minutes_range:
            if m in r:
                available_minutes.remove_if_exist(m)
    for tr in h.prettify_available_minutes(available_minutes):
        print(f"You can meet in {tr}")


if __name__ == "__main__":
    """ Validates that
    the chunk of code is going to execute
    only when we run this file directly
    """
    main()
