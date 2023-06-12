import os
from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from dotenv import load_dotenv
from third_parties.linkedin import scrape_linkedin_profile
from third_parties.loadenv import load_env


if __name__ == "__main__":
    load_env()
    print("Hello LangChain!")

    summary_template = """
        given the LinkedIn information {information} about a person, i want you to create:
         1. a short summary of the person
         2 two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOpenAI(temperature=0.9, model_name="gpt-3.5-turbo")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    
    linked_in_data=scrape_linkedin_profile()

    print(chain.run(information=linked_in_data))


