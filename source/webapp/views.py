from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, TemplateView, CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse, reverse_lazy
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from webapp.forms import PhotoForm, FavoriteForm
from webapp.models import Photo, Favorite


# Create your views here.

class IndexView(ListView):
    template_name = 'photo/index.html'
    model = Photo
    context_object_name = 'photos'
    ordering = ['-created_at']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['favorite_form'] = FavoriteForm()
        return context


class PhotoDetail(LoginRequiredMixin, TemplateView):
    template_name = 'photo/photo_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['photo'] = get_object_or_404(Photo, pk=kwargs['pk'])
        return context


class CreatePhoto(LoginRequiredMixin, CreateView):
    model = Photo
    template_name = 'photo/create_photo.html'
    form_class = PhotoForm
    permission_required = "blog.view_post"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('/')
        contex = {'form': form}
        return self.render_to_response(contex)


class PhotoUpdate(LoginRequiredMixin, UpdateView, UserPassesTestMixin):
    model = Photo
    form_class = PhotoForm
    template_name = 'photo/photo_update.html'
    permission_required = 'webapp.change_tracker'

    def get_success_url(self):
        return reverse('photo_view', kwargs={'pk': self.object.pk})


class DeleteTrackerView(LoginRequiredMixin, DeleteView):
    template_name = 'photo/photo_delete.html'
    model = Photo
    success_url = reverse_lazy('index')


class FavoriteView(FormView):
    form_class = FavoriteForm

    def post(self, request, *args, **kwargs):
        photo = get_object_or_404(Photo, pk=kwargs.get('pk'))
        form = self.get_form_class()(request.POST)
        if form.is_valid():
            user = request.user
            if not Favorite.objects.filter(user=user, photo=photo).exists():
                Favorite.objects.create(user=user, photo=photo)
                messages.success(request, 'Статья была добавлена в избранное')
        return redirect('index')







