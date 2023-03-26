# version_retention

Script to delete application versions.  
You can set the number of major and minor versions to keep. Patch versions, higher verson and another files or directories are ignored. 
<pre>
Application directory format: APPLICATION_MAJOR.MINOR.PATH

Usage: python script.py PATH CURRENT_VERSION PRESERVE_COUNT PRESERVE_MINOR_COUNT

Example: python version_retention.py "C:/my_dir" "5.2.3" "2" "3"
</pre>
