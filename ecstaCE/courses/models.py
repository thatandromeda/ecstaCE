from django.db import models


class Instructor(models.Model):
    name = models.CharField(max_length=30)
    institution = models.CharField(max_length=50)
    picture = models.ImageField(upload_to='instructors', null=True, blank=True)

    class Meta:
        verbose_name = "Instructor"
        verbose_name_plural = "Instructors"

    def __str__(self):
        pass



class Course(models.Model):
    full_name = models.CharField(max_length=50)
    short_name = models.CharField(max_length=10)
    description = models.TextField()
    instructors = models.ManyToManyField(Instructor)
    start_date = models.DateField()
    end_date = models.DateField()

    class Meta:
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        pass
