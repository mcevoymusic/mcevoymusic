from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

# Directory to save PDFs
PDF_DIR = "./downloaded_pdfs"
os.makedirs(PDF_DIR, exist_ok=True)

def scrape_asx_announcements():
    ASX_URL = "https://www.asx.com.au/markets/trade-our-cash-market/todays-announcements"
    response = requests.get(ASX_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    announcements = []

    rows = soup.select('div.announcement-row')  # Replace with the correct selector for rows

    for row in rows:
        columns = row.find_all('div', class_='announcement-column')
        price_sensitive = columns[2].text.strip()  # Adjust index based on actual structure

        if price_sensitive == "$":
            title = columns[1].text.strip()
            url = "https://www.asx.com.au" + columns[1].find('a')['href']
            pdf_url = url.replace('/announcements/', '/pdfs/') + ".pdf"
            pdf_local_path = os.path.join(PDF_DIR, title + ".pdf")

            pdf_response = requests.get(pdf_url)
            with open(pdf_local_path, 'wb') as pdf_file:
                pdf_file.write(pdf_response.content)

            announcement = {
                "title": title,
                "url": url,
                "pdfLocalPath": pdf_local_path,
                "timestamp": columns[0].text.strip()
            }
            announcements.append(announcement)

    return announcements

@app.route('/asx/announcements/price-sensitive', methods=['GET'])
def get_price_sensitive_announcements():
    try:
        announcements = scrape_asx_announcements()
        return jsonify(announcements), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
