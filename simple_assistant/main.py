from source.agent import agent1, agent2

import json 

# Основной цикл общения с агентом
def chat(thread_id: str):
    """
    Основная функция для общения с агентом.
    """
    config = {"configurable": {"thread_id": thread_id}}
    
    with open("mail/mail_test.json", "r", encoding="utf-8") as f:
        mail_test = json.load(f)


    emails_text = "\n\n".join(
    f"Письмо №{nmbr+1} Отправитель: {email['Отправитель']}\nТема: {email['Тема']}\nТекст: {email['Текст']}"
    for nmbr, email in enumerate(mail_test)
    )


    agent1_response = agent1.invoke({
            "messages": [
                {"role": "user", "content": emails_text}
            ]},
            config=config
    )

    input_agent2 = {
        "messages":{"role":"user", "content": f"Данные:\n{emails_text}\n\nАнализ первого агента:\n{agent1_response}"}
    }

    agent2_response = agent2.invoke(input_agent2, config=config)

    print("Ответ консультанта:\n", agent2_response["messages"][-1].content)
        
        

if __name__ == "__main__":
    chat('SberAX_consultant')