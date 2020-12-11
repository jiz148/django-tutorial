# from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Ad
from .owner import \
    OwnerListView, \
    OwnerDetailView, \
    OwnerCreateView, \
    OwnerUpdateView, \
    OwnerDeleteView


# Create your views here.
class AdListView(OwnerListView):
    model = Ad


class AdDetailView(OwnerDetailView):
    model = Ad
    fields = ['title', 'price', 'text']


class AdCreateView(OwnerCreateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')


class AdUpdateView(OwnerUpdateView):
    model = Ad
    fields = ['title', 'price', 'text']
    success_url = reverse_lazy('ads:all')


class AdDeleteView(OwnerDetailView):
    model = Ad
    success_url = reverse_lazy('ads:all')
