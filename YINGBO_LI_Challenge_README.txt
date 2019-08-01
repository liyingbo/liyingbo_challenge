How it works  
1. use EC2_one_EBS to build from Jenkins to create EC2_one_EBS
2. use Jenkins to deploy Tomcat/Apache with tomcat.yml, also create systemd services
3. from the prototype EC2 (installed tomocat apache) to create baked AMI
4. from AWS certificate manager to create certificate with DNS
5. use Jenkins to deploy the stack, including Autoscaling group, ELB, and with baked AMI and certificate ARN 
6. use route 53 to associate dns alisa with ALB DNS name

Note: This is from the real project. All th customer info has been modified, just show you an example. If you want to run it, 
you have to make some changes to adapt to your environment like KMS Key, security group, certificate and etc. 