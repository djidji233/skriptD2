from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import UserForm, SearchForm
from .models import Oglas

class IndexView(generic.ListView):
    template_name = 'oglasi/index.html'
    context_object_name = 'svi_oglasi' #object_list je po defaultu
    def get_queryset(self):         #rename smo ga da bi radio u foru u index.html
        return Oglas.objects.all() #returns object_list

class DetailView(generic.DetailView):
    model = Oglas
    template_name = 'oglasi/detail.html'

class OglasCreate(CreateView):
    model = Oglas
    fields = ['publisher', 'title', 'category', 'picture', 'description', 'price']

class OglasUpdate(UpdateView):
    model = Oglas
    fields = ['publisher', 'title', 'category', 'picture', 'description', 'price']

class OglasDelete(DeleteView):
    model = Oglas
    success_url = reverse_lazy('oglasi:index')

class UserFormView(View):
    form_class = UserForm
    template_name = 'oglasi/registration_form.html'

    # if method==POST or method==GET verzija
    # ili ovako

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name,{'form': form})
    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned (normalized) data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if credentials are correct - exists in DB
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request,user)
                    return redirect('oglasi:index')
                    #request.user.username - refer them this way
        # didnt login -> blank form again
        return render(request, self.template_name, {'form': form})


class SearchFormView(View):
    form_class = SearchForm
    template_name = 'oglasi/search_form.html'
    #display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})
    #process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            t = form.cleaned_data['title']
            oglasi = Oglas.objects.filter(title__icontains=t)
            context = {'svi_oglasi':oglasi}
            return render(request, 'oglasi/index.html', context)
        else:
            return render(request, 'oglasi/oglas_form.html')


