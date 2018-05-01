# linux_configs

Contains my standard dotfiles and other configuration files. Comes with scripst to link them to the relevant location and build the list to use for said linking.

#### `mkfilelist.py`

This script has a cli and is used to build a csv file specifying what files to link and how to link them. Most of the commands are self-explanatory, but it's lacking a help function yet.

#### `applyconfigs`

After building out your file list using the above python script, you can run "applyconfigs" to actually link the files. This is a basic bash script. When running this, you can specify which category of configs to link. Defaults to the "standard" category. Again, this is lacking a proper help function.
