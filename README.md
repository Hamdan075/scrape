# ⚡ Live Cricket Scoreboard 🏏

A real-time cricket scoreboard built with Python and Streamlit. This application scrapes live match data from Cricbuzz and presents it in a clean, auto-refreshing dashboard.

## ✨ Features
- **Real-Time Data**: Fetches the latest scores and match statuses from Cricbuzz.
- **Match Categories**: Automatically classifies matches into three categories:
  - 🟢 Live Matches
  - 🏆 Completed Matches
  - 📅 Upcoming Matches
- **Auto-Refresh**: Customizable auto-refresh slider (5 to 60 seconds) so you don't have to manually refresh the page to get the latest scores.
- **Smart Fallback**: Handles missing images gracefully by displaying a fallback placeholder.

## 🛠️ Prerequisites
Ensure you have Python installed, then install the required dependencies:

```bash
pip install streamlit beautifulsoup4 requests streamlit-autorefresh
```

## 🚀 How to Run
Run the Streamlit application using the following command in your terminal:

```bash
streamlit run cricket.py
```
*(If `streamlit` is not recognized, you can run it via Python: `py -m streamlit run cricket.py` or `python -m streamlit run cricket.py`)*

## 📂 Project Structure
- `cricket.py`: The main Streamlit application and web-scraping script.
- `c.jpg` *(optional)*: You can add a local image named `c.jpg` in the project directory, which will be displayed on the dashboard. If not present, a placeholder image from Unsplash is used.

## ⚙️ How it Works
The application uses `requests` and `BeautifulSoup` to scrape live cricket scores from the Cricbuzz website. The data is parsed from the HTML and categorized based on keywords in the match status (e.g., "stumps", "won", "need"). Streamlit is then used to render this data in an interactive and responsive web dashboard.
