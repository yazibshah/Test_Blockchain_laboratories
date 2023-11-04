## Project Overview

The Decentralized Payment Processor is a Flask-based API that enables users to send and receive cryptocurrency payments. It consists of two parts: Part 1 handles user registration, login, balance retrieval, and cryptocurrency transfers using MongoDB. Part 2 extends the functionality to integrate with the XRPL (XRP Ledger) for cryptocurrency transactions.

## Features

- User registration with username, email, and password.
- User login with JWT authentication.
- Retrieval of account balance for logged-in users.
- Sending cryptocurrency to other users, updating balances in MongoDB.
- Integration with XRPL for XRP transactions.
- XRPL testnet support.
- Error handling for failed transactions.

## Folder Structure

The project's folder structure is organized as follows:

- `app`: The main application folder.
    - `__init__.py`: Initializes the Flask app, MongoDB, and registers blueprints.
    - `config.py`: Contains configuration settings for the app.
    - `routes.py`: Defines the API endpoints and their functionality.
    - `models.py`: Defines the data model for users, including MongoDB setup.
- `run.py`: Entry point of the application.

## Getting Started

Follow these steps to set up and run the project:

1. **Prerequisites**:
   - Python 3.7 or higher
   - MongoDB installed and running
   - Python virtual environment (optional but recommended)

2. **Clone the Repository**:

   ```bash
   git clone https://github.com/your-username/payment-processor.git
   cd payment-processor

3. **Dependencies**
List of main dependencies:

Flask
Flask-MongoEngine
Flask-JSON
XRPL Python Library
PyJWT

4. **Set up MongoDB**
 Create a MongoDB database and configure the connection in app/config.py

5. **Run the Application**
    python run.py

## Install Dependencies
    - pip install -r requirements.txt

<!-- Here is DOcs File links -->
1. https://docs.google.com/document/d/1MYXUBsUdzyaliM61GVeMHR2MIsAX7al0/edit?usp=sharing&ouid=112394557027737983550&rtpof=true&sd=true 

2. https://docs.google.com/document/d/1Vk0MYiNLaQ2e-JeY-k30o1F1Hpx8jxUn/edit?usp=sharing&ouid=112394557027737983550&rtpof=true&sd=true

3. https://docs.google.com/document/d/1OLJWkUMt_3qAnyoZv6PMgdp7bHZXj8C0/edit?usp=sharing&ouid=112394557027737983550&rtpof=true&sd=true



