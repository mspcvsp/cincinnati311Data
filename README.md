# cincinnati311Data
City of Cincinnati 311 (Non-Emergency Service Requests) Open Data Processing Software

- [City of Cincinnati 311 Non-Emergency Requests Open Data Set](https://data.cincinnati-oh.gov/Thriving-Healthy-Neighborhoods/Cincinnati-311-Non-Emergency-Service-Requests/4cjh-bm8b)  
- [Syntax for submitting a Python Hadoop Streaming job](http://hadoop.apache.org/docs/r1.2.1/streaming.html)  
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/USER/cincinnati311Data -output /user/USER/monthlyCount -mapper /PATH/cincinnati311Data/monthly_count_mapper.py -reducer /PATH/cincinnati311Data/key_count_reducer.py
