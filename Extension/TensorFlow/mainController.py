# main_controller.py

import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense


class mainController:

    def analyze_logs(self):
        # Step 1
        # Read log file and parse each line
        log_data = []
        with open(r'C:\Env\Python\logs\laravel2.log', 'r', encoding='utf-8') as file:
            for line in file:
                parsed_line = self.parse_log(line.strip())
                if parsed_line:
                    log_data.append(parsed_line)

        # Convert to DataFrame
        df_logs = pd.DataFrame(log_data)

        # Step 2
        # Example: Convert error messages into bag-of-words model
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(df_logs['message'])

        # Step 3
        # Assume you have converted the log message levels to integer labels
        y = df_logs['level'].map({'ERROR': 1, 'WARNING': 0}).values

        # Create the model
        model = Sequential([
            Dense(10, activation='relu', input_dim=X.shape[1]),
            Dense(5, activation='relu'),
            Dense(1, activation='sigmoid')
        ])

        # Compile the model
        model.compile(optimizer='adam', loss='binary_crossentropy',
                      metrics=['accuracy'])

        # Train the model
        model.fit(X.toarray(), y, epochs=10, batch_size=32)

        # Step 4
        # Evaluate the model
        loss, accuracy = model.evaluate(X.toarray(), y)

        # Apply the model to predict new log entries
        new_log_message = "Some new error message here"
        new_log_features = vectorizer.transform([new_log_message])
        prediction = model.predict(new_log_features.toarray())

        # Output the prediction result
        print("Predicted class:",
              'ERROR' if prediction[0][0] >= 0.5 else 'WARNING')

        return "This is the demo1 function!"

    def parse_log(self, log_line):
        log_pattern = re.compile(
            r'\[(.*?)\].*?(\w+)\.(\w+): (.*?) \{"exception".*?\((.*?)\): (.*?) at (.*?)\)')
        match = log_pattern.match(log_line)
        if match:
            timestamp, env, level, message, code, error, file_path = match.groups()
            return {
                'timestamp': timestamp,
                'environment': env,
                'level': level,
                'message': message,
                'code': code,
                'error': error,
                'file_path': file_path
            }
        else:
            return None
