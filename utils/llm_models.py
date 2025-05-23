from pydantic_ai.models.openai import OpenAIModel
from pydantic_ai.providers.openai import OpenAIProvider

openrouter_model = OpenAIModel(
    'mistralai/mistral-small-3.1-24b-instruct:free',
    provider=OpenAIProvider(base_url='https://openrouter.ai/api/v1', api_key='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'),
)

ollama_model = OpenAIModel(
    model_name='mistral-small3.1', provider=OpenAIProvider(base_url='http://localhost:11434/v1')
)
