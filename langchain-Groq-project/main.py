from app.chains import get_chain

def run_chat():
    chain = get_chain()

    ## Display instructions for the user
    print(
        "Groq langchain chatbot "
        "Type 'exit' to quit \n"
    )

    ## Continuously accept user input
    while True:
        user_input = input(
            "Pass medical queries: "
        )

        ## Exit condition
        if user_input.lower() == 'exit':
            break

        ## Invoke langchain pipeline

        response = chain.invoke(
            {
                "input" : user_input
            }
        )

        ## Display the final result
        print("Bot: ", response)

if __name__ == "__main__":
    run_chat()