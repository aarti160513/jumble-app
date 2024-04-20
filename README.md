# Jumble App

App to transform an input string based on following logic

- shift right by n letters for alphabets i.e (a,b,c ... z). if you reach z return to a and continue, however
  many times is required.
- keep the chracter if character is a number (1,2,3 ... ) or space
- remove all other characters from string

## Table of Contents

- [Assumptions](#Asumptions)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [License](#license)

## Asumptions

I have choosen python spepcifically flask package, for developing the jumble APP. Flask is a very popular & widely used python packge that enables reapid API development from scratch. For unit tests & code coverage I have leveraged pytest and coverage python packages

## Installation

1. **Clone the repository & Navigate to the project**

   ```PowerShell
    git clone https://github.com/aarti160513/jumble-app.git
    cd jumble-app
   ```

2. **Create a virtual environment:**

   ```PowerShell
   python -m venv $HOME\.venv\jumble
   ```

3. **Activate the virtual environment and Install dependencies:**

   ```PowerShell
   & $HOME\.venv\jumble\Scripts\Activate.ps1
   pip install -r requirements.txt
   ```

4. **App Build:**
   Please ensure you have docker installed on your eniroment. We will use docker to build the app contianer which can later be deployed to any container hosting enironment

   ```PowerShell
   cd jumble-app
   docker build -t jumble-app .
   ```

## Usage

You can run the project locally using dokcker and test it using postman.

```PowerShell
    docker run --rm  -p 5000:5000 jumble-app
    # Test in powershell
    $headers = New-Object "System.Collections.Generic.Dictionary[[String],[String]]"
    $headers.Add("Content-Type", "application/json")

    $body = @"
    {
        `"message`": `tes%%^&&**t 123!&*klio`"
    }
    "@

    $response = Invoke-RestMethod 'http://localhost:5000/api/jumble/100' -Method 'POST' -Headers $headers -Body $body
    $response | ConvertTo-Json
```

## Project Structure

```PowerShell

├── flaskr
│   ├── __init__.py
├── tests
│   ├── conftest.py
│   ├── test_health_check.py
│   ├── test_jumble.py
├── Dockerfile
├── requirements.txt
├── LICENSE
|── README.md
└── .gitignore
```

## License

MIT LICENSE
