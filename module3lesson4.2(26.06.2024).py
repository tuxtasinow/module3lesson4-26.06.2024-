def single_root_words(root_word, *other_words):
  same_words = []
  count = 0  # Инициализируем счетчик
  for i in other_words:
      if root_word.lower() in i.lower() or i.lower() in root_word.lower():
          count += 1  # Увеличиваем счетчик при каждом совпадении
          same_words.append(i)
  return same_words


result1 = single_root_words('rich', 'richest', 'erhicalture', 'cheers', 'reliches')
print(result1)
result2 = single_root_words('disable', 'able', 'table', 'disablee', 'tagle')
print(result2)