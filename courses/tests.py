from django.test import TestCase
from django.utils import timezone

from .models import Course

# Create your tests here.

class CourseModelTests(TestCase):
	'''Tests for the Course model'''
	def test_course_creation(self):
		course = Course.objects.create(
			title="Python Regular Expressions", 
			description="Learn to write regualar epressions with python"
			)
		now = timezone.now()
		self.assertLess(course.created_at, now)