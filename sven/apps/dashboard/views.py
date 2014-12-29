from django.shortcuts import render

def index( request ):
    data = { 'one' : 'elijah', 'two' : 'ethun', 'three' : 'ray' }

    return render( request, 'dashboard/index.html', { 'datas' : data } )
