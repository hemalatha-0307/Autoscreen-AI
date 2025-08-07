# Autoscreen-AI
🚀 AutoScreen AI – An intelligent, AI-powered resume screening system built using AWS services like Textract, Comprehend, and DynamoDB. Extracts key resume fields automatically, with plans to integrate Amazon Bedrock/OpenAI for even smarter parsing.


**AutoScreen AI** is an intelligent, cloud-based resume screening project designed to automate the process of extracting key information from candidate resumes using AWS services.

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
|---------------------|-----------------------------------------------|
| Sasha Wagner Resume | |
| Other Sample Resume | ![Second Resume](images/second_resume.png)           |

---

## 📊 Output Screenshot

A quick look at the output structured data from DynamoDB, viewed in Excel format:

![DynamoDB Output Screenshot](images/output_screenshot.png)

> _Make sure your screenshot clearly shows properly wrapped text in columns._

---

## 📁 Files in This Repository

| File Name                 | Description                                      |
|--------------------------|--------------------------------------------------|
| `README.md`              | This file with full project documentation.       |
| `Sasha_Wagner_Output.csv`| Output CSV from Sasha Wagner's resume.           |
| `OtherResume_Output.csv` | Output CSV from another sample resume.           |
| `lambda_function.py`     | Lambda function handling Textract + Comprehend.  |

---

## 🔮 Future Enhancements

✨ We're working on taking AutoScreen AI even further:

- 🔍 **Amazon Bedrock** / **OpenAI API** integration  
  → Smarter, more accurate field extraction using LLMs  
- 📊 Visual dashboards for recruiter filtering  
- 📬 Automated email notifications to recruiters/candidates  

---

## ⚙️ How It Works – Project Flow

```mermaid
graph TD
    A[PDF Resume Upload to S3] --> B[Lambda Triggered]
    B --> C[Amazon Textract Extracts Text]
    C --> D[Amazon Comprehend Performs NLP]
    D --> E[Structured Data Stored in DynamoDB]
    E --> F[Data Exported to CSV]

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
| `Sasha_Wagner_Output.csv | Extracted CSV from Sasha Wagner's resume.       |
| `OtherResume_Output.csv` | Another sample resume result.                   |
| `lambda_function.py`     | Lambda function that powers this resume screener.|

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

