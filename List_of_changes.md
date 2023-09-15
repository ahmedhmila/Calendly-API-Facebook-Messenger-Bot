# List of changes
## **Hotfix 1.01**

- Removed the fixed start time at 12:30, which was previously added for testing purposes.
- Modified the script to keep the WebDriver active throughout its execution instead of quitting and restarting every 4 hours. The script now runs continuously until it reaches a predefined condition (e.g., until the clock reaches 9:59).

These enhancements are expected to improve the script's stability and efficiency by eliminating the need for frequent WebDriver restarts and fixed start times. Additionally, avoiding repeated logins and logouts helps prevent Facebook from flagging the bot as suspicious, ensuring continued message sending functionality
