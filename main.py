import streamlit as st
import os
import google.generativeai as genai
from moviepy.editor import VideoFileClip
import whisper
import tempfile

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

prompt = """
You are a video summarizer. You will be taking the transcript text and summarizing the entire video, providing the important points for claiming insurance. 
The summary must cover the following points and provide each detail on a new line:

Here's a common template for summarizing Car, Home Renovation, and Medical Insurance Claims. This template is designed to ensure that essential details unique to each type of claim are captured while maintaining a consistent structure. **Ensure every detail appears on a new line.**

Insurance Claim Summary:
- Claim Number: [CLAIM_NUMBER]
- Policyholder Name: [POLICYHOLDER_NAME]
- Policy Number: [POLICY_NUMBER]
- Claim Submission Date: [CLAIM_SUBMISSION_DATE]
- Type of Claim: [CLAIM_TYPE] (e.g., Car Insurance, Home Renovation, Medical Insurance)
- Incident Date: [INCIDENT_DATE]

Section 1: Claim-Specific Information:
For Car Insurance:
- Vehicle Information:
  - Make: [VEHICLE_MAKE]
  - Model: [VEHICLE_MODEL]
  - Year: [VEHICLE_YEAR]
  - License Plate Number: [LICENSE_PLATE]
  - Location of Incident: [CAR_INCIDENT_LOCATION]
  - Damage Area: [DAMAGE_AREA] (e.g., front bumper, rear passenger door, etc.)
  - Type of Damage: [DAMAGE_TYPE] (e.g., dent, scratch, cracked windshield)
  - Cause of Damage: [CAUSE_OF_DAMAGE] (e.g., collision, hit stationary object, etc.)
  - Severity of Damage: [DAMAGE_SEVERITY] (e.g., minor, moderate, severe)

For Home Renovation Insurance:
- Property Address: [PROPERTY_ADDRESS]
- Type of Property: [PROPERTY_TYPE] (e.g., single-family home, apartment, etc.)
- Renovation Type: [RENOVATION_TYPE] (e.g., flooring, painting, structural work, etc.)
- Location of Damage: [DAMAGE_LOCATION] (e.g., living room, kitchen, roof, etc.)
- Type of Damage: [DAMAGE_TYPE] (e.g., water damage, structural crack, etc.)
- Cause of Damage: [CAUSE_OF_DAMAGE] (e.g., poor workmanship, water leakage, etc.)
- Severity of Damage: [DAMAGE_SEVERITY] (e.g., minor, moderate, severe)

For Medical Insurance:
- Patient Name: [PATIENT_NAME]
- Relationship to Policyholder: [RELATIONSHIP_TO_POLICYHOLDER] (e.g., self, spouse, child)
- Date of Birth: [PATIENT_DOB]
- Hospital/Clinic Name: [HOSPITAL_NAME]
- Date of Admission: [ADMISSION_DATE]
- Date of Discharge: [DISCHARGE_DATE]
- Diagnosis/Medical Condition: [MEDICAL_CONDITION] (e.g., heart disease, broken leg, etc.)
- Type of Treatment/Procedure: [TREATMENT_TYPE] (e.g., surgery, medication, therapy)
- Prescribed Medications: [PRESCRIBED_MEDICATIONS]

Section 2: Narrative Summary:
The policyholder described the incident, renovation, or medical issue as follows:
"[SUMMARY_OF_NARRATIVE]"

Section 3: Supporting Documentation:
For Car Insurance:
- Photographic Evidence of Vehicle Damage: [PHOTO_EVIDENCE_YES_NO]
- Police Report Filed? [POLICE_REPORT_YES_NO]
- Witnesses Present? [WITNESSES_YES_NO]

For Home Renovation Insurance:
- Photographic Evidence of Damage: [PHOTO_EVIDENCE_YES_NO]
- Contractor Details:
  - Contractor Name: [CONTRACTOR_NAME]
  - Contractor License Number: [CONTRACTOR_LICENSE]
- Receipts/Invoices for Work: [INVOICES_YES_NO]
- Warranties on Work Done: [WARRANTY_YES_NO]

For Medical Insurance:
- Medical Reports Attached? [MEDICAL_REPORTS_YES_NO]
- Invoices/Bills Attached? [BILLS_YES_NO]
- Discharge Summary Attached? [DISCHARGE_SUMMARY_YES_NO]
- Prescription Copies Attached? [PRESCRIPTION_YES_NO]

Section 4: Claim Summary:
- Total Claim Amount: [TOTAL_CLAIM_AMOUNT]
- Amount Covered by Insurance: [COVERED_AMOUNT]
- Out-of-Pocket Expenses: [OUT_OF_POCKET]

Section 5: Next Steps:
- Further Assessment Required? [FURTHER_ASSESSMENT_YES_NO]

If anything is not provided, just say 'Not provided'.
Stick to the provided format of the summary.
Provide each detail on a new line.

Please provide the summary of the text given here:
"""

# Function to extract audio from video and transcribe using Whisper
def extract_audio_and_transcript(video_file_path):
    try:
        # Extract audio from the video
        video = VideoFileClip(video_file_path)
        audio_path = "temp_audio.wav"
        video.audio.write_audiofile(audio_path)
        
        # Load the Whisper model
        model = whisper.load_model("base")
        
        # Transcribe the audio
        transcript_result = model.transcribe(audio_path)
        transcript_text = transcript_result['text']

        return transcript_text

    except Exception as e:
        raise e

# Function to get summary using Google Gemini Pro
def generate_gemini_content(transcript_text, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt + transcript_text)
    return response.text

st.title("Video to Summary Generator")

# Upload video file
uploaded_video = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov", "mkv"])

if uploaded_video is not None:
    # Save the uploaded video to a temporary file
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_video_file:
        temp_video_file.write(uploaded_video.read())
        video_file_path = temp_video_file.name
    
    # Display the video
    st.video(video_file_path)

    # Extract and display the transcript
    if st.button("Get Summary"):
        transcript_text = extract_audio_and_transcript(video_file_path)

        if transcript_text:
            summary = generate_gemini_content(transcript_text, prompt)
            st.markdown("## Detailed Notes:")
            st.write(summary)
