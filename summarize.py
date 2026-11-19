# named entity rekognition
#key phrase extraction from user content

from openai import AzureOpenAI

# 1. Endpoint should be the "Endpoint" or "Target URI" found in the Azure portal
# Format is typically: https://<your-resource-name>.openai.azure.com/
# Or the new format: https://<your-resource-name>.services.ai.azure.com/
endpoint = "https://project25115-resource.services.ai.azure.com/"

# 2. API Key (please ensure it is not leaked)
api_key = api-key("1KpC5N3S76nK55GTEJ3Oy0qPorsV2tYmoDeSOAUNDj0Hjc8C6bqqJQQJ99CKACE1PydXJ3w3AAAAACOGsTKZ")

# 3. Deployment Name: fill in the deployment name you set in Azure AI Foundry
# It may be different from the model name (gpt-5-mini), be sure to verify
deployment_name = "gpt-5-mini"  # Please confirm this is your deployment name

# 4. Use AzureOpenAI client
client = AzureOpenAI(
    azure_endpoint=endpoint,
    api_key=api_key,
    api_version="2024-12-01-preview"  # Use a recent stable API version
)
long_text = """
Here’s an example one-paragraph summary of an article about renewable energy adoption:

Governments and businesses worldwide are accelerating the shift to renewable energy, driven by falling costs for solar and wind technology, stronger climate policies, and increasing investor and consumer demand for sustainable practices. Advances in battery storage and grid management are addressing intermittency challenges, while electrification of transport and industry is expanding demand for low-carbon power. Despite progress, deployment must scale faster and policies must ensure a just transition for workers and communities most affected by fossil-fuel phaseouts. If coordinated action continues, analysts say renewables can supply a majority of global electricity by mid-century, significantly reducing greenhouse gas emissions and improving air quality.
"""
# 5. Call the model (model parameter uses deployment name)
response = client.chat.completions.create(
    model=deployment_name,
    messages=[
        {"role": "system", "content": "You are a Summarization assistant.summarize the user text into proper summary."},
        {"role": "user", "content": long_text}
    ]
)

print(response.choices[0].message.content)