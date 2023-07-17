from langchain import OpenAI, PromptTemplate, LLMChain
from langchain.chains import SequentialChain
import os


from secret_key import open_api_key

os.environ["OPENAI_API_KEY"] = open_api_key
llm = OpenAI(temperature=0.5)


def generate_restaurant_name_and_items(cuisine):
    # Chain 1
    prompt_template_name = PromptTemplate(
        input_variables=["cuisine"],
        template="I want to open a resturant for {cuisine} food. Suggest me a fancy name for my restaurant.",
    )

    name_chain = LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    # Chain 2
    prompt_template_items = PromptTemplate(
        input_variables=["restaurant_name"],
        template="""Suggest me some menu items for my restaurant {restaurant_name}. Return it as comma separated 
        values.""",
    )

    food_items_chain = LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
                            chains=[name_chain, food_items_chain],
                            input_variables=["cuisine"],
                            output_variables=["restaurant_name", "menu_items"]
    )

    return chain({"cuisine": cuisine})


if __name__ == "__main__":
    print(generate_restaurant_name_and_items("Indian"))