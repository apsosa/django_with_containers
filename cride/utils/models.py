from django.db import models

class CRideModel(models.Model):
    """Comparte Ride base model.
    CRideModel acts as an abstract base class from which every
    other model in the project will inherit. This class provides
    every table with the following attributes:
        + created (DateTime): Store the datetime the objects was created
        + modified (DateTime): Store the last datetime the objects was modified
    """
    created = models.DateTimeField(
        'created at',
        auto_now_add = True,
        help_text='Date time on which the object was ccreated.'
        )
    modified = models.DateTimeField(
        'modified at',
        auton_now = True,
        help_text='Date time on which the object was modified.'
        )
    class Meta:
        """Meta option."""
        abstract = True
        get_lasted_by = 'created'
        orderinng = ['-created', '-modified']

#Herencia
'''
-Abstracta : Exponen un molde

Se puede heredar los meta datos de un modeloo:
class Student(CRideModel):
    name = model.CharField()

    class Meta(CRideModel.META):
        db_table = 'student_role'
Ademas al hacer la herencia Django quita el abstract true y lo deja en false


-Proxy: Extiendende de una tabla ya existente, y sirve para agregar funcionalidad

Class Person(Model.Model):
   fist_name = models.Charfield()
   last_name = models.Charfield()

class MyPerson(Person):

    class Meta:
        proxy = True
    
    def say_hi(name):
        pass
'''