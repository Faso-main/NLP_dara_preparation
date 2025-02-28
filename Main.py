from docx import Document

def parse_docx_by_bold_sections(file_path):
    doc = Document(file_path)
    categories = {}
    current_category = "Без категории"
    current_text = []

    for paragraph in doc.paragraphs:
        # Проверяем, является ли весь абзац заголовком (все runs жирные)
        is_header = all(run.bold for run in paragraph.runs if run.text.strip())
        
        if is_header and paragraph.text.strip():
            # Сохраняем предыдущую категорию
            if current_text:
                categories.setdefault(current_category, []).append(" ".join(current_text))
                current_text = []
            
            # Новая категория (убираем лишние символы)
            current_category = paragraph.text.strip().strip('*:')
        else:
            # Собираем текст внутри категории
            current_text.append(paragraph.text)
    
    # Добавляем последнюю категорию
    if current_text:
        categories.setdefault(current_category, []).append(" ".join(current_text))

    return categories

# Обработка таблиц (пример для ключевой таблицы)
def process_tables(doc):
    tables_data = []
    for table in doc.tables:
        for row in table.rows:
            row_data = [cell.text.strip() for cell in row.cells]
            tables_data.append(row_data)
    return tables_data

# Пример использования
doc_path = "Marked.docx"
result = parse_docx_by_bold_sections(doc_path)
tables = process_tables(Document(doc_path))

# Вывод результатов
print("="*50 + "\nКатегории:\n")
for category, texts in result.items():
    print(f"{category.upper()}:")
    for text in texts:
        print(f" - {text}")
    print()

print("="*50 + "\nТаблицы:\n")
for i, table in enumerate(tables, 1):
    print(f"Строка таблицы {i}: {table}")