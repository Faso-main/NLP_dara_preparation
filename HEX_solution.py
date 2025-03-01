from bs4 import BeautifulSoup
from collections import defaultdict

def extract_text_by_background(html_content):
    # Парсим HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Словарь для сопоставления CSS-классов с HEX-цветами
    color_classes = {
        'c22': '#bdd6ee',    # Голубой
        'c18': '#ffff00',     # Желтый
        'c13': '#b4c6e7',    # Светло-синий
        'c32': '#ffccff',     # Розовый
        'c35': '#f7caac',     # Персиковый
        'c24': '#dbdbdb',     # Серый
        'c33': '#f2f2f2',     # Светло-серый
        'c38': '#fff2cc'      # Бежевый
    }
    
    color_text_map = defaultdict(list)
    
    # Ищем все элементы с классами из color_classes
    for css_class, hex_color in color_classes.items():
        elements = soup.find_all(class_=css_class)
        for elem in elements:
            text = elem.get_text(strip=True)
            if text:
                color_text_map[hex_color].append(text)
    
    return color_text_map

# Пример использования
with open("Marked.html", "r", encoding="utf-8") as f:
    html_content = f.read()

result = extract_text_by_background(html_content)

# Вывод результатов
for color, texts in result.items():
    print(f"Цвет фона: {color}")
    print("Текст:", " | ".join(texts))
    print("-" * 50)