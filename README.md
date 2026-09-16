# DevOps Fundamentals Practical Assignment

This folder contains both practical tasks from the assignment:

1. **Question 1** — a simple NGINX webpage for an EC2 instance behind an Application Load Balancer
2. **Question 2** — an HTML/CSS/JavaScript website with a GitHub Actions pipeline that deploys to Amazon S3 and CloudFront

The assignment is scored on working public URLs, not on application complexity.

## Project layout

```text
q1-ec2-nginx/          Webpage to copy onto the EC2 NGINX server
website/               Question 2 static site
tests/                 Checks required page content before deploy
.github/workflows/     GitHub Actions: test -> package -> deploy
docs/                  AWS Console, CI/CD setup, and screenshot checklist
```

## Question 1

Create the VPC, subnet, Internet Gateway, route table, security group, EC2 instance, NGINX, target group, and ALB **manually in the AWS Console**.

Follow `docs/q1-aws-console-guide.md` and serve `q1-ec2-nginx/index.html`.

Submit the ALB URL, for example:

`http://my-application-alb-123456789.ap-south-1.elb.amazonaws.com`

## Question 2

The site in `website/` already shows:

- DevOps Training
- CI/CD Deployment Successful
- Version: 2.0
- Deployed automatically using GitHub Actions

Follow `docs/q2-cicd-setup.md` to:

1. Push this project to GitHub
2. Create the S3 bucket and CloudFront distribution
3. Add GitHub Actions secrets
4. Push to `main` so the pipeline deploys automatically

Public URL (Amplify Hosting, CloudFront-backed):

https://main.d1kzcf2uu5risc.amplifyapp.com

## Local test

```bash
python -m unittest discover -s tests -v
```

## Submission format

```text
Question 1: <ALB URL>
Question 2: <CloudFront URL>
Accessible Google Doc Link: <screenshots doc>
```

Use `docs/screenshots-checklist.md` while collecting screenshots.

## Cost note

Use AWS Free Tier eligible resources where you can, then delete unused resources after the reviewer has checked the URLs.
