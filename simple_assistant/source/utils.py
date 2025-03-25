from langchain.agents import tool

@tool
def check_urgency(text: str) -> str:
    """Определяет, требует ли текст письма срочного ответа. 
    
    Args:
        text (str): Текст письма для анализа
        
    Returns:
        str: 'Срочное' если содержит слово 'срочно', иначе 'Не срочное'
    """
    return "Срочное" if "срочно" in text.lower() else "Не срочное"


