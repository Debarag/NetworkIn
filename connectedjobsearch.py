# Used LinkedIn API to gather all 1st degree connections and their companies
# import pandas as pd
from linkedin import linkedin

# Provide your LinkedIn API credentials
API_KEY = 'Your API Key'
API_SECRET = 'Your API Secret'
USER_TOKEN = 'Your User Token'
USER_SECRET = 'Your User Secret'

# Create a LinkedIn application
app = linkedin.LinkedInApplication(token=USER_TOKEN)

# Authenticate the application
authentication = linkedin.LinkedInAuthentication(API_KEY, API_SECRET, USER_TOKEN, USER_SECRET)
app = linkedin.LinkedInApplication(authentication=authentication)

# Get all first-degree connections
connections = app.get_connections()

# Create empty lists to store companies and connections
companies = []
connections_list = []

# Loop through the connections and retrieve their associated companies
for connection in connections['values']:
    connection_id = connection['id']
    connection_profile = app.get_profile(member_id=connection_id, selectors=['id', 'first-name', 'last-name', 'positions'])
    
    first_name = connection_profile['firstName']
    last_name = connection_profile['lastName']
    
    if 'positions' in connection_profile:
        for position in connection_profile['positions']['values']:
            if 'company' in position:
                company_name = position['company']['name']
                companies.append(company_name)
                connections_list.append(f"{first_name} {last_name}")

# Create a pandas DataFrame
data = {'Company': companies, 'Connection': connections_list}
df = pd.DataFrame(data)

# Print the DataFrame
print(df)
