import os

# Restricted Color Scheme: Red, Black, White
RED = '\033[91m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(path):
    clear_screen()
    # Header in Red
    print(f"{RED}{BOLD}" + "="*65)
    print("""
  __   _______     ____  _     ____    _____           _ 
  \ \ / /_   _|   |  _ \| |   |  _ \  |_   _|__   ___ | |
   \ V /  | |_____| | | | |   | |_) |   | |/ _ \ / _ \| |
    | |   | |_____| |_| | |___|  __/    | | (_) | (_) | |
    |_|   |_|     |____/|_____|_|       |_|\___/ \___/|_|
    """)
    # Credits in White
    print(f"{WHITE}                 Chaitanya Kumar Sathivada{RED}")
    print("="*65 + f"{RESET}")
    
    # Path info in White/Red contrast
    print(f"{WHITE}{BOLD} CURRENT DIRECTORY:{RESET} {RED}{path}{RESET}")
    print(f"{RED}" + "-"*65 + f"{RESET}")

def run_downloader():
    # Dynamic user path detection
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    current_path = default_path

    while True:
        print_header(current_path)
        print(f"  {RED}[1]{RESET} {WHITE}Download .mp3 Playlist/Video{RESET}")
        print(f"  {RED}[2]{RESET} {WHITE}Download .mp4 Playlist/Video{RESET}")
        print(f"  {RED}[3]{RESET} {WHITE}Download Album Cover Art{RESET}")
        print(f"  {RED}[4]{RESET} {WHITE}Settings (Change Path){RESET}")
        print(f"  {RED}[E]{RESET} {WHITE}Exit Toolkit{RESET}")
        print(f"{RED}" + "-"*65 + f"{RESET}")
        
        choice = input(f"\n{WHITE}{BOLD}ACTION > {RESET}").strip().lower()

        if choice == 'e':
            print(f"{RED}Closing Toolkit...{RESET}")
            break
        
        if choice == '4':
            print(f"\n{WHITE}ENTER NEW SYSTEM PATH (Remember: {RED} Path will reset to default upon closing the tool!{WHITE}):{RESET}")
            new_path = input(f"{RED} > {RESET}").strip()
            if new_path:
                if os.path.exists(new_path):
                    current_path = new_path
                    print(f"{WHITE}Path successfully updated.{RESET}")
                else:
                    print(f"{RED}Error: Path not found.{RESET}")
            input(f"\n{WHITE}Press Enter to continue...{RESET}")
            continue

        if choice not in ['1', '2', '3']:
            continue

        while True:
            mode_map = {
                '1': "MP3 AUDIO",
                '2': "MP4 VIDEO",
                '3': "COVER ART"
            }
            mode_label = mode_map[choice]
            
            print(f"\n{RED}{BOLD}MODE: {WHITE}{mode_label}{RESET}")
            print(f"{WHITE}Type {RED}/back{WHITE} to return.{RESET}")
            url = input(f"{WHITE}URL > {RESET}").strip()

            if url.lower() == '/back':
                break
            if not url:
                continue

            # Smart folder template (Playlist name or Direct)
            output_template = "%(playlist_title&%s/|)s%(title)s.%(ext)s"

            if choice == '1':
                cmd = f'yt-dlp -x --audio-format mp3 --embed-metadata --add-metadata -P "{current_path}" -o "{output_template}" "{url}"'
            elif choice == '2':
                cmd = f'yt-dlp --recode-video mp4 --embed-metadata --add-metadata -P "{current_path}" -o "{output_template}" "{url}"'
            elif choice == '3':
                cmd = f'yt-dlp --skip-download --write-thumbnail -P "{current_path}" -o "{output_template}" "{url}"'

            print(f"\n{RED}--- INITIALIZING STREAM ---{RESET}\n")
            # Execution
            os.system(cmd)
            print(f"\n{WHITE}--- DOWNLOAD COMPLETE ---{RESET}")

if __name__ == "__main__":
    # Initialize Windows ANSI support
    os.system("") 
    run_downloader()