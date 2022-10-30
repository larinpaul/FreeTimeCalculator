import helpers as h
from dataclasses import dataclass, field


@dataclass
class TimeRange:
    """ Defines the time ranges for usage in the friend and the main modules """
    start_time : str # e.g. 00:30
    end_time : str # e.g. 05:00

    start_minutes : int = field(init=False, repr=False) # e.g. 30
    end_minutes : int = field(init=False, repr=False) # e.g. 300

    minutes_range : range = field(init=False, repr=False)

    def __post_init__(self):
        self.start_minutes = h.timerange_to_minutes(self.start_time)
        self.end_minutes = h.timerange_to_minutes(self.end_time)
        self.minutes_range = range(self.start_minutes, self.end_minutes, 1) # e.g. range(30,300)
