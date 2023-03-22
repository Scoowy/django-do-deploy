import json
import os
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib.staticfiles import finders
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.template.loader import get_template
from xhtml2pdf import pisa

from .services.files import handle_uploaded_file
from .services.analyzer import analyzeExcelFile
from .services.cleaner import clean_data
from .services.symanto import symanted_data
from .services.diffuser import fuzzed_data

from django.conf import settings


@login_required(login_url='login')
def dashboard(request):
    methodIsPOST = request.method == 'POST'

    course = request.POST['course'] if methodIsPOST else None
    professor = request.POST['professor'] if methodIsPOST else None
    filename = request.POST['filename'] if methodIsPOST else request.GET.get(
        'filename', None)

    if filename != None:
        context = analyzeExcelFile(filename, professor, course)
        return render(request, 'dashboard/index.html', context)
    else:
        context = {
            'error': f'File <strong>{filename}</strong> not exist. Upload any other file.'
        }
        return render(request, 'dashboard/upload_file.html', context)


def download_report(request):
    show_preview = request.GET.get('preview', 'false') == 'true'
    professor = request.GET.get('professor', None)
    course = request.GET.get('course', None)
    emotionsObject = request.GET.get('emotions', '{}')

    emotionsObject = json.loads(emotionsObject)

    emotions = []
    values = []

    for emotion, value in emotionsObject.items():
        emotions.append(emotion)
        values.append(value)

    rangeE = list(range(0, len(emotions), 2))

    context = {
        'professor': professor,
        'course': course,
        'emotions': emotions,
        'values': values,
        'range': rangeE
    }

    if show_preview:
        return render(request, 'dashboard/report_view_new.html', context=context)
    else:
        # return render(request, 'dashboard/report_view.html', context=context)
        # Obtener el HTML generado con información.
        template = get_template('dashboard/report_view.html')
        html = template.render(context)

        # Crear el objeto HttpResponse con el tipo MIME apropiado para el archivo PDF.
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mi_archivo.pdf"'

        # Convertir el HTML a un archivo PDF utilizando xhtml2pdf y la función de callback.
        pisa_status = pisa.CreatePDF(
            html, dest=response, link_callback=link_callback)

        # Si la conversión a PDF falla, devolver un mensaje de error.
        if pisa_status.err:
            return HttpResponse('Error al generar el archivo PDF')

        # Devolver la respuesta con el archivo PDF generado.
        return response


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        sUrl = settings.STATIC_URL        # Typically /static/
        sRoot = settings.STATIC_ROOT      # Typically /home/userX/project_static/
        mUrl = settings.MEDIA_URL         # Typically /media/
        mRoot = settings.MEDIA_ROOT       # Typically /home/userX/project_static/media/

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path


@login_required(login_url='login')
def upload_file(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'dashboard/upload_file.html')

    file = request.FILES['file'] if 'file' in request.FILES else None

    # Upload file
    uploaded, filename, err = handle_uploaded_file(file)

    if not uploaded:
        context = {
            'error': f'There was an error uploading the file: <strong>{filename}</strong>. Please try again.',
            'error_debug': f'{err.with_traceback()}'
        }
        return render(request, 'dashboard/upload_file.html', context)

    print(f'[INFO]: File uploaded to {filename}')

    # Clean data
    cleaned, cleaned_filename, err = clean_data(filename, 'words-cache.temp')

    if not cleaned:
        context = {
            'error': f'There was an error cleaning the file: <strong>{filename}</strong>. Please try again.',
            'error_debug': f'{err.with_traceback()}'
        }
        return render(request, 'dashboard/upload_file.html', context)

    print(f'[INFO]: File cleaned to {cleaned_filename}')

    # Symante logic data
    symanted, symante_filename, err = symanted_data(
        cleaned_filename, 'symanto-cache.temp')

    if not symanted:
        context = {
            'error': f'There was an error symanting the file: <strong>{cleaned_filename}</strong>. Please try again.',
            'error_debug': f'{err.with_traceback()}'
        }
        return render(request, 'dashboard/upload_file.html', context)

    print(f'[INFO]: File symanted to {symante_filename}')

    # Diffuse logic data
    diffused, diffused_filename, err = fuzzed_data(symante_filename)

    if not diffused:
        context = {
            'error': f'There was an error symanting the file: <strong>{symante_filename}</strong>. Please try again.',
            'error_debug': f'{err.with_traceback()}'
        }
        return render(request, 'dashboard/upload_file.html', context)

    print(f'[INFO]: File diffused to {diffused_filename}')

    # Analyze data in dashboard view
    return redirect(reverse('dashboard') + f'?filename={diffused_filename}')
