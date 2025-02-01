# AI-Resume-Screening-App
This AI Resume Screening App uses Machine Learning models to categorize resumes into job roles. It supports PDF, DOCX, and TXT formats, extracts text, and predicts the most suitable job category based on the content.
# 📄 AI Resume Screening App  

## 🚀 Overview  
The **AI Resume Screening App** is a machine learning-powered application that categorizes resumes into job roles based on their content. It supports **PDF, DOCX, and TXT** file formats, extracts text, and predicts the **most relevant job category** using trained AI models.  

## 📌 Features  
- ✅ **Smart Resume Classification** – Automatically assigns job categories based on resume content.  
- 📂 **Multiple File Formats** – Supports **PDF, DOCX, and TXT** files.  
- 📝 **Text Extraction** – Extracts text from uploaded resumes using AI-based processing.  
- 🤖 **Machine Learning Models** – Uses **KNN, SVM, Random Forest, Logistic Regression, and Naïve Bayes** for predictions.  
- 🎨 **Interactive UI** – Powered by **Streamlit** for a smooth and user-friendly experience.  
- ⚡ **Real-Time Predictions** – Fast and accurate categorization of resumes.  

## 🛠 Tech Stack  
- **Programming Language**: Python  
- **Machine Learning Models**: KNN, SVM, Random Forest, Logistic Regression, Naïve Bayes  
- **Feature Engineering**: TF-IDF Vectorization  
- **Frontend Framework**: Streamlit  
- **Libraries**:  
  - `scikit-learn` – ML models  
  - `streamlit` – Web-based UI  
  - `PyPDF2` – PDF text extraction  
  - `python-docx` – DOCX text extraction  
  - `pickle` – Model storage  

## 📂 Project Structure  
📁 AI-Resume-Screening/ │── app.py # Streamlit frontend │── model_training.py # ML model training script │── clf.pkl # Saved ML model │── tfidf.pkl # TF-IDF Vectorizer │── encoder.pkl # Label Encoder │── requirements.txt # Dependencies └── README.md # Documentation

markdown
Copy
Edit

## 🚀 How It Works  
1. **Upload a Resume** – Users can upload resumes in **PDF, DOCX, or TXT** format.  
2. **Text Extraction** – The app extracts text from the uploaded document.  
3. **AI Processing** – The extracted text is processed using **TF-IDF vectorization** and classified using a **trained ML model**.  
4. **Job Category Prediction** – The app predicts and displays the most relevant job category.  

## 🎯 Use Cases  
- **HR & Recruiters** – Automate resume screening for faster hiring decisions.  
- **Job Seekers** – Get insights into how AI categorizes your resume.  
- **Career Platforms** – Enhance job-matching capabilities.  

## 📸 Screenshots  
### ✅ Uploading a Resume  
![Upload Resume](./screenshots/upload.png)  

### 🎯 AI Predicts the Resume Category  
![Prediction](./screenshots/prediction.png)  

## 🏆 Future Improvements  
- 🔍 Implement **Deep Learning models (BERT, GPT, LLMs)** for better accuracy.  
- 📊 Improve **resume ranking** based on job descriptions.  
- 🤝 Add **explainable AI insights** for better interpretation of results.  

## 🤝 Contributing  
Contributions are **welcome**! If you'd like to improve the project:  
1. **Fork the repo**  
2. **Create a feature branch** (`feature-new-idea`)  
3. **Commit your changes**  
4. **Open a Pull Request**  

## 📜 License  
This project is licensed under the **MIT License**.  

---

💡 **If you find this project helpful, don't forget to ⭐ the repository!** 🚀  
