Here's a brief manual to help you set up and use the provided framework:

---

# Test Automation Framework Setup and Usage Manual

This manual guides you through setting up and using a test automation framework using Python, Selenium, Behave, and Allure.

## Prerequisites

1. **Python**: Ensure Python is installed on your machine.
2. **Java**: Ensure Java is installed on your machine.
3. **Pycharm or VScode** : IDE
   
### User Manual: Setting Up Java and Allure Framework

#### Prerequisites:
Before you can proceed with using the Allure framework, ensure you have Java installed and properly configured on your system. Follow the steps below to install Java, set the `JAVA_HOME` environment variable, download and set up Allure, and verify that everything is working correctly.

#### Step 1: Install Java
1. **Download Java:**
   - Visit the official Java website: [Oracle Java Downloads](https://www.oracle.com/java/technologies/javase-jdk11-downloads.html).
   - Choose the appropriate version for your operating system and download the installer.

2. **Install Java:**
   - Run the downloaded installer and follow the on-screen instructions to complete the installation.

---

#### Step 2: Set the `JAVA_HOME` Environment Variable

**For Windows:**
1. **Open System Properties:**
   - Right-click on `This PC` or `Computer` on your desktop or in File Explorer.
   - Select `Properties` > `Advanced system settings`.

2. **Set Environment Variable:**
   - Click on `Environment Variables`.
   - Under `System Variables`, click `New`.
   - Enter the following:
     - **Variable name:** `JAVA_HOME`
     - **Variable value:** Path to your Java installation (e.g., `C:\Program Files\Java\jdk-11.x.x`)
   - Click `OK` to save.

3. **Update the `Path` Variable:**
   - Find the `Path` variable under `System Variables`, select it, and click `Edit`.
   - Click `New` and add `%JAVA_HOME%\bin`.
   - Click `OK` to save and exit.

**For macOS/Linux:**
1. **Open Terminal.**

2. **Set `JAVA_HOME` Variable:**
   - Open your profile file with a text editor (e.g., `~/.bash_profile`, `~/.zshrc`, or `~/.bashrc`):
     ```bash
     nano ~/.bash_profile
     ```
   - Add the following line to the file:
     ```bash
     export JAVA_HOME=$(/usr/libexec/java_home)
     export PATH=$JAVA_HOME/bin:$PATH
     ```

3. **Save and apply the changes:**
   - Save the file and close the editor.
   - Apply the changes by running:
     ```bash
     source ~/.bash_profile
     ```

4. **Verify the Java Installation:**
   - Run the following command in the terminal:
     ```bash
     java -version
     ```
   - You should see the installed Java version displayed.

---

#### Step 3: Download and Install Allure Framework

1. **Download Allure:**
   - Visit the official Allure website: [[Allure Framework Downloads](https://github.com/allure-framework/allure2/releases/download/2.30.0/allure-2.30.0.zip).
   - Download the latest version of Allure Commandline.

2. **Extract Allure:**
   - Extract the downloaded file to a directory of your choice (e.g., `C:\allure` or `/usr/local/allure`).

---

#### Step 4: Set Allure in the Path Variable

**For Windows:**
1. **Open System Properties:**
   - Repeat the steps in the Environment Variable` section to access the `Environment Variables`.

2. **Update the `Path` Variable:**
   - Under `System Variables`, find the `Path` variable and click `Edit`.
   - Click `New` and add the path to your Allure `bin` directory (e.g., `C:\allure\bin`).
   - Click `OK` to save and exit.

**For macOS/Linux:**
1. **Open Terminal.**

2. **Set Allure in the Path:**
   - Open your profile file with a text editor:
     ```bash
     nano ~/.bash_profile
     ```
   - Add the following line to the file:
     ```bash
     export PATH=/path/to/allure/bin:$PATH
     ```

3. **Save and apply the changes:**
   - Save the file and close the editor.
   - Apply the changes by running:
     ```bash
     source ~/.bash_profile
     ```

---

#### Step 5: Verify Allure Installation

1. **Open Command Prompt or Terminal.**

2. **Check Allure Version:**
   - Run the following command:
     ```bash
     allure --version
     ```
   - If the setup is successful, you should see the version of Allure displayed.

---

Your system is now ready to use Allure Framework.
## Installation Steps

### Step 1: Download the Setup Script

1. Create a new file named `setup.py `Copy and paste the provided setup code into `setup.py' OR download the project.

### Step 2: Run the Setup Script

1. Open a command prompt or terminal.
2. Navigate to the directory containing `setup.py`.
3. Run the setup script with the following command:

   ```bash
   python setup.py
   ```

This script will:

- Install necessary Python dependencies (`selenium`, `webdriver_manager`, `allure-behave`, `requests`).
- Download and set up Allure.
- Verify Java installation.
- Create the necessary folder structure (`elements`, `features`, `methods`).
- Create sample feature and step definition files.
- Create the `run-testcases.py` script.

### Step 3: Manual Installations

1. **Install PyCharm**: Download and install PyCharm from [PyCharm Download](https://www.jetbrains.com/pycharm/download/).

### Folder Structure

After running the setup script, the following folder structure will be created:

```
your-project/
├── elements/
│   └── sample_element.py
├── features/
│   ├── steps/
│   │   └── search_google_steps.py
│   ├── search_google.feature
│   └── environment.py
├── methods/
│   └── utilities.py
├── configuration.py
├── run-testcases.py
└── setup.py
```

## Using the Framework

### Writing Tests

1. **Define Elements**: Add element locators and interactions in the `elements` folder.
2. **Create Features**: Write feature files in the `features` folder using Gherkin syntax.
3. **Step Definitions**: Implement step definitions in the `steps` folder under `features`.

### Running Tests

To run your tests and generate reports, use the `run-testcases.py` script:

1. Open a command prompt or terminal.
2. Navigate to the project directory.
3. Run the script with the following command:

   ```bash
   python run-testcases.py
   ```

### Viewing Reports

1. The `run-testcases.py` script will generate an Allure report.
2. The script will start a local server and open the report in your default web browser.

### Report Directory Structure

Each run will create a unique directory for the results and reports:

```
your-project/
├── allure_results_YYYY-MM-DD_XXX/
├── TestReport_YYYY-MM-DD_XXX/
│   └── allure_report/
│       └── index.html
```

### Configuration

Update the `configuration.py` file to modify webhook URLs and other settings.

---

This manual should help you get started with setting up and using the test automation framework efficiently. If you have any questions or encounter any issues, feel free to reach out for assistance.
