import os
from AIComponents.agents import Agents
from AIComponents.tools import *
from dotenv import load_dotenv
from crewai import Task
from components.subcomponents import urlbase

load_dotenv()

# Initialize the chat model
openaigpt4 = ChatOpenAI(model='gpt-4o', 
                        temperature=0.2, 
                        api_key=os.getenv('openapi_key'))

class Tasks:
    def __init__(self, Input, Context, lang):
        self.Input = Input
        self.Context = Context
        self.lang = lang

    def SearchDataTask(self):
        GemaSearchData = Task(
            description = f"""Perform research and data search regarding the results based on the question "{self.Input}" provided by the user, with a focus on {self.Context}.
                             Use SearchTools for your data search.
                             Prioritize finding and cross-validating data specifically related to SMKN 1 GRATI {urlbase}.
                             If information is not available directly from the official website, search for additional references from credible sources that align with GEMA FOUNDATION's focus.
                             Organize your data as if it's a Wikipedia article, ensuring that all information is relevant to the foundation and its work.
                             Include relevant reference links at the bottom, ensuring that GEMA SMKN 1 GRATI site is included as a source when applicable.
                             Provide context or expert advice to provide a comprehensive understanding of the topic.""", 
            expected_output = """A detailed report containing:
                                 - Clear explanations related to {self.Context} based on the user's question, with a focus on SMKN 1 GRATI goals and initiatives
                                 - Key points formatted similarly to Wikipedia entries, ensuring all information is aligned with SMKN 1 GRATI work
                                 - Relevant references from all existing but related sources to {self.input} and {self.context}""",
            agent=Agents().DataSearch(),
            tools=[SearchTools,WebsiteSearchTool]
        )
        return GemaSearchData

    def ContextUserQuer(self):
        ContextedUserQuer = Task(
            description = f"""Analyze this user input: {self.Input}.
                             Provide a clear and focused (CONTEXT) based on the identified issue.""", 
            expected_output=f"""A structured report that includes:
                                  - The original user input: {self.Input}
                                  - Explanation of what the user is really looking for
                                  - Explanation of the desired user output
                                  - Relevant and usable references""", 
            agent=Agents().Contextualize()
        )
        return ContextedUserQuer

    def AugmentContext(self):
        AugmentedContext = Task(
            description = f"""Analyze the provided (CONTEXT) and compare it with {self.Input}. Use provided information and references to better understand {self.Context}.
                             Formulate the best prompt for generating a comprehensive response to answer {self.Input} within the scope of {self.Context}.""",
            expected_output=f"""A report containing:
                                - The original user input: {self.Input}
                                - Explanation of what the user is really looking for
                                - A prompt for addressing the context (the prompt should contain pre-searched information)
                                - Relevant and usable references""", 
            agent=Agents().Augment()
        )
        return AugmentedContext

    def AnalyseAugContext(self):
        AnalysedAugContext = Task(
            description = f"""Answer the user input {self.Input} with respect to the provided (CONTEXT) based on the given prompt as guidance for providing the desired user output.
                             Use SearchTools to gather additional information if required.""", 
            expected_output=f"""A suggestion sheet in {self.lang} that includes:
                                  - In-depth explanations of key points of {self.Context}
                                  - Additional information regarding {self.Context} in line with the prompt and CONTEXT={self.Context}
                                  - Clear and detailed steps, if requested, with related information in line with CONTEXT={self.Context}!!
                                  - A list of references used
                                  Note: MUST USE {self.lang}""", 
            agent=Agents().Adviser(),
            tools=[SearchTools]
        )
        return AnalysedAugContext
        
    # def Booksearch(self):
    #     Booksearch = Task(
    #         description = f"""Use [SearchTools,WebsiteSearchTool] to access the official Gbook Gaeni API key: https://gbook.gaeni.org/api-v1/book and retrieve information from that site based on {self.Input}.""",
    #         expected_output=f"""A list of the information you retrieve.""",
    #         agent=Agents().DataSearch(),
    #         tools=[SearchTools])
    #     return Booksearch