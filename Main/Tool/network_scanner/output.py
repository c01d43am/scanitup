def display_results(devices):
    print("\n🌐 Active Host List:")
    print("IP Address      Status")
    print("------------------------------")
    for device in devices:
        print(f"{device['ip']}     ✅ Online")
    
    print("\n📟 Connected Devices Detail:")
    print("IP Address      MAC Address        Hostname          First Seen")
    print("--------------------------------------------------------------")
    for device in devices:
        print(f"{device['ip']:15} {device['mac']:17} {device['hostname']:18} {device['first_seen']}")
