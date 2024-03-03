import requests
from openai import OpenAI

client = OpenAI(api_key='add your OPENAI API Key here')


def fetch_json_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


def generate_summary_for_json(api_url):
    json_data = fetch_json_from_api(api_url)
    if json_data is None:
        return "Failed to fetch or parse JSON data from the API."

    json_str = str(json_data).replace("'", "\"")

    system_message = "You are a helpful assistant. You will generate a summary of the JSON file I provide."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": json_str}
        ],
        temperature=1,
        max_tokens=1812,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response.choices[0].message.content


api_url = "https://ipfo54urs5.execute-api.ap-south-1.amazonaws.com/portfolioprofile/?riskprofile=3"
summary = generate_summary_for_json(api_url)
print(summary)
