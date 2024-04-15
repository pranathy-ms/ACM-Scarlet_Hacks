print("Hello there, this is our Hugging Face API implementation")

import requests
import config

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

# Define the input prompt
prompt = "Given my location is 171 W Randolph St, Chicago, would you be able to provide me a sustainable, optimized travel plan given that I want to visit 4 places that are related to water bodies and vegetarian restaurants? Please give me only the list of location names in the order they need to be visited, without any description for them."

headers = {"Authorization": f"Bearer {config.API_KEY}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    # Check if the response is successful
    if response.status_code == 200:
        try:
            return response.json()[0]['generated_text']
        except Exception as e:
            print(f"Error parsing JSON: {e}")
            print(f"Response text: {response.text}")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response text: {response.text}")
        return None

# Increase token limit
MAX_TOKENS = 5000  # Set your desired maximum number of tokens
generated_output = query({"inputs": prompt, "max_length": MAX_TOKENS})

#print(generated_output)
# Print the generated output without the original prompt
print(generated_output.replace(prompt, "").strip())
# Split the generated output by newline
lines = generated_output.split('\n')

print("\nLines:")
print(lines)
places_list = [line.strip() for line in lines if line.strip().startswith(tuple([str(i) + '.' for i in range(1, 10)]))]

print(places_list)
# Print the extracted list of places
for place in places_list:
    print(place)
