# Student Wellness Advisor

This project is a web application that provides personalized wellness advice to students based on a machine learning model. It aims to help students understand their mental well-being and provides actionable steps to improve it.

## Features

- **Predicts Wellness Scores:** The application predicts anxiety, depression, and life satisfaction scores based on user input.
- **Personalized Advice:** It provides a summary of the user's well-being and actionable advice using a large language model.
- **Simple Interface:** The web interface is simple and intuitive, making it easy for students to input their data.

## Technologies Used

- **Backend:** Python, Flask, scikit-learn, pandas
- **Frontend:** HTML, CSS, JavaScript
- **Machine Learning:** A supervised learning model trained to predict wellness scores.
- **Large Language Model:** A local large language model is used to generate summaries and advice.

## How it Works

1.  **User Input:** The user fills out a comprehensive form on the web interface, providing information about their lifestyle, academic stress, and other factors.
2.  **Prediction:** The submitted data is sent to the Flask backend, which uses a pre-trained scikit-learn model to predict the user's anxiety, depression, and life satisfaction scores.
3.  **Advice Generation:** The predicted scores are then fed into a local large language model, which generates a personalized summary and actionable advice for the user.
4.  **Display Results:** The wellness scores and the generated advice are displayed to the user on the web page.

## How to Run

### Prerequisites

- Python 3.x
- A local large language model running and accessible at `http://localhost:11434`.

### Backend Setup

1.  Navigate to the `backend` directory:
    ```bash
    cd backend
    ```
2.  Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```
3.  Run the Flask application:
    ```bash
    python app.py
    ```
    The backend server will start on `http://127.0.0.1:5000`.

### Frontend Setup

1.  Open the `frontend/index.html` file in your web browser.
2.  Fill out the form and click "Predict" to get your wellness advice.
