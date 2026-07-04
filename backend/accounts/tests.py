import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient

@pytest.fixture
def client():
    return APIClient()

# Issue #7 - Single user tests
@pytest.mark.django_db
def test_register_single_user(client):
    response = client.post('/api/accounts/register/', {
        'username': 'testuser',
        'email': 'test@test.com',
        'password': 'testpass123'
    }, format='json')
    assert response.status_code == 201
    assert response.data['username'] == 'testuser'

@pytest.mark.django_db
def test_login_single_user(client):
    User.objects.create_user(username='testuser', password='testpass123')
    response = client.post('/api/token/', {
        'username': 'testuser',
        'password': 'testpass123'
    }, format='json')
    assert response.status_code == 200
    assert 'access' in response.data
    assert 'refresh' in response.data

@pytest.mark.django_db
def test_logout_single_user(client):
    User.objects.create_user(username='testuser', password='testpass123')
    login_response = client.post('/api/token/', {
        'username': 'testuser',
        'password': 'testpass123'
    }, format='json')
    access_token = login_response.data['access']
    refresh_token = login_response.data['refresh']
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {access_token}')
    response = client.post('/api/accounts/logout/', {
        'refresh': refresh_token
    }, format='json')
    assert response.status_code == 205

# Issue #8 - Multiple users test
@pytest.mark.django_db
def test_register_multiple_users(client):
    for i in range(5):
        response = client.post('/api/accounts/register/', {
            'username': f'user{i}',
            'email': f'user{i}@test.com',
            'password': 'testpass123'
        }, format='json')
        assert response.status_code == 201
        assert response.data['username'] == f'user{i}'
