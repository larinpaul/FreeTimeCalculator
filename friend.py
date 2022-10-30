import helpers as h
from time_range import TimeRange
from dataclasses import dataclass, field
from typing import ClassVar

@dataclass
class Friend:
    """ Allows the creation of Friend objects with one or more busy time ranges"""
    all_busy_minutes_range: ClassVar[list] = []
    name: str
    busy_time_ranges: list[TimeRange] = field(default_factory=list, repr=False)

    def add_busy_range(self, obj:TimeRange):
        self.busy_time_ranges.append(obj)
        # Adds the minutes range object to a class attribute:
        Friend.all_busy_minutes_range.append(obj.minutes_range)
