from django.db import models
from django.urls import reverse
from sorl.thumbnail import ImageField

from PIL import Image
Image.MAX_IMAGE_PIXELS = 1000000000

# Create your models here.

class Student(models.Model):
    """
    Model representing a student.
    """
    name = models.CharField(max_length=200, help_text="Enter a name ")
    avatar = models.ImageField(upload_to='studentsAvatar')
    studentID = models.CharField(max_length=10, help_text="Enter student ID", unique=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

    def get_absolute_url(self):
        """
        Returns the url to access a detail record for this student.
        """
        return reverse('student-detail', args=[str(self.id)])

class Subject(models.Model):
    """
    Model representing a subject.
    """
    name = models.CharField(max_length=200, help_text="Enter a name ")
    subjectID = models.CharField(max_length=10, help_text="Enter subject ID", unique=True)

    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

class Score(models.Model):
    """
    Model representing a score.
    """
    studentID = models.ForeignKey('Student', on_delete=models.CASCADE, null=True)
    score = models.IntegerField(default=0)
    subjID = models.ForeignKey('Subject', on_delete=models.CASCADE, null=True)


    def __str__(self):
        """
        String for representing the Model object
        """
        return '{0} {1} ({2})'.format(self.score, self.studentID, self.subjID)


