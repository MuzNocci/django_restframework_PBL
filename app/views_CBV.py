# from app.models import Todo
# from app.serializers import TodoSerializer
# from rest_framework import generics
# from rest_framework import status
# from rest_framework import viewsets
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework.exceptions import NotFound



### CLASS BASED VIEW
### OBSERVAÇÃO: TODO apiview [GET,POST,PUT e DELETE], deve ter os argumentos "self" e "request"



### TodoListAndCreate - GENERICS
# class TodoListAndCreate(generics.ListCreateAPIView):

#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer


# ### TodoListAndUpdateAndDelete - GENERICS
# class TodoListAndUpdateAndDelete(generics.RetrieveUpdateDestroyAPIView):

#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer



#---------------------------------------------------------------------------------------------


### TodoListAndCreate - MANUAL
# class TodoListAndCreate(APIView):


#     def get(self, request):

#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)

#         return Response(serializer.data)


#     def post(self, request):

#         serializer = TodoSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)



### TodoListAndUpdateAndDelete - MANUAL
# class TodoListAndUpdateAndDelete(APIView):


#     def get_object(self, pk):

#         try:
#             return Todo.objects.get(pk=pk)

#         except Todo.DoesNotExist:
#             raise NotFound()
        

#     def get(self, request, pk):

#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo)

#         return Response(serializer.data)
    

#     def put(self, request, pk):

#         todo = self.get_object(pk)
#         serializer = TodoSerializer(todo, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     def delete(self, request, pk):

#         todo = self.get_object(pk)
#         todo.delete()

#         return Response(status=status.HTTP_204_NO_CONTENT)



# ---------------------------------------------------------------------------------------------


### FUNCTION BASED VIEW

# from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def todo_list(request):


#     if request.method == 'GET':

#         todo = Todo.objects.all()
#         serializer = TodoSerializer(todo, many=True)
#         return Response(serializer.data)
    

#     elif request.method == 'POST':

#         serializer = TodoSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()

#             return Response(serializer.data, status=status.HTTP_201_CREATED)
        
#         return Response(serializer.erros, status=status.HTTP_400_BAD_REQUEST)



# @api_view(['GET','PUT','DELETE'])
# def todo_detail_change_and_delete(request, pk):


#     try:
#         todo = Todo.objects.get(pk=pk)

#     except Todo.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
    

#     if request.method == 'GET':
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data)
    

#     elif request.method == 'PUT':

#         serializer = TodoSerializer(todo, data=request.data)

#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        
#     elif request.method == 'DELETE':
#         todo.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)