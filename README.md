# LookOut App
This Python program will create an app that is used for hurricane preparedness


## Table of contents
[Features](#features)

[Instructions](#instructions)

[Usage](#usage)

[Functions](#functions)

## Features
### 1. Home Page:
- Displays a "Prepared-o-meter" to track your readiness.
- A weather update section to provide real-time weather alerts (future implementation).
### 2. Checklist Page
- A detailed list of essential supplies for emergencies.
- Interactive checkboxes to track the items you have prepared.
- The progress bar updates as you check off items.

### 3. Emergency Contact Page
- Automatically fetches and displays emergency contacts (police, ambulance, fire department) based on your location.
- Supports multiple contacts for each service.

### 4. Profile page Page
- Placeholder for user-specific features and preferences (future implementation).

### 5. Navigation Bar
- An intuitive navigation bar allows easy switching between pages.
- Specify which page is currently on(future implementation)

## Instructions
1. Ensure you have Python 3.8 or above installed.
2. Install required libraries using pip:
    
       pip install public_ip requests
    
3. Ensure the following files are in the repository:
   - `home.png`,`user.png`,`id-card.png`,and `test.png`: Icons for the navigation bar
   - `country_data.json`: A JSON file containing emergency contact information for various countries.
## Usage
1. Run the program by:
   1. Opening a terminal and typing
   
          python app_script.py
      
   2. double click on the file titled `app_script.py`
2. The app will detect your public IP and automatically determine your country using an IP geolocation service
   
3. Navigate through the app using the buttons in the navigation bar
    - Home Button: View your preparedness progress and weather updates
    - Checklist Button: Access and interact with the checklist of essential supplies
    - Contacts Button: View emergency contact information for your country
    - Profile Button: Reserved for future user-specific features.


## Functions
`main()`

The main function that runs the program

`layout()`

Creates the layout of the app

`getcountry()`

Gets IP dress from the public_ip module
        
`emergency_contacts()`

`has_internet_connection()`

`weather_status()`

`getIP()`

## Dependencies

## Acknowledgments
- Icons used in the navigation bar are sourced from [here](https://www.flaticon.com/authors/freepik)
- Geolocation service powered by [apiip.net](https://apiip.net/).
