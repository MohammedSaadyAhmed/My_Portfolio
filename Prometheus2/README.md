# Prometheus Task 2

## 1) How do I trigger a Prometheus alert?
- Define Alerting Rules: Create alerting rules in Prometheus configuration (in prometheus.yml file). Alerting rules define the conditions that need to be met for an alert to be triggered. These rules are written in the PromQL language (Prometheus Query Language).
- Configure Alertmanager: Prometheus uses Alertmanager to manage and send alerts to various alert notification channels. Set up Alertmanager and define notification configurations, such as email, Slack, or PagerDuty.
- Simulate Alert Condition: To trigger an alert for testing purposes, you can either:
    * Modify Metrics: Change the metric values of your target so that it matches the alerting rule's condition. For example, if the rule states 
      that the CPU usage should be above a certain threshold, artificially increase the CPU usage.
    * Send Test Alert: Some alert managers provide a way to send test alerts, allowing you to simulate alerts without changing metrics. For 
      example, in Alertmanager, you can use the amtool command to send a test notification.
- onitor Alertmanager: Once the alert conditions are met, Prometheus will fire the alert and send it to the Alertmanager. From there, the Alertmanager will handle the notifications according to your configured notification channels.
-----
## 2) What is the difference between node exporter and mysql exporter ?

- Node Exporter is a Prometheus exporter specifically designed to collect system-level metrics from the operating system and hardware of a 
machine. It runs as a separate process on the target machine and exposes a variety of metrics related to CPU usage, memory, disk I/O, network statistics, and more. Node Exporter provides valuable insights into the overall health and performance of the system it is running on.
- MySQL Exporter, on the other hand, is a Prometheus exporter specifically tailored to collect metrics from MySQL database servers. It connects to the MySQL server, executes queries, and exposes various performance-related metrics about the MySQL database instance. This allows you to monitor the health and performance of your MySQL databases and identify potential bottlenecks or issues.
-----
## 3) what is the maximum retention period to save data in Prometheus and how to increase it ?
- The maximum retention period to save data in Prometheus is determined by the configuration of the underlying storage system used by Prometheus. Prometheus uses a local storage engine to retain time-series data, and the retention period is defined in the configuration file.
By default, Prometheus stores data for 15 days (15d). However, you can adjust this retention period according to your requirements. 

-----
## 4) What are the different PromQL data types available in Prometheus Expression language?
- Scalars
- Matrix
- Vectors
- Strings
- Durations
- Instant Vectors
- Range Vectors

-----
## 5) How To calculate the average request duration over the last 5 minutes from a histogram ?
- use the rate() and histogram_quantile() functions in combination
  ```
  rate(http_request_duration_seconds_bucket{job="your_job_name", le="0.1"}[5m])
  ```

-----
## 6) What is Thanos Prometheus?
- Thanos is an open-source project that extends the capabilities of Prometheus, a popular monitoring and alerting toolkit. It aims to address the challenges related to long-term storage and high availability of Prometheus data in a distributed and scalable manner. Thanos seamlessly integrates with Prometheus and extends its capabilities beyond a single, isolated Prometheus server.

-----
## 7) what is promtool ?
- Promtool is a command-line utility provided by Prometheus, which is used for checking and validating Prometheus configuration files and rules. It helps ensure that your Prometheus setup is correctly configured, and the rules and configurations adhere to the expected format and syntax.

-----
## 8) What types of Monitoring can be done via Grafana?
- **Infrastructure Monitoring:** Grafana can monitor the health and performance of your infrastructure components
- **Application Monitoring:** Grafana can monitor applications by integrating with application-specific monitoring tools like Prometheus, Jaeger, Zipkin, and StatsD. It allows you to track application-specific metrics, request latency, error rates, and other custom application-related data.
- **Cloud Services Monitoring:** Grafana can monitor cloud services from providers like AWS, Google Cloud, and Azure. It supports cloud-specific integrations to monitor various services, such as EC2 instances, S3 buckets, RDS databases, and more.
- **Database Monitoring:** Grafana can monitor databases like MySQL, PostgreSQL, MongoDB, and others. It can display database-specific metrics such as query performance, connections, and cache utilization.
- **Log Monitoring** hile Grafana is primarily a time-series data visualization tool, it can be integrated with log management systems like Loki, Elasticsearch, and Graylog. This enables the display of logs alongside metrics, allowing for comprehensive system monitoring.
-----
## 9) Can we see different Servers CPU comparison in Grafana
- Yes, you can easily see and compare CPU usage across different servers in Grafana by creating a dashboard that displays CPU metrics from multiple servers side by side.

