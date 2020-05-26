# Streaming-Stock-Data-AWS-Lambda
## Learning Goal

This project leads you through the process of consuming “real time” data, processing the data and then dumping it in a manner that facilitates querying and further analysis, either in real time or near real time capacity.
### Tools: AWS Lambda, Kinesis, Glue, Athena; [yfinance](https://pypi.org/project/yfinance/)

## Framework
![framework](https://github.com/mendel462/Streaming-Stock-Data-AWS-Lambda/blob/master/screenshot_dashboard/Workflow.JPG)

## Data Collector (AWS Lambda) 

* [URL Trigger](https://tels36ux11.execute-api.us-east-2.amazonaws.com/default/delivery-yfinance-stream-processor) 

*This will **NOT** work with the API Gateway invocation, because downloading this dependency takes some time, too long for API Gateway to stay “on”.*

We collect the stock data of **Facebook (FB), Shopify (SHOP), Beyond Meat (BYND), Netflix (NFLX), Pinterest (PINS), Square (SQ), The Trade Desk (TTD), Okta (OKTA), Snap (SNAP), Datadog (DDOG)** on **May 14th, 2020**  

![data_collector](https://github.com/mendel462/Streaming-Stock-Data-AWS-Lambda/blob/master/screenshot_dashboard/DataCollector%20Lambda%20configuration%20page.JPG)


## Data Transformer (AWS Kinesis + AWS Lambda) 
### Kinesis Firehose Delivery Stream “Monitoring” 
![data_transformer](https://github.com/mendel462/Streaming-Stock-Data-AWS-Lambda/blob/master/screenshot_dashboard/Kinesis%20Data%20Firehose%20Delivery%20Stream%20Monitoring.JPG)
