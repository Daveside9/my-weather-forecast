🌦️ Weather App
A simple command-line weather application built with Python that fetches real-time weather data using the OpenWeatherMap API.

✨ Features
Get current temperature, humidity, pressure, and weather description.

Fetch weather data for any city worldwide.

Clean and minimal command-line interface.

Uses OpenWeatherMap’s RESTful API with metric units (°C).

🛠️ Setup Instructions
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/Daveside9/weather-app.git
cd weather-app
2. Install Dependencies
Install required packages using pip:

bash
Copy
Edit
pip install -r requirements.txt
Note: If you don’t have a requirements.txt, create one with:

ini
Copy
Edit
requests==2.31.0
3. Add Your API Key
You need a free API key from OpenWeatherMap:

Replace the placeholder API key in main.py:

python
Copy
Edit
api_key = "your_actual_api_key"
Optional: Use environment variables or a .env file for better security.

4. Run the Application
bash
Copy
Edit
python main.py
Then enter the city name when prompted.

🧾 Example Output
yaml
Copy
Edit
Enter city name: London
Weather in London:
Temperature: 19°C
Pressure: 1012 hPa
Humidity: 72%
Description: light rain
🧱 File Structure
bash
Copy
Edit
weather-app/
│
├── main.py             # Main script that runs the app
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
🔑 API Key Notes
Register for free at OpenWeatherMap.

Your API key is required to fetch weather data.

Avoid sharing your key in public repositories.

🧑‍💻 Author
Joel David
GitHub: @Daveside9

📄 License
This project is licensed under the MIT License.

