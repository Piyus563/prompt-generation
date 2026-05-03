import requests
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')


def ask_ai(prompt_text):
    """
    Sends any prompt directly to PollinationsAI and returns the raw AI response.
    Free, no API key needed, works on Windows.
    """
    try:
        url = "https://text.pollinations.ai/"
        payload = {
            "messages": [
                {
                    "role": "user",
                    "content": prompt_text
                }
            ],
            "model": "openai",
            "seed": 42,
            "private": True
        }
        headers = {"Content-Type": "application/json"}
        resp = requests.post(url, json=payload, headers=headers, timeout=60)
        if resp.status_code == 200 and resp.text.strip():
            return resp.text.strip(), None
        return None, f"AI returned status {resp.status_code}"
    except requests.Timeout:
        return None, "Request timed out after 60s."
    except Exception as e:
        return None, str(e)


@app.route('/', methods=['GET', 'POST'])
def home():
    output = ""
    error_msg = ""
    user_prompt = ""
    status_type = ""

    if request.method == 'POST':
        user_prompt = request.form.get('prompt', '').strip()

        if not user_prompt:
            error_msg = "Please enter a prompt!"
            status_type = "warning"
        else:
            result, err = ask_ai(user_prompt)
            if result:
                output = result
                status_type = "success"
            else:
                error_msg = f"AI Error: {err}"
                status_type = "error"

    return render_template('index.html',
                           output=output,
                           error_msg=error_msg,
                           user_prompt=user_prompt,
                           status_type=status_type)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
