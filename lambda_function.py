import boto3
import re
import json

s3 = boto3.client('s3')
textract = boto3.client('textract')
comprehend = boto3.client('comprehend')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('ResumeDetails')

# Simple helper to extract email
def extract_email(text):
    match = re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    return match.group(0) if match else "unknown@example.com"

# Simple helper to extract phone
def extract_phone(text):
    match = re.search(r"(\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4})", text)
    return match.group(0) if match else "Not Found"

# Helper for entity matching
def extract_entities(text, entity_type):
    response = comprehend.detect_entities(Text=text, LanguageCode='en')
    return [entity['Text'] for entity in response['Entities'] if entity['Type'] == entity_type]

# Custom helper to extract education info from lines
def extract_education(text):
    lines = text.split('\n')
    education_lines = [line for line in lines if 'university' in line.lower() or 'college' in line.lower()]
    return education_lines[0] if education_lines else "Not Found"

# Main Lambda handler
def lambda_handler(event, context):
    # Get S3 bucket & object key
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # Use Textract to get text
    response = textract.detect_document_text(Document={'S3Object': {'Bucket': bucket, 'Name': key}})
    full_text = ' '.join([item["Text"] for item in response["Blocks"] if item["BlockType"] == "LINE"])

    # Extract fields
    email = extract_email(full_text)
    phone = extract_phone(full_text)
    name_entities = extract_entities(full_text, 'PERSON')
    name = name_entities[0] if name_entities else "Name Not Found"
    education = extract_education(full_text)

    # Extract other fields manually
    skills_keywords = ['Salesforce', 'SEO', 'Word', 'Excel', 'Analytics', 'Facebook', 'Google', 'Instagram']
    skills = [word for word in skills_keywords if word.lower() in full_text.lower()]

    projects = []
    if "PROJECTS" in full_text:
        projects_part = full_text.split("PROJECTS")[-1]
        projects_lines = projects_part.split('.')
        for line in projects_lines:
            if len(line.strip()) > 20:
                projects.append(line.strip())

    achievements = []
    if "WORK EXPERIENCE" in full_text:
        work_part = full_text.split("WORK EXPERIENCE")[-1]
        achievements_lines = work_part.split('.')
        for line in achievements_lines:
            if len(line.strip()) > 20:
                achievements.append(line.strip())

    languages = extract_entities(full_text, "LANGUAGE")
    certifications = [line for line in full_text.split('\n') if "certification" in line.lower()]

    # Build item for DynamoDB
    item = {
        'email': email,
        'name': name,
        'phone': phone,
        'education': education,
        'skills': skills,
        'experience': achievements,
        'projects': projects,
        'certifications': certifications if certifications else ["Not Found"],
        'achievements': achievements[:3],  # Top 3
        'languages': languages if languages else ["Not Mentioned"]
    }

    # Save to DynamoDB
    table.put_item(Item=item)

    return {
        'statusCode': 200,
        'body': json.dumps('Resume processed and data stored in DynamoDB!')
    }
