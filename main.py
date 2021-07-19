# Clear Clutter
# These imports will be used for this project.
from colorama import Fore, Style
from colorama import init
import datetime
import shutil
import sys
import os

# Setup Terminal.
os.system('title Clear Clutter')
if len(sys.argv) > 1: os.chdir(sys.argv[1])

# Initilaze File organizer.
init(autoreset = True)
Files = []

# Create Log Functions.
class LOG:
	def INFO_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"{CurrentTime} - INFO: {message}")

	def STATUS_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(f"{CurrentTime} - STATUS: {message}")

	def WARN_LOG(message):
		CurrentTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
		print(Fore.YELLOW + Style.BRIGHT + f"{CurrentTime} - WARNING: {message}")

# This function will list out everyting that exists in the current directory.
def ListFiles(rm_file):
	global Files

	Files = os.listdir() # Listing all the content exist in the current folder.
	for i in rm_file:
		if os.path.isfile(i): Files.remove(i)

# This function will Create a Folder if it already not exists.
def CreateFolderIfNotExist(Folder):
	if not os.path.exists(Folder):
		os.makedirs(Folder)

# This function will Move all the Files.
def MoveFile(FolderName, FileName):
	Count = 0
	for File in FileName:
		if os.path.isfile(File):
			os.replace(File, f"{FolderName}/{File}")
			Count += 1

	return Count

# This function will Organize everything.
def Organizer(FolderName, Extentions = None):
	ListFiles(["main.py", "Clear Clutter.exe"])
	CreateFolderIfNotExist(FolderName)
	if Extentions != None:
		FilesBasedOnExts = [File for File in Files if os.path.splitext(File)[1].lower() in Extentions]
		NumOfFilesMoved = MoveFile(FolderName, FilesBasedOnExts)
		if len(os.listdir(FolderName)) == 0:
			shutil.rmtree(FolderName)

		return NumOfFilesMoved

	else:
		NumOfFilesMoved = MoveFile(FolderName, Files)
		if len(os.listdir(FolderName)) == 0: shutil.rmtree(FolderName)
		return NumOfFilesMoved

# Code Logic here.
LOG.WARN_LOG("Initialized Clear Clutter!")
TotalFilesMoved = 0

LOG.STATUS_LOG("Moving Files, Please wait.")
TotalFilesMoved += Organizer("Docs", [".txt", ".md", ".docx", ".xml", ".xlsx", ".pptx", ".pptm", ".pdf", ".csv", ".json", ".log"])
TotalFilesMoved += Organizer("Music", [".mp3", ".wav", ".ogg", ".flp", ".sesx", ".aup"])
TotalFilesMoved += Organizer("Videos", [".mp4", ".mpeg", ".avi", ".wmv", ".webm", ".mkv", ".flv"])
TotalFilesMoved += Organizer("Pictures", [".png", ".jpg", ".jpeg", ".svg", ".gif", ".ico"])
TotalFilesMoved += Organizer("Zip Files", [".zip", ".rar", ".iso", ".7z", ".cab", ".gz", ".taz", ".tgz"])
TotalFilesMoved += Organizer("Dev Projects", [".html", ".css", ".js", ".bat", ".py", ".cpp", ".java", ".cs", ".glass", ".sln"])
TotalFilesMoved += Organizer("Others")

# Print how many files were moved.
if TotalFilesMoved != 0: LOG.INFO_LOG(f"{TotalFilesMoved} Files moved!")
else: LOG.INFO_LOG("There were no Files to move.")

os.system("echo|set /p=Done.")
os.system("pause>nul")
sys.exit() # Exiting the program successfully.
