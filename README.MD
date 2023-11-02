# Weather App

## Description

The Weather App is a Django web application that allows users to get current weather information for a specific city. Users can input the name of a city, and the app retrieves and displays weather data from the OpenWeatherMap API. The application provides weather details such as temperature, weather condition, and an icon representing the current weather.

## Features

- Get the latest weather information for a specified city.
- Display the weather condition, and an icon representing the current weather.
- Responsive web design for a better user experience on various devices.

## Prerequisites

Before running the Weather App, make sure you have the following dependencies installed:

- Python 3.x
- Django (install using `pip install django`)
- Requests library (install using `pip install requests`)

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/davidinmichael/weather_app
   ```

2. Change to the project directory:

   ```bash
   cd weather-app
   ```

3. Create a virtual environment (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

4. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Set up the OpenWeatherMap API Key:
   - Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api).
   - Create a `.env` file in the project's root directory and add your API key:

     ```env
     OPENWEATHERMAP_API_KEY=your_api_key_here
     ```

6. Apply database migrations:

   ```bash
   python manage.py migrate
   ```

7. Start the development server:

   ```bash
   python manage.py runserver
   ```

8. Access the Weather App in your web browser at [http://localhost:8000](http://localhost:8000).

## Usage

1. Enter the name of a city in the input field on the homepage.
2. Click the "Submit" button.
3. The app will display the current weather information for the specified city.

## Deployment

To deploy the Weather App to a production server, you can follow these general steps:

1. Set up a production server (e.g., AWS, Heroku, or a VPS).
2. Configure your production environment variables.
3. Collect static files by running:

   ```bash
   python manage.py collectstatic
   ```

4. Set up a production-ready web server (e.g., Nginx or Apache) to serve your application.
5. Configure your web server to forward requests to the Gunicorn application server (if using Gunicorn).
6. Secure your server with HTTPS using an SSL certificate.
7. Monitor and maintain your server for ongoing operation.

## Contributing

If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and test them thoroughly.
4. Submit a pull request to the main repository.


## Acknowledgments

- Weather data provided by [OpenWeatherMap](https://openweathermap.org).

## Contact

If you have any questions or feedback, feel free to contact the project maintainers at [davidinmichael@gmail.com](mailto:davidinmichael@gmail.com).

Thank you for using the Weather App! We hope it serves you well.