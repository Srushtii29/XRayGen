
from django.shortcuts import render, redirect
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework import viewsets
from .serializers import ImageUploadSerializer
from PIL import Image
from .anyscale_report import generate_report
# from io import BytesIO
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing.image import img_to_array
# from tensorflow.keras.applications.vgg16 import preprocess_input
from keras.preprocessing.image import img_to_array
from tensorflow.keras.applications.resnet50 import preprocess_input
import numpy as np
from .image_utils import classify_fracture,preprocess_image
import os
import tensorflow as tf
import cv2
from .models import BrokenBonesXRay 
from .image_utils import preprocess_image, classify_fracture
# from django.core.files.uploadedfile import InMemoryUploadedFile
from django.conf import settings

from django.http.response import HttpResponse

# Load the trained model

model_file = os.path.join(os.path.dirname(__file__), 'my_model.h5')
model = tf.keras.models.load_model(model_file)
# Define the classify_fracture function for fracture classification

# Define the viewset for bone condition prediction
class BoneConditionPredictionViewSet(viewsets.ViewSet):
    parser_classes = (MultiPartParser,)

def create(self, request):
    serializer = ImageUploadSerializer(data=request.data)

    if serializer.is_valid():
        uploaded_image = serializer.validated_data['image']
        fracture_location = request.POST.get('location')

        try:
            preprocessed_image = preprocess_image(uploaded_image)
            predicted_probabilities = model.predict(preprocessed_image)
            class_labels = ['Comminuted', 'Oblique', 'Transverse']  # Adjust based on your model
            predicted_class_index = np.argmax(predicted_probabilities)
            predicted_class_label = class_labels[predicted_class_index]
            fracture_type = classify_fracture(fracture_location)
            keywords = {
                    "fracture_type": {
                        "category": fracture_type[0],
                        "sub_category": fracture_type[1],
                        "specific_subtype": predicted_class_label,
                        "fracture_subtype": "extra articular",
                    }
            }

            # Call the generate_report function with the predicted_class_label
            pdf_data = generate_report(keywords)
                # Render a template with the PDF data
            return Response(pdf_data, content_type='application/pdf')

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Define the remaining views for document type selection and broken bones upload
# (These are kept as is without modifications for simplicity)
def select_document_type(request):
    if request.method == 'POST':
        selected_type = request.POST.get('document_type')
        if selected_type == 'broken_bones':
            return redirect('upload_broken_bones')
        elif selected_type == 'pneumonia_xray':
            return redirect('upload_pneumonia_xray')
    return render(request, 'take_input/select_document_type.html')

def upload_broken_bones(request):
    if request.method == 'POST':
        uploaded_image = request.FILES['image']
        fracture_location = request.POST.get('location')
        patient_name = request.POST.get('patient_name')
        gender = request.POST.get('gender')
        age = request.POST.get('age')
        consulting_doctor = request.POST.get('consulting_doctor')
        
        # get_probablity(image,fracture_location,patient_details)


        # Preprocess the uploaded image
        preprocessed_image = preprocess_image(uploaded_image)

        # Classify the fracture based on the location
        classification = classify_fracture(fracture_location)

        # Perform the prediction
        predicted_probabilities = model.predict(preprocessed_image)

        # Get the class labels
        class_labels = ['Comminuted', 'Oblique', 'Transverse']  # Adjust this based on your model
        # Get the predicted class label based on the highest probability
        predicted_class_index = np.argmax(predicted_probabilities)
        predicted_class_label = class_labels[predicted_class_index]

        # Optionally, get the probabilities for each class
        probability_dict = {class_labels[i]: predicted_probabilities[0][i] for i in range(len(class_labels))}
        print(f"Predicted class label: {predicted_class_label}")
        print("Probabilities:")
        for label, probability in probability_dict.items():
            print(f"{label}: {probability:.2f}")
        broken_bones_xray = BrokenBonesXRay.objects.create(
            patient_name=patient_name,
            gender=gender,
            age=age,
            consulting_doctor=consulting_doctor,
            location=fracture_location,
            image=uploaded_image  # You might need to adjust this depending on your model
        )
        prefix_path = 'https://' if request.is_secure() else 'http://' 
        prefix_path += request.get_host() + settings.STATIC_URL
        # print(prefix_path)
        logo_path =  prefix_path  + "logo.jpeg"
        file_path = "take_input/static/reports/" 
        pdf_success,file_name = generate_report(predicted_class_label,logo_path,file_path=file_path)

        context = {
            'predicted_class_label': predicted_class_label,
            'probabilities': probability_dict,
            'patient_name': patient_name,
            'gender': gender,
            'age': age,
            'pdf_path': prefix_path + 'reports/' + file_name, 
            'consulting_doctor': consulting_doctor,
        }
        if pdf_success:        
            return redirect(prefix_path + 'reports/' +file_name)
        else:
            # RETURN SOME ERROR PAGE......
            return render(request, 'take_input/upload_broken_bones.html', context)
    fracture_locations = [
        'thigh_bone', 'shin_bone', 'calf_bone', 'upper_arm_bone', 'forearm_bone',
        'wrist_bone', 'ankle_bone', 'palm_bone', 'foot_bone', 'skull_bone',
        'shoulder_bone', 'hip_bone', 'kneecap', 'spine_bone', 'tailbone'
    ]
    context = {'fracture_locations': fracture_locations}
    return render(request, 'take_input/upload_broken_bones.html', context)
def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("The passwords arent matching each other!")
        else :
            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
        
        return redirect('login')
        
    return render(request,'signup.html')
def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('select_document_type')
        else:
            return HttpResponse("Invalid User!")
    return render(request,'login.html')