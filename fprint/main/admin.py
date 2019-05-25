from django.contrib import admin
from .models import Question, PrintingOrder, ModelingOrder

admin.site.register(Question)
admin.site.register(PrintingOrder)
admin.site.register(ModelingOrder)
