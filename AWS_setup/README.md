# AWS Database Connection

Starting the AWS machine instance: (See [1] for setup instructions )

1. Sign into the [AWS console](https://console.aws.amazon.com/console/home?nc2=h_ct&src=header-signin).
2. Go to the [EC2 service](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2). Under Instances is [Instances](https://us-west-2.console.aws.amazon.com/ec2/v2/home?region=us-west-2#Instances:).  Start the machine instance of interest. (Select instance > Actions button > Instance State > Start)
3. Get the IPv4 Public IP address that was assigned to the, now running, instance.  In this case it was now: 34.219.19.96
4. Open a terminal window (zsh) and ssh into the remote machine:
   1. Log onto your AWS instance using

```bash
# standard way
ssh -i ~/.ssh/aws_key.pem ubuntu@<your ip address>
# using config file  (NOTE: Config file must be upto date.)
ssh ubuntu@myaws
```

​		The config file method works because I modified `~/.ssh/config` to include

```Host myaws
HostName 18.216.164.22 # use your IP instead
        User ubuntu
        IdentityFile ~/.ssh/aws_key.pem
```

​		To edit the config file do: `nano ~/.ssh/config`, edit the IP address and save.

​		2.	You should now have a cursor like: 

​					`(base) ubuntu@ip-172-31-17-117:~$`

​				showing the ip address from where you're connecting from.

5. Setup Python on AWS:
	1. In your browser, go to https://www.anaconda.com/download/#linux

	2. Right-click on button "Download" for Python 3.X, and select "Copy Link Address"

	3. In your EC2 instance, type "wget" and paste the link in

	   ```bash
	   ubuntu@ip-172-31-38-29:~$ wget https://repo.anaconda.com/archive/Anaconda3-5.3.0-Linux-x86_64.sh
	   ```

	   If the address ends in `pkg` you have copied the OS X link instead. Go back to Anacoda's site and copy the address for Linux.

	4. Now run `sh` on the file the previous command just downloaded. Your version number may differ slightly from the one shown below.

	   ```bash
	   ubuntu@ip-172-31-38-29:~$ sh Anaconda3-5.3.0-Linux-x86_64.sh
	   ```

	5. You will see several prompts.

	   - Accept the license agreement. Press 'q' and type yes.
	   - Accept the default install location.
	   - Say "yes" when it asks if you want to run `conda init`

	6. The script should update the path, so your instance knows where python is. Ensure that the path is configured by running  

	   ```bash
	   ubuntu@ip-172-31-38-29:~$ source .bashrc
	   ```

	   You should see `(base)` prepended to your prompt (we are using environments!)

	7. You should be able to run `python` and `conda` now! Double check by running
		```
		ubuntu@ip-172-31-38-29:~$ python
		Python 3.7.3 (default, Mar 27 2019, 22:11:17) 
		[GCC 7.3.0] :: Anaconda, Inc. on linux
		Type "help", "copyright", "credits" or "license" for more information.
		>>> exit()
		ubuntu@ip-172-31-38-29:~$
		```





	5. Secury copying the eMacbook Pro to AWS: 
	`scp -i ~/.ssh/aws_key.pem environment.yml ubuntu@54.202.76.199:/home/ubuntu/environment.yml






5. To exit from ubuntu machine use `exit` to which you should get:

   ```logout
   logout
   Connection to 34.219.19.96 closed.
   (base) sean@Seans-MacBook-Pro SQL Challenges %
   ```

[^1]: Instructions for setting up the ubuntu instance: sea19_ds10/curriculum/project-03/aws-setup/00_setup_aws_ec2.md