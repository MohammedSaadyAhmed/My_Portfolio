### **README: Secure Backup and Restore Tool**

#### **Overview**
This tool provides secure, automated backup and restore functionality for Linux systems. It uses encryption to protect backups and supports scheduling for periodic execution.

---

### **Setup**

1. **Install Required Tools**:
   - Ensure the following tools are installed:  
     ```bash
     sudo apt install tar gpg gzip scp
     ```

2. **Configure SSH for Remote Backup**:
   - Set up passwordless SSH authentication between your machine and the remote server:
     ```bash
     ssh-keygen -t rsa
     ssh-copy-id user@remote_server
     ```

3. **Clone the Repository**:
   - Copy the scripts (`backup.sh`, `restore.sh`, and `backup_restore_lib.sh`) to a directory on your system.

---

### **Backup Script: `backup.sh`**

#### **Usage**:
```bash
./backup.sh <source_directory> <backup_directory> <encryption_key> <days>


#### **Parameters**:
	- <source_directory>: The directory containing the files to be backed up0.
	- <backup_directory>: The directory where backups will be stored.
	- <encryption_key>: A key used to encrypt the backup.
	- <days>: Backup files modified in the last n days.
Example:
bash
Copy code
./backup.sh /home/user/data /backups "my_secret_key" 7
This command backs up files from /home/user/data modified in the last 7 days, encrypts them, and stores the backup in /backups.

Output:
Encrypted .gpg backup files in the backup directory.
A consolidated encrypted archive transferred to the remote server.
Restore Script: restore.sh
Usage:
bash
Copy code
./restore.sh <backup_directory> <restore_directory> <decryption_key>
Parameters:
<backup_directory>: The directory containing encrypted backups.
<restore_directory>: The directory where files will be restored.
<decryption_key>: The decryption key used to unlock the backups.
Example:
bash
Copy code
./restore.sh /backups /home/user/restore "my_secret_key"
This command restores files from /backups to /home/user/restore using the provided decryption key.

Output:
Decrypted and extracted files in the specified restore directory.
Automation with Cron
To schedule daily backups:

Open the crontab editor:
bash
Copy code
crontab -e
Add the following line to schedule the script at 2 AM every day:
bash
Copy code
0 2 * * * /path/to/backup.sh /source/dir /backup/dir encryption_key 7
Save and exit. Verify the job:
bash
Copy code
crontab -l
Error Handling
If invalid parameters are provided, the scripts will display a detailed error message and exit.
Ensure all directories exist and the encryption key is valid before running the scripts.
Support
For questions or issues, feel free to reach out!

Copy code
Save the File:

Save the file as README.md in the folder where your scripts and documents are stored.
Verify the File
Ensure the file is properly saved with the .md extension.
Open the file with a Markdown viewer or a code editor to confirm the formatting.
