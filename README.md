# 🚀 ISS Overhead Notification Tracker

An automated tracking application that monitors the real-time orbital path of the International Space Station (ISS) and alerts you when it passes over your coordinates in the dark.

## ✨ Features
* **Real-time Tracking:** Fetches live coordinates from the Open Notify ISS API.
* **Smart Geofencing:** Checks if the ISS is within a 5-degree radius of your position.
* **Visibility Validation:** Cross-references the Sunrise-Sunset API to ensure notifications are only sent when it is dark outside.
* **Automated Alerts:** Sends a secure email notification via SMTP.

## 🛠️ Environment Variables
To run this project locally, create a `.env` file in your root directory and add your credentials:
`MY_EMAIL` = Your Gmail address
`MY_PASSWORD` = Your Google App Password
