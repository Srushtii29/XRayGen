Bone Fracture Detection and Report Generation :
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


Credentials-

1.Signup Page:
![Screenshot 2024-05-02 005901](https://github.com/Srushtii29/XRayGen/assets/161300923/58198130-b7d8-4178-a3be-04be3802c315)

This image depicts a sign-up form for a website or application. The form is presented in a sleek and modern design with a dark background and contrasting blue and orange circular elements.
At the top of the form, there is a heading that says "Signup Here." Below the heading, there are several input fields where users can enter their information to create a new account:

Username: A text field where users can enter their desired username. In the example shown, the placeholder text "test@123" is displayed.
Email: A text field where users can enter their email address or phone number. No value is currently filled in this field.
Password: A password field where users can enter their desired password. The field is masked, showing only dots for the characters entered.
Confirm Password: Another password field where users need to re-enter their password to confirm it matches the initial password entry.

After filling out all the required information, users can click the "Signup" button to submit the form and create their account.
Additionally, there is a line of text at the bottom that says "I already have an account," which likely serves as a link or button to navigate to the login page for existing users.
The design incorporates circular shapes with contrasting colors (blue and orange) to create a visually appealing and modern look for the sign-up form.
Overall, this image represents a typical sign-up or registration page commonly found on websites or applications, where new users can enter their credentials to create an account and gain access to the platform's features and services.

2.Login Page:
![Screenshot 2024-05-02 005908](https://github.com/Srushtii29/XRayGen/assets/161300923/adccf8fe-a730-4085-8248-61d5a1291432)
The image represents a login form, which is typically accessed when a user already has an existing account on a website or application. This login page is likely the destination when a user clicks on the "I already have an account" link from the sign-up or registration page shown in the previous image.
The login form has a similar modern and sleek design with a dark background and contrasting blue and orange circular elements. At the top, the heading "Login Here" indicates that this form is for existing users to authenticate themselves and gain access to the platform.
The form contains two input fields:

Username: A text field where users can enter their registered username. In the example, the placeholder text "test@123" is displayed.
Password: A password field where users can enter their account password. As a security measure, the password characters are masked and displayed as dots.

After entering their username and password, users can click the "Log In" button to submit their credentials and access their account.
Additionally, there is a line of text at the bottom that says "Create an account," which likely serves as a link or button to navigate to the sign-up or registration page for new users who don't have an existing account yet.
The design maintains a consistent visual style with the previous sign-up form, utilizing circular shapes and contrasting colors to create an appealing and modern look for the login page.
Overall, this image represents the login page, which is a common component of most websites and applications. It allows existing users to authenticate themselves and access their accounts by entering their registered username and password credentials.
When a new user signs up through the registration form, their entered information (username, email, password, etc.) is likely sent to the server-side application, which then stores these details in the AWS database associated with the application. Similarly, when an existing user logs in, their provided credentials (username and password) are checked against the user data stored in the AWS database for authentication.

Website- 
![Screenshot 2024-05-02 010805](https://github.com/Srushtii29/XRayGen/assets/161300923/1692c57e-5194-4382-adeb-13fe5a3ee075)
This image indicates a image from the caurosel
Above image shows a step-by-step guide on "How to Use" the XRayGen application or service. It outlines six steps for generating bone X-ray reports:

Select document type: Choose the type of document or report you want to generate.
Fill basic info: Provide basic information about the person the report is for.
Upload JPG file: Upload the JPG image file of the X-ray or bone scan.
Click "Upload & Predict": After uploading the image, initiate the prediction or analysis process.
View generated report: Once the analysis is complete, you can view the generated report.
Download Report: Finally, you can download the generated report.
![Screenshot 2024-05-02 010832](https://github.com/Srushtii29/XRayGen/assets/161300923/2917c05f-aff6-4d2c-9c51-22332b74289f)
The above image appears to be the landing or home page of the XRayGen application. It promotes the feature of generating "Instant Bone X-ray Reports." The page highlights the following key points:

It allows users to unlock instant and comprehensive reports for their bone X-rays.
Users can easily navigate through various fracture types.
It offers a swift and efficient way to analyze bone imaging.

Selecting label-
![Screenshot 2024-05-02 010824](https://github.com/Srushtii29/XRayGen/assets/161300923/6766b9bc-0196-4a55-96da-a0f0f024d4a3)
![image](https://github.com/Srushtii29/XRayGen/assets/161300923/8b37a256-87be-4181-8f9c-1e8e3c7de645)

The images provided appears to be showing options for selecting the type of medical document or imaging study. In the first image, there are two options displayed - one seems to be an X-ray or radiographic image of a spine or vertebral column, and the other appears to be an X-ray or radiographic image of a chest or thoracic cavity showing the ribcage and lungs.
In this image below we can see various social media handles linked and email to be provided so me can regularly send new updates.

In the second image, there is a text label stating "Broken Bones X-ray" which suggests that this option represents X-ray imaging studies related to fractures or broken bones. After that you can click on submit.



Patient Information Form-
![image](https://github.com/Srushtii29/XRayGen/assets/161300923/d99aa80e-7af1-46c7-a4fe-d30775a162d9)
The patient needs to fill the patient information in this form
The image appears to be a user interface for a medical application or software aimed at analyzing X-ray images and documenting patient information related to bone fractures or injuries. The interface consists of several fields and options that allow healthcare professionals or medical practitioners to input relevant data for a specific patient.


Upload X-ray Image:
The interface provides a section to upload an X-ray image file of the patient. This is likely the starting point for the analysis process, where the medical professional can upload the relevant X-ray image for examination.
Patient Name:
This field allows the user to enter the patient's name, which is essential for proper identification and record-keeping purposes.
Gender:
A drop-down menu is provided to select the patient's gender, either "Male" or "Female." This information can be useful for demographic analysis and tailoring certain medical considerations based on gender.
Age:
An input field is available to enter the patient's age. Age is a critical factor in medical diagnosis and treatment, as it can influence various aspects of patient care, such as bone density, healing rates, and potential complications.
Consulting Doctor:
This field allows the user to enter the name of the consulting doctor or healthcare professional responsible for the patient's care. This information can be useful for maintaining proper medical records and facilitating communication among healthcare providers.
Fracture Location:
One of the most important sections of the interface is the "Fracture Location" area, which provides a comprehensive list of bone options. The user can select the specific bone or body part where the fracture or injury is located. The options include:

Thigh Bone
Shin Bone
Calf Bone
Upper Arm Bone
Forearm Bone
Wrist Bone
Ankle Bone
Palm Bone
Foot Bone
Skull Bone
Shoulder Bone
Hip Bone
Kneecap
Spine Bone
Tailbone

Accurately identifying the fracture location is crucial for proper diagnosis, treatment planning, and documentation purposes.
Upload Image:
Finally, there is an "Upload Image" button, which likely initiates the process of uploading the X-ray image and submitting the entered patient information for analysis or storage in the medical database.

Overall, this user interface appears to be designed for healthcare professionals to efficiently analyze X-ray images, document patient details, and identify fracture locations in a structured manner. The collected information can be used for diagnosis, treatment planning, and maintaining comprehensive medical records for each patient.

Console(Django Server)-
![Screenshot 2024-05-02 012929](https://github.com/Srushtii29/XRayGen/assets/161300923/c8c7046b-ba82-426d-95ce-b60dab583823)
This output appears to be from a server log or console, providing information about HTTP requests and responses, as well as output related to a machine learning model's prediction.
Here's a breakdown of the information:

HTTP Requests and Responses:

The log entries show various GET and POST requests being made to different endpoints, such as /static/Logo.jpeg, /take_input/, /take_input/upload_broken_bones/.
Each request includes the HTTP method (GET or POST), the endpoint path, the HTTP version (HTTP/1.1), the response status code (200 for successful requests), and the response payload size in bytes.
There are also entries indicating "Broken pipe" errors, which typically occur when the connection between the client and server is unexpectedly terminated.


Machine Learning Model Prediction:

The log includes output related to a machine learning model's prediction.
The predicted class label is "Oblique".
Probabilities or scores are provided for three classes: "Comminuted" (0.29), "Oblique" (0.37), and "Transverse" (0.33).
This output suggests that the machine learning model is being used to classify something, potentially related to bone fractures or images, into three categories: Comminuted, Oblique, and Transverse.


Performance Metrics:

The line "1/1 0s 165ms/step" appears to be indicating some performance metric, possibly the time taken to process a single step or iteration during training or inference.



Based on the information provided in the log, it seems to be related to a web application or server that handles requests for static files (like images) and processes input data, potentially related to bone fracture analysis. The application appears to be using a machine learning model to classify the input data into different categories (Comminuted, Oblique, Transverse) and provide prediction probabilities for each class.
However, without more context about the specific application or project, it's difficult to provide a more detailed explanation.

Example of filled form and the generated report
![Screenshot 2024-05-02 012912](https://github.com/Srushtii29/XRayGen/assets/161300923/368c79b2-a552-4707-9dc7-926b61797942)
![Screenshot 2024-05-02 013022](https://github.com/Srushtii29/XRayGen/assets/161300923/058124c8-7482-4a49-9ca4-1624237afb46)
The information provided in the user interface form for uploading X-ray images and entering patient details was used to generate this detailed medical report about the patient's fracture findings and recommended course of action. The report summarizes the key patient information entered through the form, such as the patient's name, age, gender, and consulting doctor, along with the analysis and assessment based on the uploaded X-ray image showing an oblique fracture of the tibia.

Note:
Change the following variable with your own anyscale api key of mistral-7b-it model:
ANYSCALE_API_KEY = "esecret_5dq4ssflzpfqpcyl2c1zk5sqy4"
