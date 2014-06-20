import datetime

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView

from forms import DocumentForm
from models import Document


class UploadFormView(FormView):

    template_name = 'mainpage.html'
    form_class = DocumentForm
    success_url = '/'
        
    def form_valid(self, form):
    
        file_exist = False
        file_content =''
        uploaded_file = self.request.FILES.values()[0]
        
        # Checking for MIME type.
        if 'text' in uploaded_file.content_type:
            file_content = uploaded_file.read()
            file_exist = True
            newdoc = Document(
                                name = uploaded_file.name,
                                content = file_content,
                                lastviewed = datetime.datetime.now()
            )
            newdoc.save()
        
        return render_to_response(
            'mainpage.html',
            {
             'form': form,
             'file_data': file_content,
             'file_exist': file_exist
            },
            context_instance=RequestContext(self.request)
        )
