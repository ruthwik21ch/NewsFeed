📰 NewsFeed App

A Python GUI-based News Application built using Tkinter that allows users to register, login, and browse the latest news headlines. The app fetches real-time news using the NewsAPI, displays article images, and provides a text-to-speech feature to read the news aloud.

🚀 Features

🔐 User Authentication

Login and Registration system

Data stored locally using SQLite

📰 Live News Headlines

Fetches top headlines using NewsAPI

Displays title, description, and image

🔊 Text-to-Speech

Reads the news using the pyttsx3 speech engine

🌐 Read Full Article

Opens the original news source in the browser

⏭ Navigation

Move between news articles using Next and Previous buttons

🖼 Image Handling

Displays article images

Uses a default image if the news image is unavailable

🚪 Logout System

Users can safely logout and return to login screen

🛠 Technologies Used

Python

Tkinter – GUI Interface

SQLite3 – Database

Requests – API Requests

Pillow (PIL) – Image Processing

pyttsx3 – Text-to-Speech

NewsAPI – Fetching news data

📦 Installation
1️⃣ Clone the repository
git clone https://github.com/your-username/newsfeed-app.git
cd newsfeed-app

2️⃣ Install required libraries
pip install requests pillow pyttsx3

3️⃣ Run the application
python news_app.py

🔑 API Setup

This project uses NewsAPI.

Go to
https://newsapi.org

Create a free account.

Get your API key.

Replace the API key in the code:

API_KEY = "YOUR_API_KEY"

📂 Project Structure
newsfeed-app
│
├── news_app.py
├── users.db
├── README.md

📸 Application Screens

The application contains the following screens:

Login Page

Registration Page

News Feed Page

News Article Viewer

🔮 Future Improvements

Possible features that can be added:

🌙 Dark Mode

🔎 Search News

🗂 News Categories (Technology, Sports, Business, etc.)

⭐ Bookmark Articles

📱 Convert to Mobile App

🤖 AI News Summarization

🤝 Contributing

Contributions are welcome.

Fork the repository

Create a new branch

Commit your changes

Submit a pull request

📜 License

This project is licensed under the MIT License.

👨‍💻 Author

Developed by Ruthwik
