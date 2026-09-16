# Screenshot checklist for the Google Doc

The assignment asks for an accessible Google Doc with screenshots. Capture at least these.

## Question 1

- [ ] VPC
- [ ] Public subnet
- [ ] Internet Gateway attached to the VPC
- [ ] Route table with `0.0.0.0/0` to the Internet Gateway
- [ ] EC2 security group showing SSH 22 and HTTP 80
- [ ] Running EC2 instance in the public subnet
- [ ] Browser showing the NGINX page on the EC2 public IP
- [ ] Target group with the instance `healthy`
- [ ] Application Load Balancer details
- [ ] Browser showing the same page on the ALB URL

## Question 2

- [ ] GitHub repository with this project
- [ ] GitHub Actions workflow file
- [ ] Successful Actions run after a push to `main`
- [ ] S3 bucket containing `index.html`, `styles.css`, and `app.js`
- [ ] CloudFront distribution
- [ ] Browser showing the CloudFront URL with Version 2.0
- [ ] Optional: a second successful run after a website change

## Submission text

```text
Question 1: http://<alb-dns-name>
Question 2: https://<cloudfront-domain>
Accessible Google Doc Link: <doc-url>
```
