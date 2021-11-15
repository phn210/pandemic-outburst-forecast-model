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
