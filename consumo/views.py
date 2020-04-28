from .models import  Hamburguesa, Ingredientes
from django.http import HttpResponse
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def guesaf(request):
    if request.method == 'GET':
        snippets = Hamburguesa.objects.all()
        lista=[]
        for i in snippets:
            lista1=[]
            for a in i.ingredients.all():
                dicc={}
                dicc['path']='https://burgueseriawene.herokuapp.com/ingrediente/'+str(a.idi)
                lista1.append(dicc)
            lista.append({'id':i.ide,'nombre':i.nombre,'precio':i.precio,'descripcion':i.descripcion,'imagen':i.imagen,'ingredientes':lista1})

        response=json.dumps(lista)
        return HttpResponse(response,status=status.HTTP_200_OK)

    elif request.method == 'POST':
        data = json.loads(request.body.decode())
        try:
            if data['nombre']=="" or data['precio']=="" or data['descripcion']=="" or data['imagen']=="":
                return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
            h= Hamburguesa.objects.create(
                nombre=data["nombre"],
                precio=data["precio"],
                descripcion=data["descripcion"],
                imagen=data["imagen"]
            )
            h.save()
            h1=Hamburguesa.objects.latest('ide')
            resultado={'id':h1.ide,'nombre':h1.nombre,'precio':h1.precio,'descripcion':h1.descripcion,'imagen':h1.imagen,'ingredientes':[]}
            return HttpResponse(json.dumps(resultado),status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(json.dumps({'message':'input invalido'}),status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def guesas(request,idef):
    if request.method=='GET':
        h=Hamburguesa.objects.filter(ide=idef)
        if len(h)==0:
            return HttpResponse(json.dumps({'message':'hamburguesa inexistente'}),status=status.HTTP_404_NOT_FOUND)
        else:
            lista1=[]
            for a in h[0].ingredients.all():
                dicc={}
                dicc['path']='https://burgueseriawene.herokuapp.com/ingrediente/'+str(a.idi)
                lista1.append(dicc)
            resultado={'id':h[0].ide,'nombre':h[0].nombre,'precio':h[0].precio,'descripcion':h[0].descripcion,'imagen':h[0].imagen,'ingredientes':lista1}
            return HttpResponse(json.dumps(resultado),status=status.HTTP_200_OK)


    elif request.method=='DELETE':
        try:
            Hamburguesa.objects.get(ide=idef).delete()
            return HttpResponse(json.dumps({'resultado':'hamburguesa eliminada'}), status=status.HTTP_200_OK)
        except:
            return HttpResponse(json.dumps({'message': 'hamburguesa inexistente'}), status=status.HTTP_404_NOT_FOUND)


    elif request.method=='PATCH':
        try:
            burger = Hamburguesa.objects.filter(ide=idef)
            if len(burger) == 0:
                return HttpResponse(json.dumps({'message': 'hamburguesa inexistente'}),
                                    status=status.HTTP_404_NOT_FOUND)
            data = json.loads(request.body.decode())
            if "nombre" in data:
                if data['nombre'] == "":
                    return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
                burger.update(nombre=data['nombre'])
            if "precio" in data:
                if data['precio'] == "":
                    return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
                burger.update(precio=data['precio'])
            if "descripcion" in data:
                if data['descripcion'] == "":
                    return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
                burger.update(descripcion=data['descripcion'])
            if "imagen" in data:
                if data['imagen'] == "":
                    return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
                burger.update(imagen=data['imagen'])
            burger = Hamburguesa.objects.get(ide=idef)
            dicc = {}
            dicc['id'] = burger.ide
            dicc['nombre'] = burger.nombre
            dicc['precio'] = burger.precio
            dicc['descripcion'] = burger.descripcion
            dicc['imagen']=burger.imagen
            lista1=[]
            for a in burger.ingredients.all():
                dicc1={}
                dicc1['path']='https://burgueseriawene.herokuapp.com/ingrediente/'+str(a.idi)
                lista1.append(dicc1)
            dicc['ingredientes']=lista1
            hamburguesa = json.dumps(dicc)
            return HttpResponse(hamburguesa,status=status.HTTP_200_OK)
        except:
            return HttpResponse(json.dumps({'message': 'parametros invalidos'}), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def content(request):
    if request.method=='GET':
        ing=Ingredientes.objects.all()
        lista=[]
        for i in ing:
            lista.append({'id':i.idi,'nombre':i.nombre,'descripcion':i.descripcion})
        response=json.dumps(lista)
        return HttpResponse(response,status=status.HTTP_200_OK)

    elif request.method=='POST':
        data=json.loads(request.body.decode())
        try:
            if data['nombre']=="" or data['descripcion']=="":
                return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)
            ing=Ingredientes.objects.create(
                nombre=data['nombre'],
                descripcion=data['descripcion'])
            ing.save()
            ingre=Ingredientes.objects.latest('idi')
            response={'id':ingre.idi,'nombre':ingre.nombre,'descripcion':ingre.descripcion}
            return HttpResponse(json.dumps(response), status=status.HTTP_201_CREATED)
        except:
            return HttpResponse(json.dumps({'message': 'input invalido'}), status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def contenido(request,idif):
    #####falta editar el delete
    if request.method=='DELETE':
        try:
            ingre=Ingredientes.objects.get(idi=idif)
            for h in Hamburguesa.objects.all():
                if ingre in h.ingredients.all():
                    return HttpResponse(json.dumps({'resultado': 'Ingrediente no se puede borrar, esta presente en una hamburguesa'}), status=status.HTTP_409_CONFLICT)

            Ingredientes.objects.get(idi=idif).delete()
            return HttpResponse(json.dumps({'resultado':'Ingrediente eliminado'}), status=status.HTTP_200_OK)
        except:
            return HttpResponse(json.dumps({'message': 'Ingrediente inexistente'}), status=status.HTTP_404_NOT_FOUND)
    elif request.method=='GET':
        h = Ingredientes.objects.filter(idi=idif)
        if len(h) == 0:
            return HttpResponse(json.dumps({'message': 'Ingrediente inexistente'}), status=status.HTTP_404_NOT_FOUND)
        else:
            resultado = {'id': h[0].idi, 'nombre': h[0].nombre, 'descripcion': h[0].descripcion}
            return HttpResponse(json.dumps(resultado), status=status.HTTP_200_OK)

@csrf_exempt
def agregar_ingrediente(request,bur,ing):
    if request.method=='PUT':
        ingrediente=Ingredientes.objects.filter(idi=ing)
        if len(ingrediente)==0:
            return HttpResponse(json.dumps({'message': 'Ingrediente inexistente'}), status=status.HTTP_404_NOT_FOUND)
        hamburguesa=Hamburguesa.objects.filter(ide=bur)
        if len(hamburguesa)==0:
            return HttpResponse(json.dumps({'message': 'Id de hamburguesa invalido'}), status=status.HTTP_400_BAD_REQUEST)
        hamburguesa[0].ingredients.add(ingrediente[0])
        return HttpResponse(status=status.HTTP_201_CREATED)

    elif request.method=="DELETE":
        ingrediente=Ingredientes.objects.filter(idi=ing)
        if len(ingrediente)==0:
            return HttpResponse(json.dumps({'message': 'Ingrediente inexistente en la hamburguesa'}), status=status.HTTP_404_NOT_FOUND)
        hamburguesa = Hamburguesa.objects.filter(ide=bur)
        if len(hamburguesa)==0:
            return HttpResponse(json.dumps({'message': 'Id de hamburguesa invalido'}), status=status.HTTP_400_BAD_REQUEST)
        if ingrediente[0] in hamburguesa[0].ingredients.all():
            hamburguesa[0].ingredients.remove(ingrediente[0])
            return HttpResponse(json.dumps({'resultado':'ingrediente eliminado'}), status=status.HTTP_200_OK)
        return HttpResponse(json.dumps({'message': 'Ingrediente inexistente en la hamburguesa'}),status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def laden(request,idef):
    if request.method=='GET':
        return HttpResponse(json.dumps({'message':'input invalido'}),status=status.HTTP_400_BAD_REQUEST)
    elif request.method==('DELETE'):
        return HttpResponse(json.dumps({'message':'hamburguesa y/o ingrediente inexistente'}),status=status.HTTP_404_NOT_FOUND)
    elif request.method==('PATCH'):
        return HttpResponse(json.dumps({'message':'hamburguesa inexistente'}),status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def nada(request,bur,ing):
    if request.method=='PUT':
        return HttpResponse(json.dumps({'message': 'Algun parametro es invalido'}), status=status.HTTP_400_BAD_REQUEST)
    elif request.method=='DELETE':
        return HttpResponse(json.dumps({'message': 'Algun parametro es invalido'}), status=status.HTTP_400_BAD_REQUEST)

