# User-Access-Policy-Check

# Project 03: User Access Policy Check

## Overview
This project simulates a Network Access Control (NAC) system. It checks complex security policies by bringing together user roles, authentication tokens, and environmental factors like time into a single boolean logic engine.

## Technical Specifications
- **Boolean Logic:** Using multi-condition checks with `and`, `or`, and `not`.
- **Decision Trees:** Creating a hierarchy to manage different user permissions.
- **Input Sanitization:** Transforming raw user strings into normalized booleans and integers.

## Security Policy Decision Matrix
The system checks access based on these rules:

| Role   | Token Required | Time Restriction | Access Level |
| :---   | :---:          | :---:            | :---         |
| Admin  | Yes            | None (24/7)      | Full Access  |
| Editor | Yes            | 09:00 - 17:00    | Limited      |
| Guest  | Any            | None             | Denied       |

## How to Run
1. Make sure you have Python installed.
2. Run the script:
   ```bash
   python access_check.py
