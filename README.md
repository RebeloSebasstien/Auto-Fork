# Auto Fork

## Features
- **Search and Fork Repositories**: Search for repositories by keywords and fork them directly from the command line.

## Requirements
- Python 3.6+
- `requests` library
- `colorama` library

## Installation
1. Clone the repository:

    ```bash
    git clone https://github.com/RebeloSebasstien/auto-fork.git
    cd auto-fork.git
    ```

2. Install the required dependencies:

    ```bash
    pip install requests colorama
    ```

## Usage
1. Run the script:

    ```bash
    python main.py
    ```

2. Log in with your GitHub username and personal access token. The credentials will be saved for future use.
3. Search for repositories using keywords and decide whether to fork them.

## Notes
- To create a personal access token, follow the [GitHub documentation](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token).
- Be mindful of GitHub's API rate limits.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
