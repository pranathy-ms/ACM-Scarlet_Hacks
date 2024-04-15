print("Hello there, this is our Hugging Face API implementation")

import requests
import config

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"

starting_location = "171 W Randolph St, Chicago"
number_of_places = "4"
start_date_time = "15th April 2024, 8:00 am"
types_of_places = "restaurants and water bodies"

# Define the input prompt
prompt = "Given my location is "+starting_location+", would you be able to provide me a sustainable, optimized plan for places to visit given that I want to visit "+number_of_places+" places that are related to "+types_of_places+"? Please give me only the list of location names in the order they need to be visited, without any description for them."# I am planning to take this trip starting "+start_date_time+"."

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
