# pandemic-outburst-forecast-model

## Description
Forecasting Covid-19 outburst in Vietnam provinces for a short period (7 days, 14 days & 28 days)

## Forecast model:
- Tradition SIR model
- SIRV model - effect of vaccination
- Optimized parameters with Regression

### Traditional SIR model:
- Use S-I-R values of the current day to calculate the expected S-I-R values of the following day
- Performance: Loss function on total cases (and S-I-R) values

### SIRV model:
- Use S-I-R values of the current day & the V value of the 14th day before to calculate the expected S-I-R values of the following day
- Performance: Loss function on total cases (and S-I-R) values

### Regression model:
Chạy hàm predict với 2 tham số đầu vào: 
- input_file_path: file csv đầu vào. Ở đây ví dụ là file data/VN-covid19.csv
Cấu trúc file đầu vào gồm 2 cột là ObservationDate và Confirmed. 
- X là số ngày tiếp theo sẽ dự đoán Confirmed case.

Sau khi chạy dự đoán kết quả được ghi ra file có phần tiền tồ là "Predict_for_", 
Ở đây là file data/Predict_for_VN-covid19.csv
File kết quả gồm cột predict_confirmed_case là kết quả dự đoán, còn cột confirmed_case là số ca gốc.
