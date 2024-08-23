# Chapter 20 - Django API Development Using ModelViewSet

1. Commands

    Install Django Rest Framework
    ```
    pip install djangorestframework
    ```
    
    Create API V1 App
    ```
    python manage.py startapp api_v1
    ```

2. config - settings.py 

    ```
    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',

        'backend',

        'rest_framework',

        # api v1 for angular or react
        'api_v1'
    ]
    ```

3. backend - models.py

    ```
    from django.db import models

    # Category
    class Category(models.Model):
        id = models.BigAutoField(primary_key=True)
        name = models.CharField(max_length=255)

        def __str__(self):
            return self.name

        class Meta:
            db_table = 'category'
    ```

4. api_v1 - serializers.py

    ```
    from rest_framework import serializers

    from backend.models import Category

    class CategorySerializer(serializers.ModelSerializer):
        class Meta:
            model = Category
            fields = '__all__'
    ```

5. api_v1 - views.py

    ```

    from rest_framework import viewsets, status
    from rest_framework.response import Response

    from backend.models import Category
    from .serializers import CategorySerializer

    class CategoryViewSet(viewsets.ModelViewSet):
        queryset = Category.objects.all()
        serializer_class = CategorySerializer

        def list(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = self.get_serializer(queryset, many=True)
            data = {
                'data': serializer.data
            }
            return Response(data)

        def create(self, request, *args, **kwargs):
            serializer = self.get_serializer(data=request.data)
            if serializer.is_valid():
                self.perform_create(serializer)
                return Response({'message': 'Category created successfully'}, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def update(self, request, *args, **kwargs):
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            if serializer.is_valid():
                self.perform_update(serializer)
                return Response({'message': 'Category updated successfully'})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def destroy(self, request, *args, **kwargs):
            instance = self.get_object()
            self.perform_destroy(instance)
            return Response({'message': 'Category deleted successfully'})
    ```

6. api_v1 - urls.py

    ```
    from django.urls import path, include

    from rest_framework.routers import DefaultRouter

    from .views import CategoryViewSet

    router = DefaultRouter()

    router.register(r'categories', CategoryViewSet, basename='category')

    urlpatterns = [
        path('', include(router.urls)),
    ]
    ```

7. Postman Instruction

```
GET http://127.0.0.1:8000/api_v1/categories/
```

```
{
    "data": [
        {
            "id": 1,
            "name": "Horror"
        },
        {
            "id": 2,
            "name": "Mystery"
        },
        {
            "id": 4,
            "name": "Science Fiction"
        },
        {
            "id": 5,
            "name": "Action"
        }
    ]
}
```

```
POST http://127.0.0.1:8000/api_v1/categories/
```

Headers 

```
Content-Type: application/json
```

```
Body -> raw -> JSON
```

```
{
    "name": "Adventure"
}
```

```
GET http://127.0.0.1:8000/api_v1/categories/1
```

Headers 

```
Content-Type: application/json
```

```
{
    "id": 2,
    "name": "Mystery"
}
```

```
{
    "message": "Category created successfully"
}
```

```
PUT http://127.0.0.1:8000/api_v1/categories/1
```

Headers 

```
Content-Type: application/json
```

```
{
    "id": 2,
    "name": "abcd"
}
```

```
{
    "message": "Category updated successfully"
}
```

```
PATCH http://127.0.0.1:8000/api_v1/categories/1
```

Headers 

```
Content-Type: application/json
```

```
{
    "id": 2,
    "name": "abcd"
}
```

```
{
    "message": "Category updated successfully"
}
```

```
DELETE http://127.0.0.1:8000/api_v1/categories/2
```

Headers 

```
Content-Type: application/json
```

```
{
    "id": 2,
    "name": "abcd"
}
```

```
{
    "message": "Category deleted successfully"
}
```