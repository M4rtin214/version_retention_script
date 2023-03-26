# version_retention

Script to delete old versions of applications.  

- You can insert the current version of the application and set the number of major and minor versions to keep. Patch versions, higher versions and other files or directories are ignored.  

<pre>
Application directory format: APPLICATION_MAJOR.MINOR.PATH

Usage: python script.py PATH CURRENT_VERSION PRESERVE_COUNT PRESERVE_MINOR_COUNT

Example: python version_retention.py "C:/my_dir" "5.2.3" "2" "3"
</pre>
