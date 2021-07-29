from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Scheduling


class AccountTests(APITestCase):
    url = reverse('scheduling-list')
    data = {
        'method': 1,
        'timestamp': '2021-07-29T12:00:00',
        'receiver': 'Jon Do',
        'message': 'Good morning'
    }

    def test_create_scheduling(self):
        """
        Ensure we can create a new scheduling object.
        """
        response = self.client.post(self.url, self.data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Scheduling.objects.count(), 1)
        self.assertEqual(Scheduling.objects.get().status, 0)

    def test_change_status(self):
        """
        Should change scheduling status by endpoint
        """
        response = self.client.post(self.url, self.data, format='json')
        pk = response.data['id']
        url = reverse('scheduling-detail', kwargs={'pk': pk})

        data = self.client.get(url).data
        data.update({'status': 1})
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 1)

    def test_delete_scheduling(self):
        """
        Should delete a scheduling object
        """
        response = self.client.post(self.url, self.data, format='json')
        pk = response.data['id']
        url = reverse('scheduling-detail', kwargs={'pk': pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(len(self.client.get(self.url).data), 0)
