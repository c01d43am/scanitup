def display_results(devices, output_file="scan_results.txt"):
    """Display results and save them to a file."""
    output = []

    # Active Host List
    output.append("\n🌐 Active Host List:")
    output.append("IP Address      Status")
    output.append("------------------------------")
    for device in devices:
        output.append(f"{device['ip']}     ✅ Online")
    
    # Connected Devices Detail
    output.append("\n📟 Connected Devices Detail:")
    output.append("IP Address      MAC Address        Hostname          First Seen")
    output.append("--------------------------------------------------------------")
    for device in devices:
        output.append(f"{device['ip']:15} {device['mac']:17} {device['hostname']:18} {device['first_seen']}")

    # Print to terminal
    print("\n".join(output))

    # Save to file
    with open(output_file, "w") as file:
        file.write("\n".join(output))

    print(f"\n✅ Results saved to {output_file}")
