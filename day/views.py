from django.views.generic import ListView, DetailView, CreateView, UpdateView,DeleteView
from .models import Diary
from django.urls import reverse_lazy

# Create your views here.
class DiaryList(ListView):
    model = Diary
    template_name = 'diary_list.html'

class DiaryDetail(DetailView):
    model = Diary
    template_name = 'diary_detail.html' 

class DiaryCreate(CreateView):
    model = Diary
    template_name ='diary_create.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('day:diary_list')

class DiaryUpdate(UpdateView):
    model = Diary
    template_name = 'diary_update.html'
    fields = ['title', 'content']
    success_url = reverse_lazy('day:diary_list')

class DiaryDelete(DeleteView):
    model = Diary
    template_name = 'diary_delete.html'
    success_url = reverse_lazy('day:diary_list')