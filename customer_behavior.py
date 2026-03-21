"""Customer shopping behavior analysis module."""
import pandas as pd
df= pd.read_csv(r"C:/Users/nguye/Downloads/customer_shopping_behavior.csv")


df['Review Rating'] = df.groupby('Category')['Review Rating'].transform(lambda x: x.fillna(x.median()))

#chỉnh lại chữ của các cột (lowercase + thay khoảng trắng thành _, đổi tên cột cần thiết)
df.columns = df.columns.str.lower()
df.columns = df.columns.str.replace(' ','_')
df = df.rename(columns={'purchase_amount_(usd)': 'purchase_amount'})


#chia nhóm tuổi
labels = ['Young Adult','Adult','Middle-Aged','Senior']
df['age_group'] = pd.qcut(df['age'],q=4, labels = labels)


#frequency_of_purchases
frequency_mapping = {
    'Fortnightly' : 14,
    'Weekly' : 7,
    'Monthly': 30,
    'Quarterly': 90,
    'Bi-Weekly': 14,
    'Annually': 365,
    'Every 3 Months': 90
}
df['purchase_frequency_days'] = df['frequency_of_purchases'].map(frequency_mapping)

# print(df[['discount_applied', 'promo_code_used']].head(10))

# print((df['discount_applied'] == df['promo_code_used']).all())

df = df.drop('promo_code_used', axis=1)
# print(df.columns)

from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://@ACER-ASPIRE-7/customer_behavior?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

df.to_sql(
    name='customer_behavior',
    con=engine,
    if_exists='replace',
    index=False
)

print("Đưa dữ liệu thành công!")