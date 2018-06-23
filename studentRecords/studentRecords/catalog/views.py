from django.core.cache import cache
from django.shortcuts import render

# Create your views here.
from .models import Student, Subject, Score

from django.contrib.auth.decorators import login_required

cache_key_stu = "key_students"
cache_key_sub = "key_subjects"
cache_time = 600

def index(request):
    """
    View function for home page of site.
    """
    students = cache.get(cache_key_stu) # returns None if no key-value pair
    stu_cache_flag = "yes"
    if not students:
        stu_cache_flag = "no"
        students = Student.objects.all().order_by("id")
        cache.set(cache_key_stu, students, cache_time)

    sub_cache_flag = "yes"
    subjects = cache.get(cache_key_sub) # returns None if no key-value pair
    if not subjects:
        sub_cache_flag = "no"
        subjects = Subject.objects.all().order_by("id")
        cache.set(cache_key_sub, subjects, cache_time)

    num_student = students.count()
    num_subject = subjects.count()

    
    # Render the HTML template index.html with the data in the context variable
    return render(
        request,
        'index.html',
        context={'num_student':num_student,'num_subject':num_subject,
                 'stu_cache_flag':stu_cache_flag, 'sub_cache_flag':sub_cache_flag},
    )

# class-based views
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

class StudentListView(LoginRequiredMixin, generic.ListView):
    model = Student
    def get_queryset(self):
        students = cache.get(cache_key_stu) # returns None if no key-value pair
        stu_cache_flag = "yes"
        if not students:
            stu_cache_flag = "no"
            students = Student.objects.order_by("id")
            cache.set(cache_key_stu, students, cache_time)
        return students
    

class StudentDetailView(LoginRequiredMixin, generic.DetailView):
    model = Student


class SubjectListView(LoginRequiredMixin, generic.ListView):
    model = Subject

    def get_queryset(self):
        subjects = cache.get(cache_key_sub) # returns None if no key-value pair
        sub_cache_flag = "yes"
        if not subjects:
            sub_cache_flag = "no"
            subjects = Subject.objects.order_by("id")
            cache.set(cache_key_sub, subjects, cache_time)
        return subjects

