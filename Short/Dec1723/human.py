import humanize
from icecream import ic
from datetime import datetime,timedelta

def example1():
    machine_now = datetime.now()
    human_now = humanize.naturaldate(machine_now)
    ic(machine_now,human_now)
    
    machine_yesterday = machine_now - timedelta(days = 1)
    human_yesterday = humanize.naturaldate(machine_yesterday)
    ic(machine_yesterday,human_yesterday)
    
    machine_2daysago = machine_now - timedelta(days = 2)
    human_2daysago = humanize.naturaldate(machine_2daysago)
    ic(machine_2daysago,human_2daysago)

def example2():
    ic(humanize.naturalsize(1024000))
    ic(humanize.naturalsize(1010701824))
    ic(humanize.naturalsize(3.001534883e+12))
    

def example3():
    ic(humanize.scientific(25000000))
    ic(humanize.fractional(0.4369954565))


if __name__ == "__main__":
    example1()
    # example2()
    # example3()