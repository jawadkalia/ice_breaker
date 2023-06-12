from langchain.llms import HuggingFacePipeline
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, AutoModelForSeq2SeqLM
from langchain import PromptTemplate, HuggingFaceHub, LLMChain
from third_parties.loadenv import load_env
from third_parties.linkedin import scrape_linkedin_profile

load_env()

summary_template = """
        given the LinkedIn information {information} about a person, i want you to create:
         1. a short summary of the person
         2 two interesting facts about the person
    """

summary_prompt_template = PromptTemplate(
    input_variables=["information"], template=summary_template
)

model_id = 'mosaicml/mpt-7b'# go for a smaller model if you dont have the VRAM
tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, device_map='auto', trust_remote_code=True)

pipe = pipeline(
    "text-generation",
    model=model, 
    tokenizer=tokenizer,
)

local_llm = HuggingFacePipeline(pipeline=pipe)

llm_chain = LLMChain(llm=local_llm, prompt=summary_prompt_template)
linked_in_data=scrape_linkedin_profile()

print(llm_chain.run(information=linked_in_data))