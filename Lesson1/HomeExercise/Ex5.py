import pandas as pd
import matplotlib.pyplot as plt

# Đọc dữ liệu từ tệp CSV
df = pd.read_csv('file.csv')  
print(df.head())

# Vẽ biểu đồ đường dựa trên dữ liệu
plt.figure(figsize=(10, 6))
plt.plot(df['Thời gian'], df['Giá trị'], marker='o', linestyle='-', color='b')
plt.title('Biểu đồ đường')
plt.xlabel('Thời gian')
plt.ylabel('Giá trị')
plt.grid(True)
plt.show()
