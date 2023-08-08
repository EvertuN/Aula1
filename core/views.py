from django.shortcuts import render, HttpResponse


# Create your views here.

def index(request, num1, num2):
    return HttpResponse(f'<h1> Minha Primeira Página Django<h1>'
                        f'<h3> A soma de {num1} + {num2} é = {num1 + num2}<h3>')


def multiplicacao(request, num1, num2):
    return HttpResponse(f'<h1> Multiplicação<h1>'
                        f'<h3> A Multiplicação de {num1} x {num2} é = {num1 * num2} <h3>')


def divisao(request, num1, num2):
    return HttpResponse(f'<h1> Divisão<h1>'
                        f'<h3> {num1} dividido por {num2} é = {num1 / num2} <h3>')


def subtracao(request, num1, num2):
    return HttpResponse(f'<h1> Subtração<h1>'
                        f'<h3> A Subtração de {num1} - {num2} é = {num1 - num2} <h3>')
