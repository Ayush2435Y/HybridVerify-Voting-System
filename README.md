# HybridVerify Voting System

## Overview
The HybridVerify Voting System is a digital election solution developed using Python and MySQL. It is designed to simulate secure, tamper-proof elections, featuring structured voter registration, strict authentication, and duplicate-vote prevention mechanisms. 

While the system currently uses passcode-based authentication to run without specialized hardware, the underlying database and verification architecture are purpose-built to seamlessly integrate with actual biometric scanners. Transitioning to biometrics only requires replacing the passcode input with biometric hash data.

## Features
- **Secure Voter Registration:** Registers users securely by storing their Name, unique Voter ID, and authentication credentials in a centralized database.
- **Strict Authentication:** Dynamically verifies user credentials against the SQL database before granting access to cast a vote.
- **Anti-Duplication:** Actively prevents a registered Voter ID from casting multiple ballots.
- **Real-Time Tallying:** Automatically counts votes across different parties (BJP, AJP, Congress) and displays the final election results upon session completion.
- **Scalable Architecture:** The verification module is designed to make the transition from integer passcodes to biometric template matching effortless.

## Tech Stack
- **Language:** Python 3.x
- **Database:** MySQL
- **Libraries:** `mysql-connector-python`

## Setup and Installation
1. Ensure MySQL Server and Python 3.x are installed and running.
2. Import the database schema using the provided SQL file to set up the necessary tables.
3. Install the required Python module by running:
   ```bash
   pip install mysql-connector-python
