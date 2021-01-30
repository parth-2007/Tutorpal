from django.shortcuts import render
from django.http import HttpRequest
import os


def auth(request: HttpRequest):
    return render(request, 'frontend/auth/index.html')


'''
def exampleview(request: HttpRequest):
    return render(request, 'frontend/dir_of_html_file/actualt_html_file.html')
'''


# def godir(request: HttpRequest, dir: str, file: str):
#     path = 'frontend/' + dir + '/' + file + '.html'
#     print("path: ", path)
#     return render(request, path)
