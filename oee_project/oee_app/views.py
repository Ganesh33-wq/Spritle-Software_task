from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Machine
from .utils import calculate_oee

@api_view(['GET'])
def oee_data(request):
    machine_name = request.GET.get('machine_name')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')
    oee_threshold = float(request.GET.get('oee_threshold', 0.0))

    filters = {}
    if machine_name:
        filters['name'] = machine_name
    if start_date and end_date:
        filters['productionlog__date_time__range'] = [start_date, end_date]

    machines = Machine.objects.filter(**filters)

    oee_data = []
    for machine in machines:
        oee = calculate_oee(machine)
        if oee >= oee_threshold:
            oee_data.append({
                'machine_name': machine.name,
                'oee': oee,
            })

    return Response(oee_data)
