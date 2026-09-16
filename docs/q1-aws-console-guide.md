# Question 1: Manual AWS Console setup

Create this infrastructure in the AWS Management Console. Use Free Tier eligible options where possible. After the ALB is healthy, submit only the ALB URL.

The webpage to serve is `q1-ec2-nginx/index.html`.

## 1. Network

1. Create a VPC (for example `devops-q1-vpc`) with IPv4 CIDR `10.0.0.0/16`.
2. Create a public subnet in that VPC (for example `10.0.1.0/24`) and enable auto-assign public IPv4.
3. Create an Internet Gateway, attach it to the VPC, and take a screenshot.
4. Create a route table for the public subnet:
   - Destination `0.0.0.0/0` -> the Internet Gateway
   - Associate the route table with the public subnet
5. Take screenshots of the VPC, subnet, Internet Gateway, and route table. You will add these to the Google Doc.

## 2. Security group and EC2

1. Create a security group for the EC2 instance that allows:
   - SSH on port 22 from your IP
   - HTTP on port 80 from `0.0.0.0/0`
2. Launch an Amazon Linux 2023 EC2 instance in the public subnet.
   - Instance type: `t2.micro` or `t3.micro`
   - Attach the security group above
   - Create or select a key pair
3. Create a second security group for the load balancer that allows HTTP port 80 from `0.0.0.0/0`.

## 3. Install NGINX

SSH into the instance, then run:

```bash
sudo dnf update -y
sudo dnf install -y nginx
sudo systemctl enable nginx
sudo systemctl start nginx
```

Copy `q1-ec2-nginx/index.html` onto the server. From your laptop:

```bash
scp -i your-key.pem q1-ec2-nginx/index.html ec2-user@EC2_PUBLIC_IP:/tmp/index.html
```

On the EC2 instance:

```bash
sudo mv /tmp/index.html /usr/share/nginx/html/index.html
sudo systemctl restart nginx
```

Open `http://EC2_PUBLIC_IP` and confirm the page shows:

- DevOps Training
- Application deployed successfully!
- Server: AWS EC2
- Web Server: NGINX

## 4. Target group and Application Load Balancer

1. Create a target group:
   - Target type: Instances
   - Protocol: HTTP
   - Port: 80
   - VPC: the VPC created above
   - Health check path: `/`
   - Register the EC2 instance
2. Create an internet-facing Application Load Balancer, IPv4.
3. Select the same VPC and at least two public subnets (ALB needs subnets in two Availability Zones). If you only created one public subnet, create a second public subnet in another AZ, attach the same route table, and continue.
4. Attach the ALB security group.
5. Add an HTTP listener on port 80 that forwards to the target group.
6. Wait until the EC2 target is `healthy`.
7. Open `http://<ALB-DNS-name>` and confirm the same webpage loads.

## Submit

Question 1 URL example:

`http://my-application-alb-123456789.ap-south-1.elb.amazonaws.com`
