# Question 2: GitHub Actions, S3, and CloudFront

The website lives in `website/`. The workflow in `.github/workflows/deploy.yml` tests, packages, uploads to S3, and invalidates CloudFront on every push to `main`.

## 1. Create the S3 bucket

1. In AWS, create a bucket such as `yourname-devops-cicd-site`.
2. Keep Block Public Access enabled. CloudFront will be the public endpoint.
3. You do not need to enable static website hosting when using CloudFront with Origin Access Control.

## 2. Create CloudFront

1. Create a CloudFront distribution with the S3 bucket as origin.
2. Use Origin Access Control (OAC) so CloudFront can read the private bucket.
3. Default root object: `index.html`
4. Viewer protocol: HTTP and HTTPS, or redirect HTTP to HTTPS
5. Copy the distribution ID and the distribution domain name (`dxxxx.cloudfront.net`).

If AWS shows a bucket policy snippet for OAC, apply it to the bucket.

## 3. Create an IAM user for GitHub Actions

Create an IAM user with programmatic access and this policy, replacing the bucket name and account details as needed:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DeployToS3",
      "Effect": "Allow",
      "Action": [
        "s3:PutObject",
        "s3:GetObject",
        "s3:DeleteObject",
        "s3:ListBucket"
      ],
      "Resource": [
        "arn:aws:s3:::YOUR_BUCKET_NAME",
        "arn:aws:s3:::YOUR_BUCKET_NAME/*"
      ]
    },
    {
      "Sid": "InvalidateCloudFront",
      "Effect": "Allow",
      "Action": "cloudfront:CreateInvalidation",
      "Resource": "arn:aws:cloudfront::YOUR_ACCOUNT_ID:distribution/YOUR_DISTRIBUTION_ID"
    }
  ]
}
```

Create an access key for this user. Store the key only in GitHub Secrets, never in the repo.

## 4. Push this project to GitHub

```bash
git init
git add .
git commit -m "Add DevOps fundamentals assignment project"
git branch -M main
git remote add origin https://github.com/YOUR_USER/YOUR_REPO.git
git push -u origin main
```

## 5. Add GitHub Actions secrets

In the GitHub repo: Settings -> Secrets and variables -> Actions

| Secret | Value |
| --- | --- |
| `AWS_ACCESS_KEY_ID` | IAM access key ID |
| `AWS_SECRET_ACCESS_KEY` | IAM secret access key |
| `AWS_REGION` | For example `ap-south-1` |
| `S3_BUCKET_NAME` | Your S3 bucket name |
| `CLOUDFRONT_DISTRIBUTION_ID` | CloudFront distribution ID |

The first push may fail if secrets were not set yet. Re-run the workflow after adding them, or push a small change.

## 6. Prove CI/CD works

1. Confirm the CloudFront URL shows Version 2.0.
2. Change the version text in `website/index.html` if the reviewer asks for an updated deploy.
3. Push to `main`.
4. Wait for the GitHub Actions run to succeed.
5. Refresh the CloudFront URL and confirm the new version.

## Submit

Question 2 URL example:

`https://d111111abcdef8.cloudfront.net`
