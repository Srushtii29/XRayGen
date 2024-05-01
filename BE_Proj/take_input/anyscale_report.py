import openai
import io
from .models import BrokenBonesXRay
from reportlab.pdfgen import canvas
from .image_utils import  classify_fracture
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.platypus import PageTemplate, Frame

import os 

ANYSCALE_API_KEY = "esecret_5dq4ssflzpfqpcyl2c1zk5sqy4"
ANYSCALE_API_BASE_URL = "https://api.endpoints.anyscale.com/v1"

example = '''\[INST\]Here is an example of medical report/findings from a medical image generated from keywords: keywords: { "fracture_type": { "category": "long bone", "sub_category": "tebia", "fracture_subtype": "extra articular", "specific_subtype": "spiral" } report : "Clinical History: The patient presented with localized pain and tenderness in the left lower extremity following trauma.Findings: Imaging of the left lower extremity was performed. The study reveals a fracture involving the proximal aspect of the tibia, classified as an extra-articular fracture. The fracture pattern is characterized as a spiral fracture. These findings are consistent with a spiral extra-articular fracture of the proximal tibia.Impressions: Further clinical correlation and management, including potential orthopedic intervention, are recommended. Consultation with an orthopedic specialist for further evaluation and management planning is advised. Consideration for additional imaging studies, such as CT or MRI, if warranted for further characterization of the fracture pattern and assessment of soft tissue involvement is also recommended. Initiation of appropriate pain management and immobilization measures as indicated is essential.Conclusion: The imaging findings demonstrate a spiral extra-articular fracture of the proximal tibia. Clinical correlation and orthopedic consultation are advised for further management.\[/INST\]" \[INST\] Similarly,based on the given example, generate a radiological medical report for the following keywords. \[/INST\]'''



class CustomCanvas(canvas.Canvas):
    def __init__(self, buffer, *args, **kwargs):
        # Create a dummy filename
        dummy_filename = "dummy.pdf"
        canvas.Canvas.__init__(self, dummy_filename, *args, **kwargs)
        self.buffer = buffer
        self._pageSize = letter  # Set the page size directly

    def showPage(self):
        self._startPage()

    def save(self):
        self._doc.SaveToFile(self.buffer, self)


def get_fracture_severity(sub_category, age):

    severity_map = {
        "humorous": "Moderate",
        "tibia": "Moderate",
        "femur": "Severe",
        "radiusalma": "Moderate",
        "febula": "Moderate",
        "knee": "Moderate",
        "anabolic different ways": "Moderate",
        "spiral": "Mild",
        "greenstick": "Mild",
        "comminuted": "Severe",
        "segmented": "Severe",
        "transverse": "Mild",
        "oblique": "Mild",
        "rest": "Mild",
        "avulsion": "Moderate",
        "impacted": "Moderate"
    }
    if sub_category in severity_map:
      if age > 80:
          if severity_map[sub_category] == "Mild":
              return "High"
          elif severity_map[sub_category] == "Moderate":
              return "High"
          else:
              return severity_map[sub_category]
      elif age > 70:
          if severity_map[sub_category] == "Mild":
              return "Moderate"
          elif severity_map[sub_category] == "Moderate":
              return "High"
          else:
              return severity_map[sub_category]
      elif age > 50:
          if severity_map[sub_category] == "Mild":
              return "Moderate"
          else:
              return severity_map[sub_category]
      else:
          return severity_map[sub_category]
    else:
      return "Normal"


def generate_report(predicted_class_label,logo_path,file_path=None):
    latest_instance = BrokenBonesXRay.objects.latest('id')

    # Extract the required information from the instance
    keywords = {
        "fracture_type": {
            "category": classify_fracture(latest_instance.location)[0],
            "sub_category": classify_fracture(latest_instance.location)[1],
            "specific_subtype": predicted_class_label,
            "fracture_subtype": "extra articular",  # You can customize this based on your requirements
        }
    }
    # print(keywords)
    patient_info = {
        "patient_name": latest_instance.patient_name,
        "gender": latest_instance.gender,
        "age": str(latest_instance.age),
        "consulting_doctor": latest_instance.consulting_doctor
    }



    openai.api_key = ANYSCALE_API_KEY
    openai.api_base = ANYSCALE_API_BASE_URL

    prompt = f"<s>\[INST\] {example} : {keywords} \[/INST\]"

    chat_completion = openai.ChatCompletion.create(
        model="mistralai/Mistral-7B-Instruct-v0.1",
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": prompt}],
        temperature=0.6,
        stream=True
    )

    generated = ""
    for message in chat_completion:
        delta_content = message.choices[0].delta.get("content", "")
        generated += delta_content

    fracture_subtype = keywords['fracture_type']['sub_category']
    age = int(patient_info['age'])
    severity = get_fracture_severity(fracture_subtype, age)

    
    pdf_filename = patient_info["patient_name"] + "_report" +".pdf"
    
    doc = SimpleDocTemplate(file_path + pdf_filename, pagesize=letter)
    
    styles = getSampleStyleSheet() 
    logo = Image(logo_path, width=100, height=100)
    logo.hAlign = "RIGHT"


    patient_info_lines = [
        f"Name: {patient_info['patient_name']}",
        f"Gender: {patient_info['gender']}",
        f"Age: {patient_info['age']}",
        f"Consulting Doctor: {patient_info['consulting_doctor']}"
    ]

    normal_style = styles["Normal"]
    normal_style.alignment = 4
    medical_findings = [para.strip() for para in generated.split('\n\n') if para.strip()]

    report_paragraphs = [
        Paragraph("Patient Information:", styles['Heading1']),
        *[Paragraph(info, styles['Normal']) for info in patient_info_lines],
        Spacer(1, 12),
        Paragraph("Medical Findings:", styles['Heading1']),
        *[Paragraph(para, normal_style) for para in medical_findings],
        Spacer(1, 12),
        Paragraph("Severity:", styles['Heading1']),
        Paragraph(severity, styles['Normal']),
        Spacer(1, 12),
        Spacer(1, 12),
        Spacer(1, 12),
        Spacer(1, 12)
    ]

    disclaimer = ("\n\n*Please note that this report is provided as a preliminary analysis based on the information provided and available data. "
                  "We strongly advise consulting with a qualified healthcare professional promptly for further evaluation and confirmation.")


    def add_footer(canvas, doc, disclaimer):
        canvas.saveState()
        footer = Paragraph(disclaimer, styles["Italic"])
        w, h = footer.wrap(doc.width, doc.bottomMargin)
        footer.drawOn(canvas, doc.leftMargin, h)
        canvas.restoreState()

    doc.build([logo] + report_paragraphs, onFirstPage=lambda canvas, doc: add_footer(canvas, doc, disclaimer),
              onLaterPages=lambda canvas, doc: add_footer(canvas, doc, disclaimer))

    return True , pdf_filename
