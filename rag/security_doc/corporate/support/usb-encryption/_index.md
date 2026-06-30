---
title: Corporate Security USB Device Encryption Guide
---

How to encrypt your USB mass storage device in either macOS or Linux.

## MacOS Instructions

### Prerequisites

- A USB drive you wish to encrypt

- macOS 10.13 (High Sierra) or later

- Administrator privileges on your Mac

### Steps to Encrypt a USB Drive Using Disk Utility

1. Insert your USB drive into an available USB port on your Mac.

2. Open Disk Utility:

   - Navigate to Applications > Utilities > Disk Utility, or...

   - Search for "Disk Utility" using Spotlight (press Cmd + Space and type "Disk Utility")

3. Select the USB drive from the sidebar on the left. Be sure to select the drive itself (the top-level entry), not the volume underneath it.

4. Erase and format the drive:

   - Click on the "Erase" button in the top toolbar

   - Enter a name for your drive

   - For "Format", select "APFS (Encrypted)" or "Mac OS Extended (Journaled, Encrypted)"

   - For "Scheme", select "GUID Partition Map"

   - Click "Erase"

5. Create a password:

   - You'll be prompted to create a password for the encrypted drive

   - Enter a strong password and verify it

   - Optionally, enter a password hint (recommended)

   - Click "Choose"
   
   > **IMPORTANT**: Store this password securely. If you forget it, you cannot recover the data on the drive.

6. Wait for the process to complete, then click "Done".

Your USB drive is now encrypted. Whenever you connect it to a Mac, you'll be prompted to enter the password to access its contents.

### Alternative: Using FileVault from Terminal

If you prefer using Terminal, you can also encrypt your USB drive using FileVault:

```bash
# First identify your disk identifier
diskutil list

# Then encrypt the drive (replace "disk2" with your actual disk identifier)
diskutil cs convert disk2 -passphrase

# Follow the prompts to create a password
```

### Official macOS Documentation

[Apple Support: Encrypt and protect a storage device with a password](https://support.apple.com/guide/disk-utility/encrypt-protect-a-storage-device-password-dskutl35612/mac)

[Apple Support: Protect data on your Mac with FileVault](https://support.apple.com/guide/mac-help/protect-data-on-your-mac-with-filevault-mh11785/mac)

[Apple Support: Disk Utility Overview](https://support.apple.com/guide/disk-utility/welcome/mac)

## Linux Instructions

### Prerequisites

- Existing data on the USB is backed up, as encrypting will erase everything on the USB

- A USB drive you wish to encrypt

- A Linux distribution with LUKS (Linux Unified Key Setup) support (most modern distributions)

- `cryptsetup` package installed

- Root or sudo privileges

### Installing Required Packages

On Debian/Ubuntu-based distributions:

```bash
sudo apt update
sudo apt install cryptsetup
```

On Fedora/RHEL-based distributions:

```bash
sudo dnf install cryptsetup
```

On Arch-based distributions:

```bash
sudo pacman -S cryptsetup
```

### Steps to Encrypt a USB Drive Using LUKS

1. Insert your USB drive into an available USB port on your Linux machine.

2. Identify the device path of your USB drive:

   ```bash
   lsblk
   ```

   > Look for your USB drive in the output (e.g., `/dev/sdb`). Make sure you identify the correct device as the following steps will erase all data on it.

3. Create a new partition table (optional but recommended):

   ```bash
   sudo fdisk /dev/sdX  # Replace sdX with your drive identifier
   ```

   - Type o to create a new empty DOS partition table

   - Type n to add a new partition

   - Follow the prompts to create a primary partition using the entire disk

   - Type w to write the changes and exit

4. Initialize LUKS encryption on the partition:

   ```bash
   sudo cryptsetup luksFormat /dev/sdX1  # Replace sdX1 with your partition
   ```

   - You will be asked to confirm the operation by typing "YES" in uppercase

   - Then enter and verify a strong passphrase

5. Open the encrypted partition.

   ```bash
   sudo cryptsetup luksOpen /dev/sdX1 encrypted_usb  # Replace sdX1 with your partition
   ```

   - Enter the passphrase you set in the previous step.

6. Create a filesystem on the encrypted partition:

   ```bash
   sudo mkfs.ext4 /dev/mapper/encrypted_usb
   ```

   - You can also use other filesystems like `mkfs.btrfs` or `mkfs.xfs` if preferred.

7. Mount the encrypted filesystem:

   ```bash
   sudo mkdir -p /media/encrypted_usb
   sudo mount /dev/mapper/encrypted_usb /media/encrypted_usb
   ```

### Safely Unmounting the Encrypted Drive

To safely disconnect your encrypted USB drive:

1. Unmount the filesystem:

   ```bash
   sudo umount /media/encrypted_usb
   ```

2. Close the encrypted partition:

   ```bash
   sudo cryptsetup luksClose encrypted_usb
   ```

3. You can now safely remove the USB drive.

### Using the Encrypted Drive in the Future

To use your encrypted USB drive again:

1. Insert the USB drive.

2. Open the encrypted partition:

   ```bash
   sudo cryptsetup luksOpen /dev/sdX1 encrypted_usb  # Replace sdX1 with your partition
   ```

3. Mount the filesystem:

   ```bash
   sudo mount /dev/mapper/encrypted_usb /media/encrypted_usb
   ```

4. For easier mounting/unmounting

   ```bash
   # Add to ~/.bashrc, replacing sdX1 with your partition
   alias mount-encrypted='sudo cryptsetup luksOpen /dev/sdX1 encrypted_usb && sudo mount /dev/mapper/encrypted_usb /media/encrypted_usb'
   alias unmount-encrypted='sudo umount /media/encrypted_usb && sudo cryptsetup luksClose encrypted_usb'
   ```

### Best Practices for Encrypted USB Storage

1. Choose a strong passphrase that is:

    - At least 12 characters long

    - A mix of uppercase, lowercase, numbers, and special characters

    - Not based on easily guessable personal information

2. Keep a backup of important data stored on the encrypted drive.

3. Store your passphrase securely using a password manager.

4. Always unmount properly before physically removing the drive.

5. Consider multi-factor authentication for highly sensitive data.

6. Perform regular backups of important data stored on encrypted drives.
