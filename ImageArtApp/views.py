from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import FormView
from django.shortcuts import render
from .ImageGenerator import ImageGenerator
from .forms import ArtFunctionForm
import cv2


class ArtGenView(FormView):
    template_name = "ImageArtApp/artgen.html"
    form_class = ArtFunctionForm

    def get(self, request):
        form = ArtFunctionForm()
        return render(request, 'ImageArtApp/artgen.html', {'form': form})

    def post(self, request):
        form = ArtFunctionForm(request.POST)
        form.is_valid()

        gen = ImageGenerator(form.cleaned_data['red_func'], form.cleaned_data['green_func'],
                             form.cleaned_data['blue_func'])
        image = gen.get_image()

        cv2.imwrite('./ImageArtApp/static/ImageArtApp/image.png', image)
        return render(request, 'ImageArtApp/artgen.html', {'form': form})
