# Knowledge Box

## Introduction

Knowledge Box is an innovative tool designed for users to efficiently save and utilize textual information for learning and self-assessment. Initially created for the MakeUC hackathon organized by IEEE at the University of Cincinnati on November 4, 2023, this project offers a unique approach to managing knowledge.

## Features
- **Authentication (Login and Register):** Knowledge Box features user authentication system. Users can register for an account and log in to access their personalized knowledge database.
- **Passage Saving:** Users can easily save passages by typing them in or uploading images or PDFs. This flexibility allows for a variety of textual information to be stored and accessed conveniently. OCR.space API is used for extracting text from images and PDF files.
- **MCQ Generation:** To test understanding and retention, Knowledge Box can generate multiple-choice questions (MCQs) from the saved passages. This feature is ideal for self-assessment and revision. It uses NLP techniques to find keywords in passages and generate questions based on those.

## First-Time Setup

Before running the project, it is essential to perform a one-time setup. This involves running the `setup.py` script, which prepares the environment and dependencies required for Knowledge Box to run. The database information, ocr.space API key, and other configurations can be set in `config.json`.

