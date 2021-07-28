from django.test import TestCase
from ..models import Scheduling


class SchedulingTestCase(TestCase):
    def setUp(self):
        Scheduling.objects.create(
            status=0,
            method=1,
            timestamp='2021-07-28T12:00:00-0300',
            receiver='John Do',
            message='Hello'
        )

    def test_created(self):
        "Should create a instance"
        Scheduling.objects.create(
            status=0,
            method=2,
            timestamp='2021-07-28T12:00:00-0300',
            receiver='Jack',
            message='Hi people'
        )
        self.assertEqual(Scheduling.objects.count(), 2)

    def test_update(self):
        "Should change a instance"
        instance = Scheduling.objects.first()
        instance.status = 1
        instance.save()
        self.assertEqual(instance.status, 1)

    def test_delete(self):
        "Should delete a instance"
        before = Scheduling.objects.count()
        instance = Scheduling.objects.first()
        instance.delete()
        after = Scheduling.objects.count()
        self.assertNotEqual(before, after)
