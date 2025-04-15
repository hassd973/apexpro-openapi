# main.py

import os
import logging
import argparse
from dotenv import load_dotenv

# ApexPro SDK
from apexpro.client.rest_client import RestClient

# Load .env if it exists
load_dotenv()

# === LOGGING SETUP ===
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.StreamHandler(),  # logs to stdout
        logging.FileHandler("apexpro.log")  # logs to file
    ]
)

logger = logging.getLogger(__name__)

# === ENV VARIABLES ===
API_KEY = os.getenv("APEX_API_KEY")
API_SECRET = os.getenv("APEX_API_SECRET")
PASSPHRASE = os.getenv("APEX_PASSPHRASE", "")  # Optional

# === INIT CLIENT ===
def init_client():
    if not API_KEY or not API_SECRET:
        logger.error("Missing API credentials! Please set APEX_API_KEY and APEX_API_SECRET.")
        exit(1)

    try:
        client = RestClient(
            base_url="https://api.apex.exchange",  # Update if using testnet
            api_key=API_KEY,
            secret=API_SECRET,
            passphrase=PASSPHRASE
        )
        return client

    except Exception as e:
        logger.exception("Failed to initialize ApexPro client.")
        exit(1)

# === COMMAND: account info ===
def show_account_info(client):
    try:
        info = client.get_account()
        logger.info("✅ Account Info:\n%s", info)
    except Exception as e:
        logger.exception("❌ Could not retrieve account info.")

# === Placeholder: WebSocket Mode ===
def run_ws_listener():
    logger.info("📡 WebSocket listener mode not yet implemented.")

# === Placeholder: Trade Mode ===
def run_trade_logic(client):
    logger.info("🚀 Trade logic mode not yet implemented.")

# === MAIN ===
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ApexPro Bot Entrypoint")
    parser.add_argument("--mode", choices=["info", "listen", "trade"], default="info", help="Choose run mode")
    args = parser.parse_args()

    client = init_client()

    if args.mode == "info":
        show_account_info(client)
    elif args.mode == "listen":
        run_ws_listener()
    elif args.mode == "trade":
        run_trade_logic(client)
