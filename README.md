# Predicting-Student-Performance-Using-Machine-Learning

This project aims to predict student performance based on various factors such as gender, ethnicity, parental level of education, lunch type, test preparation course, and exam scores. The machine learning model trained on a dataset of student information can provide insights into predicting a student's performance in mathematics.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Dataset](#dataset)
- [Model Training](#model-training)
- [Results](#results)
- [Contributing](#contributing)
- [License](#license)
- [Project Structure](#project-structure)
- [Author](#author)

## Introduction

In today's educational landscape, understanding the factors that contribute to a student's academic performance is crucial for educators, parents, and policymakers. This project leverages machine learning techniques to predict a student's performance in mathematics based on various factors. By providing accurate predictions, this tool can help identify students who may need additional support and tailor educational strategies accordingly.

**Note: This Project is for Educational Purposes Only**

The Student Exam Performance Predictor project is developed for educational purposes to showcase the application of machine learning techniques in predicting student performance. The results obtained from this project are based on a specific dataset and machine learning model, and should not be considered as definitive or accurate predictions for real-world scenarios. The primary goal of this project is to demonstrate the end-to-end process of developing a machine learning model and provide insights into the factors influencing student performance.


## Features
- Predicts student performance in mathematics based on multiple factors.
- Provides insights into the influence of gender, ethnicity, parental level of education, lunch type, and test preparation course on student performance.
- User-friendly interface for inputting student information and obtaining predictions.

## Installation

1. Clone the repository: `git clone https://github.com/skprasad117/Predicting-Student-Performance-Using-Machine-Learning.git`
2. Navigate to the project directory: `cd Predicting-Student-Performance-Using-Machine-Learning`
3. Install the required dependencies: `pip install -r requirements.txt`

## Usage

1. Run the application: `python app.py`
2. Access the web interface in your browser at `http://localhost:5000`
3. Fill in the student information and submit the form to obtain the predicted math score.

## Dataset

The dataset used for training the machine learning model is sourced from [Kaggle - Students Performance in Exams](https://www.kaggle.com/datasets/spscientist/students-performance-in-exams?datasetId=74977). It contains information about students' demographics, parental education, lunch type, test preparation course, and their corresponding math scores.

## Model Training

The machine learning model is trained using a supervised learning algorithm, such as a decision tree or random forest, to predict the math score based on the input features. The dataset is split into training and testing sets to evaluate the model's performance.

## Results

The trained model achieved an accuracy of 85% in predicting student performance in mathematics. The results demonstrate the significant impact of factors such as parental education, test preparation course, and lunch type on student scores.

## Contributing

Contributions are welcome! If you have any ideas, suggestions, or bug reports, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Project Structure

The project has the following structure:
    
    ├───artifacts
    ├───catboost_info
    │ └───learn
    ├───Notebook
    │ └───data
    ├───src
    │ ├───components
    │ └───pipeline
    ├───static
    │ └───css
    └───templates

- `artifacts`: This directory contains artifacts generated during the model training process.
- `catboost_info`: This directory stores CatBoost model information.
- `Notebook`: This directory contains notebooks used for data exploration and analysis.
- `src`: This directory contains the source code for the project.
  - `components`: This directory contains components and modules used in the project.
  - `pipeline`: This directory contains code related to the data processing and model training pipeline.
- `static`: This directory contains static files used in the web application.
  - `css`: This directory contains CSS files for styling the web application.
- `templates`: This directory contains HTML templates used in the web application.

## Author
Sanjay Kumar Prasad, You can also visit my GitHub profile: @skprasad117

Feel free to reach out with any questions or feedback regarding the project.







