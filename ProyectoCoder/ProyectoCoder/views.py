from django.http import HttpResponse
from django.template import loader, Template, context

def saludar(request, nombre):
    Tunombre = f"Mi nombre es {nombre}, un saludo"
    return HttpResponse(Tunombre)

def ProbarTemplate(self):
    plantilla = loader.get_template("Template1.html")
    documento = plantilla.render()
    
    return HttpResponse(documento)
    


