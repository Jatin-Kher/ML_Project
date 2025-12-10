from flask import Flask, request, render_template
import sys
from src.MLproject.pipelines.prediction_pipeline import CustomData, PredictPipeline
from src.MLproject.exception import CustomException

application=Flask(__name__)

app=application

## Route for a home page



@app.route('/', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html', results=None, error=None)
    else:
        try:
            data = CustomData(
                gender=request.form.get('gender'),
                race_ethnicity=request.form.get('ethnicity'),
                parental_level_of_education=request.form.get('parental_level_of_education'),
                lunch=request.form.get('lunch'),
                test_preparation_course=request.form.get('test_preparation_course'),
                reading_score=float(request.form.get('reading_score')),
                writing_score=float(request.form.get('writing_score'))
            )
            pred_df = data.get_data_as_data_frame()
            print(pred_df)
            print("Before Prediction")

            predict_pipeline = PredictPipeline()
            print("Mid Prediction")
            results = predict_pipeline.predict(pred_df)
            print("After Prediction")
            return render_template('home.html', results=results[0])
        except Exception as e:
            print(f"Error: {str(e)}")
            return render_template('home.html', results=None, error=str(e))
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)        