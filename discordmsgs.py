import discord
from discord.ext import commands
import kustagpt
import kustatts
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

DISC_BOT = os.getenv("DISC_BOT")

# Set up the bot
intents = discord.Intents.default()
intents.message_content = True  # Make sure to enable this intent in your Discord Developer Portal

bot = commands.Bot(command_prefix='!', intents=intents)

# Function to export chat history to CSV
def export_history_to_csv(user_input, response, filename="chat_history.csv"):
    """Append user input and response to the chat history CSV file."""
    
    # Get the current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Create a dictionary for the new log entry
    log_entry = {
        "Timestamp": timestamp,
        "User": user_input.strip(),  # Strip extra spaces/newlines
        "Kusta": response.strip()   # Strip extra spaces/newlines
    }
    
    # Check if the file exists using os.path.exists()
    file_exists = os.path.exists(filename)
    
    # Open the file and append the new log entry
    with open(filename, mode='a', newline='', encoding='utf-8') as file:
        # Write the header only if the file is new
        if not file_exists:
            file.write('"Timestamp", "User", "Kusta"\n')
        # Format the log entry with spaces after the commas
        formatted_entry = f'"{log_entry["Timestamp"]}", "{log_entry["User"]}", "{log_entry["Kusta"]}"\n'
        file.write(formatted_entry)
        file.flush()

# Event when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

# Listen for messages in a specific channel
@bot.event
async def on_message(message):
    # Make sure the bot doesn't respond to its own messages
    if message.author == bot.user:
        return
    
    # Specify the channel ID you want to listen to (replace with your channel ID)
    target_channel_id = 1317313874000875551  # Replace with your channel ID
    if message.channel.id == target_channel_id:
        user_input = message.content
        
        # Get the response from gemini.py (your custom response function)
        response_text = kustagpt.gemini_response(user_input)
        
        # Save logs
        export_history_to_csv(user_input, response_text)
        
        # Send the generated response back to the same channel
        await message.channel.send(response_text)
        '''
        # Call play.py to generate and play the speech
        kustatts.gen_audio(response_text)
        '''
# Start the bot
bot.run(DISC_BOT)  # Replace with your bot's token
