# CU-AdobeLicense-Renewer

![License](https://img.shields.io/badge/license-MIT-blue.svg)
[![Renew](https://github.com/WasinUddy/CU-AdobeLicense-Renewer/actions/workflows/actions.yml/badge.svg)](https://github.com/WasinUddy/CU-AdobeLicense-Renewer/actions/workflows/actions.yml)

This repository contains a script that automates the process of renewing Adobe licenses for Chulalongkorn University students. By leveraging GitHub Actions, the script will automatically renew the license every Monday at 18:00 (6:00 PM) using the provided GitHub Secrets for authentication.

## How to Use

To use the CU-AdobeLicense-Renewer, follow these steps:

1. Fork this repository to your own GitHub account by clicking the "Fork" button at the top-right corner of this page.

2. Set up GitHub Secrets:
   - Go to your forked repository and navigate to the "Settings" tab.
   - In the left sidebar, click on "Secrets".
   - Add two new secrets: "USERNAME" and "PASSWORD".
   - Set the values of these secrets according to your Chulalongkorn University account credentials. This information will be securely stored and used by the script for authentication.

3. GitHub Actions Workflow:
   - The script is scheduled to run every Monday at 18:00 UTC (Coordinated Universal Time). If needed, you can modify the schedule in the `.github/workflows/renew-license.yml` file.
   - When the workflow runs, it will automatically execute the script, renewing your Adobe license.

## Disclaimer

Please note that this script is provided as-is, without any warranty. It is intended for educational purposes and to assist Chulalongkorn University students in automating their Adobe license renewal process. Use it responsibly and in compliance with the terms and conditions set by Chulalongkorn University.

## Contributing

Contributions to this project are welcome! If you encounter any issues or have ideas for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgements
This project is a Python implementation of https://github.com/Leomotors/adobe-renew 🤣

nah we just code it at the same time this is a Tamporal Paradox

