from category_encoders import BinaryEncoder
import pandas as pd
data = ['red', 'green','blue']
encoder = BinaryEncoder(cols=['Color'])
encoded_data = encoder.fit_transform(pd.DataFrame(data, columns=['Color']))
print(encoded_data)