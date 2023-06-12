from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType
from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """given the full name {name_of_person}, I want you to get me a link to their LinkedIn profile. your answer should contain only a url"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for LinkedIn profile page",
            func=get_profile_url,
            description="use for when you need to find and get a LinkedIn profile page",
        )
    ]

    agent = initialize_agent(
        tools=tools_for_agent,
        agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        verbose=True,
    )

    prompt_template = PromptTemplate(
        input_variables=["name_of_person"], template=template
    )

    linkedin_profile_url = agent.run(prompt_template.format_prompt(name_of_person=name))

    return linkedin_profile_url
