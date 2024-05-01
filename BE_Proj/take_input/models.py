from django.db import models

# Create your models here.
# models.py



class BrokenBonesXRay(models.Model):
    patient_name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10, choices=(('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')))
    age = models.IntegerField()
    consulting_doctor = models.CharField(max_length=100)
    location = models.CharField(max_length=100)  # Assuming this will store the fracture location

    image = models.ImageField(upload_to='xray_images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
