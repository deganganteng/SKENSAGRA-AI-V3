from langchain_community.utilities import GoogleSerperAPIWrapper
import os
from dotenv import load_dotenv
from langchain.agents import Tool
from langchain_openai import ChatOpenAI
from crewai_tools import WebsiteSearchTool

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI GPT model
openaigpt4 = ChatOpenAI(model='gpt-4', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

WebsiteSearchTool = WebsiteSearchTool()

# Initialize GoogleSerperAPIWrapper with the API key from environment variables
google_serper = GoogleSerperAPIWrapper(api_key=os.getenv('serper_api_key'))

# Wrap GoogleSerperAPIWrapper in a Tool for search queries
SearchTools = Tool(
    name="Search",
    func=google_serper.run,
    description="A tool for performing search queries that return the most relevant current information. " +
                "Input a specific, well-formed query to receive direct, focused results that answer the question at hand."
)
