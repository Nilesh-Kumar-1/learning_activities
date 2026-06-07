# Linux Notes

## Linux File Structure

Linux follows a hierarchical (tree-like) directory structure starting from the root directory `/`.

```text
/
├── bin
├── boot
├── dev
├── etc
├── home
├── root
├── run
├── sbin
├── tmp
├── usr
└── var
```

### Root Directory (`/`)

The top-level directory in Linux.

---

### `/bin`

Contains essential executable binaries (commands) available to all users.

Examples:

- ls
- cd
- mkdir

---

### `/boot`

Contains bootloader files required during system startup.

---

### `/dev`

Contains device files representing hardware connected to the system.

Examples:

- Hard disks
- USB devices
- Terminals

---

### `/etc`

Contains system configuration files.

Examples:

- Network configurations
- User settings
- Service configurations

---

### `/home`

Contains user home directories.

Example:

```text
/home
├── bob
├── alice
└── eve
```

Each user has their own files and directories.

---

### `/root`

Home directory of the root user.

```text
/root
```

---

### `/run`

Stores volatile runtime data.

Contents are stored in RAM and cleared after reboot.

---

### `/sbin`

Contains system binaries primarily used by the root user.

---

### `/tmp`

Stores temporary files.

Examples:

- Cache files
- Cookies
- Application temporary data

Accessible by all users.

---

### `/usr`

Contains user applications and utilities.

#### `/usr/bin`

User binaries.

Similar to `/bin`.

#### `/usr/local`

Stores manually installed software.

#### `/usr/sbin`

Administrative binaries.

#### `/usr/tmp`

Temporary user-related files.

---

### `/var`

Stores variable data.

Examples:

- System logs
- Event logs
- Application logs

---

# Common Linux Commands

## 1. ls

List directory contents.

```bash
ls
```

---

## 2. cd

Change directory.

```bash
cd /path/to/directory
```

---

## 3. pwd

Print current working directory.

```bash
pwd
```

---

## 4. mkdir

Create directories.

```bash
mkdir test
```

Create nested directories:

```bash
mkdir -p may30/{dir1,dir2}/{1,2}
```

---

## 5. rm

Remove files or directories.

Delete recursively:

```bash
rm -r directory_name
```

Interactive deletion:

```bash
rm -i filename
```

---

## 6. ls -l

Long listing format.

Example output:

```text
drwxrwxr-x 2 user group 4096 Jun 7 06:04 test_dir
```

### Fields Explanation

```text
drwxrwxr-x
│
├── d = directory
├── - = file
└── l = symbolic link
```

Other fields:

```text
Permissions | Link Count | Owner | Group | Size | Date/Time | Name
```

---

# Permissions

Linux permissions consist of:

| Symbol | Meaning |
|----------|---------|
| r | Read |
| w | Write |
| x | Execute |

Examples:

- Read → view file contents
- Write → modify file contents
- Execute → run a program/script

---

# Hard Links and Inodes

In Linux, a file consists of:

1. Filename
2. File content

The file content is stored in an inode.

An inode contains:

- File permissions
- Owner information
- File size
- Timestamps
- Location of data blocks

The filename is simply a pointer to the inode.

---

## Link Count

Linux deletes file data only when the link count becomes zero.

---

## Directory Link Count

Every directory starts with two links:

1. `.` (itself)
2. `..` (parent directory)

When a new subdirectory is created, it adds another link to the parent directory.

Formula:

```text
Link Count = 2 + Number of Subdirectories
```

Example:

```text
test_dir
├── dir1
├── dir2
└── dir3
```

Link count:

```text
2 + 3 = 5
```

---

# Other Useful Commands

## cat

View file contents.

```bash
cat filename.txt
```

---

## touch

Create an empty file.

```bash
touch file.txt
```

Creates a file of size 0 bytes if it does not already exist.

---

# Vim Editor Basics

Open a file:

```bash
vi filename
```

or

```bash
vim filename
```

---

## Insert Mode

Press:

```text
i
```

to start inserting text.

---

## Save and Quit

```text
:wq
```

---

## Quit Without Saving

```text
:q!
```

---

## Search

Forward search:

```text
/search_term
```

Backward search:

```text
?search_term
```

---

## Find and Replace

Replace first occurrence in current line:

```vim
:s/find/replace
```

Replace all occurrences in current line:

```vim
:s/find/replace/g
```

---

# Quick Revision Summary

| Directory | Purpose |
|------------|----------|
| /bin | Essential commands |
| /boot | Boot files |
| /dev | Device files |
| /etc | Configuration files |
| /home | User home directories |
| /root | Root user's home |
| /run | Runtime data |
| /sbin | System binaries |
| /tmp | Temporary files |
| /usr | User applications |
| /var | Logs and variable data |
