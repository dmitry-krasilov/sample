from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


from django import forms

class DocumentForm(forms.Form):
    docfile = forms.FileField()

def upload_file(request):
    variable = ''
    file_exist = False
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            variable =  request.FILES.values()[0].read()
            
            #checking for mime/type
            if request.FILES.values()[0].content_type.find('text') != -1:
                file_exist = True
    else:
        form = DocumentForm()
    
    return render_to_response('mainpage.html',
                                {'form' : form,'file_data' : variable,'file_exist' : file_exist},
                              context_instance=RequestContext(request)
                              )

