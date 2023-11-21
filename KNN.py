# Nhập thư viện cần thiết
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

# Tải dữ liệu Iris
iris_dataset = load_iris()

# Chia tập dữ liệu thành tập huấn luyện và tập kiểm tra
X_train, X_test, y_train, y_test = train_test_split(iris_dataset['data'], iris_dataset['target'], random_state=0)

# Nhập giá trị K từ người dùng
K = int(input("Nhập giá trị K: "))

# Tạo mô hình KNN với K láng giềng 
knn = KNeighborsClassifier(n_neighbors=K)

# Huấn luyện mô hình dựa trên tập huấn luyện
knn.fit(X_train, y_train) 

# Dự đoán trên tập kiểm tra
y_pred = knn.predict(X_test)

# Đánh giá mô hình
print("Độ chính xác:", np.mean(y_pred==y_test))