import streamlit as st
import pickle
import docx  
import PyPDF2  
import re
import time

# Load pre-trained model and TF-IDF vectorizer
svc_model = pickle.load(open('clf.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))
le = pickle.load(open('encoder.pkl', 'rb'))


# Function to clean resume text
def cleanResume(txt):
    cleanText = re.sub('http\S+\s', ' ', txt)
    cleanText = re.sub('RT|cc', ' ', cleanText)
    cleanText = re.sub('#\S+\s', ' ', cleanText)
    cleanText = re.sub('@\S+', '  ', cleanText)
    cleanText = re.sub('[%s]' % re.escape("""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""), ' ', cleanText)
    cleanText = re.sub(r'[^\x00-\x7f]', ' ', cleanText)
    cleanText = re.sub('\s+', ' ', cleanText)
    return cleanText


# Function to extract text from PDF
def extract_text_from_pdf(file):
    pdf_reader = PyPDF2.PdfReader(file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


# Function to extract text from DOCX
def extract_text_from_docx(file):
    doc = docx.Document(file)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text + '\n'
    return text


# Function to extract text from TXT
def extract_text_from_txt(file):
    try:
        text = file.read().decode('utf-8')
    except UnicodeDecodeError:
        text = file.read().decode('latin-1')
    return text


# Function to handle file upload and extraction
def handle_file_upload(uploaded_file):
    file_extension = uploaded_file.name.split('.')[-1].lower()
    if file_extension == 'pdf':
        text = extract_text_from_pdf(uploaded_file)
    elif file_extension == 'docx':
        text = extract_text_from_docx(uploaded_file)
    elif file_extension == 'txt':
        text = extract_text_from_txt(uploaded_file)
    else:
        raise ValueError("Unsupported file type. Please upload a PDF, DOCX, or TXT file.")
    return text


# Function to predict the category of a resume
def pred(input_resume):
    cleaned_text = cleanResume(input_resume)
    vectorized_text = tfidf.transform([cleaned_text]).toarray()
    predicted_category = svc_model.predict(vectorized_text)
    predicted_category_name = le.inverse_transform(predicted_category)
    return predicted_category_name[0]  


# Streamlit app layout
def main():
    st.set_page_config(page_title="📄 Resume Category Predictor", page_icon="📄", layout="wide")

    # Sidebar with app description
    with st.sidebar:
        st.image("https://cdn-icons-png.flaticon.com/512/1256/1256650.png", width=100)
        st.title("Resume AI Classifier")
        st.markdown("💡 Upload a resume, and AI will predict the best job category for it!")
        st.info("Supports **PDF, DOCX, and TXT** files.")

    # Main section
    st.markdown("<h1 style='text-align: center;'>📝 Resume Category Prediction</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Upload your resume below to see its predicted job category.</p>", unsafe_allow_html=True)

    # File uploader
    uploaded_file = st.file_uploader("📂 Upload Resume", type=["pdf", "docx", "txt"], help="Upload a resume in PDF, DOCX, or TXT format.")

    if uploaded_file is not None:
        try:
            with st.spinner("📜 Extracting text from resume..."):
                resume_text = handle_file_upload(uploaded_file)
                time.sleep(2)  # Simulate processing delay
            st.success("✅ Successfully extracted the resume text!")

            # Show extracted text
            if st.checkbox("👀 Show extracted text", False):
                st.text_area("Extracted Resume Text", resume_text, height=250)

            # Predict category
            st.subheader("🔍 Predicted Job Category")
            with st.spinner("🤖 AI is analyzing the resume..."):
                time.sleep(2)  # Simulate AI processing delay
                category = pred(resume_text)
            
            # Display the result in a fancy box
            st.markdown(
                f"""
                <div style="background-color: #f4f4f4; padding: 15px; border-radius: 10px; text-align: center;">
                    <h2 style="color: #4CAF50;">🎯 {category} </h2>
                </div>
                """,
                unsafe_allow_html=True
            )

        except Exception as e:
            st.error(f"❌ Error processing the file: {str(e)}")


if __name__ == "__main__":
    main()
