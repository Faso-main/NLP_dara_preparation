from docx import Document
from docx.enum.text import WD_COLOR_INDEX
from collections import defaultdict
import os

def extract_text_by_highlight(doc_path):
    doc = Document(doc_path)
    highlight_categories = defaultdict(list)

    # Соответствие кодов цветов их названиям
    color_names = {
        WD_COLOR_INDEX.YELLOW: "YELLOW",
        WD_COLOR_INDEX.GREEN: "GREEN",
        WD_COLOR_INDEX.BLUE: "BLUE",
        WD_COLOR_INDEX.BRIGHT_GREEN: "BRIGHT_GREEN",
        WD_COLOR_INDEX.DARK_BLUE: "DARK_BLUE",
        WD_COLOR_INDEX.GRAY_50: "GRAY_50",
        WD_COLOR_INDEX.GRAY_25: "GRAY_25",
        WD_COLOR_INDEX.RED: "RED",
        # и так далее
    }

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            highlight = run.font.highlight_color
            if highlight is not None and highlight in color_names:
                color = color_names[highlight]
                text = run.text.strip()
                if text:  # Игнорировать пустые пробелы
                    highlight_categories[color].append(text)

    return highlight_categories

# Пример использования
file_path = os.path.join('Marked_example')
result = extract_text_by_highlight(file_path)

# Вывод результатов
for color, texts in result.items():
    print(f"Цвет выделения: {color}")
    print("Текст:", " | ".join(texts))
    print("-" * 50)