from flask import Flask, render_template, request
import re

app = Flask(__name__)

def extract_video_id(url: str) -> str | None:
    """
    Extract the YouTube video ID from a full YouTube URL.
    Supports regular videos and shorts.
    """
    patterns = [
        r'(?:v=|\/)([0-9A-Za-z_-]{11})',       # Regular YouTube URL or embed/shorts
        r'youtu\.be\/([0-9A-Za-z_-]{11})',     # Shortened URL
    ]
    for pattern in patterns:
        match = re.search(pattern, url)
        if match:
            return match.group(1)
    return None

@app.route('/watch')
def watch():
    video_url = request.args.get('url')
    if not video_url:
        return "Missing 'url' query parameter", 400

    video_id = extract_video_id(video_url)
    if not video_id:
        return "Invalid YouTube URL", 400

    return render_template("watch.html", video_id=video_id)

@app.route('/')
def home():
    return "<h3>YouTube Embed Server is Running</h3><p>Use <code>/watch?url=...</code> to embed a video.</p>"

if __name__ == '__main__':
    app.run(debug=True)
