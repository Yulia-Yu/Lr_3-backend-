from jinja2 import Environment, FileSystemLoader

def add_spaces(text):
 return " ".join(text)

def count_dis(subjects):
 return len(subjects)


# Лабораторная 3 задание 1
env = Environment(loader=FileSystemLoader('.'))

template = env.get_template('template_3_1.html')

col = "синий зеленый красный"
list_checked = [1, 2]

result_html = template.render(
    colors=col,
    list_checked=list_checked,
    range=range
)

with open('test.html', 'w', encoding='utf-8-sig') as res:
  res.write(result_html)


# Лабораторная 3 задание 2
  books = [
   {"title": "Мастер и Маргарита",
    "author": "Булгаков М.А.",
    "price": 581.50},
   {"title": "Белая гвардия",
    "author": "Булгаков М.А.",
    "price": 600.00},
   {"title": "Война и мир",
    "author": "Толстой Л.Н.",
    "price": 899.99},
   {"title": "Анна Каренина",
    "author": "Толстой Л.Н.",
    "price": 450.10},
   {"title": "Игрок",
    "author": "Достоевский Ф.М.",
    "price": 234.55}
  ]

  env = Environment(loader=FileSystemLoader('.'))

  template = env.get_template('template_3_2.html')

  list_book = [1, 3]

  result_html = template.render(
   books=books,
   list_book=list_book,
   range=range
  )

  with open('test_2.html', 'w', encoding='utf-8-sig') as res:
   res.write(result_html)