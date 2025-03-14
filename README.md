# 📍 Phone Number Location Tracker

## 📌 Overview
This Python project allows users to track the geographical location and service provider of a given phone number. It utilizes the `phonenumbers` library for parsing phone numbers, `OpenCageGeocode` for geolocation, and `folium` for map visualization.

## 🔹 Features
- Extracts the **geographical location** (country/region) of a phone number.
- Retrieves the **service provider** (carrier) of the phone number.
- Uses OpenCage API to fetch **latitude & longitude** coordinates.
- Generates an **interactive map** to visualize the phone number's location.

## 🛠️ Tech Stack
- **Python**
- **phonenumbers** - Extracts location and service provider information.
- **OpenCageGeocode** - Fetches latitude and longitude data.
- **folium** - Creates an interactive map for visualization.

## 🚀 How It Works

1️⃣ **User Input:** Enter a phone number with the country code.
2️⃣ **Extract Information:**
   - Retrieve location (country/region) using `phonenumbers`.
   - Retrieve service provider (carrier) details.
3️⃣ **Geolocation Processing:** Query OpenCage API to obtain latitude and longitude.
4️⃣ **Map Generation:** Use `folium` to create an interactive map with the location.
5️⃣ **Output:** Save the generated map as `location.html` for viewing.

## 🔍 Example Usage
```bash
Enter phone number with country code: +1 202-555-0125
```

📌 **Location:** Washington, D.C., USA  
📡 **Service Provider:** AT&T  
🌍 **Coordinates:** `38.8951° N, 77.0364° W`  
📜 **Map Generated!** (Check `location.html`)

## 📥 Installation & Setup

1. Clone the repository:
   ```bash
   git clone <your-repo-link>
   cd phone-number-tracker
   ```
2. Install dependencies:
   ```bash
   pip install phonenumbers folium opencage
   ```
3. Get an OpenCage API key from [OpenCage Geocoder](https://opencagedata.com/) and replace `key` in the script:
   ```python
   key = "YOUR_API_KEY"
   ```
4. Run the script:
   ```bash
   python tracker.py
   ```

## 📜 License
This project is licensed under the MIT License.

## 🤝 Contributing
Pull requests and suggestions are welcome! Feel free to open an issue or contribute to improve this project.

## 📌 Author
Developed by **Anupama Ushetti**. 
