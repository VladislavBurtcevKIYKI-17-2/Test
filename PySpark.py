from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# Создание Spark сессии
spark = SparkSession.builder.appName("ProductCategoryPairs").getOrCreate()

# Предположим, у нас есть датафреймы products_df и categories_df с полями 'product_name' и 'category_name'

# Создадим датафрейм для всех пар «Имя продукта – Имя категории»
product_category_pairs_df = products_df.crossJoin(categories_df)

# Создадим датафрейм с именами продуктов, у которых нет категорий
products_without_categories_df = products_df.join(categories_df, products_df['product_name'] == categories_df['product_name'], 'left_anti') 

# Выведем результаты
product_category_pairs_df.show()
products_without_categories_df.show()

# Закрытие Spark сессии
spark.stop()
