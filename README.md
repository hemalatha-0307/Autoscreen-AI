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
|---------------------|-----------------------------------------------|
| Sasha Wagner Resume | |
| Other Sample Resume | ![Second Resume](images/second_resume.png)           |

---

## 📊 Output Screenshot

A quick look at the output structured data from DynamoDB, viewed in Excel format:

![DynamoDB Output Screenshot](images/output_screenshot.png)

> _Make sure your screenshot clearly shows properly wrapped text in columns._

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

- 📄 Upload resumes to an S3 bucket (PDF format).
- ⚙️ Fully automated Lambda function processes the resume.
- 🧠 AI-driven field extraction using NLP from Amazon Comprehend.
- 🗃️ Extracted data stored neatly in DynamoDB (as JSON).
- ⬇️ Downloadable results in CSV format.
- 🔜 **Upcoming**: Integration with **Amazon Bedrock/OpenAI API** to enhance accuracy in field detection like education, experience, and achievements.

---

## 📌 Technologies Used

- AWS S3
- AWS Lambda (Python 3.9)
- Amazon Textract
- Amazon Comprehend
- Amazon DynamoDB

---


## 📁 Files in This Repository

| File Name                | Description                                      |
|--------------------------|--------------------------------------------------|
| `README.md`              | This file with full project documentation.       |
| `results.csv`            | Output CSV from Sasha Wagner's resume.           |
| `selected.csv`           | Output CSV from Hal Feeney's resume.           |
| `lambda_function.py`     | Lambda function handling Textract + Comprehend.  |

---

## 🔮 Future Enhancements

✨ I am working on taking AutoScreen AI even further:
- 🤖 **LLM Integration using Amazon Bedrock** (or OpenAI): To extract fields like Education, Skills, and Experience more accurately            using foundation models.
- 📝 Improve detection of candidate achievements, certifications, and project descriptions using advanced NLP models.

---

## 🔗 Project Demo
👉 Check my LinkedIn post here: [LinkedIn Demo Post](https://www.linkedin.com/in/hemalatha-m-064190332?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)


---

