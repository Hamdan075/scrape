import requests
from bs4 import BeautifulSoup
import streamlit as st
from streamlit_autorefresh import st_autorefresh

def fetch_cricket_matches():
    url = "https://www.cricbuzz.com/cricket-match/live-scores"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    matches = []

    match_blocks = [a for a in soup.find_all('a') if a.get('href') and '/live-cricket-scores/' in a.get('href') and 'flex-col' in a.get('class', [])]

    for mb in match_blocks:
        title = mb.get('title', 'No title').strip()
        
        texts = list(mb.stripped_strings)
        status = texts[-1] if texts else "Status not found"
        
        score_parts = texts[1:-1]
        score = " | ".join(score_parts) if score_parts else "Score unavailable"
        
        matches.append({"title": title, "score": score, "status": status})

    return matches

def classify_match(match):
    status = match["status"].lower()

    if any(word in status for word in ["won", "tie", "abandoned", "no result", "stumps", "draw"]):
        return "completed"

    if any(word in status for word in ["over", "day", "innings", "trail", "need", "requires"]):
        return "live"

    return "upcoming"

def main():
    st.set_page_config(
        page_title="⚡ Live Cricket Scoreboard",   
        page_icon="🏏",                       
        layout="centered",                           
        initial_sidebar_state="expanded"          
    )

    st.title("⚡ Live Cricket Scoreboard")
    try:
        st.image("c.jpg", caption="Cricket Updates")
    except Exception:
        st.image("https://images.unsplash.com/photo-1531415074968-036ba1b575da?auto=format&fit=crop&w=800&q=80", caption="Cricket Updates")

    refresh_seconds = st.slider("Auto-refresh every (sec):", 5, 60, 15)
    st_autorefresh(interval=refresh_seconds * 1000, key="refresh")

    matches = fetch_cricket_matches()
    if not matches:
        st.error("No matches found or unable to fetch.")
        return

    live_matches = [m for m in matches if classify_match(m) == "live"]
    completed_matches = [m for m in matches if classify_match(m) == "completed"]
    upcoming_matches = [m for m in matches if classify_match(m) == "upcoming"]

    option = st.selectbox(
        "Select match type to display:",
        ["Live Matches", "Completed Matches", "Upcoming Matches"]
    )

    if option == "Live Matches":
        st.subheader(f"🟢 Live Matches ({len(live_matches)})")
        if not live_matches:
            st.info("No live matches right now.")
        for m in live_matches:
            st.write(f"**{m['title']}** — {m['score']}*")

    elif option == "Completed Matches":
        st.subheader(f"🏆 Completed Matches ({len(completed_matches)})")
        if not completed_matches:
            st.info("No completed matches yet today.")
        for m in completed_matches:
            st.success(f"{m['title']} — {m['status']}")

    else: 
        st.subheader(f"📅 Upcoming Matches ({len(upcoming_matches)})")
        if not upcoming_matches:
            st.info("No upcoming matches listed right now.")
        for m in upcoming_matches:
            st.info(f"{m['title']} — *{m['status']}*")

if __name__ == "__main__":
    main()