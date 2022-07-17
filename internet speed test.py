# Python program to test
# internet speed

import speedtest


st = speedtest.Speedtest()

# download speed
print("Download speed : ",st.download())

# upload speed
print("Upload speed : ",st.upload())

# ping test
servernames =[]
st.get_servers(servernames)
print("Ping", st.results.ping)
