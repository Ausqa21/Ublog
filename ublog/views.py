from django.shortcuts import render


def post_list(request):
    return render(request, './ublog/post_list.html', {})
