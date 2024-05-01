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
![Screenshot 2024-05-02 010824](https://github.com/Srushtii29/XRayGen/assets/161300923/6766b9bc-0196-4a55-96da-a0f0f024d4a3)
The above image appears to be the landing or home page of the XRayGen application. It promotes the feature of generating "Instant Bone X-ray Reports." The page highlights the following key points:

It allows users to unlock instant and comprehensive reports for their bone X-rays.
Users can easily navigate through various fracture types.
It offers a swift and efficient way to analyze bone imaging.
