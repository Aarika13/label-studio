from django.http import HttpResponse

def download_file(request):
    with open('ocr_tasks.json', mode='r') as f:
        response = HttpResponse(f.read(), content_type='application/json')
        response['Content-Disposition'] = 'attachment; filename="ocr_tasks.json"'
        return response
