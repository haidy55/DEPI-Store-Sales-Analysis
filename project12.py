import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

df = pd.read_excel('C:/Users/user/Downloads/clean.xlsx')


# إجمالي المبيعات لكل منطقة
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print(region_sales)

# رسم بياني لأداء المبيعات لكل منطقة
plt.figure(figsize=(8, 6))
region_sales.plot(kind='bar', color='skyblue')
plt.title('Total Sales by Region')
plt.ylabel('Sales')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.show()

# إجمالي المبيعات لكل فئة في كل منطقة
region_category_sales = df.groupby(['Region', 'Category'])['Sales'].sum().unstack()
print(region_category_sales)

# رسم بياني للمبيعات حسب المنطقة والفئة
region_category_sales.plot(kind='bar', stacked=True, figsize=(10, 6))
plt.title('Sales by Region and Category')
plt.ylabel('Sales')
plt.xlabel('Region')
plt.xticks(rotation=45)
plt.legend(title='Category')
plt.show()





# تحويل تاريخ الطلب إلى تاريخ فعلي
df['Order Date'] = pd.to_datetime(df['Order Date'])

# إضافة عمود الشهر والسنة
df['Year-Month'] = df['Order Date'].dt.to_period('M')

# إجمالي المبيعات الشهرية
monthly_sales = df.groupby('Year-Month')['Sales'].sum()
print(monthly_sales)

# رسم بياني لاتجاهات المبيعات الشهرية
plt.figure(figsize=(10, 6))
monthly_sales.plot(kind='line', marker='o', color='green')
plt.title('Monthly Sales Trends')
plt.ylabel('Sales')
plt.xlabel('Month-Year')
plt.xticks(rotation=45)
plt.grid(True)
plt.show()







# إجمالي المبيعات لكل طريقة شحن
ship_sales = df.groupby('Ship Mode')['Sales'].sum().sort_values(ascending=False)
print(ship_sales)

# رسم بياني لأداء المبيعات حسب طريقة الشحن
plt.figure(figsize=(8, 6))
ship_sales.plot(kind='bar', color='orange')
plt.title('Sales by Shipping Mode')
plt.ylabel('Sales')
plt.xlabel('Ship Mode')
plt.xticks(rotation=45)
plt.show()







# إجمالي المبيعات لكل شريحة عملاء
segment_sales = df.groupby('Segment')['Sales'].sum().sort_values(ascending=False)
print(segment_sales)

# رسم بياني لأداء المبيعات حسب شريحة العملاء
plt.figure(figsize=(8, 6))
segment_sales.plot(kind='bar', color='purple')
plt.title('Sales by Customer Segment')
plt.ylabel('Sales')
plt.xlabel('Segment')
plt.xticks(rotation=45)
plt.show()









# إجمالي المبيعات لكل فئة فرعية
sub_category_sales = df.groupby('Sub-Category')['Sales'].sum().sort_values(ascending=False)
print(sub_category_sales)

# رسم بياني لأداء المبيعات حسب الفئات الفرعية
plt.figure(figsize=(10, 6))
sub_category_sales.plot(kind='bar', color='red')
plt.title('Sales by Sub-Category')
plt.ylabel('Sales')
plt.xlabel('Sub-Category')
plt.xticks(rotation=90)
plt.show()










# أعلى 10 منتجات مبيعًا
top_products = df.groupby('Product Name')['Sales'].sum().nlargest(10)

# رسم بياني عمودي لمبيعات المنتجات
plt.figure(figsize=(12, 6))
top_products.plot(kind='barh', color='skyblue')
plt.title('Top 10 Best-Selling Products')
plt.xlabel('Sales')
plt.ylabel('Product Name')
plt.show()












# حساب إجمالي المبيعات لكل فئة
category_sales = df.groupby('Category')['Sales'].sum()

# رسم بياني دائري لتوزيع المبيعات حسب الفئات
plt.figure(figsize=(10, 8))
plt.pie(
    category_sales, 
    labels=category_sales.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    explode=[0.1] * len(category_sales),  # تفجير القطع لزيادة الوضوح
    shadow=True
)
plt.title('Sales Distribution by Category')
plt.axis('equal')  # لضمان أن المخطط دائري
plt.show()








# حساب إجمالي المبيعات لكل منطقة
region_sales = df.groupby('Region')['Sales'].sum()

# رسم بياني دائري لتوزيع المبيعات حسب المناطق
plt.figure(figsize=(10, 8))
plt.pie(
    region_sales, 
    labels=region_sales.index, 
    autopct='%1.1f%%', 
    startangle=90, 
    explode=[0.1] * len(region_sales),  # تفجير القطع لزيادة الوضوح
    shadow=True
)
plt.title('Sales Distribution by Region')
plt.axis('equal')  # لضمان أن المخطط دائري
plt.show()



