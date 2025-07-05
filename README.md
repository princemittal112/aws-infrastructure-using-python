# AWS Infrastructure Automation with Python 🐍☁️

This repo automates AWS infrastructure provisioning using **Python** and **Boto3**, empowering you to script, control, and manage your cloud environment programmatically.

---

## 📋 What It Does

- 🚀 **Launch EC2 instances** (with user-data or tagging)
- 📦 **Create S3 buckets** with optional configurations (versioning, encryption)
- 🔧 (Optional) **Tear down/cleanup** of infrastructure
- 🔁 Integrates with **Terraform workflows** via Python (if applicable)

---

## 📂 Repository Structure

<img width="175" alt="Screenshot 2025-07-05 at 2 22 13 PM" src="https://github.com/user-attachments/assets/8107dd89-bb59-491f-927a-5cd6f2e270e5" />


## 🛠 Prerequisites

- Python 3.8+
- AWS credentials configured via AWS CLI (aws configure) or environment vars
- Boto3 for AWS SDK

## 🧠 Best Practices Covered

- Infrastructure scripting using Boto3
- Argument parsing (argparse) for flexibility
- Clear separation of concerns: EC2, S3, Terraform
- Idempotent bucket creation and safe EC2 provisioning]
- Extensible and modular script design


