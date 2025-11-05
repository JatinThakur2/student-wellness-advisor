import pandas as pd
import numpy as np
import re

def clean_data(df):
    # Drop the timestamp and username columns
    df = df.drop(columns=['Timestamp', 'Username'])

    # Clean column names
    df.columns = [re.sub(r'[\s/()-]+', '_', col).lower().strip('_') for col in df.columns]

    # Clean string columns
    for col in df.select_dtypes(include=['object']).columns:
        df[col] = df[col].str.strip()

    # Replace non-standard missing values with NaN
    df.replace(['NA', 'NIL', 'Nil', 'No', 'Nope', 'No consumption', 'None', 'No activity', 'Not much', 'low', 'Depends', 'No expectations', 'No clue', 'Rare', 'Rarely', 'Rarely only on ocassions', 'Weekly', 'Once a month', 'Once a week', 'Once in two weeks', 'None of the above', '.', 'Missing'], np.nan, inplace=True)

    # Age
    df['age'] = pd.to_numeric(df['age'], errors='coerce')

    # Gender
    df['gender'] = df['gender'].replace({'Male': 0, 'Female': 1, 'Non-binary': 2, 'Other': 2})

    # Relationship Status
    df['relationship_status'] = df['relationship_status'].replace({'Single': 0, 'In a relationship': 1, 'Married/Partnered': 2, 'Other': 3})

    # Sleep Quality
    df['sleep_quality'] = pd.to_numeric(df['sleep_quality'], errors='coerce')

    # Water Intake
    df['water_intake_litres'] = df['water_intake_litres'].str.extract('(\d+\.?\d*)').astype(float)

    # Food Quality
    df['food_quality'] = pd.to_numeric(df['food_quality'], errors='coerce')

    # Meals Count
    df['meals_count'] = df['meals_count'].str.extract('(\d+)').astype(float)

    # Caffeine Intake
    df['caffeine_intake_cups'] = df['caffeine_intake_cups'].str.extract('(\d+)').astype(float)

    # Alcohol Consumption
    df['alcohol_consumption_drinks_week'] = df['alcohol_consumption_drinks_week'].str.extract('(\d+)').astype(float)

    # Smoking Status
    df['smoking_status'] = df['smoking_status'].replace({'Yes': 1, 'No': 0})

    # Chronic Health Issues
    df['chronic_health_issues'] = df['chronic_health_issues'].replace({'Yes': 1, 'No': 0})

    # Medication Use
    df['medication_use'] = df['medication_use'].replace({'Yes': 1, 'No': 0})

    # Physical Activity
    df['physical_activity_minutes_day'] = df['physical_activity_minutes_day'].str.extract('(\d+)').astype(float)

    # Sedentary Time
    df['sedentary_time_hours_day'] = df['sedentary_time_hours_day'].str.extract('(\d+\.?\d*)').astype(float)

    # Environment Noise
    df['environment_noise'] = pd.to_numeric(df['environment_noise'], errors='coerce')

    # Lighting Quality
    df['lighting_quality'] = pd.to_numeric(df['lighting_quality'], errors='coerce')

    # Study Space Quality
    df['study_space_quality'] = pd.to_numeric(df['study_space_quality'], errors='coerce')

    # Roommate Situation
    df['roommate_situation'] = df['roommate_situation'].replace({'Alone': 0, 'Shared room': 1, 'Shared apartment': 2})

    # Living Arrangement
    df['living_arrangement'] = df['living_arrangement'].replace({'Off-campus shared': 0, 'On-campus dorm': 1, 'Living with family': 2})

    # Commute Time
    df['commute_time_minutes_day'] = df['commute_time_minutes_day'].str.extract('(\d+)').astype(float)

    # Study Hours
    df['study_hours_last_24h'] = df['study_hours_last_24h'].str.extract('(\d+\.?\d*)').astype(float)

    # Study Stress
    df['study_stress'] = pd.to_numeric(df['study_stress'], errors='coerce')

    # Upcoming Exam/Assignment Stress
    df['upcoming_exam_assignment_stress'] = pd.to_numeric(df['upcoming_exam_assignment_stress'], errors='coerce')

    # Grades Estimate / GPA
    df['grades_estimate_gpa'] = df['grades_estimate_gpa'].str.extract('(\d+\.?\d*)').astype(float)

    # Financial Stress
    df['financial_stress'] = pd.to_numeric(df['financial_stress'], errors='coerce')

    # Mood
    df['mood_last_24h'] = pd.to_numeric(df['mood_last_24h'], errors='coerce')

    # Anxiety Score
    df['anxiety_score_gad_7'] = pd.to_numeric(df['anxiety_score_gad_7'], errors='coerce')

    # Depression Score
    df['depression_score_phq_9'] = pd.to_numeric(df['depression_score_phq_9'], errors='coerce')

    # Life Satisfaction
    df['life_satisfaction'] = pd.to_numeric(df['life_satisfaction'], errors='coerce')

    # Screen Time
    df['screen_time_hours_day'] = df['screen_time_hours_day'].str.extract('(\d+\.?\d*)').astype(float)

    # Social Media Time
    df['social_media_time_hours_day'] = df['social_media_time_hours_day'].str.extract('(\d+\.?\d*)').astype(float)

    # Social Interaction Time
    df['social_interaction_time_minutes_day'] = df['social_interaction_time_minutes_day'].str.extract('(\d+\.?\d*)').astype(float)

    # Fill remaining NaN values with the mean of the column
    for col in df.columns:
        if df[col].dtype in ['float64', 'int64']:
            df[col].fillna(df[col].mean(), inplace=True)

    return df

if __name__ == '__main__':
    df = pd.read_csv('/home/jatin/College/project/student-wellness-advisor/Student Wellness Survey (data).csv')
    cleaned_df = clean_data(df.copy())
    cleaned_df.to_csv('/home/jatin/College/project/student-wellness-advisor/backend/cleaned_data.csv', index=False)
    print("Data cleaning complete. Cleaned data saved to backend/cleaned_data.csv")