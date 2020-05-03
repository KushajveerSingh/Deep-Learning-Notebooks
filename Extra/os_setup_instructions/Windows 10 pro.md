1. Remove unnecessary files using **Add or remove programs**.
2. Update windows using **Check for updates**.
3. Install google chrome, [link](https://www.google.com/chrome/).
4. Setup **kushajreal@gmail.com** account in chrome, and modify the extension bar to **Nbviewer, SetupVPN, ImageDownloader, CleanUpYoutube, AdBlock plus**.
5. Download **Winrar** using file in folder, or check for newer version [link](https://getintopc.com/?s=winrar).
6. Download **ultraiso** using file in folder.
7. Download **IDM**, [link](https://getintopc.com/?s=idm).
8. Download **Microsoft Office**, [link](https://getintopc.com/?s=microsoft+office)
9. Download **Lenovo Vantage**, [link](https://www.lenovo.com/us/en/software/vantage).
10. Check for system update in Lenovo Vantage.
11. Download **Geforce Experience**, [link](https://www.nvidia.com/en-in/geforce/geforce-experience/).
12. Update Nvidia Driver to the latest version using Geforce Experience.
13. Install steam, [link](https://store.steampowered.com/).
14. Setup AOE2 DE
    - Copy the **AoE2DE** folder to **C:/Program Files (x86)/Steam/steamapps/common**.
    - Open Steam->Library.
    - Click **Install Game** and **ensure it's set to install in the same folder** that you just restored your game files to.
15. Increase Performance of Windows 10 [link](https://www.windowscentral.com/tips-tricks-increase-pc-performance-windows-10):
    - Disable Startup apps **Settings -> Apps -> Startup**.
    - Disable Relaunch apps on startup **Settings -> Sign-in options -> Privacy section -> _Turn off_ Use my sign-in info to automatically finish setting up my device**.
    - Disable Background apps **Settings -> Privacy -> Background apps -> _Turn off_ Let apps run in the background**.
    - Remove temporary files **Settings -> System -> Storage -> Local Disk -> Temporary files**.
    - Change power plan **Control panel -> Hardware and Sound -> Power Options -> _High Performance power_**.
    - Disable visual effects **Settings -> System -> About -> Related settings (System info) -> Advanced system settings -> Advanced -> Performance (Settings) -> Visual Effects -> Adjust for best performance -> Apply -> Ok
        - To keep the fonts the same use **Custom -> Unselect all except _Smooth edges of screen fonts_**
    - Disable transparency effects **Settings -> Persolnalization -> Colors -> (Turn off) Transparency effects**.
16. Create a restore point. Use this after updates in case some settings got affected.
    - **Start -> Create a restore point -> System Protection -> System Restore -> Next**.
16. Dual boot Ubuntu 20.04 (iso in folder if needed) [link](https://www.wikihow.com/index.php?title=Dual-Boot-Windows-10-and-Ubuntu-16.04&oldid=23740914):
    - Turn off fast boot (Control Panel -> Power Options -> Choose what the power button does -> Change settings that are currently unavailable -> (Uncheck) Turn on fast startup (recommended))
    - Turn off secure boot (Simply get into BIOS) (Update and recovery -> Restart -> Troubleshoot -> Advanced options -> UEFI Firmware settings -> Restart). Now move to boot and turn off secure boot.
    - Insert USB and boot into it. **Try Ubuntu**.
    - **Gparted Partition Editor**
        - Select the Windows partition. Click the *orange right facing arrow* and shrink the partition.
    - Click on *Install Ubuntu** on the desktop.
    - Choose something else for installation type
    - Update the free space partition as
        - Create root partition:
            - Type (Primary)
            - Location (Beginning of this space)
            - Use as (ext4 journaling file system)
            - Mount point (/)
        - Create swap partition
            - Type (Logical)
            - Location (Beginning of this space)
            - Use as (Swap area)
        

