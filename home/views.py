from django.views.generic import TemplateView, ListView, DetailView
from django.shortcuts import render
# from projects.models import Post
# from .services import get_posts
# import requests


# class LoginView(TemplateView):
#     template_name = 'home/home.html'
#     def get_context_data(self, *args, **kwargs):
#         context = {
#             'posts' : get_posts
#         }
#         return context

class LoginView(TemplateView):
    template_name = 'registration/login.html'