Here's a brief manual to help you set up and use the provided framework:

---

# Test Automation Framework Setup and Usage Manual

This manual guides you through setting up and using a test automation framework using Python, Selenium, Behave, and Allure.

## Prerequisites

1. **Python**: Ensure Python is installed on your machine.
2. **Java**: Ensure Java is installed on your machine.

## Installation Steps

### Step 1: Download the Setup Script

1. Create a new file named `setup.py `Copy and paste the provided setup code into `setup.py OR download the project.

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
