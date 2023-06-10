from django.db.models import Sum

def calculate_oee(machine):
    availability = machine.productionlog_set.count() / (machine.productionlog_set.count() + machine.unplanned_downtime)
    performance = (machine.ideal_cycle_time * machine.productionlog_set.aggregate(Sum('units_produced'))['units_produced__sum']) / (machine.available_operating_time * machine.productionlog_set.count())
    quality = 1.0  # Assuming quality is always 100%
    oee = availability * performance * quality
    return oee
