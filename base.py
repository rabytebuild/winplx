import winrs
# Define the username and password for the RDP connection
username = "rhsalisu" # Replace with actual username
password = "Rabiu2004@" # Replace with actual password
# Create a new instance of the WinRSConnection object
connection = winrs.WinRSConnection(username, password)
# Connect to the remote server using the WinRSConnection object
connection.connect()
# Send the SSH command to connect to the remote server
output = connection.send('Welcome to Remote Desktop Protocol')
# Print out the output received from the remote server
print("Output:", output)
