from app.llm import get_llm
from app.prompts import get_prompt

from langchain_core.output_parsers import StrOutputParser

## Create a complete langchain pipeline

def get_chain():
    ## Step 1: Create the LLM
    llm = get_llm()

    ## Step 2: create the prompt template
    prompt = get_prompt()

    ## Step 3: Create output parser
    parser = StrOutputParser()

    ## Step 4: Connect the components using | operator

    chain  = prompt | llm | parser

    return chain