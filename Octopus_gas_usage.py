import matplotlib.pyplot as plt # Allows plotting
import datetime # Allows handling of datetime values
import dateutil.parser # Allows you to parse date strings to datetime
import requests # Allows HTTPS requests

group=input('Enter month/day/week: ');
inputparms = {'period_from': '2020-04-01T00:00:00','period_to': datetime.datetime.now().isoformat() , 'group_by': group, 'page_size': '25000'}
gas_req=requests.get("https://api.octopus.energy/v1/gas-meter-points/7617955204/meters/G4P01317861700/consumption/",params=inputparms,auth=('sk_live_uod1Ofo1tdDV9GuhLjVEtpzS:',''))
elec_req=requests.get("https://api.octopus.energy/v1/electricity-meter-points/2200042036243/meters/16P7164601/consumption/",params=inputparms,auth=('sk_live_uod1Ofo1tdDV9GuhLjVEtpzS:',''))
# temp_req=requests.get("https://history.openweathermap.org/data/2.5/aggregated/month?q=Bristol,GBR&month=7",auth=('2b9e21f4455779d09c60631be843a868:',''))

# print(temp_req.text)

gas_json=gas_req.json()
elec_json=elec_req.json()


##group='month'
##with open('/Users/jack/Desktop/Scratch/test_month.txt') as json_file:
##    data=json.load(json_file)

# Declare lists for interval start and gas consumption
interval_start=list()
gas_consumption=list()
elec_consumption=list()

# Loop through the results dict, parse out interval start and consumption
for gas_loop in gas_json["results"]:
    interval_start.append(dateutil.parser.parse(gas_loop["interval_start"]),)
    gas_consumption.append(gas_loop["consumption"])

for elec_loop in elec_json["results"]:
    elec_consumption.append(elec_loop["consumption"])

# Set up initial plot of gas consumption
fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Date')
ax1.set_ylabel('Gas consumption (m^3)', color=color)
ax1.plot(interval_start, gas_consumption, color=color)
ax1.tick_params(axis='y', labelcolor=color)
plt.ylim(bottom=0) # Make sure 0 is visible on y-axis

# Set up second plot as a twin axis
ax2 = ax1.twinx()

color = 'tab:blue'
ax2.set_ylabel('Electricity consumption (kWh)', color=color)  # we already handled the x-label with ax1
ax2.plot(interval_start, elec_consumption, color=color)
ax2.tick_params(axis='y', labelcolor=color)
plt.ylim(bottom=0) # Make sure 0 is visible on y-axis
fig.tight_layout()
plt.show()
