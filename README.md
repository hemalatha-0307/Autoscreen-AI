# Autoscreen-AI
🚀 AutoScreen AI – An intelligent, AI-powered resume screening system built using AWS services like Textract, Comprehend, and DynamoDB. Extracts key resume fields automatically, with plans to integrate Amazon Bedrock/OpenAI for even smarter parsing.

---

This system utilizes:
- 🗂️ **Amazon Textract** for extracting text from PDF resumes  
- 🧠 **Amazon Comprehend** for NLP-based field/entity detection  
- 🗃️ **DynamoDB** to store structured data  
- 📤 **CSV output** for recruiters to download and review  
- 🔄 Future integration with **Amazon Bedrock** or **OpenAI API** to improve context-aware data extraction

---

## 💼 What AutoScreen AI Can Do

✔️ Auto-extracts fields like:
- Name  
- Email & Phone  
- Education  
- Work Experience  
- Projects  
- Certifications  
- Languages Known  
- Achievements

✔️ No manual parsing needed  
✔️ Structured resume insights in tabular format  
✔️ Ready for HR analytics or filtering  
✔️ Output stored in **DynamoDB** and downloadable as `.csv`

---

## 🧪 Sample Resumes Used

Here are the resumes that were analyzed using AutoScreen AI:

| Resume Name         | Image Preview                                |
|---------------------|----------------------------------------------|
| Sasha Wagner Resume | ![Sasha](Sasha%20Wagner.png)   | 
| Hal Feeney Resume   | ![Hal](Hal%20Feeney.png)       |

---

## 📊 Output Screenshot

A quick look at the output structured data from DynamoDB:

![DynamoDB Output Screenshot](DynamoDB%20table.png)

---

## ⚙️ How It Works – Project Flow

1. Resume (PDF) uploaded to **S3 Bucket**.
2. **Lambda function** is triggered.
3. **Textract** reads the text from the resume.
4. **Comprehend** analyzes and extracts entities like Name, Email, Skills, etc.
5. Final structured data is saved in **DynamoDB**.
6. Data is exported as CSV for viewing or processing.

---

## 💡 Key Features
  🚀 End-to-End Automation – No manual intervention needed; resumes are auto-processed from upload to output.
  🧠 AI-Powered Analysis – Uses Amazon Comprehend to intelligently extract relevant fields like name, email, skills, education, and more.
  📦 Structured Data Storage – Cleanly stores extracted data in DynamoDB for fast access and scalability.
  📊 Recruiter-Ready Output – Generates CSV files that can be directly used for filtering or analysis.
  🔐 Secure & Scalable – Built on AWS cloud infrastructure ensuring data security and seamless scaling for multiple resumes.

---

## 📌 Technologies Used

- AWS S3
- AWS Lambda (Python 3.9)
- Amazon Textract
- Amazon Comprehend
- Amazon DynamoDB

---

## 📁 Files in This Repository

| File Name                  | Description                                      |
|----------------------------|--------------------------------------------------|
| `README.md`                | This file with full project documentation.       |
| `Sasha Wagner results.csv` | Output CSV from Sasha Wagner's resume.           |
| `Hal feeney results.csv`   | Output CSV from Hal Feeney's resume.             |
| `lambda_function.py`       | Lambda function handling Textract + Comprehend.  |
| `Sasha Wagner.png`         | Sasha Wagner Resume.  |
| `Hal Feeney.png`           | Hal Feeney Resume .  |
| `DynamoDB table.png`       | Output DynamoDB table in AWS.  |

---

## 🔮 Future Enhancements

✨ I am working on taking AutoScreen AI even further:
- 🤖 **LLM Integration using Amazon Bedrock** (or OpenAI): To extract fields like Education, Skills, and Experience more accurately            using foundation models.
- 📝 Improve detection of candidate achievements, certifications, and project descriptions using advanced NLP models.

---

## 🔗 Project Demo
👉 Check my LinkedIn post here: [LinkedIn Demo Post](https://www.linkedin.com/in/hemalatha-m-064190332?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)

---

