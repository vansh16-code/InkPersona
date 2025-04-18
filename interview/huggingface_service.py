from transformers import pipeline

generator = pipeline('text-generation', model='gpt2')

def generate_response(character_name: str, character_description: str, question: str):
    prompt = f"""
    You are {character_name}. 
    {character_description}

    Answer the following question directly based on your personality and experiences. Only give the answer, nothing else. Do not explain your traits or history—just answer the question as you would based on your character's past and beliefs.

    Question: {question}
    Answer:
    """
    
    response = generator(
        prompt, 
        max_new_tokens=100,  
        num_return_sequences=1,
        do_sample=True,      
        temperature=0.7      
    )
    
    # Extract and clean up the response to return only the answer
    answer = response[0]['generated_text'].strip().split("Answer:")[-1].strip()

    return answer
