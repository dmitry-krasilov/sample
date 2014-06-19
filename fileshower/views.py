from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from forms import DocumentForm


def upload_file(request):
    file_content = ''
    file_exist = False
    
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            file_content = request.FILES.values()[0].read()
 
            # Checking for MIME type.
            if request.FILES.values()[0].content_type.find('text') != -1:
                file_exist = True
            
    else:
        form = DocumentForm()
    
    return render_to_response('mainpage.html',
                                     {'form': form,
                                 'file_data': file_content,
                                'file_exist': file_exist},
                              context_instance=RequestContext(request)
                              )

