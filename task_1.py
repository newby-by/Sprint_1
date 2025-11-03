"""The task1 is solved here though.
"""


def get_period_in_minutes(period: list[str]) -> int:
    """Calculation a period time in minutes.

    period: str - a period time (e.g. 1h 45m, 25m, 360s)
    return: int - minutes
    """
    
    if not period:
        return None
    
    minutes: int = 0
    ENDS = {
        'h': 60,
        'm': 1,
        's': 1./60
    }
    perts_of_period = period.split()
    
    for short in ENDS:
        for part in perts_of_period:
            if short in part:
                minutes += int(part[:-1]) * ENDS[short]
                break
    
    return int(minutes)



time_string = '1h 45m,360s,25m,30m 120s,2h 60s'

minutes = 0
list_of_times = time_string.split(',')
for t in list_of_times:
    minutes += get_period_in_minutes(t)

print(minutes)
