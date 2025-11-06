
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import joblib
import json

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

    # Evaluate on the test set
    y_pred = model.predict(X_test)

    # Compute metrics per target
    r2 = r2_score(y_test, y_pred, multioutput='raw_values')
    mae = mean_absolute_error(y_test, y_pred, multioutput='raw_values')
    mse = mean_squared_error(y_test, y_pred, multioutput='raw_values')

    # Package results in a friendly structure
    metrics = {}
    for i, target in enumerate(targets):
        metrics[target] = {
            'r2': float(r2[i]),
            'mae': float(mae[i]),
            'mse': float(mse[i])
        }

    # Also include uniform average R2 across targets for a quick summary
    metrics_summary = {
        'r2_uniform_average': float(r2_score(y_test, y_pred)),
        'mae_uniform_average': float(mean_absolute_error(y_test, y_pred)),
        'mse_uniform_average': float(mean_squared_error(y_test, y_pred))
    }

    # Save the model
    joblib.dump(model, 'backend/wellness_model.joblib')

    # Save test results alongside the model for reference
    results_path = 'backend/test_results.json'
    with open(results_path, 'w') as f:
        json.dump({'per_target': metrics, 'summary': metrics_summary}, f, indent=2)

    # Print a concise report
    print("Model training complete. Model saved to backend/wellness_model.joblib")
    print("\nTest set results (per target):")
    for target, vals in metrics.items():
        print(f"- {target}: R2={vals['r2']:.3f}, MAE={vals['mae']:.3f}, MSE={vals['mse']:.3f}")
    print("\nSummary (uniform average across targets):")
    print(
        f"R2={metrics_summary['r2_uniform_average']:.3f}, "
        f"MAE={metrics_summary['mae_uniform_average']:.3f}, "
        f"MSE={metrics_summary['mse_uniform_average']:.3f}"
    )
    print(f"\nDetailed results saved to {results_path}")

if __name__ == '__main__':
    train_model()
