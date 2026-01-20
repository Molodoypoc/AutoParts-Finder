import pandas as pd
from .models import Part

def get_parts_analytics():
    # Извлекаем данные из БД через ORM
    queryset = Part.objects.all().values('category', 'price')
    if not queryset.exists():
        return None
    
    # Создаем DataFrame
    df = pd.DataFrame(list(queryset))
    
    # Глубокая аналитика: считаем среднюю цену по категориям
    stats = df.groupby('category')['price'].agg(['mean', 'count']).round(2)
    
    # Конвертируем в словарь для передачи в шаблон
    return stats.to_dict('index')