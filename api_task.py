# ============================================================
#  API & JSON Task — Fetching Live Data
#  Name  : Shaik Arshiya Tabasum
#  Roll  : 24JR1A0529
#  API Used: JokeAPI (https://v2.jokeapi.dev) — Free, No Key
# ============================================================

import requests
import json
import datetime

API_URL = "https://v2.jokeapi.dev/joke/Programming,Miscellaneous?safe-mode"

def fetch_joke():
    print("=" * 55)
    print("       😄 Live Joke Fetcher — API & JSON Task")
    print("   AIML Internship | Shaik Arshiya Tabasum | 24JR1A0529")
    print("=" * 55)
    print(f"\n🌐 Fetching live data from: {API_URL}\n")

    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        # Parse JSON response
        data = response.json()

        print("✅ API Response Received Successfully!")
        print(f"📊 HTTP Status Code : {response.status_code}")
        print(f"📁 Response Type    : JSON")
        print("-" * 55)

        # Display formatted output
        print(f"\n🎭 Joke Category : {data.get('category', 'N/A')}")
        print(f"📝 Joke Type     : {data.get('type', 'N/A')}")
        print()

        if data.get("type") == "twopart":
            print(f"❓ Setup   : {data['setup']}")
            print(f"😂 Punchline: {data['delivery']}")
        elif data.get("type") == "single":
            print(f"😂 Joke: {data['joke']}")

        print("\n" + "=" * 55)
        print("📦 Raw JSON Response (Parsed):")
        print("-" * 55)
        print(json.dumps(data, indent=4))
        print("=" * 55)

        # Save output to file
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("api_output.txt", "w") as f:
            f.write(f"API Task Output — {timestamp}\n")
            f.write(f"API URL: {API_URL}\n")
            f.write(f"Status Code: {response.status_code}\n\n")
            if data.get("type") == "twopart":
                f.write(f"Setup: {data['setup']}\n")
                f.write(f"Punchline: {data['delivery']}\n")
            else:
                f.write(f"Joke: {data.get('joke', '')}\n")
            f.write("\nFull JSON:\n")
            f.write(json.dumps(data, indent=4))

        print("\n✅ Output saved to api_output.txt")

    except requests.exceptions.ConnectionError:
        print("❌ Connection Error: Could not reach the API. Check your internet.")
    except requests.exceptions.Timeout:
        print("❌ Timeout Error: The API took too long to respond.")
    except requests.exceptions.HTTPError as e:
        print(f"❌ HTTP Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected Error: {e}")

if __name__ == "__main__":
    fetch_joke()
