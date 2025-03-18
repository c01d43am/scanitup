banners = [
    """
      .----.        [ S C A A N ]        .------.
    |  ░░░░  |  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  |  ░░░░  |
    |  ░██░  |  ██░░░░░░░░░░░░░░░░░░██  |  ░██░  |
    |  ░██░  |  ██░ SCANNING...   ░░██  |  ░██░  |
    |  ░██░  |  ██░ Hosts Found:  ░░██  |  ░██░  |
    |  ░██░  |  ██░ Extracting MAC░░██  |  ░██░  |
    |  ░██░  |  ██░ Tracing Routes░░██  |  ░██░  |
    |  ░██░  |  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██  |  ░██░  |
    '--------'     [█]██████████[█]     '--------'
    [  🔍  ]      [ STEALTH MODE ON]    [  🔍  ]
    [  🌐  ]        [███████████]       [  🌐  ]
    ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
       NETWORK INFILTRATION IN PROGRESS...
    """
]

# Function to get a random banner
def get_banner():
    import random
    return random.choice(banners)
