from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views.generic import FormView

from forms import DocumentForm

class UploadFormView(FormView):

    template_name = 'mainpage.html'
    form_class = DocumentForm
    success_url = '/'
        
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        file_exist = False
        file_content = self.request.FILES.values()[0].read()
 
        # Checking for MIME type.
        if self.request.FILES.values()[0].content_type.find('text') != -1:
            file_exist = True
        
        return render_to_response('mainpage.html',
                                     {'form': form,
                                 'file_data': file_content,
                                'file_exist': file_exist},
                              context_instance=RequestContext(self.request)
                              )
  
