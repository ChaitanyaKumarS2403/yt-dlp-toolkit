import os
import shutil
import signal
import sys

# Restricted Color Scheme: Red, Black, White
RED = '\033[91m'
WHITE = '\033[97m'
BOLD = '\033[1m'
RESET = '\033[0m'

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_header(path):
    clear_screen()
    print(f"{RED}{BOLD}" + "="*65)
    print("""
  __   _______     ____  _     ____    _____            _ 
  \ \ / /_   _|   |  _ \| |   |  _ \  |_   _|__   ___ | |
   \ V /  | |_____| | | | |   | |_) |   | |/ _ \ / _ \| |
    | |   | |_____| |_| | |___|  __/    | | (_) | (_) | |
    |_|   |_|     |____/|_____|_|       |_|\___/ \___/|_|
    """)
    print(f"{WHITE}                 Chaitanya Kumar Sathivada{RED}")
    print("="*65 + f"{RESET}")
    print(f"{WHITE}{BOLD} Your Downloaded files will be saved to the CURRENT DIRECTORY.{RESET}")
    print(f"{WHITE}{BOLD}           You can change the path in Settings{RESET}")
    print("")
    print(f"{WHITE}{BOLD} CURRENT DIRECTORY:{RESET} {RED}{path}{RESET}")
    print(f"{RED}" + "-"*65 + f"{RESET}")

def run_downloader():
    default_path = os.path.join(os.path.expanduser("~"), "Downloads")
    current_path = default_path

    while True:
        print_header(current_path)
        print(f"{BOLD}{RED}SELECT MODE {WHITE}by entering the option value:{RESET}")
        print("")
        print(f"  {RED}[1]{RESET} {WHITE}Download Audio (MP3){RESET}")
        print(f"  {RED}[2]{RESET} {WHITE}Download Video (MP4/MKV){RESET}")
        print(f"  {RED}[3]{RESET} {WHITE}Download Thumbnail / Cover{RESET}")
        print(f"  {RED}[4]{RESET} {WHITE}Settings{RESET}")
        print(f"  {RED}[E]{RESET} {WHITE}Exit Toolkit{RESET}")
        print(f"{RED}" + "-"*65 + f"{RESET}")
        
        choice = input(f"\n{WHITE}{BOLD}Choose the {RED}MODE : {RESET}").strip().lower()

        if choice == 'e':
            print(f"{RED}Closing Toolkit...{RESET}")
            break
        
        if choice == '4':
            print(f"\n{WHITE}ENTER NEW SYSTEM PATH (NOTE: {RED}Resets on restart{WHITE}):{RESET}")
            new_path = input(f"{RED} > {RESET}").strip()
            if new_path and os.path.exists(new_path):
                current_path = new_path
                print(f"{WHITE}Path updated.{RESET}")
            else:
                print(f"{RED}Error: Path not found.{RESET}")
            input(f"\n{WHITE}Press Enter...{RESET}")
            continue

        if choice not in ['1', '2', '3']:
            continue

        while True:
            mode_map = {'1': "[AUDIO MODE]", '2': "[VIDEO MODE]", '3': "[THUMBNAIL MODE]"}
            print(f"\n{RED}{BOLD}CURRENT MODE: {WHITE}{mode_map[choice]}{RESET}")
            print(f"{WHITE}Type {RED}//{WHITE} and hit enter to go back to modes.{RESET}")
            print("")
            print(f"{RED}NOTE: {WHITE}Make sure the URL is copied from the '{RED}Share{WHITE}' option below the YouTube video only and {RED}NOT from the URL Bar.{RESET}")
            url = input(f"{WHITE}Paste your copied URL here : {RESET}").strip()

            if url.lower() == '//': break
            if not url: continue

            output_template = "%(playlist_title&%s/|)s%(title)s.%(ext)s"
            cmd = ""

            if choice == '1':
                cmd = f'yt-dlp -x --audio-format mp3 --embed-thumbnail --convert-thumbnails jpg --embed-metadata -P "{current_path}" -o "{output_template}" "{url}"'
            
            elif choice == '2':
                print(f"\n{WHITE}CHOOSE FORMAT:{RESET}")
                print(f" {RED}[A]{RESET} {WHITE}MKV ({RED}Fastest{WHITE}){RESET}")
                print(f" {RED}[B]{RESET} {WHITE}MP4 ({RED}Slower{WHITE}){RESET}")
                print(f" {RED}[X]{RESET} {WHITE}Cancel & Go Back{RESET}")
                v_choice = input(f"\n{WHITE}{BOLD}Choose your desired {RED}FORMAT > {RESET}").strip().lower()
                
                if v_choice == 'x':
                    break # Breaks out of the download logic to the URL input

                ext = "mp4" if v_choice == 'b' else "mkv"
                if ext == "mp4":
                    cmd = f'yt-dlp --recode-video mp4 --embed-metadata -P "{current_path}" -o "{output_template}" "{url}"'
                else:
                    cmd = f'yt-dlp --merge-output-format mkv --embed-metadata -P "{current_path}" -o "{output_template}" "{url}"'

            elif choice == '3':
                cmd = f'yt-dlp --skip-download --write-thumbnail -P "{current_path}" -o "{output_template}" "{url}"'

            if cmd:
                print(f"\n{RED}--- INITIALIZING ---{RESET}")
                print(f"{WHITE}Press {RED}Ctrl+C{WHITE} at any time to cancel download.{RESET}\n")
                try:
                    os.system(cmd)
                    print("")
                    print(f"{WHITE}="*65)
                    print(f"\n{RED}--- DOWNLOAD COMPLETE | CHECK YOUR DOWNLOAD PATH FOR THE MEDIA FILE ---{RESET}")
                    print(f"{WHITE}="*65)
                except KeyboardInterrupt:
                    print(f"\n{RED}!!! DOWNLOAD CANCELLED BY USER !!!{RESET}")

if __name__ == "__main__":
    # Handle KeyboardInterrupt globally to prevent ugly Python tracebacks
    signal.signal(signal.SIGINT, lambda x, y: print(f"\n{RED}Operation Interrupted.{RESET}") or sys.exit(0))
    os.system("") 
    run_downloader()