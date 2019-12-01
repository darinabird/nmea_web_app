from django.template.response import TemplateResponse
from django.http import HttpResponseBadRequest

from .forms import GPSDataForm
from .models import GPSData


def index(request, *args, **kwargs):
    order_by = ('height__order_by', 'speed__order_by')

    queryset = GPSData.objects.all()
    form = GPSDataForm()

    if request.method != 'GET':
        return HttpResponseBadRequest()

    if request.GET:
        form = GPSDataForm(request.GET)

        if not form.is_valid():
            return HttpResponseBadRequest()

    filter_param = {}

    height = request.GET.get('height', '')
    if height != '':

        height_condition = request.GET.get('height_condition', '')
        if height_condition != '':
            filter_param[height_condition] = height
        else:
            filter_param['height'] = height

    speed = request.GET.get('speed', '')
    if speed != '':

        # speed = float(speed)
        speed_condition = request.GET.get('speed_condition', '')
        if speed_condition != '':
            filter_param[speed_condition] = speed
        else:
            filter_param['speed'] = speed

    queryset = queryset.filter(**filter_param)

    hob = request.GET.get(order_by[0])
    if hob is not None and hob.lower() == 'desc':
        queryset = queryset.order_by('-height')
    if hob is not None and hob.lower() == 'asc':
        queryset = queryset.order_by('height')

    sob = request.GET.get(order_by[1])
    if sob is not None and sob.lower() == 'desc':
        queryset = queryset.order_by('-speed')
    if sob is not None and hob.lower() == 'asc':
        queryset = queryset.order_by('speed')

    return TemplateResponse(request=request, template='table/base.html', context={'qs': queryset, 'form': form})
