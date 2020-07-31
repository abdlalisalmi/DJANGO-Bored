from django.shortcuts import render
import requests
from .models import SearchHistory


def homePage(request):
    template_name = 'homePage.html'

    if (request.method == 'POST'):
        select = request.POST['select']
        select_list = ["education", "recreational", "social", "diy",
                       "charity", "cooking", "relaxation", "music", "busywork"]
        if not select in select_list:
            select = "random"

        url = 'https://www.boredapi.com/api/activity/' if select == 'random' else 'https://www.boredapi.com/api/activity/' + \
            '?type={}'.format(select)

        res = requests.get(url).json()

        search = SearchHistory.objects.create(
            activity=res['activity'],
            activity_type=res['type'],
            activity_key=res['key'],
        )

        data = {
            'res': res
        }
        return render(request, template_name, data)
    return render(request, template_name)
