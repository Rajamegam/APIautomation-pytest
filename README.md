# **API Automation Using Pytest Framework**

## **Description**

This project is designed for automating API test cases, enabling teams to seamlessly integrate the framework into their projects with minimal effort. The framework follows a modular and layered architecture, promoting ease of use, reusability, and scalability.

---

## **Layered Design**

1. **Test Layer**: Contains test cases, logically grouped by functionality or feature.
2. **Framework Layer**: Provides core utilities like request handlers, assertions, logging, and reporting.
3. **Configuration Layer**: Manages global variables, environment settings, and API endpoints.
4. **Data Layer**: Separates test data (e.g., JSON, CSV, or YAML) from code.

---

## **Framework Utilities**

### **Logging**
- Uses Python’s `logging` module for detailed logs of request and response details (e.g., URL, response body, response code, status).
- Generates a new log file for each run, with timestamps for better traceability.

### **Reporting**
- Creates detailed HTML reports using the `pytest-html` plugin.
- Includes comprehensive results and logs for debugging.

### **Test Execution Control**
- Supports tagging or markers to categorize tests (e.g., smoke, regression).
- Enables selective test execution using:
  ```bash
  pytest -m <marker>
  ```

### **Fixtures**
- Implements reusable pytest fixtures for setups like session initialization and token generation.
- Uses `autouse` fixtures for common pre-test requirements.

### **API Mocking**
- Allows mocking API responses to simulate isolated test scenarios.

### **CI/CD Integration**
- Automates test execution via GitHub Actions for seamless integration into development workflows.

---

## **Installation**

### **Steps to Set Up the Framework**

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Create a `requirements.txt` File**:
   List the following libraries in the `requirements.txt` file:
   ```text
   pytest~=8.3.3
   requests~=2.32.3
   pytest-html
   Faker~=30.8.2
   logging
   pytest-dependency
   pytest-order
   pytest-ordering
   allure-pytest
   pytest-send-email
   pandas
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Verify Installation**:
   ```bash
   pip freeze
   ```

---

## **Commands for Execution**

### **Run All Test Methods**
```bash
pytest
```

### **Run Selected Test Methods**
```bash
pytest <path_to_test_file>
```

Example:
```bash
pytest tests/api/test_login.py
```

---

## **Markers for Grouping and Execution Control**

### **Grouping Test Cases**
- **Regression Tests**:
  ```python
  @pytest.mark.Regression
  ```

- **Smoke Tests**:
  ```python
  @pytest.mark.smoke
  ```

To execute tests for a specific group:
```bash
pytest -m <marker_name>
```
Example:
```bash
pytest -m Regression
```

### **Marking Dependencies**
- Specify dependencies among test cases:
  ```python
  @pytest.mark.dependency(depends=["<test_method_name>"])
  ```
Example:
```python
@pytest.mark.dependency(depends=["test_login"])
def test_dashboard():
    ...
```

### **Ordering Test Execution**
- Define execution order of test cases:
  ```python
  @pytest.mark.order(<execution_order>)
  ```
Example:
```python
@pytest.mark.order(1)
def test_login():
    ...

@pytest.mark.order(2)
def test_dashboard():
    ...
```

---

## **HTML Report Generation**

Generate a self-contained HTML report:
```bash
pytest --html=<report_directory/report_name> --self-contained-html
```
Example:
```bash
pytest --html=reports/report.html --self-contained-html
```

---

## **Email Report Sending**

Send the latest generated report and log files via email:
```bash
python Utils/email_utils.py
```

---

## **Project Structure**

```text
Project
├── .github          # GitHub Actions configuration files
├── Excel_data       # Test data (e.g., JSON, Excel)
├── Logs             # Log files generated for each run
├── Reports          # HTML reports of test runs
├── Tests            # Test cases organized by project features
├── Utilities        
│   ├── Properties.ini       # Reusable values like client details, endpoints, credentials
│   ├── Data_generator.py    # Methods to generate random JSON data
│   ├── configurations.py    # Reads values from Properties.ini
├── Utils
│   ├── assertions.py        # Reusable assertion functions
│   ├── baseclass.py         # API methods (POST, PUT, GET, PATCH, DELETE)
│   ├── email_utils.py       # Functions to send reports and logs via email
│   ├── log_utils.py         # Logging functions for test cases
├── pytest.ini       # Custom marker registration for test cases
├── requirements.txt # Required dependencies
```

---

### **Details of Key Directories and Files**

- **`.github`**: Contains configuration files for GitHub Actions.
- **`Logs`**: Stores log files generated for each test run.
- **`Reports`**: Stores test execution reports.
- **`Tests`**: Contains all test case files.
- **`Utilities`**:
  - `Properties.ini`: Stores reusable configuration values.
  - `Data_generator.py`: Generates random JSON values for reusable test data.
  - `configurations.py`: Reads and provides values from `Properties.ini`.
- **`Utils`**:
  - `assertions.py`: Contains reusable assertion functions.
  - `baseclass.py`: Provides reusable API methods (POST, PUT, GET, PATCH, DELETE).
  - `email_utils.py`: Sends the latest generated report and log file via email.
  - `log_utils.py`: Provides logging functions for use in test cases.
- **`pytest.ini`**: Registers custom markers for organizing test cases.
- **`requirements.txt`**: Lists all necessary dependencies for the framework.

