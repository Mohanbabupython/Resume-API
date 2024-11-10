#Testcases for CRUD Operation..
from django.test import TestCase
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Resume
from rest_framework.reverse import reverse
from django.urls import reverse


class ResumeAPITestCase(APITestCase):
    def setUp(self):
        """
        Create a user
        """
        #user authentication
        self.user = User.objects.create_user(username='mohanbabu', password='123456')
        response = self.client.post('/api/token/', {'username': 'mohanbabu', 'password': '123456'}, format='json')
        self.token = response.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.url = reverse('resume-list')

    def test_create_resume(self):
        """
        Test creating a new Resume.
        """
        data = {
            "full_name": "Mohan",
            "age": 23,
            "qualification": "BE",
            "current_salary": 30000.00,
            "expected_salary": 50000.00,
            "role": "SE"
        }

        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['full_name'], data['full_name'])
        self.assertEqual(response.data['age'], data['age'])
        self.assertEqual(response.data['role'], data['role'])

    def test_read_resume(self):
        """
        Test reading an existing Resume.
        """
        resume = Resume.objects.create(
            full_name="Mohan",
            age= 23,
            qualification= "BE",
            current_salary= 30000.00,
            expected_salary= 50000.00,
            role= "SE"
        )
        url = reverse('resume-detail', args=[resume.id])
        
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], resume.full_name)
        self.assertEqual(response.data['age'], resume.age)

    def test_update_resume(self):
        """
        Test updating an existing Resume.
        """
        # First, create a resume to update
        resume = Resume.objects.create(
            full_name= "Mohan",
            age= 23,
            qualification= "BE",
            current_salary= 30000.00,
            expected_salary= 50000.00,
            role= "SE"
        )
        url = reverse('resume-detail', args=[resume.id])
        
        # Data to update
        updated_data = {
            "full_name": "Mohan",
            "age": 23,
            "qualification": "BE",
            "current_salary": 30000.00,
            "expected_salary": 50000.00,
            "role": "Software Engineer"
        }

        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['full_name'], updated_data['full_name'])
        self.assertEqual(response.data['age'], updated_data['age'])

    def test_delete_resume(self):
        """
        Test deleting a Resume.
        """
        # Create a resume to delete
        resume = Resume.objects.create(
            full_name='Mohan',
            age=23,
            qualification='BE',
            current_salary=30000.00,
            expected_salary=50000.00,
            role='Software Engineer'
        )
        url = reverse('resume-detail', args=[resume.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Resume.DoesNotExist):
            Resume.objects.get(id=resume.id)
