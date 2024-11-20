import dotenv
import os
import subprocess

# Load environment variables from .env file
dotenv.load_dotenv()

# Retrieve environment variables
ngrok_username = os.getenv("NGROK_USERNAME")
ngrok_password = os.getenv("NGROK_PASSWORD")

# Ensure ngrok_username and ngrok_password are not None or empty
if not ngrok_username or not ngrok_password:
    raise ValueError("NGROK_USERNAME and NGROK_PASSWORD must be set in the .env file")

# Format the ngrok command with basic authentication
ngrok_command = [
    "ngrok",
    "http",
    "--domain=mentally-proper-martin.ngrok-free.app",
    "5000",
    "--basic-auth",
    f"{ngrok_username}:{ngrok_password}",
]

# Debug print to verify the command
print("Running command:", " ".join(ngrok_command))

# Run the ngrok command using subprocess
subprocess.run(ngrok_command, check=True)
