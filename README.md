# Wikipedia 1000 Core Topics
## A handy tool to download the 1,000 core topics of Wikipedia

I needed a way of getting approximately 1,000 Wikipedia articles into a MediaWiki but Wikipedia doest not offer a dump of this size. Wikipedia only offers dumps of either all the articles or just one, and I needed a dump somewhere in the middle so I created these scripts.  Although the scripts are relatively simple, they work surprisingly well. The only non pre-installed Python library it uses is the Wikipedia library which can be downloaded [here](https://pypi.python.org/pypi/wikipedia).

This tool uses a combination of Python 3 and and Bash scripting to do the following:

1. Download the [1,000 core topics](https://en.wikipedia.org/wiki/Wikipedia:1,000_core_topics) from Wikipedia.
2. Write each of those ~1,000 articles to a MediaWiki friendly XML format
3. Loads the articles into a MediaWiki using a Bash script.

### Usage
To download the pages:

    ``` 
    #Make sure you do this in an directory with just the file
    #Be prepared to wait
    $ python3 top1000.py
    Abkhazia
    Abortion
    Abraham Lincoln
    Actinium
    Adam Smith
    Addiction
    Adolf Hitler
    Advertising
    Aeschylus
    #etc.
      ```
    Once you're done, make sure to copy the Python script out of the folder with all the articles.

To load the pages into your MediaWiki:
    Put the articles downloaded in the previous step in a directory in your home folder called `articles`. Then, edit `import.sh` and replace `pi` in the section of the line `for file in /home/pi/articles/*` with the name of your home directory. Next move the script into your MediaWiki installations `maintenance` directory. For me, that's `/var/www/html/wiki/maintenance/` but, that may be different for you so please check.

    Now type the following:

    ```
    #You may need to run these commands with root privileges depending on your system configuration.
    # chmod +X import.sh
    # ./import.sh
    #This command may take well over an hour depending on your computers CPU speed
    # php initSiteStats.php
    ```
