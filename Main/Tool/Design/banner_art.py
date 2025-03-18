banners = [
    """
      .----.        [ S C A A N ]        .------.
     /  ▓▓  \      STEALTH MODE ON      /   ▓▓   \\
    |  ░░░░  |  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  |  ░░░░  |
    |  ░██░  |  ██░░░░░░░░░░░░░░░░░░██  |  ░██░  |
    |  ░██░  |  ██░ SCANNING...   ░░██  |  ░██░  |
    |  ░██░  |  ██░ Hosts Found:  ░░██  |  ░██░  |
    |  ░██░  |  ██░ Extracting MAC░░██  |  ░██░  |
    |  ░██░  |  ██░ Tracing Routes░░██  |  ░██░  |
    |  ░██░  |  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  |  ░██░  |
    '--------'     [█]██████████[█]     '--------'
    [  🔍  ]       [█████████████]      [  🔍  ]
    [  🌐  ]        [███████████]       [  🌐  ]
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       NETWORK INFILTRATION IN PROGRESS...
    """
]

# Function to get a random banner
def get_banner():
    import random
    return random.choice(banners)
