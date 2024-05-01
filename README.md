Bone Fracture Detection and Report Generation
This project is a Django-based web application that allows users to upload X-ray images of broken bones and automatically generates a medical report based on the detected fracture type. The application utilizes machine learning models, including a deep learning model (my_model.h5) for classifying fractures as oblique, transverse, or comminuted, and provides a detailed report with relevant information for healthcare professionals.
Features

Upload X-ray images of broken bones
Automatic fracture classification using machine learning models, including a deep learning model (my_model.h5) for classifying fracture types
Generation of a comprehensive medical report in PDF format
Inclusion of patient information and consulting doctor details

Usage

Run the Django development server.
Open your web browser and navigate to the provided URL.
Select the "Broken Bones" option from the document type selection page.
Upload an X-ray image of a broken bone.
Provide the necessary patient information, such as name, gender, age, and consulting doctor.
Click the "Submit" button to initiate the fracture classification and report generation process.
Once the process is complete, the application will display the generated medical report in PDF format.

Contributing
Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.
License
This project is licensed under the MIT License.
Acknowledgments

Django - The web framework used for this project.
TensorFlow - The machine learning library used for fracture classification.
AnyScale - The AI platform used for generating the medical report.
ReportLab - The library used for generating PDF reports.

Pages
Signup Page:
![Screenshot 2024-05-02 005901](https://github.com/Srushtii29/XRayGen/assets/161300923/58198130-b7d8-4178-a3be-04be3802c315)
