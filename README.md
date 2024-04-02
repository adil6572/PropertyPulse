# PropertyPulse

## Introduction

PropertyPulse is a versatile web scraping tool designed to streamline the process of gathering real estate data from various websites. By providing an API endpoint, PropertyPulse allows users to extract essential property information effortlessly, enabling seamless integration into their applications.

## Features

- **Web Scraping**: Utilizes advanced web scraping techniques to extract comprehensive real estate data, including property details, pricing, location, and images, from multiple websites.
- **RESTful API Endpoint**: Offers a user-friendly RESTful API endpoint that accepts URLs of real estate listing webpages as input and delivers scraped data in JSON format, ensuring ease of integration and accessibility.
- **Support for Multiple Websites**: Supports scraping data from a diverse range of real estate websites, providing users with access to a vast and diverse dataset.

## Supported Websites

- **[Realtor.com](https://www.realtor.com/)**: PropertyPulse supports scraping data from Realtor.com, a leading real estate marketplace, providing users with access to a vast array of property listings and information.

## Installation

To get started with PropertyPulse, follow these steps:

1. **Clone the Repository**: Clone the PropertyPulse repository to your local machine using the following command:

   ```bash
   git clone https://github.com/adil6572/PropertyPulse.git
   ```

2. **Navigate to the Project Directory**: Move into the PropertyPulse directory:

   ```bash
   cd PropertyPulse
   ```

3. **Create Conda Environment**: Create a Conda environment named `api` using the provided YAML file:

   ```bash
   conda env create -f environment.yml
   ```

4. **Activate Conda Environment**: Activate the newly created Conda environment:

   ```bash
   conda activate api
   ```

## Usage

To utilize PropertyPulse and access its functionalities, execute the `main.py` script located in the `api` directory:

1. **Navigate to the API Directory**: Move into the `api` directory:

   ```bash
   cd api
   ```

2. **Run the Script**: Execute the `main.py` script using Python:

   ```bash
   python main.py
   ```

## Contributing

PropertyPulse welcomes contributions from the community. If you encounter any issues or have suggestions for enhancements, please don't hesitate to open an issue or submit a pull request. Your contributions are greatly appreciated!

## License

This project is licensed under the terms of the [MIT License](LICENSE). Feel free to use and modify the code according to your requirements.
