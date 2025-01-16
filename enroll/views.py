from django.shortcuts import render,redirect
from .forms import StudentRegistation
from .models import User 
from django.views.generic.base import TemplateView, RedirectView
from django.views import View

# Add and Show User use Class Base Views
class UserAddShow(TemplateView):
    template_name = 'enroll/addandshow.html'
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        fm = StudentRegistation()
        student = User.objects.all()
        context = {'student' : student, 'form' : fm}
        return context
    
    def post(self, request):
        fm = StudentRegistation(request.POST)
        if fm.is_valid():
            name = fm.cleaned_data['name']
            email = fm.cleaned_data['email']
            password = fm.cleaned_data['password']
            Usersave = User(name = name, email = email, password = password)
            Usersave.save()
            return redirect('/')


class UserUpdateView(View):
    def get(self, request, id):
        user = User.objects.get(pk=id)
        fm = StudentRegistation(instance=user)
        return render(request, 'enroll/updatestudent.html', {'form' : fm})
    
    def post(self, request, id):
        user = User.objects.get(pk=id)
        fm = StudentRegistation(request.POST, instance=user)
        if fm.is_valid():
            fm.save()
        return redirect('/')
        

# Delete User use Class Base Views
class UserDeleteView(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)
        
         
