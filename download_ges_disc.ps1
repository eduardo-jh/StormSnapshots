# A script to download data from NASA GES DISC
# By Eduardo Jimenez Hernandez, PhD student University of Arizona
# 27 Aug 2021
$dir = "D:\Downloads"
$username = "eduardojh"
$filelist = $dir + "\subset_GPM_3IMERGHHE_06_20210901_043513.txt"
$cookies = $dir + "\.urs_cookies"
# Create cookies file in order to save the login information when downloading multiple files
$null > $dir\.urs_cookies
# Download files from a text file
wget --load-cookies $cookies --save-cookies $cookies --auth-no-challenge=on --keep-session-cookies --user=$username --ask-password -i $filelist
