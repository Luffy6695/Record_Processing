# Enterprise Records Validation, Deduplication and Analysis Using Pandas

## Description

This project processes enterprise records using Python and Pandas. It performs data validation, duplicate removal, summary analysis, and identification of records that require attention.

## Features

- Validates required fields
- Identifies invalid records
- Removes duplicate records
- Generates summary statistics
- Identifies aging records
- Identifies records with excessive owner changes

## Technologies Used

- Python
- Pandas
- JSON


Validation :-
Validates records based on required fields, source, status, category, date, and owner changes.

Deduplication :-
Removes duplicate records using source and ID.

Summary :-
Generates statistics based on status, source, and category.

Findings :-
Identifies:
- Open records older than 7 days
- Records with more than 3 owner changes

Final Output :-
Displays the processed records and results generated from the analysis.

## Project Structure

```text
enterprise_project/
├── report.py
├── records.json
├── README.md
├── .gitignore
└── venv/

