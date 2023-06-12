from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI

from langchain.agents import initialize_agent, Tool, AgentType

from tools.tools import get_profile_url


def lookup(name: str) -> str:
    llm = ChatOpenAI(temperature=0, model="gpt-3.5-turbo")

    template = """given the full name {name_of_person}, I want you to get me a link to their twitter profile. and extract from it the username. 
    your answer should contain only a username"""

    tools_for_agent = [
        Tool(
            name="Crawl Google for twitter profile page",
            func=get_profile_url,
            description="use for when you need to find and get a twitter profile page",
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

    twitter_username = agent.run(prompt_template.format_prompt(name_of_person=name))

    return twitter_username
