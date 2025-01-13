# buzzline-01-tesfai
This project introduces streaming data. The Python language includes generators - we'll use this feature to generate some streaming buzzline messages. As the code runs, it will continuously update log files. We'll use a consumer to modify this log file and alert us when a special message is detected.

## Task 1: Set Up Your Machine
1. **Install Git**:
   - Follow the installation instructions for your operating system from [Git official site](https://git-scm.com/).

2. **Install Python Version 3.11**:
   - Download and install Python from [Python.org](https://www.python.org/). Make sure to check the option to "Add Python to PATH" during installation.

3. **Install VS Code**:
   - Download and install VS Code from [Visual Studio Code](https://code.visualstudio.com/).

4. **Configure Git**:
   - Open your terminal (PowerShell, Command Prompt) and run the following commands to configure your Git username and email:
     ```bash
     git config --global user.name "Your Name"
     git config --global user.email "your-email@example.com"
     ```

5. **Turn on VS Code File/Autosave**:
   - Open VS Code, then go to `File > Preferences > Settings`. Search for "Auto Save" and set it to **afterDelay** for automatic saving of files.

6. **Install necessary VS Code extensions**:
   - **Python by Microsoft**: For Python language support.
   - **GitLens**: For enhanced Git integration and version control features.