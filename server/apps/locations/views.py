from django.shortcuts import render
from django.views.generic import ListView, DetailView
from rest_framework import status, viewsets, mixins
from .serializers import *

# Create your views here.


class StateViewSet(viewsets.ModelViewSet):
    model = State
    queryset = model.objects.all()
    serializer_class = StateSerializer
    read_only = True


# class ZipcodeViewSet(viewsets.ModelViewSet):
#     model = Zipcode
#     queryset = model.objects.all()
#     serializer_class = ZipcodeSerializer
#     read_only = True
#
#     def list(self, request):
#         raise NotImplementedError

class StateListView(ListView):
    model = State
    template_name = "state/list.html"
    paginate_by = None

    def get_queryset(self):
        return self.model.objects.all().order_by("name")

    def get_context_data(self, **kwargs):
        context = super(StateListView, self).get_context_data(**kwargs)
        context["title"] = "State List"
        return context


class StateDetailView(DetailView):
    model = State
    template_name = "state/detail.html"
    #
    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(StateDetailView, self).get_context_data(**kwargs)
    #     context["title"] = "Dating in {}".format(context["object"].name)
    #     return context

