
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model():
    # Load the cleaned data
    df = pd.read_csv('backend/cleaned_data.csv')

    # Define features (X) and targets (y)
    features = [
        'age', 'gender', 'relationship_status', 'sleep_quality',
        'water_intake_litres', 'food_quality', 'meals_count',
        'caffeine_intake_cups', 'alcohol_consumption_drinks_week',
        'smoking_status', 'chronic_health_issues', 'medication_use',
        'physical_activity_minutes_day', 'sedentary_time_hours_day',
        'environment_noise', 'lighting_quality', 'study_space_quality',
        'roommate_situation', 'living_arrangement', 'commute_time_minutes_day',
        'study_hours_last_24h', 'study_stress',
        'upcoming_exam_assignment_stress', 'grades_estimate_gpa',
        'financial_stress', 'mood_last_24h', 'screen_time_hours_day',
        'social_media_time_hours_day', 'social_interaction_time_minutes_day'
    ]
    targets = ['anxiety_score_gad_7', 'depression_score_phq_9', 'life_satisfaction']

    X = df[features]
    y = df[targets]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Train the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Save the model
    joblib.dump(model, 'backend/wellness_model.joblib')

    print("Model training complete. Model saved to backend/wellness_model.joblib")

if __name__ == '__main__':
    train_model()
