from django.test import TestCase 
import pytest
from django.test import TestCase
from .models import User
# Crear un nuevo producto

@pytest.mark.django_db
def test_crear_Usuario():
    
    user = User.objects.create(
    Name='Jesus',
    password = '4321',
    email = 'tadjes0118@outlook.com'
    )
    
    assert User.objects.count() == 1
    assert user.Name == 'Jesus'
    assert user.password == '4321'
    assert user.email == 'tadjes0118@outlook.com'