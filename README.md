# Autoscreen-AI
🚀 AutoScreen AI – An intelligent, AI-powered resume screening system built using AWS services like Textract, Comprehend, and DynamoDB. Extracts key resume fields automatically, with plans to integrate Amazon Bedrock/OpenAI for even smarter parsing.


**AutoScreen AI** is an intelligent, cloud-based resume screening project designed to automate the process of extracting key information from candidate resumes using AWS services.

It uses:
- **Amazon Textract** to extract raw text from PDF resumes.
- **Amazon Comprehend** to analyze and detect meaningful information like name, email, skills, etc.
- **AWS Lambda** to coordinate the process and structure the data.
- **Amazon DynamoDB** to store the extracted structured data.

---

## 💡 Key Features

- 📄 Upload resumes to an S3 bucket (PDF format).
- ⚙️ Fully automated Lambda function processes the resume.
- 🧠 AI-driven field extraction using NLP from Amazon Comprehend.
- 🗃️ Extracted data stored neatly in DynamoDB (as JSON).
- ⬇️ Downloadable results in CSV format.
- 🔜 **Upcoming**: Integration with **Amazon Bedrock/OpenAI API** to enhance accuracy in field detection like education, experience, and achievements.

---

## 🧪 Sample Resume Used

**Resume:** Sasha Wagner  
**Used for:** Demo Output  
**File:** [`Sasha_Wagner_Output.csv`](./Sasha_Wagner_Output.csv)

---

## 📷 Output Screenshot

Here’s a glimpse of the real output extracted from the resume:

> _Insert a clean screenshot here showing your CSV opened in Excel or any tool in a tabular format, preferably with auto-adjusted row height and wrapped text._

---

## 📁 Files in This Repository

| File Name                | Description                                      |
|-------------------------|--------------------------------------------------|
| `README.md`             | This file explaining the project.                |
| `Sasha_Wagner_Output.csv` | Extracted CSV from Sasha Wagner's resume.       |
| `OtherResume_Output.csv` | Another sample resume result.                   |
| `resumeGPT.py`          | Lambda function that powers this resume screener.|

---

## 🎯 Future Enhancements

We plan to integrate:
- ✅ **Amazon Bedrock** or **OpenAI API** for even more accurate field detection.
- 📊 Dashboard insights on candidate data.
- 📬 Auto-email triggers after screening.

---

## 🤖 How It Works – Project Flow

1. Resume (PDF) uploaded to **S3 Bucket**.
2. **Lambda function** is triggered.
3. **Textract** reads the text from the resume.
4. **Comprehend** analyzes and extracts entities like Name, Email, Skills, etc.
5. Final structured data is saved in **DynamoDB**.
6. Data is exported as CSV for viewing or processing.

---

## 📌 Technologies Used

- AWS S3
- AWS Lambda (Python 3.9)
- Amazon Textract
- Amazon Comprehend
- Amazon DynamoDB

---

## 🧠 Contact

For feedback, improvements, or ideas – feel free to connect!

---

