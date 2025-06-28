# Please modify the settings below according to your needs.

# List of source URLs to fetch proxy configurations from.
# Add or remove URLs as needed. All URLs in this list are automatically enabled.
SOURCE_URLS = [
    "https://raw.githubusercontent.com/pooriaredorg/POORIARED/refs/heads/main/POORIARED.txt",
    "https://raw.githubusercontent.com/pooriaredorg/POORIA--REDFREE8/refs/heads/main/POORIAM--REDFREE8.txt",
    "https://raw.githubusercontent.com/4n0nymou3/ss-config-updater/refs/heads/main/configs.txt",
    # "https://raw.githubusercontent.com/pooriaredorg/POORIAREDORG.pages/refs/heads/main/POORIAREDORG.pages.txt",
    "https://t.me/s/redfree8",
    "https://t.me/s/redv2ray_channel",
    "https://t.me/s/pooriared",
    # "https://t.me/s/redfree88",
    # Add more URLs here if you want to include additional sources.
]

# Set to True to fetch the maximum possible number of configurations.
# If True, SPECIFIC_CONFIG_COUNT will be ignored.
USE_MAXIMUM_POWER = False

# Desired number of configurations to fetch.
# This is used only if USE_MAXIMUM_POWER is False.
SPECIFIC_CONFIG_COUNT = 100

# Dictionary of protocols to enable or disable.
# Set each protocol to True to enable, False to disable.
ENABLED_PROTOCOLS = {
    "wireguard://": False,
    "hysteria2://": True,
    "vless://": True,
    "vmess://": True,
    "ss://": True,
    "trojan://": True,
    "tuic://": True,
}

# Maximum age of configurations in days.
# Configurations older than this will be considered invalid.
MAX_CONFIG_AGE_DAYS = 7
