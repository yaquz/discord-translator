def detect_language(text):
    # Простейший способ определения языка: проверка первых символов
    for char in text:
        if char in "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM":
            return "en"
        elif char in "йцукенгшщзхъфывапролджэячсмитьбюёЙЦУКЕНГШЩЗХЪФЫВАПРОЛДЖЭЯЧСМИТЬБЮЁ":
            return "ru"
    return "unknown"

def transliterate(text, lang):
    english = ['`', 'Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P', '[', ']', 'A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L',
               ';', "'", 'Z', 'X', 'C', 'V', 'B', 'N', 'M', ',', '.', '`', 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p',
               '[', ']', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', ';', "'", 'z', 'x', 'c', 'v', 'b', 'n', 'm', ',', '.']
    russian = ['Ё', 'Й', 'Ц', 'У', 'К', 'Е', 'Н', 'Г', 'Ш', 'Щ', 'З', 'Х', 'Ъ', 'Ф', 'Ы', 'В', 'А', 'П', 'Р', 'О', 'Л', 'Д',
               'Ж', 'Э', 'Я', 'Ч', 'С', 'М', 'И', 'Т', 'Ь', 'Б', 'Ю', 'ё', 'й', 'ц', 'у', 'к', 'е', 'н', 'г', 'ш', 'щ', 'з',
               'х', 'ъ', 'ф', 'ы', 'в', 'а', 'п', 'р', 'о', 'л', 'д', 'ж', 'э', 'я', 'ч', 'с', 'м', 'и', 'т', 'ь', 'б', 'ю']

    if lang == "en":
        translator = dict(zip(english, russian))
    elif lang == "ru":
        translator = dict(zip(russian, english))
    else:
        return text

    return "".join(translator.get(char, char) for char in text)

# пример использования НЕ в боте

"""
input_text = input("Введите текст: ")
language = detect_language(input_text)
output_text = transliterate(input_text, language)
print("Переведённый текст:", output_text)
"""
