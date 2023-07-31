from django.forms import ModelForm, Textarea
from django.contrib.admin.widgets import AdminDateWidget, AdminTimeWidget, AdminSplitDateTime
from .models import Task


class TaskForm(ModelForm):

    class Meta:
        model = Task
        fields = (
            "name",
            'description',
            'deadline',
            )

        widgets={
            "deadline": AdminSplitDateTime()

        }