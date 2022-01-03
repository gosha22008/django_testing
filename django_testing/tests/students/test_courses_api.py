import pytest
from rest_framework.test import APIClient

from students.models import Course, Student

@pytest.fixture()
def client():
    return APIClient()


@pytest.mark.django_db
def test_get_course(client):
    Student.objects.create(name='Юрий', birth_date='2002-12-01')
    Course.objects.create(name='Python')

    response = client.get('/api/v1/courses/')

    assert response.status_code == 200
    data = response.json()
    assert len(data) == 1
    assert data[0]['name'] == 'Python'


@pytest.mark.django_db
def test_create_course(client):
    response = client.post('/api/v1/courses/', data={'name': 'Java'}, format='json')

    assert response.status_code == 201
